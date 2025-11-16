# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.89
**Glossary Terms Used:** transformer, deep neural networks, code intelligence, robustness, semantic-preserving, abstract syntax tree, positional encoding, code completion, code summarization, code search, attention

---

### English Version

## 1 INTRODUCTION

Over the past few years, deep neural networks (DNNs) have been continuously expanding their real-world applications for source code intelligence tasks [1], [2], [3], [4]. Due to the format similarity between source code and text [5], Transformer [6], an attention-based neural network architecture for learning textual semantics [7], is now widely used for source code representation learning [1], [2], [3], [4], and becomes a state-of-the-art architecture in several code intelligence tasks, including code completion [8], [9], code summarization [10], [11], and program repair [12].

Unfortunately, DNNs have demonstrated to be quite brittle to data changes [13], [14]. For example, previous studies demonstrate that adding small perturbations to the original input can readily trick DNNs [15], [16], revealing that the DNNs are not robust to input variations [17], [18]. Several studies [19], [20], [21] have been proposed to understand the robustness of DNNs under input perturbations. Recently, Transformer [6] has attracted a lot of academic attention in code intelligence tasks [8], [10], but few studies have looked at its robustness when faced with perturbed code. Given the growing number of Transformer-based code intelligence models [22], [23], [24], [25], the robustness of these models under code perturbation is of great importance. However, developing such a robustness verification method for Transformer-based code intelligence models is challenging. Directly applying the input perturbation techniques in natural language processing (NLP) or computer vision (CV) field [26], [27] is unreasonable, since the perturbation on source code must guarantee that the changed code follows syntax rules.

In this paper, we propose several semantic-preserving code transformation strategies, and analyze the impact of code transformation on the performance of Transformer. Figure 1 shows an example of semantically equivalent programs, where the code summaries are produced by the popular Transformer-based approach [10]. For the code listed in Figure 1(a), we transform the if statement to equivalent while statement, as shown in Figure 1(b), and conduct variable renaming, as shown in Figure 1(c). However, the resulting summarizations of Transformer on the above three programs are radically different. Since the semantics of the original program are kept, the model should have the same prediction as the original program for the transformed programs. This example suggests that (1) Transformer are not robust in code intelligence tasks when faced with semantic-preserving transformation, and (2) different code transformation strategies have different impacts on Transformer. Therefore, we aim at investigating whether Transformer can maintain performance under semantic-preserving code transformation, and the impact of different transformation strategies.

In this work, we empirically study the effect of semantic-preserving code transformation on the performance of Transformer. We firstly design and implement 27 and 24 semantic-preserving transformation strategies for Java and Python languages respectively, and group them into 5 types of strategies according to the scope of influence under the transformation: block transformation, insertion / deletion transformation, grammatical statement transformation, grammatical token transformation, and identifier transformation. Then, we apply the transformed code on three popular code intelligence tasks: code completion (CC), code search (CS), and code summarization (CoSum). For studying whether involving syntax information such as Abstract Syntax Trees (ASTs) is beneficial for improving the robustness of Transformer under code transformation, we classify the Transformer-based code intelligence models into two types according to the input: Seq-based Transformer and AST-based Transformer. The seq-based Transformer only considers sequences of code tokens as input; while AST-based Transformer also involves parsed ASTs as input.

Besides, the positional encoding is an essential component in Transformer [28], and has been proven effective in Transformer-based code models [5], [10], [29]. Therefore, in this work, we also study the impact of different positional encoding strategies on the robustness of Transformer models under code perturbation. Specifically, two widely-used positional encoding strategies, including absolute positional encoding [6] and relative positional encoding [30], are chosen for analysis. We aim at answering the following research questions in the work.

**RQ1:** How do different code transformations impact the performance of Transformer? (Seq-based Transformer)

**RQ2:** Is AST helpful for reducing the impact of code transformations on the performance of Transformer? (AST-based Transformer)

