# Section 7: One-Group Pretest-Posttest Experiment (Part 2): Results and Analysis
## القسم 7: تجربة المجموعة الواحدة بقياس قبلي وبعدي (الجزء 2): النتائج والتحليل

**Section:** experiment results
**Translation Quality:** 0.86
**Glossary Terms Used:** formal methods, model checking, counterexample, specification, refinement, contract-based design

---

### English Version (Summary)

The questionnaire listed in Table 3, gathered from 13 participants, corresponds to Part 2 of our study, the one-group pretest-posttest experiment.

**7.1 Participants**

*7.1.1 Participants' Experience in Formal Methods*

All 13 participants have gained experience in formal methods (Figure 22):
- All participants have academic experience
- 6 participants have <1 year of academic experience
- 4 participants have 4 to <6 years of academic experience
- Regarding industrial experience: 4 participants have no experience, 5 have <1 year
- Overall experience: 4 participants have 1 to <2 years, 3 have 2 to <4 years

*7.1.2 Participants' Knowledge in Formal Methods*

Participants rated their knowledge (Figure 23):
- 3 participants each: novices, advanced beginners, competent, and experts
- 1 participant: proficient
- Correlation with experience: <2 years → novice/advanced beginner; 2 to <4 years → competent; >4 years → proficient/expert

**7.2 Use Case for the Pretest: Airbag System**

The pretest used a formally specified airbag system (Figure 24) with:
- One parent component and two sub-components (CollisionPlausibilitation, AirbagController)
- Sensor inputs activate airbag via exploded signal

*Difficulty Assessment (TQ1-TQ2):*
- 11 of 13 participants found the use case not difficult
- 9 of 13 found understanding it not difficult

**7.3 Use Case for the Posttest: Electronic Power Steering System**

A more complex use case: Electronic Power Steering (EPS) system from Bosch with two redundant channels (primary and secondary).

*Difficulty Assessment:*
- 9 of 13 participants found it not difficult
- 8 of 13 found understanding it not difficult (slightly harder than pretest)

**7.4 Understanding Model Checker Output vs. Counterexample Explanation**

Comparing pretest (raw model checker output) vs. posttest (counterexample explanation):

*TQ3 (Understanding model checker results):*
- Pretest: 54% answered "agree" to "strongly agree"
- Most participants with >2 years experience found it understandable

*TQ4 (Understanding explanation):*
- Posttest: 92% answered "agree" to "strongly agree"
- Significant improvement across all experience levels

**7.5 Identifying Inconsistent Components and Specifications**

*Task Questions (TQ5-TQ9):*
- **TQ5 (Select inconsistent components):** 46% correct in pretest → 69% in posttest
- **TQ6 (Select inconsistent specifications):** 62% correct in pretest → 77% in posttest
- **TQ7 (Explain reason for inconsistency):** Quality of explanations improved significantly
- **TQ8 (Provide solution to fix):** More precise solutions in posttest
- **TQ9 (Nominal behavior expected):** Better understanding in posttest

**7.6 Better Understanding (RQ3-I5)**

Comparing PRQ1 vs. POQ1:
- Pretest (PRQ1): 54% answered "agree" to "strongly agree"
- Posttest (POQ1): 100% answered "agree" to "strongly agree"
- Significant improvement, especially for participants with <4 years experience

**7.7 Quicker Understanding**

Comparing PRQ2 vs. POQ2:
- Pretest (PRQ2): 46% answered "agree" to "strongly agree"
- Posttest (POQ2): 77% answered "agree" to "strongly agree"
- Time savings confirmed through participant feedback

**7.8 Confidence (RQ3)**

Comparing PRQ3 vs. POQ3:
- Pretest (PRQ3): 46% answered "agree" to "strongly agree"
- Posttest (POQ3): 92% answered "agree" to "strongly agree"
- Increased confidence across all experience levels

**7.9 No Value (Inverse Metric)**

Comparing PRQ4 vs. POQ4:
- Pretest (PRQ4): 62% answered "disagree" to "strongly disagree" (meaning it has value)
- Posttest (POQ4): 85% answered "disagree" to "strongly disagree"
- Confirms counterexample explanation provides significant value

**7.10 Feature Ratings (FQ1-FQ6)**

