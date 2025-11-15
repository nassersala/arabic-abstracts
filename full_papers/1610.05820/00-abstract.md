# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** machine learning (تعلم الآلة), model (نموذج), training (التدريب), inference (استنتاج), membership inference (استنتاج العضوية), attack (هجوم), privacy (خصوصية), security (أمان), dataset (مجموعة بيانات), classification (تصنيف), mitigation (تخفيف)

---

### English Version

We quantify the privacy loss of machine learning models by membership inference attacks. Given a machine learning model and a record, we determine whether this record was in the model's training dataset. Our method trains an inference model to recognize differences in the target model's predictions on the inputs that it trained on versus the inputs that it did not train on. We empirically evaluate our attacks on classification models trained by commercial "machine learning as a service" providers such as Google and Amazon. Using realistic datasets and classification tasks, including a hospital discharge dataset whose membership is sensitive, we show that these models can be vulnerable to membership inference attacks. We then investigate the factors that influence this leakage and evaluate mitigation strategies.

---

### النسخة العربية

نقيس فقدان الخصوصية في نماذج تعلم الآلة من خلال هجمات استنتاج العضوية. بإعطاء نموذج تعلم آلة وسجل، نحدد ما إذا كان هذا السجل موجوداً في مجموعة بيانات تدريب النموذج. تقوم طريقتنا بتدريب نموذج استنتاج للتعرف على الفروقات في تنبؤات النموذج المستهدف على المدخلات التي تدرب عليها مقابل المدخلات التي لم يتدرب عليها. نقيّم هجماتنا تجريبياً على نماذج التصنيف المدربة من قبل مزودي "تعلم الآلة كخدمة" التجاريين مثل جوجل وأمازون. باستخدام مجموعات بيانات ومهام تصنيف واقعية، بما في ذلك مجموعة بيانات خروج المستشفى التي تعتبر عضويتها حساسة، نوضح أن هذه النماذج يمكن أن تكون عرضة لهجمات استنتاج العضوية. ثم نحقق في العوامل التي تؤثر على هذا التسريب ونقيّم استراتيجيات التخفيف.

---

### Translation Notes

- **Key terms introduced:** membership inference attack (هجوم استنتاج العضوية), privacy loss (فقدان الخصوصية), target model (النموذج المستهدف), privacy leakage (تسريب الخصوصية)
- **Special handling:** Focus on security and privacy terminology consistency
- **Context:** This abstract introduces the first systematic study of membership inference attacks

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90
