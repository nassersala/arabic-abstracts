# Section 6: Encapsulation in a Graphical Tooling Environment
## القسم 6: التغليف في بيئة أدوات رسومية

**Section:** tooling
**Translation Quality:** 0.86
**Glossary Terms Used:** graphical editor (محرر رسومي), domain specific language (لغة خاصة بالمجال), model transformation (تحويل النماذج), GMF (إطار النمذجة الرسومية), Epsilon (إبسيلون), OnTrack (OnTrack), verification (التحقق), automated verification (التحقق الآلي)

---

### English Version

**Introduction**

In this section we discuss the last step of our methodology namely the design and implementation of graphical tool support for the developed DSL.

**6.1 Background: GMF and Epsilon**

The Graphical Modeling Framework (GMF) is an Eclipse-based framework for developing graphical editors for domain-specific modeling languages. GMF generates a Java-based graphical editor from:
- A domain model (UML class diagram)
- A graphical definition (visual representation)
- A tooling definition (palette items)
- A mapping between these elements

Epsilon is a family of languages and tools for model management. The Epsilon Transformation Language (ETL) allows transformation between different modeling languages. We use Epsilon to transform models created in the GMF editor into CASL specifications.

**6.2 Contribution: The OnTrack Tool**

OnTrack is a graphical tool for railway scheme plan modeling and verification that implements our methodology. It consists of:

**Graphical Editor:** Built using GMF, the editor provides a visual interface for creating railway scheme plans. Engineers can:
- Draw track layouts with linear units, points, and connectors
- Define routes with control and release tables
- Specify movement authorities

The editor uses railway-specific visual notation familiar to domain engineers, lowering the barrier to entry.

**Model Transformation:** Using Epsilon ETL, graphical models are automatically transformed into CASL specifications. The transformation:
- Maps visual elements to CASL sorts and operations
- Generates axioms from the scheme plan structure
- Incorporates the domain-specific lemmas
- Creates the safety property to be verified

**Verification Integration:** OnTrack integrates with HETS for automated verification:
- Generated CASL specifications are passed to HETS
- HETS invokes SPASS for automated proof
- Results are returned to the user
- Failed proofs identify unsafe scheme plans

**6.3 Contribution: Verification Results**

We have verified numerous railway scheme plans using OnTrack, including:
- The example station from Figure 4 (verified safe)
- Larger stations with 10+ routes (verified safe)
- Intentionally unsafe configurations (correctly identified as unsafe)

Verification times range from seconds for small stations to minutes for larger configurations. The automation enabled by domain lemmas makes verification scalable and practical.

**Performance:** For a typical station with 5 routes:
- Model creation: 5-10 minutes (manual drawing)
- Translation to CASL: < 1 second (automatic)
- Verification: 2-5 seconds (automatic)

This demonstrates that the verification process is efficient enough for practical use in railway engineering workflows.

**User Feedback:** Railway engineers from Invensys Rail have evaluated OnTrack and confirmed:
- The graphical notation is familiar and usable
- The verification process is accessible (no formal methods expertise required)
- The automated nature makes it practical for real projects
- Integration with existing workflows (via XLDL import/export) would increase adoption

The OnTrack tool successfully demonstrates that formal methods can be made accessible to domain practitioners through appropriate encapsulation in domain-specific tooling.

---

### النسخة العربية

**مقدمة**

في هذا القسم نناقش الخطوة الأخيرة من منهجيتنا وهي تصميم وتنفيذ دعم الأدوات الرسومية للغة الخاصة بالمجال المطورة.

**6.1 خلفية: GMF و Epsilon**

إطار النمذجة الرسومية (GMF) هو إطار عمل قائم على Eclipse لتطوير محررات رسومية للغات النمذجة الخاصة بالمجال. يُنشئ GMF محررًا رسوميًا قائمًا على Java من:
- نموذج المجال (مخطط فئات UML)
- تعريف رسومي (تمثيل بصري)
- تعريف الأدوات (عناصر اللوحة)
- تعيين بين هذه العناصر

