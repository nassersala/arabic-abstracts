# Section 5: Automating Verification for the Signalling Domain
## القسم 5: أتمتة التحقق لمجال الإشارات

**Section:** verification
**Translation Quality:** 0.87
**Glossary Terms Used:** automated theorem proving (إثبات النظريات الآلي), verification (التحقق), domain knowledge (معرفة المجال), lemmas (لمّات), scalability (قابلية التوسع), proof support (دعم الإثبات), CASL (CASL), HETS (HETS), SPASS (SPASS)

---

### English Version

**Introduction**

We now consider the task of verifying our safety property over models formulated using our formal DSL. We begin by introducing the proof support that is available for CASL. We then show that verification is only possible thanks to exploitation of domain specific lemmas that we introduce thanks to domain knowledge.

**5.1 Background: Theorem Proving for CASL**

The Heterogeneous Toolset (HETS) provides proof support for CASL specifications. HETS integrates various theorem provers including SPASS (an automated first-order theorem prover) and Isabelle (an interactive theorem prover). For our railway verification, we primarily use SPASS for automated proof attempts.

HETS allows us to:
- Parse and type-check CASL specifications
- Translate specifications to theorem prover formats
- Manage proof attempts and results
- Provide feedback on failed proofs

The integration with automated theorem provers enables "push-button" verification when appropriate lemmas are available.

**5.2 Contribution: Unsuccessful Verification Attempts**

Initial attempts to verify the safety property directly using automated theorem proving failed. The property stating that "overlapping movement authorities are not assigned at the same time" could not be proven automatically for arbitrary railway configurations.

The reasons for this failure include:
- The specification is too abstract and general
- The proof search space is too large
- Domain-specific insights are not captured in the basic formalization

This demonstrates that naive application of formal methods is insufficient - domain knowledge must be explicitly captured to enable scalable verification.

**5.3 Contribution: Supporting Verification with Domain-Specific Lemmas**

We introduce domain-specific lemmas that capture implicit knowledge about railway operations. These lemmas refactor the verification problem into manageable pieces. Key lemmas include:

**Lemma 1 (Route Disjointness):** Routes that share no track units cannot have overlapping movement authorities.

**Lemma 2 (Control Table Correctness):** If the control table is correctly specified, then routes assigned according to the control table rules do not conflict.

**Lemma 3 (Release Monotonicity):** Release operations only decrease the extent of movement authorities, never increase them.

**Lemma 4 (Extension Safety):** Movement authority extension preserves the non-overlapping property if the route being added does not conflict with existing routes.

These lemmas are proven once using a combination of automated and interactive theorem proving. Once proven, they enable automatic verification of specific railway configurations by reducing complex proofs to simpler checks that can be discharged automatically by SPASS.

**Verification Process**

With the domain-specific lemmas in place, verification of a railway scheme plan proceeds as follows:

1. The graphical model is translated to CASL specification
2. The specification is enriched with domain lemmas
3. The safety property is posed as a theorem
4. HETS invokes SPASS to attempt automated proof
5. The proof succeeds by applying the domain lemmas

This demonstrates that scalable verification is achieved through systematic exploitation of domain knowledge captured as lemmas. The verification becomes "push-button" from the user's perspective, while the underlying proof uses domain-specific insights.

---

### النسخة العربية

**مقدمة**

نعتبر الآن مهمة التحقق من خاصية السلامة لدينا على النماذج المصاغة باستخدام لغتنا الخاصة بالمجال الرسمية. نبدأ بتقديم دعم الإثبات المتاح لـ CASL. ثم نظهر أن التحقق ممكن فقط بفضل استغلال اللمّات الخاصة بالمجال التي نقدمها بفضل معرفة المجال.

**5.1 خلفية: إثبات النظريات لـ CASL**

توفر مجموعة الأدوات غير المتجانسة (HETS) دعم الإثبات لمواصفات CASL. يدمج HETS مُثبتات النظريات المختلفة بما في ذلك SPASS (مُثبت نظريات من الدرجة الأولى آلي) و Isabelle (مُثبت نظريات تفاعلي). للتحقق من السكك الحديدية لدينا، نستخدم في المقام الأول SPASS لمحاولات الإثبات الآلي.