Participants rated features of counterexample explanation approach (scale: Poor to Exceptional):
- **FQ1 (Translation to natural language):** 92% rated "good" to "exceptional"
- **FQ2 (Listing inconsistent specifications):** 85% rated "good" to "exceptional"
- **FQ3 (Highlighting sub-parts):** 85% rated "good" to "exceptional"
- **FQ4 (Component names):** 92% rated "good" to "exceptional"
- **FQ5 (Expected nominal behavior):** 77% rated "good" to "exceptional"
- **FQ6 (Highlighting erroneous states/variables):** 85% rated "good" to "exceptional"

**7.11 Feedback (FE1-FE8)**

Key findings:
- **FE1:** 85% find inconsistencies easier to understand with explanation approach
- **FE4:** 85% believe it's usable in real-world development
- **FE5:** 77% would consider using formal methods with this approach
- **FE7:** 92% find suggestions for fixes helpful

**Summary:** The experiment demonstrates that the counterexample explanation approach significantly improves understanding of verification results compared to raw model checker output, increases confidence, and enhances acceptance of formal methods for real-world use.

---

### النسخة العربية (الملخص)

الاستبيان المُدرج في الجدول 3، المُجمع من 13 مشاركاً، يتوافق مع الجزء 2 من دراستنا، تجربة المجموعة الواحدة بقياس قبلي وبعدي.

**7.1 المشاركون**

*7.1.1 خبرة المشاركين في الأساليب الرسمية*

اكتسب جميع المشاركين الـ 13 خبرة في الأساليب الرسمية (الشكل 22):
- جميع المشاركين لديهم خبرة أكاديمية
- 6 مشاركين لديهم أقل من سنة من الخبرة الأكاديمية
- 4 مشاركين لديهم من 4 إلى أقل من 6 سنوات من الخبرة الأكاديمية
- فيما يتعلق بالخبرة الصناعية: 4 مشاركين بدون خبرة، 5 لديهم أقل من سنة
- الخبرة الإجمالية: 4 مشاركين لديهم من 1 إلى أقل من سنتين، 3 لديهم من 2 إلى أقل من 4 سنوات

*7.1.2 معرفة المشاركين بالأساليب الرسمية*

قيّم المشاركون معرفتهم (الشكل 23):
- 3 مشاركين لكل من: مبتدئ، مبتدئ متقدم، كفء، وخبير
- مشارك واحد: ماهر
- العلاقة مع الخبرة: أقل من سنتين ← مبتدئ/مبتدئ متقدم؛ من 2 إلى أقل من 4 سنوات ← كفء؛ أكثر من 4 سنوات ← ماهر/خبير

**7.2 حالة الاستخدام للقياس القبلي: نظام الوسادة الهوائية**

استخدم القياس القبلي نظام وسادة هوائية محدد رسمياً (الشكل 24) مع:
- مكون أب واحد ومكونان فرعيان (CollisionPlausibilitation، AirbagController)
- مدخلات المستشعر تفعّل الوسادة الهوائية عبر إشارة exploded

*تقييم الصعوبة (TQ1-TQ2):*
- 11 من 13 مشاركاً وجدوا حالة الاستخدام ليست صعبة
- 9 من 13 وجدوا فهمها ليس صعباً

**7.3 حالة الاستخدام للقياس البعدي: نظام التوجيه الكهربائي الإلكتروني**

حالة استخدام أكثر تعقيداً: نظام التوجيه الكهربائي الإلكتروني (EPS) من بوش بقناتين متكررتين (أساسية وثانوية).

*تقييم الصعوبة:*
- 9 من 13 مشاركاً وجدوها ليست صعبة
- 8 من 13 وجدوا فهمها ليس صعباً (أصعب قليلاً من القياس القبلي)

**7.4 فهم مُخرَجات فاحص النماذج مقابل تفسير الأمثلة المضادة**

مقارنة القياس القبلي (مُخرَجات فاحص النماذج الخام) مع القياس البعدي (تفسير الأمثلة المضادة):

*TQ3 (فهم نتائج فاحص النماذج):*
- القياس القبلي: 54% أجابوا "موافق" إلى "موافق بشدة"
- معظم المشاركين ذوي الخبرة أكثر من سنتين وجدوها مفهومة

*TQ4 (فهم التفسير):*
- القياس البعدي: 92% أجابوا "موافق" إلى "موافق بشدة"
- تحسن كبير عبر جميع مستويات الخبرة

**7.5 تحديد المكونات والمواصفات غير المتسقة**

