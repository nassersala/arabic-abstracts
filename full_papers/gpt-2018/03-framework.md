# Section 3: Framework
## القسم 3: الإطار العام

**Section:** Framework
**Translation Quality:** 0.89
**Glossary Terms Used:** language model, transformer, decoder, self-attention, embedding, fine-tuning, supervised, unsupervised, stochastic gradient descent, softmax, auxiliary objective

---

### English Version

Our training procedure consists of two stages. The first stage is learning a high-capacity language model on a large corpus of text. This is followed by a fine-tuning stage, where we adapt the model to a discriminative task with labeled data.

### 3.1 Unsupervised pre-training

Given an unsupervised corpus of tokens $U = \{u_1, \ldots, u_n\}$, we use a standard language modeling objective to maximize the following likelihood:

$$L_1(U) = \sum_i \log P(u_i | u_{i-k}, \ldots, u_{i-1}; \Theta)$$ (1)

where $k$ is the size of the context window, and the conditional probability $P$ is modeled using a neural network with parameters $\Theta$. These parameters are trained using stochastic gradient descent [51].

In our experiments, we use a multi-layer Transformer decoder [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens:

$$h_0 = UW_e + W_p$$
$$h_l = \text{transformer\_block}(h_{l-1}) \quad \forall i \in [1, n]$$
$$P(u) = \text{softmax}(h_n W_e^T)$$ (2)

where $U = (u_{-k}, \ldots, u_{-1})$ is the context vector of tokens, $n$ is the number of layers, $W_e$ is the token embedding matrix, and $W_p$ is the position embedding matrix.

### 3.2 Supervised fine-tuning

After training the model with the objective in Eq. 1, we adapt the parameters to the supervised target task. We assume a labeled dataset $\mathcal{C}$, where each instance consists of a sequence of input tokens, $x^1, \ldots, x^m$, along with a label $y$. The inputs are passed through our pre-trained model to obtain the final transformer block's activation $h_l^m$, which is then fed into an added linear output layer with parameters $W_y$ to predict $y$:

$$P(y | x^1, \ldots, x^m) = \text{softmax}(h_l^m W_y)$$ (3)

This gives us the following objective to maximize:

$$L_2(\mathcal{C}) = \sum_{(x,y)} \log P(y | x^1, \ldots, x^m)$$ (4)

We additionally found that including language modeling as an auxiliary objective to the fine-tuning helped learning by (a) improving generalization of the supervised model, and (b) accelerating convergence. This is in line with prior work [50,43], who also observed improved performance with such an auxiliary objective. Specifically, we optimize the following objective (with weight $\lambda$):

$$L_3(\mathcal{C}) = L_2(\mathcal{C}) + \lambda \cdot L_1(\mathcal{C})$$ (5)

Overall, the only extra parameters we require during fine-tuning are $W_y$, and embeddings for delimiter tokens (described below in Section 3.3).

### 3.3 Task-specific input transformations

For some tasks, like text classification, we can directly fine-tune our model as described above. Certain other tasks, like question answering or textual entailment, have structured inputs such as ordered sentence pairs, or triplets of document, question, and answers. Since our pre-trained model was trained on contiguous sequences of text, we require some modifications to apply it to these tasks. Previous work proposed learning task specific architectures on top of transferred representations [44]. Such an approach re-introduces a significant amount of task-specific customization and does not use transfer learning for these additional architectural components. Instead, we use a traversal-style approach [52], where we convert structured inputs into an ordered sequence that our pre-trained model can process. These input transformations allow us to avoid making extensive changes to the architecture across tasks. We provide a brief description of these input transformations below and Figure 1 provides a visual illustration. All transformations include adding randomly initialized start and end tokens ($\langle s \rangle$, $\langle e \rangle$).

**Textual entailment** For entailment tasks, we concatenate the premise $p$ and hypothesis $h$ token sequences, with a delimiter token ($\$$) in between.

**Similarity** For similarity tasks, there is no inherent ordering of the two sentences being compared. To reflect this, we modify the input sequence to contain both possible sentence orderings (with a delimiter in between) and process each independently to produce two sequence representations $h_l^m$ which are added element-wise before being fed into the linear output layer.

**Question Answering and Commonsense Reasoning** For these tasks, we are given a context document $z$, a question $q$, and a set of possible answers $\{a_k\}$. We concatenate the document context and question with each possible answer, adding a delimiter token in between to get $[z; q; \$; a_k]$. Each of these sequences are processed independently with our model and then normalized via a softmax layer to produce an output distribution over possible answers.

---

### النسخة العربية

يتكون إجراء التدريب الخاص بنا من مرحلتين. المرحلة الأولى هي تعلم نموذج لغة عالي السعة على مدونة كبيرة من النصوص. يتبع ذلك مرحلة الضبط الدقيق، حيث نُكيّف النموذج لمهمة تمييزية مع بيانات مُعنونة.

### 3.1 التدريب المسبق غير الموجه

بالنظر إلى مدونة غير موجهة من الرموز $U = \{u_1, \ldots, u_n\}$، نستخدم هدف نمذجة لغة قياسي لتعظيم الاحتمالية التالية:

$$L_1(U) = \sum_i \log P(u_i | u_{i-k}, \ldots, u_{i-1}; \Theta)$$ (1)

حيث $k$ هو حجم نافذة السياق، والاحتمال الشرطي $P$ يتم نمذجته باستخدام شبكة عصبية بمعاملات $\Theta$. يتم تدريب هذه المعاملات باستخدام الانحدار التدرجي العشوائي [51].

في تجاربنا، نستخدم فك تشفير محوّل متعدد الطبقات [34] لنموذج اللغة، وهو نوع من المحوّل [62]. يطبق هذا النموذج عملية انتباه ذاتي متعدد الرؤوس على رموز سياق الإدخال متبوعة بطبقات التغذية الأمامية الموضعية لإنتاج توزيع إخراج على الرموز المستهدفة:

$$h_0 = UW_e + W_p$$
$$h_l = \text{transformer\_block}(h_{l-1}) \quad \forall i \in [1, n]$$
$$P(u) = \text{softmax}(h_n W_e^T)$$ (2)

حيث $U = (u_{-k}, \ldots, u_{-1})$ هو متجه السياق من الرموز، و $n$ هو عدد الطبقات، و $W_e$ هي مصفوفة تضمين الرموز، و $W_p$ هي مصفوفة التضمين الموضعي.

### 3.2 الضبط الدقيق الموجه

بعد تدريب النموذج بالهدف في المعادلة 1، نُكيّف المعاملات للمهمة المستهدفة الموجهة. نفترض مجموعة بيانات مُعنونة $\mathcal{C}$، حيث تتكون كل حالة من تسلسل من رموز الإدخال، $x^1, \ldots, x^m$، مع تسمية $y$. يتم تمرير المدخلات عبر نموذجنا المُدرب مسبقاً للحصول على تنشيط كتلة المحوّل النهائية $h_l^m$، والتي يتم بعد ذلك إدخالها في طبقة إخراج خطية مضافة بمعاملات $W_y$ للتنبؤ بـ $y$:

$$P(y | x^1, \ldots, x^m) = \text{softmax}(h_l^m W_y)$$ (3)

هذا يعطينا الهدف التالي للتعظيم:

$$L_2(\mathcal{C}) = \sum_{(x,y)} \log P(y | x^1, \ldots, x^m)$$ (4)

وجدنا بالإضافة إلى ذلك أن تضمين نمذجة اللغة كهدف مساعد للضبط الدقيق ساعد التعلم من خلال (أ) تحسين تعميم النموذج الموجه، و (ب) تسريع التقارب. هذا يتماشى مع الأعمال السابقة [50،43]، الذين لاحظوا أيضاً تحسناً في الأداء مع مثل هذا الهدف المساعد. على وجه التحديد، نُحسّن الهدف التالي (بوزن $\lambda$):

$$L_3(\mathcal{C}) = L_2(\mathcal{C}) + \lambda \cdot L_1(\mathcal{C})$$ (5)

بشكل عام، المعاملات الإضافية الوحيدة التي نحتاجها أثناء الضبط الدقيق هي $W_y$، وتضمينات لرموز الفصل (الموصوفة أدناه في القسم 3.3).

### 3.3 تحويلات الإدخال الخاصة بالمهمة

بالنسبة لبعض المهام، مثل تصنيف النصوص، يمكننا ضبط نموذجنا بدقة مباشرة كما هو موصوف أعلاه. بعض المهام الأخرى، مثل الإجابة على الأسئلة أو الاستلزام النصي، لديها مدخلات منظمة مثل أزواج جمل مرتبة، أو ثلاثيات من مستند، وسؤال، وإجابات. نظراً لأن نموذجنا المُدرب مسبقاً تم تدريبه على تسلسلات متجاورة من النص، فإننا نحتاج إلى بعض التعديلات لتطبيقه على هذه المهام. اقترحت الأعمال السابقة تعلم معماريات خاصة بالمهمة فوق التمثيلات المنقولة [44]. مثل هذا النهج يُعيد تقديم كمية كبيرة من التخصيص الخاص بالمهمة ولا يستخدم التعلم بالنقل لهذه المكونات المعمارية الإضافية. بدلاً من ذلك، نستخدم نهجاً بأسلوب الاجتياز [52]، حيث نُحوّل المدخلات المنظمة إلى تسلسل مرتب يمكن لنموذجنا المُدرب مسبقاً معالجته. تسمح لنا تحويلات الإدخال هذه بتجنب إجراء تغييرات واسعة النطاق على المعمارية عبر المهام. نقدم وصفاً موجزاً لتحويلات الإدخال هذه أدناه ويوفر الشكل 1 توضيحاً مرئياً. تتضمن جميع التحويلات إضافة رموز بداية ونهاية مُهيّأة عشوائياً ($\langle s \rangle$، $\langle e \rangle$).

**الاستلزام النصي** لمهام الاستلزام، نُسلسل تسلسلات رموز المقدمة $p$ والفرضية $h$، مع رمز فاصل ($\$$) بينهما.

**التشابه** لمهام التشابه، لا يوجد ترتيب متأصل للجملتين اللتين يتم مقارنتهما. لنعكس هذا، نُعدّل تسلسل الإدخال ليحتوي على كلا ترتيبي الجمل المحتملين (مع فاصل بينهما) ونعالج كل منهما بشكل مستقل لإنتاج تمثيلين للتسلسل $h_l^m$ يتم جمعهما عنصرياً قبل إدخالهما في طبقة الإخراج الخطية.

**الإجابة على الأسئلة والاستدلال المنطقي** لهذه المهام، نُعطى مستند سياق $z$، وسؤال $q$، ومجموعة من الإجابات المحتملة $\{a_k\}$. نُسلسل سياق المستند والسؤال مع كل إجابة محتملة، مع إضافة رمز فاصل بينهما للحصول على $[z; q; \$; a_k]$. تتم معالجة كل من هذه التسلسلات بشكل مستقل مع نموذجنا ثم يتم تطبيعها عبر طبقة softmax لإنتاج توزيع إخراج على الإجابات المحتملة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Transformer architecture and input transformations)
- **Key terms introduced:**
  - High-capacity = عالي السعة
  - Context window = نافذة السياق
  - Conditional probability = الاحتمال الشرطي
  - Stochastic gradient descent = الانحدار التدرجي العشوائي
  - Multi-headed self-attention = انتباه ذاتي متعدد الرؤوس
  - Position-wise feedforward = التغذية الأمامية الموضعية
  - Token embedding = تضمين الرموز
  - Position embedding = التضمين الموضعي
  - Activation = تنشيط
  - Delimiter token = رمز فاصل
  - Traversal-style approach = نهج بأسلوب الاجتياز

- **Equations:** All 5 equations preserved in LaTeX format with Arabic explanations
- **Mathematical notation:** Preserved exactly (L1, L2, L3, Θ, Wp, We, etc.)
- **Citations:** Preserved [51], [34], [62], [50,43], [44], [52]

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.89
