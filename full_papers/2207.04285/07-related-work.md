# Section 7: Related Work
## القسم 7: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** code intelligence, transformer, code completion, code summarization, code search, deep learning, LSTM, RNN, attention, pre-trained models, data augmentation, adversarial attack, robustness

---

### English Version

## 7 RELATED WORK

### 7.1 Code intelligence task

**Code completion task.** The success of deep learning boosts a series of code completion works based on deep learning models [56], [57]. For example, Alon et al. [58] proposed a structural language model based on Transformer, which leverages the syntax to model the code snippet as a tree to complete code. Liu et al. [59] pretrained a language model with a Transformer-based architecture and fine-tuned it for code completion. Kim et al. [8] proposed TravTrans, a Transformer-based approach that leverages ASTs for code completion.

**Code summarization task.** In recent years, many works that applied deep learning models in code summarization achieved great success and became more and more popular [60], [61]. For instance, Iyer et al. [62] proposed an LSTM-based model with attention to generate code summaries for source code. Wei et al. [63] and Zhang et al. [35] further introduced retrieved information for summarizing source code with the help of most similar code snippets. Alon et al. [64] sampled and encoded random AST paths into LSTMs to generate summaries of source code. Ahmad et al. [10] utilized Transformer on code summarization for better mapping the source code to their corresponding natural language summaries.

**Code search task.** The goal of code search is to find the most semantically related code from a collection of code based on a given natural language [37]. The traditional code search techniques are mainly based on information retrieval [65], [66], while the most popular approaches in recent years are based on deep neural networks [38], [39]. Sachdev et al. [67] proposed a neural code search engine which used a basic word-embedding for a code corpus. Gu et al. [3] proposed an RNN-based code search model to represent source code and natural language queries through joint embedding. Fan et al. [40] utilized a self-attention network to construct a code representation network for building the semantic relationship between code snippets and queries. Besides, large-scale pre-train models such as CodeBERT [4] and GraphCodeBERT [68] also demonstrated good performance on the code search task.

### 7.2 Code transformation

Code transformations are widely used for compiler optimizations [69], [70], testability transformation [71], [72], [73], refactoring [74], [75], etc. In recent years, there have been an amount of works in the field of code intelligence that employs code transformation.

**Data augmentation.** Yu et al. [76] applied a source-to-source transformation strategy to increase the generalization capacity of deep learning models based on program-level data augmentation, and Wang et al. [77] incorporated curriculum learning into program-level data augmentation in order to optimize the efficiency of fine-tuning pre-trained models. Bui et al. [78] proposed a self-supervised contrastive learning framework to generate transformed code snippets and identify semantically-equivalent code snippets from large-scale unlabeled data of source code, which could generate additional dataset for fine-tuning the pre-training models.

**Adversarial attack.** Quiring et al. [79] used semantics-preserving code transformations to generate adversarial examples and present a black-box attack that seeks examples by Monte-Carlo tree search. Li et al. [80] leveraged code transformations to attack DL-based detectors and decouple feature learning and classifier learning to present a static analysis-based vulnerability detector. Zhang et al. [81] applied reinforcement learning to select semantics-preserving samples and proposed a black-box attack approach against GNN malware detection models.

**Others applications.** Chen et al. [82] suggested a symbolic execution acceleration framework by machine-learning based compiler optimization tuning based on code transformation. Wu et al. [83] proposed an automating CUDA synchronization framework for bug detection at the LLVM-bitcode level via program transformation.

### 7.3 Robustness of code intelligence

Given the increased research interest in code intelligence, some works on the robustness of source code representation models are proposed [53], [54], [84], [85], [86], [87].

Yefet et al. [84] proposed an adversarial attacks generation approach for code via gradient based optimization, and it was effective in generating both targeted and non-targeted attacks. Rabin et al. [85] defined the generalizability in neural program models and studied the generalizability of method name prediction models using six semantic-preserving changes. Ramakrishnan et al. [87] proposed an adversarial-training method for neural models of code to enhance the robustness. Zhang et al. [53] defined the robust and non-robust features of DNNs, and proposed an identifier renaming algorithm (namely Metropolis-Hastings Modifier) for adversarial example generation on source code. Yang et al. [54] designed a black-box attack approach that was aware of natural semantics when generating adversarial examples of code, which was better than that of Zhang et al. [53]. Bielik et al. [86] refined the representation of source code and applied adversarial-training to improve robustness of neural models while preserving high accuracy.

