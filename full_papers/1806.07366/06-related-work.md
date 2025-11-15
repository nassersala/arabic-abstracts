# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related work
**Translation Quality:** 0.86
**Glossary Terms Used:** neural network, deep learning, continuous, differential equation, optimization, architecture

---

### English Version

**Relationship to residual networks:** Lu et al. (2017) previously noted the connection between ResNets and Euler discretization of ODEs, and trained a variant where the number of layers in each "block" is chosen as a hyperparameter. Our work makes this connection explicit by directly parameterizing the continuous dynamics.

**Hypernetworks and meta-learning:** Ha et al. (2016) introduced hypernetworks, which use one network to generate the weights of another. Our approach can be seen as using an ODE solver as a hypernetwork, continuously generating new "layers" on the fly.

**Adaptive computation time:** Graves (2016) proposed allowing RNNs to choose how many computational steps to take based on the input. Our framework provides a natural way to adaptively choose the computational budget based on problem difficulty, with formal guarantees about numerical error.

**Reversible architectures:** Gomez et al. (2017) and Chang et al. (2018) proposed reversible architectures where the forward pass can be reconstructed from the output, allowing constant memory training. Our approach similarly allows constant memory training, but uses the adjoint method rather than reversibility.

**Momentum networks:** Lu et al. (2018) introduced a second-order ODE perspective on neural networks. Our work focuses on first-order ODEs, which are more straightforward to solve numerically.

**Normalizing flows:** Rezende & Mohamed (2015) and Dinh et al. (2016) introduced normalizing flows as a way to build expressive generative models. We extend this work by introducing continuous normalizing flows.

**Time-series modeling:** Traditional approaches to irregular time-series include Gaussian processes (Rasmussen & Williams, 2006) and methods based on interpolation. Neural approaches include GRU-D (Che et al., 2018) which imputes missing values. Our approach avoids explicit imputation by using continuous-time dynamics.

---

### النسخة العربية

**العلاقة بالشبكات المتبقية:** لاحظ Lu et al. (2017) سابقاً الصلة بين ResNets وتقطيع أويلر للمعادلات التفاضلية العادية، ودربوا متغيراً حيث يتم اختيار عدد الطبقات في كل "كتلة" كمعامل فائق. يجعل عملنا هذه الصلة صريحة من خلال تحديد معاملات الديناميكيات المستمرة بشكل مباشر.

**الشبكات الفائقة والتعلم الفوقي:** قدم Ha et al. (2016) الشبكات الفائقة، والتي تستخدم شبكة واحدة لتوليد أوزان شبكة أخرى. يمكن النظر إلى نهجنا على أنه يستخدم حلال المعادلات التفاضلية العادية كشبكة فائقة، يولد "طبقات" جديدة بشكل مستمر أثناء التنفيذ.

**وقت الحوسبة التكيفي:** اقترح Graves (2016) السماح للشبكات العصبية التكرارية باختيار عدد الخطوات الحسابية التي يجب اتخاذها بناءً على المدخل. يوفر إطار عملنا طريقة طبيعية لاختيار الميزانية الحسابية بشكل تكيفي بناءً على صعوبة المشكلة، مع ضمانات رسمية حول الخطأ العددي.

**المعماريات القابلة للعكس:** اقترح Gomez et al. (2017) و Chang et al. (2018) معماريات قابلة للعكس حيث يمكن إعادة بناء المرور الأمامي من المخرج، مما يسمح بتدريب ذاكرة ثابتة. يسمح نهجنا بالمثل بتدريب ذاكرة ثابتة، لكنه يستخدم طريقة المرافق بدلاً من القابلية للعكس.

**شبكات الزخم:** قدم Lu et al. (2018) منظوراً للمعادلات التفاضلية العادية من الدرجة الثانية على الشبكات العصبية. يركز عملنا على المعادلات التفاضلية العادية من الدرجة الأولى، والتي يسهل حلها عددياً.

**تدفقات التطبيع:** قدم Rezende & Mohamed (2015) و Dinh et al. (2016) تدفقات التطبيع كطريقة لبناء نماذج توليدية تعبيرية. نوسع هذا العمل من خلال تقديم تدفقات التطبيع المستمرة.

**نمذجة السلاسل الزمنية:** تشمل الأساليب التقليدية للسلاسل الزمنية غير المنتظمة عمليات غاوس (Rasmussen & Williams, 2006) والطرق القائمة على الاستيفاء. تشمل الأساليب العصبية GRU-D (Che et al., 2018) والذي يحتسب القيم المفقودة. يتجنب نهجنا الاحتساب الصريح باستخدام ديناميكيات الزمن المستمر.

---

### Translation Notes

- **Key terms introduced:** hypernetworks, adaptive computation, reversible architectures, Gaussian processes, interpolation
- **Equations:** None
- **Citations:** Lu et al. (2017, 2018), Ha et al. (2016), Graves (2016), Gomez et al. (2017), Chang et al. (2018), Rezende & Mohamed (2015), Dinh et al. (2016), Rasmussen & Williams (2006), Che et al. (2018)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
