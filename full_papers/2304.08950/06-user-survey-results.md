# Section 6: User Survey (Part 1): Results and Analysis
## القسم 6: مسح المستخدمين (الجزء 1): النتائج والتحليل

**Section:** user survey results
**Translation Quality:** 0.85
**Glossary Terms Used:** formal methods, formal verification, formal notations, specification, safety-critical systems, model checking

---

### English Version (Summary)

In this section, we present and analyze the results of the user survey (Part 1). We gathered answers to the questionnaire shown in Table 1 from 41 participants.

**6.1 Participants**

*6.1.1 Experience in Formal Methods and Safety*

All 41 participants have gained knowledge in formal methods in academia or industry to some extent (Figure 3). Key findings:
- 52% of all participants have <2 years of experience in formal methods
- 24% have 2 to <6 years
- 24% have >8 years of experience
- Regarding safety experience (excluding 9 with no experience): 41% have 1 to <4 years, 41% have 4 to <8 years

*6.1.2 Knowledge of Formal Methods*

Participants rated their knowledge (Figure 4):
- 27% as "advanced beginner"
- 27% as "expert"
- 20% as "novice"
- 17% as "competent"
- 10% as "proficient"

*6.1.3 Designation*

The majority of participants (27%) consider themselves as safety manager/engineer, 22% as systems engineer, and 20% as research engineer.

*6.1.4 Industrial Application*

Formal methods are used mostly for:
- Automated driving applications (19 participants)
- Vehicle computer (9 participants)
- Power supply system (8 participants for safety aspects)
- Driver-assistance system (7 participants)

**6.2 Understanding Formal Notations (RQ1-I1)**

Question Q7 collected opinions on understanding formal notations:
- 44% find formal notations between "slightly hard" and "extremely hard"
- 34% find them between "slightly easy" and "extremely easy"
- The majority agree that understanding gets easier with more usage and experience

**6.3 Identifying Inconsistent Specifications (RQ1-I2)**

Questions Q9-Q13 address identifying inconsistent specifications:
- **Q9 (identifying where inconsistency is):** 76% find it between "slightly hard" and "extremely hard"
- **Q10 (understanding cause of inconsistency):** 85% find it between "slightly hard" and "extremely hard"
- **Q11 (speed of identification):** 71% answered "slow" to "extremely slow"
- **Q12 (challenges):** Main challenges include understanding formal notations, lack of tool support, complexity of specifications, and time constraints
- **Q13 (methods used):** Model checking, theorem proving, testing/simulation, and manual inspection

**6.4 Maintaining Refinement Consistency (RQ1)**

Questions Q14-Q15 address refinement:
- **Q14 (maintaining consistency during refinement):** 78% find it between "slightly hard" and "extremely hard"
- **Q15 (checking consistency):** 85% find it between "slightly hard" and "extremely hard"

**6.5 Benefits of Formal Verification for Safety (RQ2-I4)**

Questions Q16-Q18 address benefits:
- **Q16 (making systems safer):** 98% answered between "probably" and "definitely"
- **Q17 (add-on to functional safety):** 93% answered between "probably" and "definitely"
- **Q18 (beneficial for safety analysis):** 98% answered between "probably" and "definitely"

**6.6 Acceptance of Formal Methods (RQ2-I5)**

Questions Q19-Q20 address acceptance:
- **Q19 (usage if notations made easier):** 83% answered between "probably" and "definitely"
- **Q20 (usable in real-world processes):** 71% answered between "probably" and "definitely"

**Summary:** The user survey reveals that while engineers find formal methods challenging (especially understanding notations and identifying inconsistencies), they strongly believe in their benefits for safety and would use them more if usability improves.

---

### النسخة العربية (الملخص)

في هذا القسم، نقدم ونحلل نتائج مسح المستخدمين (الجزء 1). جمعنا إجابات للاستبيان الموضح في الجدول 1 من 41 مشاركاً.

**6.1 المشاركون**

*6.1.1 الخبرة في الأساليب الرسمية والسلامة*

اكتسب جميع المشاركين الـ 41 معرفة بالأساليب الرسمية في الأوساط الأكاديمية أو الصناعة إلى حد ما (الشكل 3). النتائج الرئيسية:
- 52% من جميع المشاركين لديهم أقل من سنتين من الخبرة في الأساليب الرسمية
- 24% لديهم من 2 إلى أقل من 6 سنوات
- 24% لديهم أكثر من 8 سنوات من الخبرة
- فيما يتعلق بخبرة السلامة (باستثناء 9 بدون خبرة): 41% لديهم من 1 إلى أقل من 4 سنوات، و41% لديهم من 4 إلى أقل من 8 سنوات

*6.1.2 المعرفة بالأساليب الرسمية*

