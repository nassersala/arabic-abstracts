# Section 1: Introduction / القسم 1: المقدمة

**Section:** 1. Introduction
**Arabic Translation:** 1. المقدمة
**Quality Score:** 0.94
**Source:** Translated from paper.pdf pages 3-4

---

## English

What does it mean for data to be anonymized? Samarati and Sweeney discovered that removing explicit identifiers from dataset records was not enough to prevent information from being re-identified [Sam01, Swe02], and they proposed the first definition of anonymization. This notion, called k-anonymity, is a property of a dataset: each combination of re-identifying fields must be present at least k times. In the following decade, further research showed that sensitive information about individuals could still be leaked when releasing k-anonymous datasets, and many variants and definitions were proposed, such as l-diversity [MGKV06], t-closeness [LLV07], and n-confusion [ST12].

A common shortcoming of these approaches is that they defined anonymity as a property of the dataset: without knowing how the dataset is generated, arbitrary information can be leaked. This approach was changed with the introduction of differential privacy [DM05, Dwo06] (DP): rather than being a property of the sanitized dataset, anonymity was instead defined as a property of the process. It was inspired by Dalenius' privacy goal that "Anything about an individual that can be learned from the dataset can also be learned without access to the dataset" [Dal77], a goal similar to one already used in probabilistic encryption [SM84].

Thanks to its useful properties, DP quickly became the flagship of data privacy definitions. Many algorithms and statistical processes were changed to satisfy DP and were adopted by organizations like Apple [Tea17], Facebook [MDH+20] [HDS+20], Google [ABC+20] [BDD+20] [BBD+21] [WZL+20], LinkedIn [RCM+20] [RSP+20], Microsoft [DKY17], OhmConnect [MP20], and the US Census Bureau [AAG+10] [GAP18] [FMM19].

Since the original introduction of differential privacy, many variants and extensions have been proposed to adapt it to different contexts or assumptions. These new definitions enable practitioners to get privacy guarantees, even in cases that the original DP definition does not cover well. This happens in a variety of scenarios: the noise mandated by DP can be too large and force the data custodian to consider a weaker alternative, the risk model might be inappropriate for certain use cases, or the context might require the data owner to make stronger statements on what information the privacy mechanism can reveal.

Figure 1 shows the prevalence of this phenomenon: approximately 225 different notions, inspired by DP, were defined in the last years. As we show in Figure 1, this phenomenon does not seem to slow down over time. These definitions can be extensions or variants of DP. An extension encompasses the original DP notion as a special case, while a variant changes some aspect, typically to weaken or strengthen the original definition.

With so many definitions, it is difficult for new practitioners to get an overview of this research area. Many definitions have similar goals, so it is also challenging to understand which are appropriate to use in which context. These difficulties also affect experts: a number of definitions listed in this work have been defined independently multiple times (often with identical meaning but different names, or identical names but different meanings). Finally, variants are often introduced without a comparison to related notions.

This systematization of knowledge attempts to solve these problems. It is a taxonomy of variants and extensions of DP, providing short explanations of the intuition, use cases and basic properties of each. By categorizing these definitions, we attempt to simplify the understanding of existing variants and extensions, and of the relations between them. We hope to make it easier for new practitioners to understand whether their use case needs an alternative definition, and if so, which existing notions are the most appropriate, and what their basic properties are.

**Contributions and organization**

We systematize the scientific literature on variants and extensions of differential privacy, and propose a unified and comprehensive taxonomy of these definitions. We define seven dimensions: these are ways in which the original definition of DP can be modified or extended. We list variants and extensions that belong to each dimension, and we highlight representative definitions for each. Whenever possible, we compare these definitions and establish a partial ordering between the strengths of different notions. Furthermore, for each definition, we specify whether it satisfies Kifer et al.'s privacy axioms [KL10, KL12], (post-processing and convexity), and whether they are composable.

Our survey is organized as follows:

• In Section 2, we recall the original definition of DP and introduce our dimensions along which DP can be modified. Moreover, we present the basic properties of DP, and define how definitions can related to each other.

• In the following 7 sections (Sections 3 to 9), we introduce our dimensions, and list and compare the corresponding definitions.