---

### النسخة العربية

## 7 الأعمال ذات الصلة

### 7.1 مهام ذكاء الشفرة

**مهمة إكمال الشفرة.** أدى نجاح التعلم العميق إلى تعزيز سلسلة من أعمال إكمال الشفرة القائمة على نماذج التعلم العميق [56]، [57]. على سبيل المثال، اقترح Alon وآخرون [58] نموذجاً لغوياً هيكلياً قائماً على المحول، والذي يستفيد من البناء النحوي لنمذجة مقتطف الشفرة كشجرة لإكمال الشفرة. قام Liu وآخرون [59] بالتدريب المسبق لنموذج لغوي بمعمارية قائمة على المحول وضبطه بدقة لإكمال الشفرة. اقترح Kim وآخرون [8] TravTrans، وهو نهج قائم على المحول يستفيد من ASTs لإكمال الشفرة.

**مهمة تلخيص الشفرة.** في السنوات الأخيرة، حققت العديد من الأعمال التي طبقت نماذج التعلم العميق في تلخيص الشفرة نجاحاً كبيراً وأصبحت أكثر وأكثر شعبية [60]، [61]. على سبيل المثال، اقترح Iyer وآخرون [62] نموذجاً قائماً على LSTM مع الانتباه لتوليد ملخصات الشفرة للشفرة المصدرية. قدم Wei وآخرون [63] و Zhang وآخرون [35] بشكل أكبر معلومات مُستردة لتلخيص الشفرة المصدرية بمساعدة مقتطفات الشفرة الأكثر تشابهاً. قام Alon وآخرون [64] بأخذ عينات وترميز مسارات AST عشوائية في LSTMs لتوليد ملخصات الشفرة المصدرية. استخدم Ahmad وآخرون [10] المحول في تلخيص الشفرة لتعيين أفضل للشفرة المصدرية إلى ملخصات اللغة الطبيعية المقابلة لها.

**مهمة البحث في الشفرة.** الهدف من البحث في الشفرة هو إيجاد الشفرة الأكثر ارتباطاً دلالياً من مجموعة من الشفرة بناءً على لغة طبيعية معطاة [37]. تقنيات البحث في الشفرة التقليدية تعتمد بشكل أساسي على استرجاع المعلومات [65]، [66]، بينما النُهج الأكثر شعبية في السنوات الأخيرة تعتمد على الشبكات العصبية العميقة [38]، [39]. اقترح Sachdev وآخرون [67] محرك بحث عصبي في الشفرة استخدم تضميناً أساسياً للكلمات لمجموعة شفرة. اقترح Gu وآخرون [3] نموذج بحث في الشفرة قائم على RNN لتمثيل الشفرة المصدرية واستعلامات اللغة الطبيعية من خلال التضمين المشترك. استخدم Fan وآخرون [40] شبكة انتباه ذاتي لبناء شبكة تمثيل شفرة لبناء العلاقة الدلالية بين مقتطفات الشفرة والاستعلامات. بالإضافة إلى ذلك، أظهرت نماذج التدريب المسبق واسعة النطاق مثل CodeBERT [4] و GraphCodeBERT [68] أيضاً أداءً جيداً في مهمة البحث في الشفرة.

### 7.2 تحويل الشفرة

تُستخدم تحويلات الشفرة على نطاق واسع لتحسينات المترجم [69]، [70]، وتحويل قابلية الاختبار [71]، [72]، [73]، وإعادة الهيكلة [74]، [75]، وما إلى ذلك. في السنوات الأخيرة، كان هناك عدد من الأعمال في مجال ذكاء الشفرة التي توظف تحويل الشفرة.

**تعزيز البيانات.** طبق Yu وآخرون [76] استراتيجية تحويل من مصدر إلى مصدر لزيادة قدرة التعميم لنماذج التعلم العميق القائمة على تعزيز البيانات على مستوى البرنامج، ودمج Wang وآخرون [77] التعلم المنهجي في تعزيز البيانات على مستوى البرنامج من أجل تحسين كفاءة الضبط الدقيق للنماذج المُدربة مسبقاً. اقترح Bui وآخرون [78] إطار عمل للتعلم التباين ذاتي الإشراف لتوليد مقتطفات شفرة مُحولة وتحديد مقتطفات الشفرة المتكافئة دلالياً من بيانات واسعة النطاق غير مُصنفة للشفرة المصدرية، والتي يمكن أن تولد مجموعة بيانات إضافية للضبط الدقيق لنماذج التدريب المسبق.

