# Section 4: Counterexample Explanation in a Nutshell
## القسم 4: تفسير الأمثلة المضادة في إيجاز

**Section:** counterexample explanation approach
**Translation Quality:** 0.87
**Glossary Terms Used:** contract-based design (CBD), model checking, counterexample, refinement, specification, Kripke structure, Linear Temporal Logic (LTL), pattern-based language

---

### English Version

Contract-based design (CBD) (Cimatti and Tonetta 2012) is a scalable solution to overcome a manual analysis by automatically and compositionally verifying the consistency of system and requirement refinements using model checking. Thus, CBD provides assurances for consistent refinements early in the development process, which promises to ease corresponding testing activities at later stages. However, using such a formal method in industry is challenging due to usability issues, e.g., the difficulty of understanding model checking results. Thus, we have proposed a counterexample explanation approach that eases the error comprehension of engineers—especially of non-experts in formal methods—if the refinement check fails. The approach generates a user-friendly explanation that localizes the fault at the levels of requirements and components. Examples of a CBD and explanations of counterexamples will be given in the context of the study in Section 7.

The counterexample explanation approach comprises of six steps illustrated in Figure 1. Steps ① and ⑥ are performed manually while the other steps are completely automated. Step ① is the translation of CBD by importing SysML models from Rhapsody and DNG requirements into FASTEN (Ratiu et al. 2021). FASTEN is an open-source platform to experiment with rigorous modeling of safety-critical systems. Translating the (largely informal) requirements from DNG into contracts is a manual effort, further detailed in the context of Bosch by Post et al. (2012); Post and Hoenicke (2012). CBD languages provided by FASTEN allow us to model component-based architectures, requirements as contracts (assumptions and guarantees), and refinements, hence creating a CBD. After the design, in Step ②, FASTEN automatically translates a CBD to a formal system model K and refinement specification that allows model checking by NuSMV/nuXMV in Step ③. This refinement specification follows the scheme by Cimatti and Tonetta (2012) who define a refinement check by a set of LTL formulae (Kaleeswaran et al. 2020, Section 2). If the model checker identifies any refinement inconsistency during the verification, it returns the violated LTL refinement specification and the counterexample.

Taking the violated LTL refinement specification and counterexample as input, the counterexample explanation approach extracts erroneous parts in Step ④. To extract such parts, we identify (i) the inconsistent specifications in the violated LTL refinement specification, (ii) inconsistent sub-specifications in the inconsistent specifications, (iii) erroneous contracts and components by using the inconsistent specifications and by referring to the refinement formula, (iv) erroneous states in the counterexample, and (v) erroneous variables by using the inconsistent sub-specifications (cf. 4A–4E in Figure 1).

Finally in Step ⑤, a statement is generated explaining inconsistency along with the counterexample highlighting erroneous states and erroneous variables. The generated statement consists of the erroneous components, violated contract information, and inconsistent specifications expressed in a pattern-based language referring to requirements and SysML model being the initial user input of the approach (cf. ① in Figure 1). Finally, the inconsistent sub-specifications are highlighted in the pattern-based expression. With the statement, the engineer gets a high-level understanding of the refinement inconsistency. Further, the counterexample with highlighted erroneous parts supports the engineer in understanding the erroneous behavior of the system. Finally, the engineer can correct the refinement inconsistencies by remodeling the component model and changing the requirements (cf. ⑥ in Figure 1). To ensure the correctness of the changes, the engineer re-verifies the changed refinement.

---

### النسخة العربية

التصميم القائم على العقود (CBD) (سيماتي وتونيتا 2012) هو حل قابل للتوسع للتغلب على التحليل اليدوي من خلال التحقق التلقائي والتركيبي من اتساق تحسينات النظام والمتطلبات باستخدام فحص النماذج. وبالتالي، يوفر CBD ضمانات للتحسينات المتسقة في وقت مبكر من عملية التطوير، مما يَعِد بتسهيل أنشطة الاختبار المقابلة في المراحل اللاحقة. ومع ذلك، فإن استخدام مثل هذا الأسلوب الرسمي في الصناعة يُعد تحدياً بسبب مشاكل قابلية الاستخدام، على سبيل المثال، صعوبة فهم نتائج فحص النماذج. لذلك، اقترحنا نهج تفسير الأمثلة المضادة الذي يُسهل فهم الأخطاء للمهندسين - خاصة غير الخبراء في الأساليب الرسمية - إذا فشل فحص التحسين. ينتج النهج تفسيراً سهل الاستخدام يُحدد موقع الخلل على مستويات المتطلبات والمكونات. ستُقدم أمثلة على CBD وتفسيرات الأمثلة المضادة في سياق الدراسة في القسم 7.

