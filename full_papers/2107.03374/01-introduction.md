# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** نماذج اللغة الكبيرة, تعلم عميق, توليد البرامج, معمارية, ضبط دقيق, مجموعة بيانات, تعلم تمثيلي

---

### English Version

Scalable sequence prediction models (Graves, 2014; Vaswani et al., 2017; Child et al., 2019) have become a general-purpose method for generation and representation learning in many domains, including natural language processing (Mikolov et al., 2013; Sutskever et al., 2014; Dai & Le, 2015; Peters et al., 2018; Radford et al., 2018; Devlin et al., 2018), computer vision (Van Oord et al., 2016; Menick & Kalchbrenner, 2018; Chen et al., 2020; Bao et al., 2021), audio and speech processing (Oord et al., 2016; 2018; Dhariwal et al., 2020; Baevski et al., 2020), biology (Alley et al., 2019; Rives et al., 2021), and even across multiple modalities (Das et al., 2017; Lu et al., 2019; Ramesh et al., 2021; Zellers et al., 2021). More recently, language models have also fueled progress towards the longstanding challenge of program synthesis (Simon, 1963; Manna & Waldinger, 1971), spurred by the presence of code in large datasets (Husain et al., 2019; Gao et al., 2020) and the resulting programming capabilities of language models trained on these datasets (Wang & Komatsuzaki, 2021). Popular language modeling objectives like masked language modeling (Devlin et al., 2018) and span prediction (Raffel et al., 2020) have also been adapted to train their programming counterparts CodeBERT (Feng et al., 2020) and PyMT5 (Clement et al., 2020).

Similarly, our early investigation of GPT-3 (Brown et al., 2020) revealed that it could generate simple programs from Python docstrings. While rudimentary, this capability was exciting because GPT-3 was not explicitly trained for code generation. Given the considerable success of large language models in other modalities and the abundance of publicly available code, we hypothesized that a specialized GPT model, called Codex, could excel at a variety of coding tasks. This paper describes several early Codex models, whose descendants power GitHub Copilot and the Codex models in the OpenAI API.

---

### النسخة العربية

أصبحت نماذج التنبؤ بالتسلسلات القابلة للتوسع (Graves, 2014; Vaswani et al., 2017; Child et al., 2019) طريقة عامة الغرض للتوليد والتعلم التمثيلي في العديد من المجالات، بما في ذلك معالجة اللغة الطبيعية (Mikolov et al., 2013; Sutskever et al., 2014; Dai & Le, 2015; Peters et al., 2018; Radford et al., 2018; Devlin et al., 2018)، ورؤية حاسوبية (Van Oord et al., 2016; Menick & Kalchbrenner, 2018; Chen et al., 2020; Bao et al., 2021)، ومعالجة الصوت والكلام (Oord et al., 2016; 2018; Dhariwal et al., 2020; Baevski et al., 2020)، وعلم الأحياء (Alley et al., 2019; Rives et al., 2021)، وحتى عبر طرائق متعددة (Das et al., 2017; Lu et al., 2019; Ramesh et al., 2021; Zellers et al., 2021). في الآونة الأخيرة، غذت نماذج اللغة أيضاً التقدم نحو التحدي طويل الأمد لتوليد البرامج (Simon, 1963; Manna & Waldinger, 1971)، مدفوعاً بوجود الشفرة البرمجية في مجموعات البيانات الكبيرة (Husain et al., 2019; Gao et al., 2020) وقدرات البرمجة الناتجة لنماذج اللغة المدربة على هذه مجموعات البيانات (Wang & Komatsuzaki, 2021). تم أيضاً تكييف أهداف نمذجة اللغة الشائعة مثل نمذجة اللغة المقنعة (Devlin et al., 2018) والتنبؤ بالنطاق (Raffel et al., 2020) لتدريب نظيراتها البرمجية CodeBERT (Feng et al., 2020) و PyMT5 (Clement et al., 2020).

بالمثل، كشف تحقيقنا المبكر في GPT-3 (Brown et al., 2020) أنه يمكنه توليد برامج بسيطة من سلاسل التوثيق في Python. على الرغم من أن هذه القدرة كانت أولية، إلا أنها كانت مثيرة لأن GPT-3 لم يتم تدريبه صراحةً لتوليد الشفرة البرمجية. بالنظر إلى النجاح الكبير لنماذج اللغة الكبيرة في طرائق أخرى ووفرة الشفرة البرمجية المتاحة للعامة، افترضنا أن نموذج GPT متخصص، يُسمى Codex، يمكن أن يتفوق في مجموعة متنوعة من مهام البرمجة. تصف هذه الورقة العديد من نماذج Codex المبكرة، والتي تشغل سلالاتها GitHub Copilot ونماذج Codex في واجهة برمجة التطبيقات OpenAI API.

---

### Translation Notes

- **Key terms introduced:** sequence prediction models (نماذج التنبؤ بالتسلسلات), representation learning (التعلم التمثيلي), program synthesis (توليد البرامج), masked language modeling (نمذجة اللغة المقنعة), docstrings (سلاسل التوثيق)
- **Figures referenced:** None
- **Equations:** None
- **Citations:** [35 references cited] - all kept in original format
- **Special handling:** Model names (GPT-3, CodeBERT, PyMT5, Codex) kept in English; GitHub Copilot kept as proper noun

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.85
- **Overall section score:** 0.88
