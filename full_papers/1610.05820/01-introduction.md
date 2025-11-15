# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** machine learning (تعلم الآلة), privacy (خصوصية), training data (بيانات التدريب), overfitting (فرط الملاءمة), generalization (التعميم), inference attack (هجوم استنتاج), black-box (صندوق أسود), model (نموذج), membership (عضوية)

---

### English Version

Machine learning (ML) is increasingly used to produce predictive models for applications ranging from personalized language models to recommender systems to medical diagnosis. These models are trained on datasets that may contain sensitive information about individuals: their preferences and interests, demographic attributes, location, health, and much more. When a model is made accessible, either as a service or as a publicly released artifact, does it leak information about the data that it was trained on?

Privacy-preserving machine learning, or PPML, aims to protect the privacy of individual training records from the potential adversaries who have access to the ML model. The question, however, is: what exactly should be protected? And, more importantly, is the protection actually effective? In this paper, we measure the effectiveness of ML models' privacy by means of membership inference attacks.

In a membership inference attack, given a machine learning model and a record, the attacker determines whether the record was in the model's training dataset. For instance, consider a model trained to predict patient health outcomes based on hospital records. A successful membership inference attack would allow the attacker to determine whether a specific patient's record was used to train the model. This information alone can be sensitive: it reveals that the person was a patient at that hospital, potentially exposing the individual's health status.

The ability to perform membership inference raises serious privacy concerns. Even if the model does not explicitly output individual training records, simply revealing that a particular person's data was part of the training set may violate their privacy. This is especially problematic for sensitive applications such as health, location, or financial data.

**Our attack model.** We focus on black-box membership inference attacks, where the adversary can only observe the predictions (but not the parameters or other internals) of the target model. This is a realistic threat model because many machine learning models are deployed as services (e.g., Google Prediction API, Amazon Machine Learning, Microsoft Azure ML), where users can submit queries and obtain predictions but cannot access the model's parameters.

**Shadow training technique.** Our approach is based on training a separate "attack model" that can distinguish whether a given record was in the training set of the target model or not. To train this attack model, we need examples of model behavior on both training and non-training inputs. Since we don't have access to the target model's training data, we develop a shadow training technique: we train shadow models on synthetic datasets sampled from the same distribution as the target model's training data. These shadow models mimic the target model's behavior. We then use the shadow models' predictions on their own training and non-training data to train our attack model.

**Contributions.** Our contributions in this paper are as follows:

1. **Attack methodology:** We develop a general methodology for membership inference attacks against machine learning models. Our attacks work in the black-box setting and do not require knowledge of the target model's parameters or architecture.

2. **Empirical evaluation:** We empirically evaluate our attacks on several state-of-the-art machine learning models, including deep neural networks, provided by commercial ML-as-a-service platforms (Google Prediction API and Amazon Machine Learning). We demonstrate that these models are vulnerable to membership inference attacks, achieving attack precision of up to 90% on some models.

3. **Real-world datasets:** We evaluate our attacks on realistic classification tasks using datasets from various domains, including a hospital discharge dataset. We show that membership inference can succeed even when the model achieves high classification accuracy and generalizes well.

4. **Understanding privacy leakage:** We investigate the factors that influence the success of membership inference attacks. We show that overfitting is a significant factor, but not the only one. Even well-regularized models that generalize well can be vulnerable to our attacks.

5. **Mitigation strategies:** We evaluate several defense mechanisms and mitigation strategies, including regularization techniques, dropout, and model stacking. We find that while these techniques can reduce the success of membership inference attacks, they do not completely eliminate the vulnerability.

**Organization.** The rest of this paper is organized as follows. Section II provides background and discusses related work on privacy in machine learning. Section III describes our membership inference attack in detail. Section IV explains our shadow training technique for generating training data for the attack model. Section V describes our experimental setup. Section VI presents our empirical evaluation results. Section VII analyzes the factors that attacks exploit. Section VIII evaluates mitigation strategies. Section IX discusses broader implications and future work. Section X concludes.

---

### النسخة العربية

يُستخدم تعلم الآلة بشكل متزايد لإنتاج نماذج تنبؤية لتطبيقات تتراوح من نماذج اللغة الشخصية إلى أنظمة التوصية إلى التشخيص الطبي. يتم تدريب هذه النماذج على مجموعات بيانات قد تحتوي على معلومات حساسة عن الأفراد: تفضيلاتهم واهتماماتهم، والسمات الديموغرافية، والموقع، والصحة، وغير ذلك الكثير. عندما يُتاح الوصول إلى نموذج، سواء كخدمة أو كمنتج منشور علناً، هل يسرّب معلومات عن البيانات التي تم تدريبه عليها؟

يهدف تعلم الآلة الحافظ للخصوصية (PPML) إلى حماية خصوصية سجلات التدريب الفردية من الخصوم المحتملين الذين لديهم وصول إلى نموذج تعلم الآلة. لكن السؤال هو: ما الذي يجب حمايته بالضبط؟ والأهم من ذلك، هل الحماية فعالة حقاً؟ في هذا البحث، نقيس فعالية خصوصية نماذج تعلم الآلة عن طريق هجمات استنتاج العضوية.

في هجوم استنتاج العضوية، بإعطاء نموذج تعلم آلة وسجل، يحدد المهاجم ما إذا كان السجل موجوداً في مجموعة بيانات تدريب النموذج. على سبيل المثال، اعتبر نموذجاً مدرباً للتنبؤ بنتائج صحة المرضى بناءً على السجلات الطبية للمستشفى. سيسمح هجوم استنتاج العضوية الناجح للمهاجم بتحديد ما إذا كان سجل مريض معين قد استُخدم لتدريب النموذج. هذه المعلومات وحدها يمكن أن تكون حساسة: فهي تكشف أن الشخص كان مريضاً في ذلك المستشفى، مما قد يكشف عن الحالة الصحية للفرد.