يتكون نهج تفسير الأمثلة المضادة من ست خطوات موضحة في الشكل 1. تُنفذ الخطوتان ① و⑥ يدوياً بينما الخطوات الأخرى آلية تماماً. الخطوة ① هي ترجمة CBD من خلال استيراد نماذج SysML من Rhapsody ومتطلبات DNG إلى FASTEN (راتيو وآخرون 2021). FASTEN هي منصة مفتوحة المصدر للتجريب مع النمذجة الصارمة للأنظمة الحرجة من حيث السلامة. ترجمة المتطلبات (غير الرسمية إلى حد كبير) من DNG إلى عقود هو جهد يدوي، مُفصل أكثر في سياق بوش من قبل بوست وآخرون (2012)؛ بوست وهونيكي (2012). تسمح لغات CBD التي توفرها FASTEN بنمذجة المعماريات القائمة على المكونات، والمتطلبات كعقود (افتراضات وضمانات)، والتحسينات، وبالتالي إنشاء CBD. بعد التصميم، في الخطوة ②، تُترجم FASTEN تلقائياً CBD إلى نموذج نظام رسمي K ومواصفة تحسين تسمح بفحص النماذج بواسطة NuSMV/nuXMV في الخطوة ③. تتبع مواصفة التحسين هذه المخطط الذي وضعه سيماتي وتونيتا (2012) الذين يُعرّفون فحص التحسين من خلال مجموعة من صيغ LTL (كالسواران وآخرون 2020، القسم 2). إذا حدد فاحص النماذج أي تعارض في التحسين أثناء التحقق، فإنه يُرجع مواصفة تحسين LTL المُنتهكة والمثال المضاد.

بأخذ مواصفة تحسين LTL المُنتهكة والمثال المضاد كمدخلات، يستخرج نهج تفسير الأمثلة المضادة الأجزاء الخاطئة في الخطوة ④. لاستخراج هذه الأجزاء، نحدد (i) المواصفات غير المتسقة في مواصفة تحسين LTL المُنتهكة، (ii) المواصفات الفرعية غير المتسقة في المواصفات غير المتسقة، (iii) العقود والمكونات الخاطئة باستخدام المواصفات غير المتسقة وبالإشارة إلى صيغة التحسين، (iv) الحالات الخاطئة في المثال المضاد، و(v) المتغيرات الخاطئة باستخدام المواصفات الفرعية غير المتسقة (راجع 4A-4E في الشكل 1).

أخيراً في الخطوة ⑤، يتم إنشاء بيان يشرح التعارض مع المثال المضاد الذي يبرز الحالات الخاطئة والمتغيرات الخاطئة. يتكون البيان المُنتَج من المكونات الخاطئة، ومعلومات العقد المُنتهك، والمواصفات غير المتسقة المُعبر عنها بلغة قائمة على الأنماط تشير إلى المتطلبات ونموذج SysML الذي يكون المدخل الأولي للمستخدم للنهج (راجع ① في الشكل 1). أخيراً، يتم إبراز المواصفات الفرعية غير المتسقة في التعبير القائم على الأنماط. مع البيان، يحصل المهندس على فهم عالي المستوى لتعارض التحسين. علاوة على ذلك، يدعم المثال المضاد مع الأجزاء الخاطئة المُبرزة المهندس في فهم السلوك الخاطئ للنظام. أخيراً، يمكن للمهندس تصحيح تعارضات التحسين من خلال إعادة نمذجة نموذج المكون وتغيير المتطلبات (راجع ⑥ في الشكل 1). لضمان صحة التغييرات، يُعيد المهندس التحقق من التحسين المُعدل.

---

### Translation Notes

- **Figures referenced:** Figure 1 (flowchart showing 6-step counterexample explanation approach)
- **Key terms introduced:**
  - error comprehension = فهم الأخطاء
  - user-friendly explanation = تفسير سهل الاستخدام
  - fault localization = تحديد موقع الخلل
  - component-based architectures = المعماريات القائمة على المكونات
  - erroneous states = الحالات الخاطئة
  - erroneous variables = المتغيرات الخاطئة
  - erroneous components = المكونات الخاطئة
  - inconsistent sub-specifications = المواصفات الفرعية غير المتسقة
  - high-level understanding = فهم عالي المستوى

- **Equations:** None
- **Citations:** 5 references cited
- **Special handling:**
  - Tool names (FASTEN, Rhapsody, DNG, NuSMV, nuXMV) kept in English
  - Step numbering (①-⑥) preserved as in original
  - Figure 1 references maintained throughout
  - Technical workflow described with precision

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