• In Section 10, we summarize the results from the previous sections into a table, showing the corresponding properties with proofs, and list the known relations.

• In Section 11 we detail the methodology and scope of this work and review the related literature.

• Finally, in 12 we conclude this work.

---

## Arabic / العربية

ما الذي يعنيه أن تكون البيانات مجهولة الهوية؟ اكتشف ساماراتي وسويني أن إزالة المعرفات الصريحة من سجلات مجموعة البيانات لم تكن كافية لمنع إعادة تحديد الهوية للمعلومات [Sam01, Swe02]، واقترحوا أول تعريف لإخفاء الهوية. هذا المفهوم، المسمى إخفاء الهوية-k، هو خاصية لمجموعة البيانات: يجب أن يكون كل مزيج من الحقول المعيدة لتحديد الهوية موجوداً على الأقل k مرة. في العقد التالي، أظهرت الأبحاث الإضافية أن المعلومات الحساسة حول الأفراد لا يزال من الممكن تسريبها عند نشر مجموعات بيانات مجهولة الهوية-k، وتم اقتراح العديد من المتغيرات والتعريفات، مثل التنوع-l [MGKV06]، والقرب-t [LLV07]، والارتباك-n [ST12].

القصور المشترك في هذه المناهج هو أنها عرّفت إخفاء الهوية كخاصية لمجموعة البيانات: دون معرفة كيفية توليد مجموعة البيانات، يمكن تسريب معلومات عشوائية. تغير هذا النهج مع تقديم الخصوصية التفاضلية [DM05, Dwo06] (DP): بدلاً من كونها خاصية لمجموعة البيانات المعقمة، تم تعريف إخفاء الهوية بدلاً من ذلك كخاصية للعملية. تم استلهامها من هدف خصوصية داليوس القائل بأن "أي شيء عن فرد يمكن تعلمه من مجموعة البيانات يمكن أيضاً تعلمه دون الوصول إلى مجموعة البيانات" [Dal77]، وهو هدف مشابه لهدف استخدم بالفعل في التشفير الاحتمالي [SM84].

بفضل خصائصها المفيدة، أصبحت الخصوصية التفاضلية بسرعة الرائدة في تعريفات خصوصية البيانات. تم تغيير العديد من الخوارزميات والعمليات الإحصائية لتلبية متطلبات الخصوصية التفاضلية وتم اعتمادها من قبل منظمات مثل أبل [Tea17]، وفيسبوك [MDH+20] [HDS+20]، وجوجل [ABC+20] [BDD+20] [BBD+21] [WZL+20]، ولينكد إن [RCM+20] [RSP+20]، ومايكروسوفت [DKY17]، و OhmConnect [MP20]، ومكتب الإحصاء الأمريكي [AAG+10] [GAP18] [FMM19].

منذ التقديم الأصلي للخصوصية التفاضلية، تم اقتراح العديد من المتغيرات والإضافات لتكييفها مع سياقات أو افتراضات مختلفة. تمكّن هذه التعريفات الجديدة الممارسين من الحصول على ضمانات الخصوصية، حتى في الحالات التي لا يغطيها تعريف الخصوصية التفاضلية الأصلي بشكل جيد. يحدث هذا في مجموعة متنوعة من السيناريوهات: يمكن أن يكون الضوضاء المطلوب بواسطة الخصوصية التفاضلية كبيراً جداً ويجبر حارس البيانات على النظر في بديل أضعف، أو قد يكون نموذج المخاطر غير مناسب لحالات استخدام معينة، أو قد يتطلب السياق من مالك البيانات تقديم بيانات أقوى حول المعلومات التي يمكن أن تكشفها آلية الخصوصية.

يُظهر الشكل 1 انتشار هذه الظاهرة: تم تعريف حوالي 225 مفهوماً مختلفاً، مستوحى من الخصوصية التفاضلية، في السنوات الأخيرة. كما نظهر في الشكل 1، لا يبدو أن هذه الظاهرة تتباطأ مع مرور الوقت. يمكن أن تكون هذه التعريفات إضافات أو متغيرات للخصوصية التفاضلية. تشمل الإضافة مفهوم الخصوصية التفاضلية الأصلي كحالة خاصة، بينما يغير المتغير بعض الجوانب، عادةً لإضعاف أو تقوية التعريف الأصلي.

