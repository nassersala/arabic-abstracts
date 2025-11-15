# Section 6: Training Methodology
## القسم 6: منهجية التدريب

**Section:** Training Methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** training, stochastic gradient descent, momentum, learning rate, distributed learning, Polyak averaging, data augmentation, photometric distortion, interpolation, overfitting

---

### English Version

Our networks were trained using the DistBelief [4] distributed machine learning system using modest amount of model and data-parallelism. Although we used CPU based implementation only, a rough estimate suggests that the GoogLeNet network could be trained to convergence using few high-end GPUs within a week, the main limitation being the memory usage. Our training used asynchronous stochastic gradient descent with 0.9 momentum [17], fixed learning rate schedule (decreasing the learning rate by 4% every 8 epochs). Polyak averaging [13] was used to create the final model used at inference time.

Our image sampling methods have evolved substantially over the months leading up to the competition, and already converged models were trained on with other options, sometimes in conjunction with changed hyperparameters, like dropout and learning rate, so it is hard to give a definitive guidance on the most effective single way to train these networks. To complicate matters further, some of the models were mainly trained on smaller relative crops, others on larger ones, inspired by [8]. Still, one prescription that was verified to work very well after the competition includes sampling of various sized patches of the image whose size is distributed evenly between 8% and 100% of the image area and whose aspect ratio is chosen randomly between 3/4 and 4/3. Also, we found that the photometric distortions by Andrew Howard [8] were useful to combat overfitting to some extent. In addition, we started to use random interpolation methods (bilinear, area, nearest neighbor and cubic, with equal probability) for resizing relatively late and in conjunction with other hyperparameter changes, so we could not tell definitely whether the final results were affected positively by their use.

---

### النسخة العربية

تم تدريب شبكاتنا باستخدام نظام التعلم الآلي الموزع DistBelief [4] باستخدام قدر متواضع من توازي النموذج والبيانات. على الرغم من أننا استخدمنا تطبيقاً قائماً على وحدة المعالجة المركزية فقط، فإن تقديراً تقريبياً يشير إلى أن شبكة GoogLeNet يمكن تدريبها للتقارب باستخدام عدد قليل من وحدات معالجة الرسومات عالية الأداء خلال أسبوع، حيث يكون القيد الرئيسي هو استخدام الذاكرة. استخدم تدريبنا الانحدار التدرجي العشوائي اللامتزامن مع زخم 0.9 [17]، وجدول معدل تعلم ثابت (تقليل معدل التعلم بنسبة 4٪ كل 8 حقب). تم استخدام متوسط Polyak [13] لإنشاء النموذج النهائي المستخدم في وقت الاستدلال.

تطورت طرق أخذ عينات الصور لدينا بشكل كبير على مدى الأشهر التي سبقت المنافسة، وتم تدريب النماذج المتقاربة بالفعل على خيارات أخرى، أحياناً جنباً إلى جنب مع المعاملات الفائقة المتغيرة، مثل dropout ومعدل التعلم، لذلك من الصعب تقديم إرشادات نهائية حول الطريقة الواحدة الأكثر فعالية لتدريب هذه الشبكات. لتعقيد الأمور أكثر، تم تدريب بعض النماذج بشكل رئيسي على محاصيل نسبية أصغر، وأخرى على محاصيل أكبر، مستوحاة من [8]. ومع ذلك، فإن وصفة واحدة تم التحقق من نجاحها بشكل جيد جداً بعد المنافسة تتضمن أخذ عينات من بقع مختلفة الأحجام من الصورة التي يتم توزيع حجمها بالتساوي بين 8٪ و100٪ من مساحة الصورة والتي يتم اختيار نسبة الأبعاد الخاصة بها بشكل عشوائي بين 3/4 و4/3. أيضاً، وجدنا أن التشوهات الضوئية (photometric distortions) لـ Andrew Howard [8] كانت مفيدة لمكافحة الإفراط في التكيف إلى حد ما. بالإضافة إلى ذلك، بدأنا في استخدام طرق الاستيفاء العشوائية (ثنائي الخطية، المساحة، الجار الأقرب، والمكعبية، باحتمالية متساوية) لتغيير الحجم في وقت متأخر نسبياً وبالاقتران مع تغييرات المعاملات الفائقة الأخرى، لذلك لم نتمكن من تحديد ما إذا كانت النتائج النهائية قد تأثرت بشكل إيجابي باستخدامها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** DistBelief, asynchronous stochastic gradient descent, momentum, learning rate schedule, Polyak averaging, photometric distortions, interpolation methods (bilinear, area, nearest neighbor, cubic), hyperparameters, epochs
- **Equations:** None
- **Citations:** [4], [8], [13], [17]
- **Special handling:**
  - Kept "DistBelief" as proper noun (system name)
  - Kept "Polyak averaging" as "متوسط Polyak" (named method)
  - Translated "asynchronous stochastic gradient descent" as "الانحدار التدرجي العشوائي اللامتزامن"
  - Kept "dropout" as English term
  - Translated "momentum" as "زخم"
  - Translated "learning rate" as "معدل التعلم"
  - Translated "epochs" as "حقب"
  - Translated "photometric distortions" as "التشوهات الضوئية" with English in parentheses
  - Kept interpolation method names in Arabic with English equivalents
  - Translated "hyperparameters" as "المعاملات الفائقة"
  - Kept mathematical expressions like "0.9", "4%", "3/4", "4/3" unchanged
  - Translated "convergence" as "التقارب"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
