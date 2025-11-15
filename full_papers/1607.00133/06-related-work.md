# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** privacy-preserving, machine learning, differential privacy, Rényi differential privacy, convex optimization, SGD, neural networks, secure function evaluation, secure multi-party computation, k-anonymity, empirical risk minimization, collaborative filtering

---

### English Version

The problem of privacy-preserving data mining, or machine learning, has been a focus of active work in several research communities since the late 90s. The existing literature can be broadly classified along several axes: the class of models, the learning algorithm, and the privacy guarantees.

**Privacy guarantees.** Early works on privacy-preserving learning were done in the framework of secure function evaluation (SFE) and secure multi-party computations (MPC), where the input is split between two or more parties, and the focus is on minimizing information leaked during the joint computation of some agreed-to functionality. In contrast, we assume that data is held centrally, and we are concerned with leakage from the functionality's output (i.e., the model).

Another approach, k-anonymity and closely related notions, seeks to offer a degree of protection to underlying data by generalizing and suppressing certain identifying attributes. The approach has strong theoretical and empirical limitations that make it all but inapplicable to de-anonymization of high-dimensional, diverse input datasets. Rather than pursue input sanitization, we keep the underlying raw records intact and perturb derived data instead.

The theory of differential privacy, which provides the analytical framework for our work, has been applied to a large collection of machine learning tasks that differed from ours either in the training mechanism or in the target model.

The moments accountant is closely related to the notion of Rényi differential privacy, which proposes (scaled) α(λ) as a means of quantifying privacy guarantees. In a concurrent and independent work Bun and Steinke introduce a relaxation of differential privacy (generalizing the work of Dwork and Rothblum) defined via a linear upper bound on α(λ). Taken together, these works demonstrate that the moments accountant is a useful technique for theoretical and empirical analyses of complex privacy-preserving algorithms.

**Learning algorithm.** A common target for learning with privacy is a class of convex optimization problems amenable to a wide variety of techniques. In concurrent work, Wu et al. achieve 83% accuracy on MNIST via convex empirical risk minimization. Training multi-layer neural networks is non-convex, and typically solved by an application of SGD, whose theoretical guarantees are poorly understood.

For the CIFAR neural network we incorporate differentially private training of the PCA projection matrix, which is used to reduce dimensionality of inputs.

**Model class.** The first end-to-end differentially private system was evaluated on the Netflix Prize dataset, a version of a collaborative filtering problem. Although the problem shared many similarities with ours—high-dimensional inputs, non-convex objective function—the approach taken by McSherry and Mironov differed significantly. They identified the core of the learning task, effectively sufficient statistics, that can be computed in a differentially private manner via a Gaussian mechanism. In our approach no such sufficient statistics exist.

In a recent work Shokri and Shmatikov designed and evaluated a system for distributed training of a deep neural network. Participants, who hold their data closely, communicate sanitized updates to a central authority. The sanitization relies on an additive-noise mechanism, based on a sensitivity estimate, which could be improved to a hard sensitivity guarantee. They compute privacy loss per parameter (not for an entire model). By our preferred measure, the total privacy loss per participant on the MNIST dataset exceeds several thousand.

A different, recent approach towards differentially private deep learning is explored by Phan et al. This work focuses on learning autoencoders. Privacy is based on perturbing the objective functions of these autoencoders.

---

### النسخة العربية

كانت مشكلة استخراج البيانات أو تعلم الآلة مع الحفاظ على الخصوصية محل تركيز للعمل النشط في عدة مجتمعات بحثية منذ أواخر التسعينيات. يمكن تصنيف الأدبيات الموجودة على نطاق واسع على طول عدة محاور: فئة النماذج، وخوارزمية التعلم، وضمانات الخصوصية.

**ضمانات الخصوصية.** تم إجراء الأعمال المبكرة حول التعلم مع الحفاظ على الخصوصية في إطار التقييم الآمن للدوال (SFE) والحسابات الآمنة متعددة الأطراف (MPC)، حيث يتم تقسيم المدخلات بين طرفين أو أكثر، ويكون التركيز على تقليل المعلومات المسربة أثناء الحساب المشترك لبعض الوظائف المتفق عليها. في المقابل، نفترض أن البيانات محفوظة مركزياً، ونحن معنيون بالتسرب من مخرجات الوظيفة (أي النموذج).

نهج آخر، k-anonymity والمفاهيم ذات الصلة الوثيقة، يسعى لتقديم درجة من الحماية للبيانات الأساسية من خلال تعميم وقمع سمات تعريفية معينة. يحتوي النهج على قيود نظرية وتجريبية قوية تجعله غير قابل للتطبيق تقريباً على إزالة إخفاء الهوية عن مجموعات بيانات إدخال عالية الأبعاد ومتنوعة. بدلاً من متابعة تطهير المدخلات، نحتفظ بالسجلات الخام الأساسية سليمة ونضطرب البيانات المشتقة بدلاً من ذلك.

