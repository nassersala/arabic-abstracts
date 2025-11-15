# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.86
**Glossary Terms Used:** machine learning, embedding, graph neural network, automated theorem prover, discriminatively-trained models, generative models

---

### English Version

**Machine Learning for Inductive Program Synthesis.** There is relatively little work on using machine learning for programming by example. The most closely related work is that of Menon et al. (2013), in which a hand-coded set of features of input-output examples are used as "clues." When a clue appears in the input-output examples (e.g., the output is a permutation of the input), it reweights the probabilities of productions in a probabilistic context free grammar by a learned amount. This work shares the idea of learning to guide the search over program space conditional on input-output examples. One difference is in the domains. Menon et al. (2013) operate on short string manipulation programs, where it is arguably easier to hand-code features to recognize patterns in the input-output examples (e.g., if the outputs are always permutations or substrings of the input). Our work shows that there are strong cues in patterns in input-output examples in the domain of numbers and lists. However, the main difference is the scale. Menon et al. (2013) learns from a small (280 examples), manually-constructed dataset, which limits the capacity of the machine learning model that can be trained. Thus, it forces the machine learning component to be relatively simple. Indeed, Menon et al. (2013) use a log-linear model and rely on hand-constructed features. LIPS automatically generates training data, which yields datasets with millions of programs and enables high-capacity deep learning models to be brought to bear on the problem.

**Learning Representations of Program State.** Piech et al. (2015) propose to learn joint embeddings of program states and programs to automatically extend teacher feedback to many similar programs in the MOOC setting. This work is similar in that it considers embedding program states, but the domain is different, and it otherwise specifically focuses on syntactic differences between semantically equivalent programs to provide stylistic feedback. Li et al. (2016) use graph neural networks (GNNs) to predict logical descriptions from program states, focusing on data structure shapes instead of numerical and list data. Such GNNs may be a suitable architecture to encode states appearing when extending our DSL to handle more complex data structures.

**Learning to Infer.** Very recently, Alemi et al. (2016) used neural sequence models in tandem with an automated theorem prover. Similar to our Sort and Add strategy, a neural network component is trained to select premises that the theorem prover can use to prove a theorem. A recent extension (Loos et al., 2017) is similar to our DFS enumeration strategy and uses a neural network to guide the proof search at intermediate steps. The main differences are in the domains, and that they train on an existing corpus of theorems. More broadly, if we view a DSL as defining a model and search as a form of inference algorithm, then there is a large body of work on using discriminatively-trained models to aid inference in generative models. Examples include Dayan et al. (1995); Kingma & Welling (2014); Shotton et al. (2013); Stuhlmüller et al. (2013); Heess et al. (2013); Jampani et al. (2015).

---

### النسخة العربية

**تعلم الآلة للتوليد الاستقرائي للبرامج.** هناك عمل قليل نسبياً حول استخدام تعلم الآلة للبرمجة بالأمثلة. العمل الأكثر صلة هو عمل Menon وآخرون (2013)، الذي يتم فيه استخدام مجموعة من الميزات المشفرة يدوياً لأمثلة الإدخال والإخراج كـ "إشارات". عندما تظهر إشارة في أمثلة الإدخال والإخراج (على سبيل المثال، المخرج هو تبديل للمدخل)، فإنها تعيد ترجيح احتماليات الإنتاج في قواعد نحوية خالية من السياق احتمالية بمقدار متعلم. يشترك هذا العمل في فكرة تعلم كيفية توجيه البحث عبر فضاء البرامج مشروطاً بأمثلة الإدخال والإخراج. أحد الاختلافات في المجالات. يعمل Menon وآخرون (2013) على برامج معالجة سلاسل نصية قصيرة، حيث يمكن القول إنه من الأسهل ترميز الميزات يدوياً للتعرف على الأنماط في أمثلة الإدخال والإخراج (على سبيل المثال، إذا كانت المخرجات دائماً تبديلات أو سلاسل فرعية من المدخل). يُظهر عملنا أن هناك إشارات قوية في الأنماط في أمثلة الإدخال والإخراج في مجال الأرقام والقوائم. ومع ذلك، فإن الاختلاف الرئيسي هو النطاق. يتعلم Menon وآخرون (2013) من مجموعة بيانات صغيرة (280 مثالاً) مبنية يدوياً، مما يحد من قدرة نموذج تعلم الآلة الذي يمكن تدريبه. وبالتالي، فإنه يجبر مكون تعلم الآلة على أن يكون بسيطاً نسبياً. في الواقع، يستخدم Menon وآخرون (2013) نموذجاً لوغاريتمياً خطياً ويعتمدون على ميزات مبنية يدوياً. يولد LIPS بيانات التدريب تلقائياً، مما ينتج مجموعات بيانات مع ملايين البرامج ويمكّن نماذج التعلم العميق عالية السعة من معالجة المشكلة.

