# Section 6: Threats to Validity
## القسم 6: التهديدات للصلاحية

**Section:** threats-to-validity
**Translation Quality:** 0.89
**Glossary Terms Used:** internal validity, construct validity, external validity, dataset, preprocessing, hyperparameters, evaluation metrics, abstract syntax tree

---

### English Version

## 6 THREATS TO VALIDITY

In this section, we describe the possible threats we may face in this study and discuss how we mitigate them.

**Internal validity** is mainly about the data prepossessing and training models. To reduce the threats, we conduct experiments based on the released code scripts, and the default training hyper-parameters for all models. Besides, we run each experiment for three times and compute the average results for all tasks.

**Construct validity** is mainly about the suitability of our evaluation metrics. To reduce this risk, we select the most widely-used metrics for different tasks to evaluate the impact. For example, we use BLEU [45], ROUGE-L [46] and Meteor [47] to evaluate the impact of different transformations on code summarization task.

**External validity** is mainly concerned with dataset we use. In our experiments, we select Java and Python datasets from CodeSearchNet. However, CodeSearchNet has some problems that will affect our experiments. For example, some instances of code in CodeSearchNet cannot be parsed into an abstract syntax tree. To reduce the threats, we filter the datasets following the previous work [55]. To further reduce the threats, we plan to collect more open-source projects to reproduce our experiments.

---

### النسخة العربية

## 6 التهديدات للصلاحية

في هذا القسم، نصف التهديدات المحتملة التي قد نواجهها في هذه الدراسة ونناقش كيفية تخفيفها.

**الصلاحية الداخلية** تتعلق بشكل أساسي بالمعالجة المسبقة للبيانات وتدريب النماذج. لتقليل التهديدات، نجري التجارب بناءً على نصوص الشفرة المُصدرة، والمعاملات الفائقة الافتراضية للتدريب لجميع النماذج. بالإضافة إلى ذلك، نشغل كل تجربة ثلاث مرات ونحسب النتائج المتوسطة لجميع المهام.

**صلاحية البناء** تتعلق بشكل أساسي بملاءمة مقاييس التقييم الخاصة بنا. لتقليل هذا الخطر، نختار المقاييس الأكثر استخداماً على نطاق واسع لمهام مختلفة لتقييم التأثير. على سبيل المثال، نستخدم BLEU [45] و ROUGE-L [46] و Meteor [47] لتقييم تأثير التحويلات المختلفة على مهمة تلخيص الشفرة.

**الصلاحية الخارجية** تتعلق بشكل أساسي بمجموعة البيانات التي نستخدمها. في تجاربنا، نختار مجموعات بيانات جافا وبايثون من CodeSearchNet. ومع ذلك، فإن CodeSearchNet لديها بعض المشاكل التي ستؤثر على تجاربنا. على سبيل المثال، لا يمكن تحليل بعض حالات الشفرة في CodeSearchNet إلى شجرة بنية تركيبية مجردة. لتقليل التهديدات، نُرشح مجموعات البيانات متابعةً للعمل السابق [55]. لتقليل التهديدات بشكل أكبر، نخطط لجمع المزيد من المشاريع مفتوحة المصدر لإعادة إنتاج تجاربنا.

---

### Translation Notes

- **Key terms introduced:**
  - Internal validity (الصلاحية الداخلية)
  - Construct validity (صلاحية البناء)
  - External validity (الصلاحية الخارجية)
  - Data preprocessing (المعالجة المسبقة للبيانات)
  - Mitigation (تخفيف)

- **Citations:** References [45], [46], [47], [55]
- **Special handling:**
  - Three types of validity clearly distinguished
  - Mitigation strategies for each type explained
  - Short, concise section

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.89
