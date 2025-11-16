# Section 6: Advanced Features
## القسم 6: الميزات المتقدمة

**Section:** Advanced Features (Nested Top Actions, Media Recovery, Operation Logging)
**Translation Quality:** 0.86
**Glossary Terms Used:** nested top action, media recovery, operation logging, savepoint, index management, archive log, image copy

---

### English Version

Beyond the core restart recovery algorithm, ARIES supports several advanced features that enable sophisticated transaction processing and recovery capabilities.

#### 6.1 Nested Top Actions

Nested top actions allow a transaction to perform a sequence of operations that, once completed, should not be undone even if the enclosing transaction aborts. This is essential for operations like:
- Index structure modifications (B-tree splits, merges)
- Space management operations (allocating and deallocating pages)
- Hash table reorganizations

**Mechanism:**

A nested top action is bracketed by special markers:
1. Before starting the nested action, record the current LastLSN as a savepoint
2. Perform the sequence of updates within the nested action
3. After completing the nested action, write a "dummy CLR" with:
   - UndoNxtLSN pointing to the savepoint (before the nested action)
   - No actual undo information (the action is complete and should not be undone)

**Effect:**

If the transaction later aborts, the Undo pass will:
- Process log records backward
- Encounter the dummy CLR
- Use its UndoNxtLSN to skip over the entire nested action
- Resume undo from before the nested action began

This ensures that completed structural modifications remain even when the transaction that initiated them rolls back.

**Example—B-Tree Split:**

When inserting into a full B-tree node:
1. Begin nested top action
2. Split the node, creating a new node
3. Update parent pointers
4. Write dummy CLR
5. Insert the original record

If the transaction aborts after the split, the split itself is not undone—the tree structure remains valid. Only the final record insertion is undone.

#### 6.2 Media Recovery

Media recovery handles failures where disk pages are lost or corrupted due to media failures (disk crashes, corruption). ARIES separates media recovery from system crash recovery, allowing each to operate independently.

**Archive Logs:**

Periodically, the system archives portions of the log to stable storage separate from the database disk. Archive logs provide a complete history of updates for media recovery.

**Image Copies (Fuzzy Dumps):**

The system can create fuzzy image copies of the database:
- A fuzzy dump copies database pages while the system continues running
- Pages may be copied at different times (hence "fuzzy")
- Each page in the image copy has its PageLSN recorded
- The dump also records the log's current position

**Media Recovery Process:**

To recover a lost page P:
1. Restore page P from the most recent image copy
2. Note the PageLSN of the restored page (PageLSN_copy)
3. Scan forward in the archive log from a point before PageLSN_copy
4. Redo all updates to page P with LSN > PageLSN_copy
5. Continue until reaching the current end of log

**Key Properties:**

- **Independence:** Media recovery can proceed for individual pages while the rest of the system continues operating
- **Selective Recovery:** Only affected pages need to be restored, not the entire database
- **Integration with Restart:** Media recovery uses the same redo logic as restart recovery
- **No Undo Required:** Lost pages only need redo (they contain committed data from before the failure)

#### 6.3 Operation Logging (Logical Logging)

While the basic ARIES description uses physical logging (before/after images), ARIES also supports operation logging for higher concurrency and efficiency.

**Physical vs. Logical Logging:**

- **Physical (Physiological):** Logs before and after images of bytes/records
  - Simple and reliable
  - Large log records for big updates
  - May limit concurrency (locks cover physical locations)

- **Logical (Operation):** Logs the operation and its parameters
  - Compact log records
  - Enables higher concurrency (locks cover logical entities, not physical locations)
  - More complex redo/undo procedures

**Example—Page-Oriented Physical Logging:**

For a record insertion:
- Log: PageID, Offset, Before: "", After: "record contents"
- Redo: Write the after-image at the offset
- Undo: Write the before-image (delete the record)

**Example—Logical Operation Logging:**

For a record insertion:
- Log: Operation: INSERT, Key: K, Value: V
- Redo: Insert(K, V) into the appropriate page (may be different than original if page reorganized)
- Undo: Delete(K) from the appropriate page

**Benefits of Operation Logging:**

