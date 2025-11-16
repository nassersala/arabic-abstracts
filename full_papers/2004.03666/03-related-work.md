# Section 3: Related Work
## القسم 3: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** component interoperability (تشغيل بيني للمكونات), formal methods (الأساليب الرسمية), model checking (فحص النماذج), compositional state modeling (نمذجة الحالة التركيبية), distributed systems (أنظمة موزعة)

---

### English Version

**Related Work on Component Interoperability**

The need to modularize software and hardware development to foster interoperability has driven a variety of research and standardization efforts. Notably, the FACE Technical Standard standardizes the concept of a Unit of Portability, a software component whose interface is defined using a standardized modeling language [16]. The well-defined boundary of FACE Units of Portability enables compositional analysis earlier than would otherwise be possible [25]. Similarly, the Hardware Open Systems Technologies (HOST) standard defines an approach for modular hardware components [14].

**Related Work on Application of Formal Methods**

A variety of efforts have explored the potential of formal methods application to avionics engineering. The Defense Advanced Research Projects Agency (DARPA) High-Assurance Cyber Military Systems (HACMS) project successfully generated code from a formally verified model of assume-guarantee contracts [13]. The HACMS project used a tool called Assume Guarantee Reasoning Environment (AGREE) developed by Collins Aerospace that generates formal, invariant-oriented specifications from AADL models. AGREE generates the formal specification from the model, but is not capable of reasoning about infinite time conditions and requires that the user explicitly state assumptions and guarantees about system conditions. Vestal describes application of finite state automata to embedded software scheduling [27]. Boddy et al. generated a processor schedule using a formal problem specification derived from an AADL model [7]. Boddy's approach treats existing properties in an AADL model such as periodic thread deadlines as constraints and uses them to express a scheduling problem in terms of constraints derived from the model.

**Related Work on Model Checking**

This paper uses NuSMV, a symbolic model checker that supports Linear Temporal Logic (LTL) and Computation Tree Logic (CTL) model checking [11]. A variety of prior efforts use NuSMV. For example, Szpyrka et al. describe a process for generating NuSMV specifications from Petri Nets [26]. Most closely related to this project, Meenakshi et al describe a similar methodology for translating Simulink models to NuSMV in [19]. However, the methodology described by Meenakshi et al is focused on naive NuSMV generation from a given Simulink model.

**Related Work on Compositional State Modeling**

Ranganath et al. described an approach to modeling communication patterns of medical devices [24]. Ranganath's approach aims to reduce the computational burden of reasoning about integrated systems by abstracting details behind standardized interfaces. Beurdouche et al. used a compositional approach to modeling the state of Transport Layer Security (TLS) communication, creating a composite state machine by assembling state machines of individual components [4].

**SLICED as Associated to Related Work**

The aim of SLICED and the focus on this paper is on generation of abstract, interoperable specifications to allow formal analysis of systems composed of models from multiple parties. SLICED is an extension of the interface specification approaches of FACE and HOST with an aim of enabling analysis akin to that performed by Beurdouche. SLICED uses a modularization approach similar to the communication patterns described by Ranganath, abstracting the patterns into standardized components akin to those specified by AADL.

---

### النسخة العربية

**الأعمال ذات الصلة بالتشغيل البيني للمكونات**

دفعت الحاجة إلى تعديل تطوير البرمجيات والأجهزة لتعزيز التشغيل البيني مجموعة متنوعة من جهود البحث والتوحيد القياسي. والجدير بالذكر أن المعيار الفني لـ FACE يوحد مفهوم وحدة النقل، وهي مكون برمجي يتم تحديد واجهته باستخدام لغة نمذجة موحدة [16]. تمكن الحدود المحددة جيداً لوحدات النقل في FACE من التحليل التركيبي في وقت أبكر مما كان ممكناً بخلاف ذلك [25]. وبالمثل، يحدد معيار تقنيات الأنظمة المفتوحة للأجهزة (HOST) نهجاً للمكونات الأجهزة المعيارية [14].

**الأعمال ذات الصلة بتطبيق الأساليب الرسمية**