**تعلم تمثيلات حالة البرنامج.** يقترح Piech وآخرون (2015) تعلم تضمينات مشتركة لحالات البرامج والبرامج لتوسيع ملاحظات المعلم تلقائياً إلى العديد من البرامج المماثلة في بيئة MOOC. هذا العمل مشابه من حيث أنه يعتبر تضمين حالات البرامج، لكن المجال مختلف، وهو يركز بشكل خاص على الاختلافات النحوية بين البرامج المكافئة دلالياً لتقديم ملاحظات أسلوبية. يستخدم Li وآخرون (2016) الشبكات العصبية البيانية (GNNs) للتنبؤ بالأوصاف المنطقية من حالات البرامج، مع التركيز على أشكال بنية البيانات بدلاً من البيانات الرقمية وبيانات القوائم. قد تكون هذه الشبكات العصبية البيانية معمارية مناسبة لترميز الحالات الظاهرة عند توسيع لغتنا الخاصة بالمجال للتعامل مع بنى بيانات أكثر تعقيداً.

**تعلم الاستنتاج.** في الآونة الأخيرة جداً، استخدم Alemi وآخرون (2016) نماذج التسلسل العصبية جنباً إلى جنب مع مثبت نظريات آلي. على غرار استراتيجية الفرز والإضافة الخاصة بنا، يتم تدريب مكون شبكة عصبية لاختيار المقدمات التي يمكن لمثبت النظريات استخدامها لإثبات نظرية. امتداد حديث (Loos وآخرون، 2017) مماثل لاستراتيجية تعداد DFS الخاصة بنا ويستخدم شبكة عصبية لتوجيه بحث الإثبات في خطوات وسيطة. الاختلافات الرئيسية في المجالات، وأنهم يدربون على مدونة موجودة من النظريات. بشكل أوسع، إذا نظرنا إلى اللغة الخاصة بالمجال على أنها تحدد نموذجاً والبحث كشكل من أشكال خوارزمية الاستنتاج، فهناك مجموعة كبيرة من الأعمال حول استخدام النماذج المدربة بشكل تمييزي للمساعدة في الاستنتاج في النماذج التوليدية. تشمل الأمثلة Dayan وآخرون (1995)؛ Kingma و Welling (2014)؛ Shotton وآخرون (2013)؛ Stuhlmüller وآخرون (2013)؛ Heess وآخرون (2013)؛ Jampani وآخرون (2015).

---

### Translation Notes

- **Key terms introduced:**
  - programming by example = البرمجة بالأمثلة
  - hand-coded features = ميزات مشفرة يدوياً
  - clue = إشارة
  - probabilistic context free grammar = قواعد نحوية خالية من السياق احتمالية
  - log-linear model = نموذج لوغاريتمي خطي
  - joint embeddings = تضمينات مشتركة
  - MOOC (Massive Open Online Course) = MOOC (kept as abbreviation)
  - syntactic differences = اختلافات نحوية
  - semantically equivalent = مكافئة دلالياً
  - graph neural networks (GNNs) = الشبكات العصبية البيانية
  - automated theorem prover = مثبت نظريات آلي
  - premises = مقدمات
  - discriminatively-trained models = نماذج مدربة بشكل تمييزي
  - generative models = نماذج توليدية

- **Citations:** Multiple references (Menon et al. 2013, Piech et al. 2015, Li et al. 2016, Alemi et al. 2016, Loos et al. 2017, Dayan et al. 1995, etc.)
- **Special handling:** Preserved all citation formats and author names

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