تم تطبيق نظرية الخصوصية التفاضلية، التي توفر الإطار التحليلي لعملنا، على مجموعة كبيرة من مهام تعلم الآلة التي اختلفت عن مهامنا إما في آلية التدريب أو في النموذج المستهدف.

يرتبط محاسب العزوم ارتباطاً وثيقاً بمفهوم خصوصية رينيي التفاضلية (Rényi differential privacy)، الذي يقترح α(λ) (المقيس) كوسيلة لقياس ضمانات الخصوصية. في عمل متزامن ومستقل، يقدم Bun و Steinke استرخاءً للخصوصية التفاضلية (تعميم عمل Dwork و Rothblum) يُعرَّف عبر حد علوي خطي على α(λ). إذا أُخذت معاً، توضح هذه الأعمال أن محاسب العزوم تقنية مفيدة للتحليلات النظرية والتجريبية للخوارزميات المعقدة التي تحافظ على الخصوصية.

**خوارزمية التعلم.** هدف شائع للتعلم مع الخصوصية هو فئة من مشاكل التحسين المحدبة القابلة لمجموعة واسعة من التقنيات. في عمل متزامن، يحقق Wu وزملاؤه دقة 83% على MNIST عبر تصغير المخاطر التجريبية المحدبة. تدريب الشبكات العصبية متعددة الطبقات غير محدب، وعادة ما يتم حله من خلال تطبيق SGD، الذي لا تُفهم ضماناته النظرية جيداً.

بالنسبة للشبكة العصبية CIFAR، ندمج التدريب الخاص بالخصوصية التفاضلية لمصفوفة إسقاط PCA، التي تُستخدم لتقليل أبعاد المدخلات.

**فئة النموذج.** تم تقييم أول نظام خاص بالخصوصية التفاضلية من البداية إلى النهاية على مجموعة بيانات Netflix Prize، وهي نسخة من مشكلة الترشيح التعاوني. على الرغم من أن المشكلة شاركت العديد من أوجه التشابه مع مشكلتنا—مدخلات عالية الأبعاد، دالة هدف غير محدبة—اختلف النهج الذي اتبعه McSherry و Mironov بشكل كبير. حددوا جوهر مهمة التعلم، وهو فعلياً الإحصاءات الكافية، التي يمكن حسابها بطريقة خاصة بالخصوصية التفاضلية عبر آلية غاوس. في نهجنا لا توجد مثل هذه الإحصاءات الكافية.

في عمل حديث، صمم Shokri و Shmatikov وقيما نظاماً للتدريب الموزع لشبكة عصبية عميقة. يتواصل المشاركون، الذين يحتفظون ببياناتهم عن كثب، بتحديثات مطهرة إلى سلطة مركزية. يعتمد التطهير على آلية ضوضاء إضافية، بناءً على تقدير الحساسية، والذي يمكن تحسينه إلى ضمان حساسية ثابت. يحسبون خسارة الخصوصية لكل معامل (وليس للنموذج بأكمله). وفقاً لمقياسنا المفضل، تتجاوز خسارة الخصوصية الإجمالية لكل مشارك على مجموعة بيانات MNIST عدة آلاف.

يستكشف Phan وزملاؤه نهجاً مختلفاً وحديثاً نحو التعلم العميق الخاص بالخصوصية التفاضلية. يركز هذا العمل على تعلم المشفرات التلقائية (autoencoders). تعتمد الخصوصية على اضطراب دوال الهدف لهذه المشفرات التلقائية.

---

### Translation Notes

- **Key concepts:**
  - Comparison with secure multi-party computation approaches
  - Critique of k-anonymity for high-dimensional data
  - Relation to Rényi differential privacy and moments accountant
  - Comparison with other differentially private deep learning systems
  - Distinction between convex and non-convex learning

- **Technical terms:**
  - "secure function evaluation (SFE)" - التقييم الآمن للدوال
  - "secure multi-party computation (MPC)" - الحسابات الآمنة متعددة الأطراف
  - "k-anonymity" - k-anonymity (kept as is, technical term)
  - "de-anonymization" - إزالة إخفاء الهوية
  - "Rényi differential privacy" - خصوصية رينيي التفاضلية (named after Rényi)
  - "empirical risk minimization" - تصغير المخاطر التجريبية
  - "collaborative filtering" - الترشيح التعاوني
  - "sufficient statistics" - الإحصاءات الكافية
  - "autoencoders" - المشفرات التلقائية

- **Comparison clarity:**
  - Emphasized key differences between this work and prior approaches
  - Maintained accuracy in describing other researchers' methods
  - Preserved technical precision in comparisons

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