مع وجود العديد من التعريفات، من الصعب على الممارسين الجدد الحصول على نظرة عامة على هذا المجال البحثي. العديد من التعريفات لها أهداف متشابهة، لذلك من الصعب أيضاً فهم أيها مناسب للاستخدام في أي سياق. تؤثر هذه الصعوبات أيضاً على الخبراء: تم تعريف عدد من التعريفات المدرجة في هذا العمل بشكل مستقل عدة مرات (غالباً بمعنى متطابق ولكن أسماء مختلفة، أو أسماء متطابقة ولكن معانٍ مختلفة). وأخيراً، غالباً ما يتم تقديم المتغيرات دون مقارنة بالمفاهيم ذات الصلة.

تحاول منهجة المعرفة هذه حل هذه المشكلات. إنها تصنيف للمتغيرات والإضافات للخصوصية التفاضلية، مع تقديم شروحات موجزة للحدس وحالات الاستخدام والخصائص الأساسية لكل منها. من خلال تصنيف هذه التعريفات، نحاول تبسيط فهم المتغيرات والإضافات الموجودة، والعلاقات بينها. نأمل أن نسهل على الممارسين الجدد فهم ما إذا كانت حالة الاستخدام الخاصة بهم تحتاج إلى تعريف بديل، وإذا كان الأمر كذلك، ما هي المفاهيم الموجودة الأكثر ملاءمة، وما هي خصائصها الأساسية.

**المساهمات والتنظيم**

نقوم بمنهجة الأدبيات العلمية حول متغيرات وإضافات الخصوصية التفاضلية، ونقترح تصنيفاً موحداً وشاملاً لهذه التعريفات. نحدد سبعة أبعاد: هذه هي الطرق التي يمكن من خلالها تعديل أو توسيع التعريف الأصلي للخصوصية التفاضلية. نسرد المتغيرات والإضافات التي تنتمي إلى كل بُعد، ونسلط الضوء على التعريفات التمثيلية لكل منها. كلما أمكن، نقارن هذه التعريفات ونضع ترتيباً جزئياً بين قوة المفاهيم المختلفة. علاوة على ذلك، لكل تعريف، نحدد ما إذا كان يحقق بديهيات الخصوصية لكيفر وآخرين [KL10, KL12]، (المعالجة اللاحقة والتحدب)، وما إذا كانت قابلة للتركيب.

يتم تنظيم مسحنا على النحو التالي:

• في القسم 2، نستذكر التعريف الأصلي للخصوصية التفاضلية ونقدم أبعادنا التي يمكن على طولها تعديل الخصوصية التفاضلية. علاوة على ذلك، نقدم الخصائص الأساسية للخصوصية التفاضلية، ونحدد كيف يمكن أن تترابط التعريفات مع بعضها البعض.

• في الأقسام السبعة التالية (الأقسام من 3 إلى 9)، نقدم أبعادنا، ونسرد ونقارن التعريفات المقابلة.

• في القسم 10، نلخص النتائج من الأقسام السابقة في جدول، نعرض الخصائص المقابلة مع البراهين، ونسرد العلاقات المعروفة.

• في القسم 11 نفصل المنهجية ونطاق هذا العمل ونراجع الأدبيات ذات الصلة.

• أخيراً، في القسم 12 نختتم هذا العمل.

---

## Back-Translation (Validation)

What does it mean for data to be anonymous? Samarati and Sweeney discovered that removing explicit identifiers from dataset records was not sufficient to prevent re-identification of information [Sam01, Swe02], and they proposed the first definition of anonymization. This concept, called k-anonymity, is a property of a dataset: each combination of re-identifying fields must be present at least k times. In the following decade, additional research showed that sensitive information about individuals could still be leaked when publishing k-anonymous datasets, and many variants and definitions were proposed, such as l-diversity [MGKV06], t-closeness [LLV07], and n-confusion [ST12].

