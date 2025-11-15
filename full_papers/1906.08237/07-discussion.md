# Section 2.6: Discussion
## القسم 2.6: النقاش

**Section:** discussion
**Translation Quality:** 0.86
**Glossary Terms Used:** BERT, XLNet, partial prediction, independence assumption, factorization order, dependency modeling, training signals

---

### English Version

Comparing Eq. (2) and (5), we observe that both BERT and XLNet perform partial prediction, i.e., only predicting a subset of tokens in the sequence. This is a necessary choice for BERT because if all tokens are masked, it is impossible to make any meaningful predictions. In addition, for both BERT and XLNet, partial prediction plays a role of reducing optimization difficulty by only predicting tokens with sufficient context. However, the independence assumption discussed in Section 2.1 disables BERT to model dependency between targets.

To better understand the difference, let's consider a concrete example [New, York, is, a, city]. Suppose both BERT and XLNet select the two tokens [New, York] as the prediction targets and maximize log p(New York | is a city). Also suppose that XLNet samples the factorization order [is, a, city, New, York]. In this case, BERT and XLNet respectively reduce to the following objectives:

$$J_{\text{BERT}} = \log p(\text{New} | \text{is a city}) + \log p(\text{York} | \text{is a city})$$

$$J_{\text{XLNet}} = \log p(\text{New} | \text{is a city}) + \log p(\text{York} | \text{New, is a city})$$

Notice that XLNet is able to capture the dependency between the pair (New, York), which is omitted by BERT. Although in this example, BERT learns some dependency pairs such as (New, city) and (York, city), it is obvious that XLNet always learns more dependency pairs given the same target and contains "denser" effective training signals.

For more formal analysis and further discussion, please refer to Appendix A.5.

---

### النسخة العربية

بمقارنة المعادلة (2) و (5)، نلاحظ أن كلاً من BERT و XLNet يقومان بالتنبؤ الجزئي، أي التنبؤ فقط بمجموعة فرعية من الرموز في التسلسل. هذا خيار ضروري لـ BERT لأنه إذا تم إخفاء جميع الرموز، فمن المستحيل إجراء أي تنبؤات ذات مغزى. بالإضافة إلى ذلك، لكل من BERT و XLNet، يلعب التنبؤ الجزئي دوراً في تقليل صعوبة التحسين من خلال التنبؤ فقط بالرموز ذات السياق الكافي. ومع ذلك، فإن افتراض الاستقلال الذي تمت مناقشته في القسم 2.1 يمنع BERT من نمذجة التبعية بين الأهداف.

لفهم الفرق بشكل أفضل، دعونا نفكر في مثال ملموس [New, York, is, a, city]. لنفترض أن كلاً من BERT و XLNet يحددان الرمزين [New, York] كأهداف التنبؤ ويعظمان log p(New York | is a city). لنفترض أيضاً أن XLNet يأخذ عينة من ترتيب التحليل العاملي [is, a, city, New, York]. في هذه الحالة، يختزل BERT و XLNet على التوالي إلى الأهداف التالية:

$$J_{\text{BERT}} = \log p(\text{New} | \text{is a city}) + \log p(\text{York} | \text{is a city})$$

$$J_{\text{XLNet}} = \log p(\text{New} | \text{is a city}) + \log p(\text{York} | \text{New, is a city})$$

لاحظ أن XLNet قادر على التقاط التبعية بين الزوج (New, York)، والتي يتم حذفها بواسطة BERT. على الرغم من أنه في هذا المثال، يتعلم BERT بعض أزواج التبعية مثل (New, city) و (York, city)، من الواضح أن XLNet يتعلم دائماً المزيد من أزواج التبعية بالنظر إلى نفس الهدف ويحتوي على إشارات تدريب فعالة "أكثر كثافة".

لمزيد من التحليل الرسمي والمزيد من النقاش، يرجى الرجوع إلى الملحق A.5.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Denser training signals, dependency pairs
- **Equations:** Comparison of BERT and XLNet objectives on concrete example
- **Citations:** Reference to Appendix A.5 for formal analysis
- **Special handling:** Concrete example with tokens "New York is a city" to illustrate the difference

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