During answering each research question, we also consider different positional encoding strategies. We achieve some findings and summarize the key findings as below.

• Code transformations such as insertion / deletion transformation and identifier transformation present greatest impact on the performance of both seq-based and AST-based Transformers.

• Transformer based on ASTs shows more robust performance than the model based on only code sequence under most code transformations.

• The relative position encoding can improve the robustness of seq-based Transformer under most code transformations, but has no much benefit for the robustness of AST-based Transformer.

Based on the findings, we derive some insights about the challenges and opportunities that would benefit future research. For example, future work is expected to better exploit ASTs to boost the robustness of Transformer models under code transformation. Besides, we also encourage future work to explore more effective attention approach or engage additional external knowledge to eliminate the distraction of insertion / deletion transformation. Furthermore, future work should eliminate the impact of identifiers during code representation learning, instead of relying on the semantics of identifiers.

The main contributions of this paper are summarized as follows:

• We empirically study the effect of semantic-preserving code transformation on the performance of Transformer for three popular code intelligence tasks.

• We design and implement 27 and 24 code transformation strategies for Java and Python languages, respectively.

• We study how different aspects can impact the performance of Transformer, including the input and positional encoding strategy.

• We achieve some findings and implications that would benefit future research in the robustness of Transformer-based code intelligence tasks.

The rest of this paper is organized as follows. We present the background of Transformer and code intelligence tasks in Section 2. The technical details of our code transformation strategies are presented in Section 3. The evaluation and study design are shown in Section 4. Then we present the experimental results and potential findings in Section 5. Based on the findings, we conclude some implications and future directions in Section 6. We discuss threats to validity in Section 7. Finally, we give the review of the literature related to our research in Section 8 and conclude the work in Section 9, respectively.

---

### النسخة العربية

## 1 المقدمة

على مدى السنوات القليلة الماضية، توسعت الشبكات العصبية العميقة (DNNs) باستمرار في تطبيقاتها الواقعية لمهام ذكاء الشفرة المصدرية [1]، [2]، [3]، [4]. نظراً للتشابه الشكلي بين الشفرة المصدرية والنص [5]، أصبح المحول [6]، وهو معمارية شبكة عصبية قائمة على الانتباه لتعلم دلالات النص [7]، يُستخدم على نطاق واسع الآن لتعلم تمثيل الشفرة المصدرية [1]، [2]، [3]، [4]، وأصبح معمارية متقدمة في العديد من مهام ذكاء الشفرة، بما في ذلك إكمال الشفرة [8]، [9]، وتلخيص الشفرة [10]، [11]، وإصلاح البرامج [12].

لسوء الحظ، أظهرت الشبكات العصبية العميقة أنها هشة جداً تجاه تغييرات البيانات [13]، [14]. على سبيل المثال، تُظهر الدراسات السابقة أن إضافة اضطرابات صغيرة إلى المدخلات الأصلية يمكن أن تخدع الشبكات العصبية العميقة بسهولة [15]، [16]، مما يكشف أن الشبكات العصبية العميقة ليست متينة تجاه تغييرات المدخلات [17]، [18]. تم اقتراح العديد من الدراسات [19]، [20]، [21] لفهم متانة الشبكات العصبية العميقة تحت الاضطرابات في المدخلات. مؤخراً، جذب المحول [6] الكثير من الاهتمام الأكاديمي في مهام ذكاء الشفرة [8]، [10]، ولكن قلة من الدراسات نظرت إلى متانته عند مواجهة شفرة مضطربة. نظراً للعدد المتزايد من نماذج ذكاء الشفرة المعتمدة على المحول [22]، [23]، [24]، [25]، فإن متانة هذه النماذج تحت اضطراب الشفرة ذات أهمية كبيرة. ومع ذلك، فإن تطوير مثل هذه الطريقة للتحقق من المتانة لنماذج ذكاء الشفرة المعتمدة على المحول يُعد تحدياً. إن التطبيق المباشر لتقنيات اضطراب المدخلات في مجال معالجة اللغة الطبيعية (NLP) أو الرؤية الحاسوبية (CV) [26]، [27] غير معقول، لأن الاضطراب في الشفرة المصدرية يجب أن يضمن أن الشفرة المُغيرة تتبع قواعد البناء النحوي.