- **Page Reorganization:** Pages can be reorganized between log time and redo time
- **High Concurrency:** Lock granularity matches logical operations (e.g., record-level locks)
- **Index Maintenance:** Insert/delete operations in indexes can use logical logging
- **Smaller Logs:** Operation descriptions often more compact than full images

**Interaction with CLRs:**

CLRs in a system with operation logging contain:
- The logical inverse operation
- Redo information (redoing the undo operation)
- UndoNxtLSN for skipping compensated actions

#### 6.4 Support for Fine-Granularity Locking

ARIES's design specifically enables fine-granularity locking (record-level or key-level locks) through several mechanisms:

**1. Precise Page State Tracking:**
PageLSNs allow the system to determine exactly which operations have been applied, enabling multiple transactions to operate on the same page concurrently.

**2. Operation Logging:**
Logical logging allows locks to cover logical entities (records, keys) rather than physical page locations, maximizing concurrency.

**3. Index Latching:**
ARIES distinguishes between:
- **Locks:** Held for transaction duration, ensure serializability
- **Latches:** Short-term physical locks on pages, ensure physical consistency
Latches can be released immediately after a page update, while logical locks persist.

**4. Nested Top Actions:**
Index structure modifications use nested top actions, preventing structural changes from being undone while still allowing transaction rollback.

**Example—Concurrent B-Tree Operations:**