تثير القدرة على تنفيذ استنتاج العضوية مخاوف خطيرة بشأن الخصوصية. حتى لو لم يخرج النموذج صراحة سجلات التدريب الفردية، فإن مجرد الكشف عن أن بيانات شخص معين كانت جزءاً من مجموعة التدريب قد ينتهك خصوصيته. هذا يمثل مشكلة خاصة للتطبيقات الحساسة مثل البيانات الصحية أو بيانات الموقع أو البيانات المالية.

**نموذج هجومنا.** نركز على هجمات استنتاج العضوية من نوع الصندوق الأسود، حيث يمكن للخصم فقط ملاحظة تنبؤات النموذج المستهدف (وليس المعاملات أو المكونات الداخلية الأخرى). هذا نموذج تهديد واقعي لأن العديد من نماذج تعلم الآلة يتم نشرها كخدمات (مثل Google Prediction API، وAmazon Machine Learning، وMicrosoft Azure ML)، حيث يمكن للمستخدمين إرسال استعلامات والحصول على تنبؤات ولكن لا يمكنهم الوصول إلى معاملات النموذج.

**تقنية التدريب الظلي.** يعتمد نهجنا على تدريب "نموذج هجوم" منفصل يمكنه التمييز بين ما إذا كان سجل معين موجوداً في مجموعة تدريب النموذج المستهدف أم لا. لتدريب نموذج الهجوم هذا، نحتاج إلى أمثلة على سلوك النموذج على كل من مدخلات التدريب وغير التدريب. نظراً لأننا لا نملك وصولاً إلى بيانات تدريب النموذج المستهدف، نطور تقنية التدريب الظلي: نقوم بتدريب نماذج ظلية على مجموعات بيانات اصطناعية مُعاينة من نفس التوزيع الخاص ببيانات تدريب النموذج المستهدف. تحاكي هذه النماذج الظلية سلوك النموذج المستهدف. ثم نستخدم تنبؤات النماذج الظلية على بيانات التدريب وغير التدريب الخاصة بها لتدريب نموذج الهجوم.

**المساهمات.** مساهماتنا في هذا البحث هي كما يلي:

1. **منهجية الهجوم:** نطور منهجية عامة لهجمات استنتاج العضوية ضد نماذج تعلم الآلة. تعمل هجماتنا في إعداد الصندوق الأسود ولا تتطلب معرفة معاملات النموذج المستهدف أو معماريته.

2. **التقييم التجريبي:** نقيّم هجماتنا تجريبياً على عدة نماذج متقدمة لتعلم الآلة، بما في ذلك الشبكات العصبية العميقة، المقدمة من منصات تعلم الآلة كخدمة التجارية (Google Prediction API وAmazon Machine Learning). نوضح أن هذه النماذج عرضة لهجمات استنتاج العضوية، محققين دقة هجوم تصل إلى 90% على بعض النماذج.

3. **مجموعات بيانات واقعية:** نقيّم هجماتنا على مهام تصنيف واقعية باستخدام مجموعات بيانات من مجالات مختلفة، بما في ذلك مجموعة بيانات خروج المستشفى. نوضح أن استنتاج العضوية يمكن أن ينجح حتى عندما يحقق النموذج دقة تصنيف عالية ويعمم جيداً.

4. **فهم تسريب الخصوصية:** نحقق في العوامل التي تؤثر على نجاح هجمات استنتاج العضوية. نوضح أن فرط الملاءمة عامل مهم، ولكن ليس الوحيد. حتى النماذج المنتظمة جيداً التي تعمم بشكل جيد يمكن أن تكون عرضة لهجماتنا.

5. **استراتيجيات التخفيف:** نقيّم عدة آليات دفاع واستراتيجيات تخفيف، بما في ذلك تقنيات الانتظام، والإسقاط، وتكديس النماذج. نجد أنه بينما يمكن لهذه التقنيات تقليل نجاح هجمات استنتاج العضوية، فإنها لا تقضي تماماً على الثغرة.

**تنظيم البحث.** يتم تنظيم بقية هذا البحث على النحو التالي. يقدم القسم الثاني الخلفية ويناقش الأعمال ذات الصلة بالخصوصية في تعلم الآلة. يصف القسم الثالث هجوم استنتاج العضوية الخاص بنا بالتفصيل. يشرح القسم الرابع تقنية التدريب الظلي لتوليد بيانات تدريب لنموذج الهجوم. يصف القسم الخامس إعدادنا التجريبي. يعرض القسم السادس نتائج تقييمنا التجريبي. يحلل القسم السابع العوامل التي تستغلها الهجمات. يقيّم القسم الثامن استراتيجيات التخفيف. يناقش القسم التاسع الآثار الأوسع والعمل المستقبلي. يختتم القسم العاشر البحث.

---

### Translation Notes

- **Key terms introduced:**
  - Privacy-preserving machine learning (تعلم الآلة الحافظ للخصوصية)
  - Membership inference attack (هجوم استنتاج العضوية)
  - Black-box attack (هجوم الصندوق الأسود)
  - Shadow training (التدريب الظلي)
  - Shadow models (النماذج الظلية)
  - Attack model (نموذج الهجوم)
  - Target model (النموذج المستهدف)
  - Privacy leakage (تسريب الخصوصية)
  - ML-as-a-service (تعلم الآلة كخدمة)

- **Figures referenced:** None in introduction
- **Equations:** None in introduction
- **Citations:** Multiple references to sections II-X
- **Special handling:** Maintained formal academic tone, preserved section numbering system

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