**الهجوم الخصامي.** استخدم Quiring وآخرون [79] تحويلات الشفرة الحافظة للدلالة لتوليد أمثلة خصامية وتقديم هجوم صندوق أسود يبحث عن الأمثلة بواسطة بحث شجرة مونت كارلو. استفاد Li وآخرون [80] من تحويلات الشفرة لمهاجمة كاشفات قائمة على التعلم العميق وفصل تعلم الميزات وتعلم المُصنف لتقديم كاشف ثغرات قائم على التحليل الثابت. طبق Zhang وآخرون [81] التعلم التعزيزي لاختيار عينات حافظة للدلالة واقترحوا نهج هجوم صندوق أسود ضد نماذج كشف البرامج الضارة GNN.

**التطبيقات الأخرى.** اقترح Chen وآخرون [82] إطار عمل لتسريع التنفيذ الرمزي عن طريق ضبط تحسين المترجم القائم على التعلم الآلي بناءً على تحويل الشفرة. اقترح Wu وآخرون [83] إطار عمل لأتمتة المزامنة CUDA لاكتشاف الأخطاء على مستوى LLVM-bitcode عبر تحويل البرنامج.

### 7.3 متانة ذكاء الشفرة

نظراً لزيادة الاهتمام البحثي في ذكاء الشفرة، تم اقتراح بعض الأعمال حول متانة نماذج تمثيل الشفرة المصدرية [53]، [54]، [84]، [85]، [86]، [87].

اقترح Yefet وآخرون [84] نهج توليد هجمات خصامية للشفرة عبر التحسين القائم على التدرج، وكان فعالاً في توليد كل من الهجمات المستهدفة وغير المستهدفة. عرّف Rabin وآخرون [85] قابلية التعميم في نماذج البرامج العصبية ودرسوا قابلية التعميم لنماذج التنبؤ باسم الطريقة باستخدام ستة تغييرات حافظة للدلالة. اقترح Ramakrishnan وآخرون [87] طريقة تدريب خصامية لنماذج الشفرة العصبية لتعزيز المتانة. عرّف Zhang وآخرون [53] الميزات المتينة وغير المتينة للشبكات العصبية العميقة، واقترحوا خوارزمية إعادة تسمية المعرف (وهي Metropolis-Hastings Modifier) لتوليد الأمثلة الخصامية على الشفرة المصدرية. صمم Yang وآخرون [54] نهج هجوم صندوق أسود كان واعياً للدلالات الطبيعية عند توليد أمثلة خصامية للشفرة، والذي كان أفضل من ذلك لـ Zhang وآخرون [53]. حسّن Bielik وآخرون [86] تمثيل الشفرة المصدرية وطبقوا التدريب الخصامي لتحسين متانة النماذج العصبية مع الحفاظ على دقة عالية.

---

### Translation Notes

- **Citations:** References [3], [4], [8], [10], [35], [37], [38], [39], [40], [53], [54], [56]-[87]
- **Key terms introduced:**
  - Pre-trained models (نماذج مُدربة مسبقاً)
  - Word embedding (تضمين الكلمات)
  - Joint embedding (تضمين مشترك)
  - Self-attention network (شبكة انتباه ذاتي)
  - Data augmentation (تعزيز البيانات)
  - Curriculum learning (تعلم منهجي)
  - Contrastive learning (تعلم تباين)
  - Adversarial attack (هجوم خصامي)
  - Black-box attack (هجوم صندوق أسود)
  - Monte-Carlo tree search (بحث شجرة مونت كارلو)
  - Reinforcement learning (تعلم تعزيزي)
  - Symbolic execution (تنفيذ رمزي)
  - Compiler optimization (تحسين المترجم)
  - Generalizability (قابلية التعميم)
  - Adversarial training (تدريب خصامي)
  - Gradient-based optimization (تحسين قائم على التدرج)

- **Special handling:**
  - Three subsections covering different aspects of related work
  - Many citations to prior work in the field
  - Focus on code intelligence, transformation, and robustness

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86