Two transactions T1 and T2 inserting different keys:
- Both may update the same B-tree page
- Each holds a lock on its respective key
- Page latches ensure one update completes before the other begins
- PageLSNs track the order of updates
- If T1 aborts, only its key insertion is undone (T2's remains)
- If the page was split (nested top action), the split remains

#### 6.5 Restart After Media Recovery

If a system crashes during media recovery, restart recovery proceeds normally:
1. Analysis determines which media recovery operations were in progress
2. Redo repeats the media recovery work (idempotent)
3. Undo is typically not required (media recovery only redoes)

This ensures that media recovery can itself recover from failures.

---

### النسخة العربية

بعيداً عن خوارزمية استرداد إعادة التشغيل الأساسية، تدعم ARIES عدة ميزات متقدمة تمكّن من معالجة واسترداد معاملات متطورة.

#### 6.1 الإجراءات العليا المتداخلة

تسمح الإجراءات العليا المتداخلة لمعاملة بتنفيذ تسلسل من العمليات التي، بمجرد اكتمالها، لا ينبغي التراجع عنها حتى لو أُحبطت المعاملة المُحيطة. هذا ضروري لعمليات مثل:
- تعديلات بنية الفهرس (انقسامات ودمج شجرة B)
- عمليات إدارة المساحة (تخصيص وإلغاء تخصيص الصفحات)
- إعادة تنظيم جداول التجزئة

**الآلية:**

يُحصر إجراء علوي متداخل بعلامات خاصة:
1. قبل بدء الإجراء المتداخل، سجّل LastLSN الحالي كنقطة حفظ
2. نفّذ تسلسل التحديثات ضمن الإجراء المتداخل
3. بعد اكتمال الإجراء المتداخل، اكتب "CLR وهمي" مع:
   - UndoNxtLSN يشير إلى نقطة الحفظ (قبل الإجراء المتداخل)
   - بدون معلومات تراجع فعلية (الإجراء مكتمل ولا ينبغي التراجع عنه)

**التأثير:**

إذا أُحبطت المعاملة لاحقاً، فإن مرحلة التراجع ستقوم بـ:
- معالجة سجلات السجل للخلف
- مواجهة CLR الوهمي
- استخدام UndoNxtLSN الخاص به لتخطي الإجراء المتداخل بأكمله
- استئناف التراجع من قبل بدء الإجراء المتداخل

يضمن هذا بقاء التعديلات البنيوية المكتملة حتى عندما تتراجع المعاملة التي بدأتها.

**مثال—انقسام شجرة B:**

عند الإدراج في عقدة شجرة B ممتلئة:
1. ابدأ إجراء علوي متداخل
2. قسّم العقدة، منشئاً عقدة جديدة
3. حدّث مؤشرات الأب
4. اكتب CLR وهمي
5. أدرج السجل الأصلي

إذا أُحبطت المعاملة بعد الانقسام، فإن الانقسام نفسه لا يُتراجع عنه—تبقى بنية الشجرة صالحة. فقط إدراج السجل النهائي يُتراجع عنه.

#### 6.2 استرداد الوسائط

يتعامل استرداد الوسائط مع الفشل حيث تُفقد أو تتلف صفحات القرص بسبب فشل الوسائط (أعطال القرص، التلف). تفصل ARIES استرداد الوسائط عن استرداد أعطال النظام، مما يسمح لكل منهما بالعمل بشكل مستقل.

**سجلات الأرشيف:**

بشكل دوري، يُؤرشف النظام أجزاء من السجل إلى تخزين مستقر منفصل عن قرص قاعدة البيانات. توفر سجلات الأرشيف سجلاً كاملاً للتحديثات لاسترداد الوسائط.

**نسخ الصور (تفريغات ضبابية):**

يمكن للنظام إنشاء نسخ صور ضبابية لقاعدة البيانات:
- يقوم التفريغ الضبابي بنسخ صفحات قاعدة البيانات بينما يستمر النظام في العمل
- قد تُنسخ الصفحات في أوقات مختلفة (ومن هنا "ضبابية")
- يُسجل PageLSN لكل صفحة في نسخة الصورة
- يسجل التفريغ أيضاً الموضع الحالي للسجل

**عملية استرداد الوسائط:**

لاسترداد صفحة مفقودة P:
1. استعد الصفحة P من أحدث نسخة صورة
2. لاحظ PageLSN للصفحة المستعادة (PageLSN_copy)
3. امسح للأمام في سجل الأرشيف من نقطة قبل PageLSN_copy
4. أعد جميع التحديثات على الصفحة P مع LSN > PageLSN_copy
5. استمر حتى الوصول إلى النهاية الحالية للسجل

**الخصائص الرئيسية:**

- **الاستقلالية:** يمكن أن يستمر استرداد الوسائط لصفحات فردية بينما يستمر باقي النظام في العمل
- **الاسترداد الانتقائي:** فقط الصفحات المتأثرة تحتاج إلى الاستعادة، وليس قاعدة البيانات بأكملها
- **التكامل مع إعادة التشغيل:** يستخدم استرداد الوسائط نفس منطق الإعادة الخاص باسترداد إعادة التشغيل
- **لا حاجة للتراجع:** الصفحات المفقودة تحتاج فقط للإعادة (تحتوي على بيانات مُنهاة من قبل الفشل)

#### 6.3 تسجيل العمليات (التسجيل المنطقي)

بينما يستخدم وصف ARIES الأساسي التسجيل الفيزيائي (صور قبل/بعد)، تدعم ARIES أيضاً تسجيل العمليات لتزامن وكفاءة أعلى.

**التسجيل الفيزيائي مقابل المنطقي:**

- **الفيزيائي (الفسيولوجي):** يسجل صور قبل وبعد للبايتات/السجلات
  - بسيط وموثوق
  - سجلات سجل كبيرة للتحديثات الكبيرة
  - قد يحد من التزامن (الأقفال تغطي المواقع الفيزيائية)

- **المنطقي (العملية):** يسجل العملية ومعاملاتها
  - سجلات سجل مدمجة
  - يمكّن تزامناً أعلى (الأقفال تغطي الكيانات المنطقية، وليس المواقع الفيزيائية)
  - إجراءات إعادة/تراجع أكثر تعقيداً

**مثال—التسجيل الفيزيائي الموجه للصفحات:**

لإدراج سجل:
- السجل: PageID، Offset، قبل: ""، بعد: "محتويات السجل"
- الإعادة: اكتب صورة-بعد في الإزاحة
- التراجع: اكتب صورة-قبل (احذف السجل)

**مثال—تسجيل العمليات المنطقية:**

لإدراج سجل:
- السجل: العملية: INSERT، المفتاح: K، القيمة: V
- الإعادة: Insert(K, V) في الصفحة المناسبة (قد تكون مختلفة عن الأصلية إذا أُعيد تنظيم الصفحة)
- التراجع: Delete(K) من الصفحة المناسبة

**فوائد تسجيل العمليات:**

- **إعادة تنظيم الصفحة:** يمكن إعادة تنظيم الصفحات بين وقت التسجيل ووقت الإعادة
- **تزامن عالٍ:** تتطابق دقة القفل مع العمليات المنطقية (مثل أقفال مستوى السجل)
- **صيانة الفهرس:** يمكن لعمليات الإدراج/الحذف في الفهارس استخدام التسجيل المنطقي
- **سجلات أصغر:** أوصاف العمليات غالباً أكثر إحكاماً من الصور الكاملة

**التفاعل مع CLRs:**

تحتوي CLRs في نظام مع تسجيل العمليات على:
- العملية المنطقية العكسية
- معلومات الإعادة (إعادة عملية التراجع)
- UndoNxtLSN لتخطي الإجراءات المعوّضة

#### 6.4 دعم القفل دقيق التفصيل

يمكّن تصميم ARIES بشكل خاص القفل دقيق التفصيل (أقفال مستوى السجل أو مستوى المفتاح) من خلال عدة آليات:

**1. تتبع حالة الصفحة الدقيق:**
تسمح PageLSNs للنظام بتحديد العمليات التي تم تطبيقها بالضبط، مما يمكّن معاملات متعددة من العمل على نفس الصفحة بشكل متزامن.

**2. تسجيل العمليات:**
يسمح التسجيل المنطقي للأقفال بتغطية الكيانات المنطقية (السجلات، المفاتيح) بدلاً من مواقع الصفحات الفيزيائية، مما يزيد التزامن إلى أقصى حد.

**3. إغلاق الفهرس:**
تميز ARIES بين:
- **الأقفال:** محتفظ بها لمدة المعاملة، تضمن القابلية للتسلسل
- **المزالج:** أقفال فيزيائية قصيرة المدى على الصفحات، تضمن الاتساق الفيزيائي
يمكن إطلاق المزالج فوراً بعد تحديث الصفحة، بينما تستمر الأقفال المنطقية.

**4. الإجراءات العليا المتداخلة:**
تستخدم تعديلات بنية الفهرس إجراءات عليا متداخلة، مما يمنع التراجع عن التغييرات البنيوية مع السماح لا يزال بالتراجع عن المعاملات.

**مثال—عمليات شجرة B المتزامنة:**

معاملتان T1 و T2 تُدرجان مفاتيح مختلفة:
- قد يقوم كلاهما بتحديث نفس صفحة شجرة B
- يحتفظ كل منهما بقفل على مفتاحه الخاص
- تضمن مزالج الصفحات اكتمال تحديث واحد قبل بدء الآخر
- تتتبع PageLSNs ترتيب التحديثات
- إذا أُحبطت T1، فقط إدراج مفتاحها يُتراجع عنه (يبقى إدراج T2)
- إذا انقسمت الصفحة (إجراء علوي متداخل)، يبقى الانقسام

#### 6.5 إعادة التشغيل بعد استرداد الوسائط

إذا تعطل نظام أثناء استرداد الوسائط، يستمر استرداد إعادة التشغيل بشكل طبيعي:
1. يحدد التحليل عمليات استرداد الوسائط التي كانت قيد التنفيذ
2. تكرر الإعادة عمل استرداد الوسائط (متساوية القوة)
3. التراجع غير مطلوب عادة (استرداد الوسائط يعيد فقط)

يضمن هذا أن استرداد الوسائط يمكنه نفسه الاسترداد من الفشل.

---

### Translation Notes

- **Advanced Concepts:**
  - Nested top action → إجراء علوي متداخل
  - Dummy CLR → CLR وهمي (placeholder CLR with no undo info)
  - Fuzzy dump → تفريغ ضبابي (backup taken while system running)
  - Archive log → سجل الأرشيف
  - Image copy → نسخة صورة

- **Locking vs. Latching:**
  - Lock → قفل (transaction-duration, logical)
  - Latch → مزلاج (short-term, physical)

- **Logging Types:**
  - Physical logging → التسجيل الفيزيائي
  - Logical logging → التسجيل المنطقي
  - Physiological → الفسيولوجي (page-oriented physical)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.86