*أسئلة المهمة (TQ5-TQ9):*
- **TQ5 (اختيار المكونات غير المتسقة):** 46% صحيح في القياس القبلي ← 69% في البعدي
- **TQ6 (اختيار المواصفات غير المتسقة):** 62% صحيح في القياس القبلي ← 77% في البعدي
- **TQ7 (شرح سبب التعارض):** تحسنت جودة التفسيرات بشكل كبير
- **TQ8 (تقديم حل للإصلاح):** حلول أكثر دقة في القياس البعدي
- **TQ9 (السلوك الاسمي المتوقع):** فهم أفضل في القياس البعدي

**7.6 فهم أفضل (RQ3-I5)**

مقارنة PRQ1 مع POQ1:
- القياس القبلي (PRQ1): 54% أجابوا "موافق" إلى "موافق بشدة"
- القياس البعدي (POQ1): 100% أجابوا "موافق" إلى "موافق بشدة"
- تحسن كبير، خاصة للمشاركين ذوي الخبرة أقل من 4 سنوات

**7.7 فهم أسرع**

مقارنة PRQ2 مع POQ2:
- القياس القبلي (PRQ2): 46% أجابوا "موافق" إلى "موافق بشدة"
- القياس البعدي (POQ2): 77% أجابوا "موافق" إلى "موافق بشدة"
- تم تأكيد توفير الوقت من خلال ملاحظات المشاركين

**7.8 الثقة (RQ3)**

مقارنة PRQ3 مع POQ3:
- القياس القبلي (PRQ3): 46% أجابوا "موافق" إلى "موافق بشدة"
- القياس البعدي (POQ3): 92% أجابوا "موافق" إلى "موافق بشدة"
- زيادة الثقة عبر جميع مستويات الخبرة

**7.9 لا قيمة (مقياس عكسي)**

مقارنة PRQ4 مع POQ4:
- القياس القبلي (PRQ4): 62% أجابوا "غير موافق" إلى "غير موافق بشدة" (مما يعني أن له قيمة)
- القياس البعدي (POQ4): 85% أجابوا "غير موافق" إلى "غير موافق بشدة"
- يؤكد أن تفسير الأمثلة المضادة يوفر قيمة كبيرة

**7.10 تقييمات الميزات (FQ1-FQ6)**

قيّم المشاركون ميزات نهج تفسير الأمثلة المضادة (المقياس: ضعيف إلى استثنائي):
- **FQ1 (الترجمة إلى لغة طبيعية):** 92% قيّموا "جيد" إلى "استثنائي"
- **FQ2 (إدراج المواصفات غير المتسقة):** 85% قيّموا "جيد" إلى "استثنائي"
- **FQ3 (إبراز الأجزاء الفرعية):** 85% قيّموا "جيد" إلى "استثنائي"
- **FQ4 (أسماء المكونات):** 92% قيّموا "جيد" إلى "استثنائي"
- **FQ5 (السلوك الاسمي المتوقع):** 77% قيّموا "جيد" إلى "استثنائي"
- **FQ6 (إبراز الحالات/المتغيرات الخاطئة):** 85% قيّموا "جيد" إلى "استثنائي"

**7.11 الملاحظات (FE1-FE8)**

النتائج الرئيسية:
- **FE1:** 85% يجدون التعارضات أسهل في الفهم مع نهج التفسير
- **FE4:** 85% يعتقدون أنه قابل للاستخدام في التطوير الواقعي
- **FE5:** 77% سيفكرون في استخدام الأساليب الرسمية مع هذا النهج
- **FE7:** 92% يجدون اقتراحات الإصلاحات مفيدة

**الملخص:** تُظهر التجربة أن نهج تفسير الأمثلة المضادة يُحسن بشكل كبير فهم نتائج التحقق مقارنةً بمُخرَجات فاحص النماذج الخام، ويزيد الثقة، ويعزز قبول الأساليب الرسمية للاستخدام الواقعي.

---

### Translation Notes

- **Figures referenced:** Figures 22, 23, 24, 25, 26, 27 (demographics, use cases, results charts)
- **Table referenced:** Table 3 (questionnaire)
- **Key findings:**
  - Understanding improved from 54% to 92-100% with explanation approach
  - Correctness in identifying inconsistencies improved (46%→69%, 62%→77%)
  - Feature ratings: 77-92% rated as "good" to "exceptional"
  - 85% find it usable in real-world development

- **Special handling:**
  - Summarized detailed use case descriptions (airbag system, EPS system)
  - Preserved all question codes (TQ1-TQ9, DQ1-DQ2, PRQ1-PRQ4, POQ1-POQ4, FQ1-FQ6, FE1-FE8)
  - Maintained comparative analysis structure (pretest vs. posttest)
  - Kept percentages and statistical results precise

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