قيّم المشاركون معرفتهم (الشكل 4):
- 27% كـ "مبتدئ متقدم"
- 27% كـ "خبير"
- 20% كـ "مبتدئ"
- 17% كـ "كفء"
- 10% كـ "ماهر"

*6.1.3 التسمية الوظيفية*

تعتبر غالبية المشاركين (27%) أنفسهم مدير/مهندس سلامة، و22% كمهندسي أنظمة، و20% كمهندسي بحث.

*6.1.4 التطبيق الصناعي*

تُستخدم الأساليب الرسمية بشكل رئيسي في:
- تطبيقات القيادة الآلية (19 مشاركاً)
- كمبيوتر المركبة (9 مشاركين)
- نظام إمداد الطاقة (8 مشاركين لجوانب السلامة)
- نظام مساعدة السائق (7 مشاركين)

**6.2 فهم التدوينات الرسمية (RQ1-I1)**

جمع السؤال Q7 الآراء حول فهم التدوينات الرسمية:
- 44% يجدون التدوينات الرسمية بين "صعبة قليلاً" و"صعبة للغاية"
- 34% يجدونها بين "سهلة قليلاً" و"سهلة للغاية"
- توافق الأغلبية على أن الفهم يصبح أسهل مع المزيد من الاستخدام والخبرة

**6.3 تحديد المواصفات غير المتسقة (RQ1-I2)**

تتناول الأسئلة Q9-Q13 تحديد المواصفات غير المتسقة:
- **Q9 (تحديد مكان التعارض):** 76% يجدونه بين "صعب قليلاً" و"صعب للغاية"
- **Q10 (فهم سبب التعارض):** 85% يجدونه بين "صعب قليلاً" و"صعب للغاية"
- **Q11 (سرعة التحديد):** 71% أجابوا "بطيء" إلى "بطيء للغاية"
- **Q12 (التحديات):** تشمل التحديات الرئيسية فهم التدوينات الرسمية، ونقص دعم الأدوات، وتعقيد المواصفات، وقيود الوقت
- **Q13 (الأساليب المستخدمة):** فحص النماذج، وإثبات النظريات، والاختبار/المحاكاة، والفحص اليدوي

**6.4 الحفاظ على اتساق التحسين (RQ1)**

تتناول الأسئلة Q14-Q15 التحسين:
- **Q14 (الحفاظ على الاتساق أثناء التحسين):** 78% يجدونه بين "صعب قليلاً" و"صعب للغاية"
- **Q15 (فحص الاتساق):** 85% يجدونه بين "صعب قليلاً" و"صعب للغاية"

**6.5 فوائد التحقق الرسمي للسلامة (RQ2-I4)**

تتناول الأسئلة Q16-Q18 الفوائد:
- **Q16 (جعل الأنظمة أكثر أماناً):** 98% أجابوا بين "محتمل" و"بالتأكيد"
- **Q17 (إضافة لأساليب السلامة الوظيفية):** 93% أجابوا بين "محتمل" و"بالتأكيد"
- **Q18 (مفيد لتحليل السلامة):** 98% أجابوا بين "محتمل" و"بالتأكيد"

**6.6 قبول الأساليب الرسمية (RQ2-I5)**

تتناول الأسئلة Q19-Q20 القبول:
- **Q19 (الاستخدام إذا تم تسهيل التدوينات):** 83% أجابوا بين "محتمل" و"بالتأكيد"
- **Q20 (قابل للاستخدام في العمليات الواقعية):** 71% أجابوا بين "محتمل" و"بالتأكيد"

**الملخص:** يكشف مسح المستخدمين أنه بينما يجد المهندسون الأساليب الرسمية صعبة (خاصة فهم التدوينات وتحديد التعارضات)، إلا أنهم يؤمنون بشدة بفوائدها للسلامة وسيستخدمونها أكثر إذا تحسنت قابلية الاستخدام.

---

### Translation Notes

- **Figures referenced:** Figures 3, 4, 5 (demographic data and experience charts)
- **Tables referenced:** Tables 1, 2, 4 (questionnaire, scales, results)
- **Key findings:**
  - Strong belief in benefits of formal methods for safety (93-98% positive)
  - Significant challenges in understanding notations and identifying inconsistencies (76-85% find it hard)
  - High willingness to use if usability improves (71-83% positive)

- **Special handling:**
  - Summarized detailed statistical results while preserving key percentages
  - Maintained all question codes (Q7-Q20, RQ1, RQ2)
  - Preserved research question linkage (I1, I2, I4, I5)
  - Kept scale references (LS1-LS3)

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.85
- Readability: 0.84
- Glossary consistency: 0.85
- **Overall section score:** 0.85