Epsilon هي عائلة من اللغات والأدوات لإدارة النماذج. تسمح لغة تحويل Epsilon (ETL) بالتحويل بين لغات النمذجة المختلفة. نستخدم Epsilon لتحويل النماذج المُنشأة في محرر GMF إلى مواصفات CASL.

**6.2 المساهمة: أداة OnTrack**

OnTrack هي أداة رسومية لنمذجة والتحقق من مخططات خطط السكك الحديدية التي تنفذ منهجيتنا. تتكون من:

**المحرر الرسومي:** مبني باستخدام GMF، يوفر المحرر واجهة بصرية لإنشاء مخططات خطط السكك الحديدية. يمكن للمهندسين:
- رسم تخطيطات المسار مع الوحدات الخطية والنقاط والموصلات
- تعريف المسارات مع جداول التحكم والإفراج
- تحديد سلطات الحركة

يستخدم المحرر ترميزًا بصريًا خاصًا بالسكك الحديدية مألوفًا لمهندسي المجال، مما يقلل من حاجز الدخول.

**تحويل النموذج:** باستخدام Epsilon ETL، يتم تحويل النماذج الرسومية تلقائيًا إلى مواصفات CASL. يقوم التحويل بـ:
- تعيين العناصر المرئية إلى أنواع وعمليات CASL
- توليد بديهيات من بنية مخطط الخطة
- دمج اللمّات الخاصة بالمجال
- إنشاء خاصية السلامة المراد التحقق منها

**تكامل التحقق:** يتكامل OnTrack مع HETS للتحقق الآلي:
- يتم تمرير مواصفات CASL المُولّدة إلى HETS
- يستدعي HETS SPASS للإثبات الآلي
- يتم إرجاع النتائج إلى المستخدم
- تحدد الإثباتات الفاشلة مخططات الخطط غير الآمنة

**6.3 المساهمة: نتائج التحقق**

تحققنا من العديد من مخططات خطط السكك الحديدية باستخدام OnTrack، بما في ذلك:
- المحطة المثال من الشكل 4 (تم التحقق من أمانها)
- محطات أكبر مع أكثر من 10 مسارات (تم التحقق من أمانها)
- تكوينات غير آمنة عمدًا (تم تحديدها بشكل صحيح على أنها غير آمنة)

تتراوح أوقات التحقق من ثوانٍ للمحطات الصغيرة إلى دقائق للتكوينات الأكبر. تجعل الأتمتة الممكنة بواسطة لمّات المجال التحقق قابلاً للتوسع وعمليًا.

**الأداء:** بالنسبة لمحطة نموذجية ذات 5 مسارات:
- إنشاء النموذج: 5-10 دقائق (رسم يدوي)
- الترجمة إلى CASL: أقل من ثانية واحدة (تلقائي)
- التحقق: 2-5 ثوانٍ (تلقائي)

يوضح هذا أن عملية التحقق كفؤة بما يكفي للاستخدام العملي في سير عمل هندسة السكك الحديدية.

**تعليقات المستخدمين:** قيّم مهندسو السكك الحديدية من Invensys Rail أداة OnTrack وأكدوا:
- الترميز الرسومي مألوف وقابل للاستخدام
- عملية التحقق متاحة (لا حاجة لخبرة في الأساليب الرسمية)
- الطبيعة الآلية تجعلها عملية للمشاريع الحقيقية
- التكامل مع سير العمل الحالي (عبر استيراد/تصدير XLDL) سيزيد من الاعتماد

توضح أداة OnTrack بنجاح أن الأساليب الرسمية يمكن جعلها متاحة لممارسي المجال من خلال التغليف المناسب في الأدوات الخاصة بالمجال.

---

### Translation Notes

- **Key tools:** GMF (Graphical Modeling Framework), Epsilon, OnTrack, HETS, SPASS
- **Main components:** Graphical editor, model transformation, verification integration
- **Performance metrics:** Model creation time, translation time, verification time
- **User evaluation:** Feedback from industrial partner Invensys Rail
- **Integration:** XLDL import/export for workflow integration

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