استكشفت مجموعة متنوعة من الجهود إمكانات تطبيق الأساليب الرسمية على هندسة إلكترونيات الطيران. نجح مشروع الأنظمة العسكرية السيبرانية عالية الضمان (HACMS) التابع لوكالة مشاريع الأبحاث الدفاعية المتقدمة (DARPA) في توليد الشفرة من نموذج تم التحقق منه رسمياً لعقود الافتراض والضمان [13]. استخدم مشروع HACMS أداة تسمى بيئة استدلال الافتراض والضمان (AGREE) طورتها Collins Aerospace التي تولد مواصفات رسمية موجهة نحو الثوابت من نماذج AADL. تولد AGREE المواصفات الرسمية من النموذج، ولكنها غير قادرة على الاستدلال حول شروط الوقت اللانهائي وتتطلب أن يذكر المستخدم صراحةً الافتراضات والضمانات حول شروط النظام. يصف Vestal تطبيق آلات الحالة المحدودة على جدولة البرمجيات المدمجة [27]. ولَّد Boddy وآخرون جدولاً للمعالج باستخدام مواصفة مسألة رسمية مشتقة من نموذج AADL [7]. يتعامل نهج Boddy مع الخصائص الموجودة في نموذج AADL مثل المواعيد النهائية للخيوط الدورية كقيود ويستخدمها للتعبير عن مسألة جدولة من حيث القيود المشتقة من النموذج.

**الأعمال ذات الصلة بفحص النماذج**

تستخدم هذه الورقة NuSMV، وهو فاحص نماذج رمزي يدعم فحص النماذج بمنطق زمني خطي (LTL) ومنطق شجرة الحوسبة (CTL) [11]. تستخدم مجموعة متنوعة من الجهود السابقة NuSMV. على سبيل المثال، يصف Szpyrka وآخرون عملية لتوليد مواصفات NuSMV من شبكات بتري [26]. الأكثر صلة بهذا المشروع، يصف Meenakshi وآخرون منهجية مماثلة لترجمة نماذج Simulink إلى NuSMV في [19]. ومع ذلك، فإن المنهجية الموصوفة من قبل Meenakshi وآخرون تركز على توليد NuSMV الساذج من نموذج Simulink معين.

**الأعمال ذات الصلة بنمذجة الحالة التركيبية**

وصف Ranganath وآخرون نهجاً لنمذجة أنماط الاتصال للأجهزة الطبية [24]. يهدف نهج Ranganath إلى تقليل العبء الحسابي للاستدلال حول الأنظمة المتكاملة من خلال تجريد التفاصيل خلف واجهات موحدة. استخدم Beurdouche وآخرون نهجاً تركيبياً لنمذجة حالة اتصال أمان طبقة النقل (TLS)، وإنشاء آلة حالة مركبة من خلال تجميع آلات حالة المكونات الفردية [4].

**SLICED وعلاقتها بالأعمال ذات الصلة**

يتمثل هدف SLICED والتركيز في هذه الورقة على توليد مواصفات مجردة وقابلة للتشغيل البيني للسماح بالتحليل الرسمي للأنظمة المكونة من نماذج من أطراف متعددة. SLICED هو امتداد لنُهُج مواصفات الواجهة في FACE و HOST بهدف تمكين التحليل المماثل لذلك الذي أجراه Beurdouche. تستخدم SLICED نهج تعديل مماثل لأنماط الاتصال الموصوفة من قبل Ranganath، وتجريد الأنماط إلى مكونات موحدة مماثلة لتلك المحددة بواسطة AADL.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Component interoperability - التشغيل البيني للمكونات
  - Unit of Portability - وحدة النقل
  - FACE Technical Standard - المعيار الفني لـ FACE
  - HOST (Hardware Open Systems Technologies) - تقنيات الأنظمة المفتوحة للأجهزة
  - DARPA - وكالة مشاريع الأبحاث الدفاعية المتقدمة
  - HACMS (High-Assurance Cyber Military Systems) - الأنظمة العسكرية السيبرانية عالية الضمان
  - AGREE (Assume Guarantee Reasoning Environment) - بيئة استدلال الافتراض والضمان
  - Assume-guarantee contracts - عقود الافتراض والضمان
  - Linear Temporal Logic (LTL) - منطق زمني خطي
  - Computation Tree Logic (CTL) - منطق شجرة الحوسبة
  - Petri Nets - شبكات بتري
  - Transport Layer Security (TLS) - أمان طبقة النقل
  - Compositional state modeling - نمذجة الحالة التركيبية
- **Equations:** 0
- **Citations:** [4], [7], [11], [13], [14], [16], [19], [24], [25], [26], [27]
- **Special handling:**
  - Proper nouns (FACE, HOST, DARPA, HACMS, AGREE, NuSMV, AADL, TLS) kept mostly in English with Arabic explanations
  - Technical acronyms explained in Arabic

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.89
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.86