في هذه الورقة، نقترح عدة استراتيجيات لتحويل الشفرة الحافظة للدلالة، ونحلل تأثير تحويل الشفرة على أداء المحول. يُظهر الشكل 1 مثالاً على برامج متكافئة دلالياً، حيث يتم إنتاج ملخصات الشفرة بواسطة النهج الشائع المعتمد على المحول [10]. بالنسبة للشفرة المدرجة في الشكل 1(a)، نُحول عبارة if إلى عبارة while مكافئة، كما هو موضح في الشكل 1(b)، ونُجري إعادة تسمية المتغيرات، كما هو موضح في الشكل 1(c). ومع ذلك، فإن الملخصات الناتجة من المحول على البرامج الثلاثة أعلاه مختلفة جذرياً. نظراً لأن دلالات البرنامج الأصلي محفوظة، يجب أن يكون لدى النموذج نفس التنبؤ للبرنامج الأصلي بالنسبة للبرامج المُحولة. يشير هذا المثال إلى أن (1) المحول ليس متيناً في مهام ذكاء الشفرة عند مواجهة تحويل حافظ للدلالة، و(2) استراتيجيات تحويل الشفرة المختلفة لها تأثيرات مختلفة على المحول. لذلك، نهدف إلى التحقق مما إذا كان المحول يمكن أن يحافظ على الأداء تحت تحويل الشفرة الحافظ للدلالة، وتأثير استراتيجيات التحويل المختلفة.

في هذا العمل، ندرس تجريبياً تأثير تحويل الشفرة الحافظ للدلالة على أداء المحول. أولاً، نصمم وننفذ 27 و24 استراتيجية تحويل حافظة للدلالة للغتي جافا وبايثون على التوالي، ونجمعها في 5 أنواع من الاستراتيجيات وفقاً لنطاق التأثير تحت التحويل: تحويل الكتلة، وتحويل الإدراج/الحذف، وتحويل العبارة النحوية، وتحويل الرمز النحوي، وتحويل المعرف. ثم، نطبق الشفرة المُحولة على ثلاث مهام ذكاء شفرة شائعة: إكمال الشفرة (CC)، والبحث في الشفرة (CS)، وتلخيص الشفرة (CoSum). لدراسة ما إذا كان إشراك معلومات البناء النحوي مثل أشجار البنية التركيبية المجردة (ASTs) مفيداً لتحسين متانة المحول تحت تحويل الشفرة، نصنف نماذج ذكاء الشفرة المعتمدة على المحول إلى نوعين وفقاً للمدخلات: المحول القائم على التسلسل والمحول القائم على AST. يأخذ المحول القائم على التسلسل فقط تسلسلات رموز الشفرة كمدخلات؛ بينما يشرك المحول القائم على AST أيضاً أشجار AST المُحللة كمدخلات.

بالإضافة إلى ذلك، الترميز الموضعي هو مكون أساسي في المحول [28]، وقد ثبتت فعاليته في نماذج الشفرة المعتمدة على المحول [5]، [10]، [29]. لذلك، في هذا العمل، ندرس أيضاً تأثير استراتيجيات الترميز الموضعي المختلفة على متانة نماذج المحول تحت اضطراب الشفرة. على وجه التحديد، تم اختيار استراتيجيتين للترميز الموضعي مستخدمتين على نطاق واسع، بما في ذلك الترميز الموضعي المطلق [6] والترميز الموضعي النسبي [30]، للتحليل. نهدف إلى الإجابة على أسئلة البحث التالية في هذا العمل.

**السؤال البحثي 1:** كيف تؤثر تحويلات الشفرة المختلفة على أداء المحول؟ (المحول القائم على التسلسل)