يسمح لنا HETS بـ:
- تحليل والتحقق من نوع مواصفات CASL
- ترجمة المواصفات إلى تنسيقات مُثبت النظريات
- إدارة محاولات الإثبات والنتائج
- تقديم تعليقات على الإثباتات الفاشلة

يمكّن التكامل مع مُثبتات النظريات الآلية من التحقق "بضغطة زر" عندما تكون اللمّات المناسبة متاحة.

**5.2 المساهمة: محاولات التحقق غير الناجحة**

فشلت المحاولات الأولية للتحقق من خاصية السلامة مباشرة باستخدام إثبات النظريات الآلي. لم يكن من الممكن إثبات الخاصية التي تنص على أن "سلطات الحركة المتداخلة لا يتم تعيينها في نفس الوقت" تلقائيًا لتكوينات السكك الحديدية التعسفية.

تشمل أسباب هذا الفشل:
- المواصفات مجردة جدًا وعامة جدًا
- مساحة بحث الإثبات كبيرة جدًا
- لا يتم التقاط الرؤى الخاصة بالمجال في الصياغة الرسمية الأساسية

يوضح هذا أن التطبيق الساذج للأساليب الرسمية غير كافٍ - يجب التقاط معرفة المجال بشكل صريح لتمكين التحقق القابل للتوسع.

**5.3 المساهمة: دعم التحقق باللمّات الخاصة بالمجال**

نقدم لمّات خاصة بالمجال تلتقط المعرفة الضمنية حول عمليات السكك الحديدية. تعيد هذه اللمّات صياغة مشكلة التحقق إلى قطع يمكن إدارتها. تشمل اللمّات الرئيسية:

**اللمّة 1 (انفصال المسار):** المسارات التي لا تشترك في وحدات مسار لا يمكن أن يكون لها سلطات حركة متداخلة.

**اللمّة 2 (صحة جدول التحكم):** إذا تم تحديد جدول التحكم بشكل صحيح، فإن المسارات المعينة وفقًا لقواعد جدول التحكم لا تتعارض.

**اللمّة 3 (أحادية الإفراج):** عمليات الإفراج تقلل فقط من مدى سلطات الحركة، ولا تزيدها أبدًا.

**اللمّة 4 (سلامة التمديد):** تمديد سلطة الحركة يحافظ على خاصية عدم التداخل إذا كان المسار المضاف لا يتعارض مع المسارات الموجودة.

يتم إثبات هذه اللمّات مرة واحدة باستخدام مزيج من إثبات النظريات الآلي والتفاعلي. بمجرد إثباتها، تمكّن من التحقق التلقائي من تكوينات السكك الحديدية المحددة عن طريق تقليل الإثباتات المعقدة إلى فحوصات أبسط يمكن تفريغها تلقائيًا بواسطة SPASS.

**عملية التحقق**

مع وجود اللمّات الخاصة بالمجال في مكانها، يتم التحقق من مخطط خطة السكك الحديدية على النحو التالي:

1. يتم ترجمة النموذج الرسومي إلى مواصفات CASL
2. يتم إثراء المواصفات بلمّات المجال
3. يتم طرح خاصية السلامة كنظرية
4. يستدعي HETS SPASS لمحاولة الإثبات الآلي
5. ينجح الإثبات بتطبيق لمّات المجال

يوضح هذا أن التحقق القابل للتوسع يتحقق من خلال الاستغلال المنهجي لمعرفة المجال الملتقطة كلمّات. يصبح التحقق "بضغطة زر" من وجهة نظر المستخدم، بينما يستخدم الإثبات الأساسي رؤى خاصة بالمجال.

---

### Translation Notes

- **Key tools:** HETS (Heterogeneous Toolset), SPASS (automated theorem prover), Isabelle
- **Main concepts:** Domain-specific lemmas, proof support, automated verification, scalability
- **Lemmas:** Four key domain lemmas identified and formalized
- **Process:** Verification workflow from model to automated proof

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
