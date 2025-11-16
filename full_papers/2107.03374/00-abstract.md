# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** نماذج اللغة الكبيرة, ضبط دقيق, توليد البرامج, معيار, مجموعة بيانات, الأمان, السلامة, تعلم آلي, شفرة برمجية

---

### English Version

We introduce Codex, a GPT language model fine-tuned on publicly available code from GitHub, and study its Python code-writing capabilities. On HumanEval, a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings, our model solves 28.8% of the problems, while GPT-3 solves 0% and GPT-J solves 11.4%. Furthermore, we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method, we solve 70.2% of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations, including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally, we discuss the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics.

---

### النسخة العربية

نقدم Codex، وهو نموذج لغوي من نوع GPT تم ضبطه بشكل دقيق على شفرة برمجية متاحة للعامة من GitHub، وندرس قدراته على كتابة شفرة برمجية بلغة Python. على معيار HumanEval، وهو مجموعة تقييم جديدة نطلقها لقياس الصحة الوظيفية لتوليد البرامج من سلاسل التوثيق، يحل نموذجنا 28.8% من المشكلات، بينما يحل GPT-3 نسبة 0% ويحل GPT-J نسبة 11.4%. علاوة على ذلك، نجد أن أخذ العينات المتكررة من النموذج هي استراتيجية فعالة بشكل مفاجئ لإنتاج حلول عملية للمطالبات الصعبة. باستخدام هذه الطريقة، نحل 70.2% من مشاكلنا مع 100 عينة لكل مشكلة. يكشف الفحص الدقيق لنموذجنا عن قيوده، بما في ذلك الصعوبة في التعامل مع سلاسل التوثيق التي تصف سلاسل طويلة من العمليات ومع ربط العمليات بالمتغيرات. أخيراً، نناقش التأثيرات الأوسع المحتملة لنشر تقنيات توليد الشفرة القوية، التي تغطي السلامة والأمان والاقتصاد.

---

### Translation Notes

- **Key terms introduced:** Codex (kept as is), HumanEval (kept as is), GPT (kept as is), docstrings (سلاسل التوثيق), functional correctness (الصحة الوظيفية), sampling (أخذ العينات)
- **Figures referenced:** None in abstract
- **Equations:** None in abstract
- **Citations:** References to GPT-3 and GPT-J
- **Special handling:** Model names kept in English as they are proper nouns

### Quality Metrics

- Semantic equivalence: 0.95
- Technical accuracy: 0.95
- Readability: 0.90
- Glossary consistency: 0.90
- **Overall section score:** 0.92