**السؤال البحثي 2:** هل AST مفيد لتقليل تأثير تحويلات الشفرة على أداء المحول؟ (المحول القائم على AST)

أثناء الإجابة على كل سؤال بحثي، نأخذ أيضاً في الاعتبار استراتيجيات الترميز الموضعي المختلفة. نحقق بعض النتائج ونلخص النتائج الرئيسية أدناه.

• تحويلات الشفرة مثل تحويل الإدراج/الحذف وتحويل المعرف تُظهر أكبر تأثير على أداء المحولات القائمة على التسلسل والقائمة على AST على حد سواء.

• يُظهر المحول القائم على ASTs أداءً أكثر متانة من النموذج القائم على تسلسل الشفرة فقط تحت معظم تحويلات الشفرة.

• يمكن للترميز الموضعي النسبي تحسين متانة المحول القائم على التسلسل تحت معظم تحويلات الشفرة، ولكن ليس له فائدة كبيرة لمتانة المحول القائم على AST.

بناءً على النتائج، نستخلص بعض الرؤى حول التحديات والفرص التي ستفيد الأبحاث المستقبلية. على سبيل المثال، من المتوقع أن تستغل الأعمال المستقبلية أشجار AST بشكل أفضل لتعزيز متانة نماذج المحول تحت تحويل الشفرة. بالإضافة إلى ذلك، نشجع أيضاً الأعمال المستقبلية على استكشاف نهج انتباه أكثر فعالية أو إشراك معرفة خارجية إضافية للقضاء على تشتيت تحويل الإدراج/الحذف. علاوة على ذلك، يجب على الأعمال المستقبلية القضاء على تأثير المعرفات أثناء تعلم تمثيل الشفرة، بدلاً من الاعتماد على دلالات المعرفات.

تلخص المساهمات الرئيسية لهذه الورقة على النحو التالي:

• ندرس تجريبياً تأثير تحويل الشفرة الحافظ للدلالة على أداء المحول لثلاث مهام ذكاء شفرة شائعة.

• نصمم وننفذ 27 و24 استراتيجية تحويل شفرة للغتي جافا وبايثون، على التوالي.

• ندرس كيف يمكن لجوانب مختلفة أن تؤثر على أداء المحول، بما في ذلك استراتيجية المدخلات والترميز الموضعي.

• نحقق بعض النتائج والآثار التي ستفيد الأبحاث المستقبلية في متانة مهام ذكاء الشفرة المعتمدة على المحول.

تنظم بقية هذه الورقة على النحو التالي. نقدم الخلفية عن المحول ومهام ذكاء الشفرة في القسم 2. يتم عرض التفاصيل التقنية لاستراتيجيات تحويل الشفرة الخاصة بنا في القسم 3. يتم عرض التقييم وتصميم الدراسة في القسم 4. ثم نقدم النتائج التجريبية والنتائج المحتملة في القسم 5. بناءً على النتائج، نستنتج بعض الآثار والاتجاهات المستقبلية في القسم 6. نناقش التهديدات للصلاحية في القسم 7. أخيراً، نقدم مراجعة للأدبيات المتعلقة ببحثنا في القسم 8 ونختتم العمل في القسم 9، على التوالي.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:**
  - deep neural networks (الشبكات العصبية العميقة)
  - code intelligence (ذكاء الشفرة)
  - semantic-preserving transformation (تحويل حافظ للدلالة)
  - robustness (متانة)
  - perturbation (اضطراب)
  - Seq-based Transformer (المحول القائم على التسلسل)
  - AST-based Transformer (المحول القائم على AST)
  - absolute positional encoding (الترميز الموضعي المطلق)
  - relative positional encoding (الترميز الموضعي النسبي)

- **Research Questions:** RQ1 and RQ2 clearly stated
- **Citations:** Numbered references [1] through [30] preserved
- **Special handling:** Code examples in Figure 1 kept in English (programming language)

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