The common shortcoming of these approaches is that they defined anonymization as a property of the dataset: without knowing how the dataset is generated, arbitrary information can be leaked. This approach changed with the introduction of differential privacy [DM05, Dwo06] (DP): instead of being a property of the sanitized dataset, anonymization was instead defined as a property of the process. It was inspired by Dalenius' privacy goal stating that "Anything about an individual that can be learned from the dataset can also be learned without access to the dataset" [Dal77], a goal similar to one already used in probabilistic encryption [SM84].

Thanks to its useful properties, differential privacy quickly became the leader in data privacy definitions. Many algorithms and statistical processes were modified to meet differential privacy requirements and were adopted by organizations such as Apple [Tea17], Facebook [MDH+20] [HDS+20], Google [ABC+20] [BDD+20] [BBD+21] [WZL+20], LinkedIn [RCM+20] [RSP+20], Microsoft [DKY17], OhmConnect [MP20], and the US Census Bureau [AAG+10] [GAP18] [FMM19].

Since the original introduction of differential privacy, many variants and extensions have been proposed to adapt it to different contexts or assumptions. These new definitions enable practitioners to obtain privacy guarantees, even in cases that the original differential privacy definition does not cover well. This happens in a variety of scenarios: the noise required by differential privacy can be too large and force the data custodian to consider a weaker alternative, or the risk model may be inappropriate for certain use cases, or the context may require the data owner to provide stronger statements about what information the privacy mechanism can reveal.

Figure 1 shows the prevalence of this phenomenon: approximately 225 different concepts, inspired by differential privacy, were defined in recent years. As we show in Figure 1, this phenomenon does not appear to slow down over time. These definitions can be extensions or variants of differential privacy. An extension includes the original differential privacy concept as a special case, while a variant changes some aspects, usually to weaken or strengthen the original definition.

With so many definitions, it is difficult for new practitioners to get an overview of this research area. Many definitions have similar goals, so it is also difficult to understand which is appropriate to use in which context. These difficulties also affect experts: a number of definitions listed in this work have been defined independently several times (often with identical meaning but different names, or identical names but different meanings). Finally, variants are often introduced without comparison to related concepts.

This systematization of knowledge attempts to solve these problems. It is a classification of variants and extensions of differential privacy, providing brief explanations of the intuition, use cases, and basic properties of each. By classifying these definitions, we attempt to simplify the understanding of existing variants and extensions, and the relationships between them. We hope to make it easier for new practitioners to understand whether their use case needs an alternative definition, and if so, what existing concepts are most appropriate, and what their basic properties are.

**Contributions and organization**

We systematize the scientific literature on variants and extensions of differential privacy, and propose a unified and comprehensive taxonomy of these definitions. We define seven dimensions: these are the ways in which the original definition of differential privacy can be modified or extended. We list the variants and extensions that belong to each dimension, and highlight representative definitions for each. Whenever possible, we compare these definitions and establish a partial ordering between the strength of different concepts. Furthermore, for each definition, we specify whether it satisfies Kifer et al.'s privacy axioms [KL10, KL12], (post-processing and convexity), and whether they are composable.

Our survey is organized as follows:

• In Section 2, we recall the original definition of differential privacy and introduce our dimensions along which differential privacy can be modified. Moreover, we present the basic properties of differential privacy, and define how definitions can relate to each other.

• In the following seven sections (Sections 3 to 9), we introduce our dimensions, and list and compare the corresponding definitions.

• In Section 10, we summarize the results from the previous sections in a table, display the corresponding properties with proofs, and list the known relations.

• In Section 11 we detail the methodology and scope of this work and review the related literature.

• Finally, in Section 12 we conclude this work.

---

## Glossary Terms Used

- anonymized → مجهولة الهوية
- k-anonymity → إخفاء الهوية-k
- l-diversity → التنوع-l
- t-closeness → القرب-t
- n-confusion → الارتباك-n
- differential privacy → الخصوصية التفاضلية
- sanitized dataset → مجموعة البيانات المعقمة
- process → العملية
- probabilistic encryption → التشفير الاحتمالي
- data privacy → خصوصية البيانات
- variants → متغيرات
- extensions → إضافات
- taxonomy → تصنيف
- dimensions → أبعاد
- privacy axioms → بديهيات الخصوصية
- post-processing → المعالجة اللاحقة
- convexity → التحدب
- composable → قابلة للتركيب
