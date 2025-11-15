# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** neural networks, deep learning, backpropagation, supervised learning, semantic meaning, adversarial examples, perturbation, generalization, disentangle, representation

---

### English Version

Deep neural networks are powerful learning models that achieve
excellent performance on visual and speech recognition problems
\cite{krizhevsky2012imagenet, deepSpeechReviewSPM2012}.
Neural networks achieve high performance because they can express
arbitrary computation that consists of a modest number of massively parallel
nonlinear steps. But as the resulting computation is automatically discovered by backpropagation via supervised
learning, it can be difficult to interpret and can have counter-intuitive properties.
In this paper, we discuss two counter-intuitive properties of deep neural networks.

The first property is concerned with the semantic meaning of individual units. Previous
works \cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring} analyzed
the semantic meaning of various units by finding the set of inputs
that maximally activate a given unit.  The inspection of individual units makes the implicit
assumption that the units of the last feature layer form a distinguished basis which is
particularly useful for extracting semantic information.
Instead, we show in section \ref{sec:image} that random projections of $\phi(x)$ are semantically
indistinguishable from the coordinates of $\phi(x)$. This puts into question
the conjecture that neural networks disentangle variation factors across coordinates.
Generally, it seems that it is the entire space of activations,
rather than the individual units, that contains the bulk of the semantic information.
A similar, but even stronger conclusion was reached recently by Mikolov et al.
\cite{mikolov2013efficient} for word representations, where the various directions
in the vector space representing the words are shown to give rise to a
surprisingly rich semantic encoding of relations and analogies.
At the same time, the vector representations are stable up to a rotation of the
space, so the individual units of the vector representations are unlikely to
contain semantic information.

The second property is concerned with the stability of neural networks with respect to small
perturbations to their inputs. Consider a state-of-the-art
deep neural network that generalizes well on an object recognition task.
We expect such  network to be robust to small perturbations of its input,
because small perturbation cannot change the object category of an image.
However, we find that applying an \emph{imperceptible}
non-random perturbation to a test image, it is possible to arbitrarily change
the network's prediction  (see figure \ref{fig:alexnegative}).
These perturbations are found by optimizing the input to maximize
the prediction error.  We term the so perturbed examples ``adversarial examples''.

It is natural to expect that the precise configuration of the minimal
necessary perturbations is a random artifact of the normal variability that
arises in different runs of backpropagation learning. Yet, we found that
adversarial examples are relatively robust, and are shared by neural networks
with varied number of layers, activations or trained on different subsets
of the training data.
That is, if we use one neural net to generate a set of adversarial examples, we find
that these examples are still statistically hard for another neural network
even when it was trained with different hyperparameters or, most surprisingly,
when it was trained on a different set of examples.

These results suggest that the deep neural networks that are learned by
backpropagation have nonintuitive characteristics and intrinsic blind spots, whose structure
is connected to the data distribution in a non-obvious way.

---

### النسخة العربية

الشبكات العصبية العميقة هي نماذج تعلم قوية تحقق أداءً ممتازاً في مشاكل التعرف على الصور والكلام \cite{krizhevsky2012imagenet, deepSpeechReviewSPM2012}. تحقق الشبكات العصبية أداءً عالياً لأنها يمكنها التعبير عن حسابات عشوائية تتكون من عدد متواضع من الخطوات غير الخطية الموازية بشكل هائل. ولكن نظراً لأن الحساب الناتج يتم اكتشافه تلقائياً بواسطة الانتشار العكسي عبر التعلم الخاضع للإشراف، فقد يكون من الصعب تفسيره ويمكن أن يكون له خصائص متناقضة. في هذا البحث، نناقش خاصيتين متناقضتين للشبكات العصبية العميقة.

الخاصية الأولى تتعلق بالمعنى الدلالي للوحدات الفردية. قامت الأعمال السابقة \cite{girshick2013rich, zeiler2013visualizing, goodfellow2009measuring} بتحليل المعنى الدلالي لمختلف الوحدات من خلال إيجاد مجموعة المدخلات التي تُنشِّط وحدة معينة بشكل أقصى. يفترض فحص الوحدات الفردية ضمنياً أن وحدات طبقة الميزات الأخيرة تشكل أساساً متميزاً مفيداً بشكل خاص لاستخراج المعلومات الدلالية. بدلاً من ذلك، نُظهر في القسم \ref{sec:image} أن الإسقاطات العشوائية لـ $\phi(x)$ لا يمكن تمييزها دلالياً عن إحداثيات $\phi(x)$. هذا يضع موضع تساؤل الافتراض بأن الشبكات العصبية تفصل عوامل التباين عبر الإحداثيات. بشكل عام، يبدو أن الفضاء الكامل للتنشيطات، وليس الوحدات الفردية، هو الذي يحتوي على الجزء الأكبر من المعلومات الدلالية. تم التوصل إلى نتيجة مماثلة، ولكن أقوى، مؤخراً بواسطة Mikolov وآخرون \cite{mikolov2013efficient} لتمثيلات الكلمات، حيث تبين أن الاتجاهات المختلفة في الفضاء المتجه الذي يمثل الكلمات تؤدي إلى ترميز دلالي غني بشكل مفاجئ للعلاقات والتشابهات. في الوقت نفسه، فإن التمثيلات المتجهة مستقرة حتى الدوران في الفضاء، لذلك فإن الوحدات الفردية لتمثيلات المتجهات من غير المحتمل أن تحتوي على معلومات دلالية.

الخاصية الثانية تتعلق باستقرار الشبكات العصبية فيما يتعلق بالاضطرابات الصغيرة في مدخلاتها. لنفكر في شبكة عصبية عميقة متطورة تُعمِّم بشكل جيد على مهمة التعرف على الأشياء. نتوقع أن تكون مثل هذه الشبكة قوية ضد الاضطرابات الصغيرة في مدخلاتها، لأن الاضطراب الصغير لا يمكن أن يغير فئة الكائن في الصورة. ومع ذلك، نجد أنه من خلال تطبيق اضطراب غير عشوائي \emph{غير محسوس} على صورة اختبار، من الممكن تغيير تنبؤ الشبكة بشكل عشوائي (انظر الشكل \ref{fig:alexnegative}). يتم إيجاد هذه الاضطرابات من خلال تحسين المدخلات لتعظيم خطأ التنبؤ. نُطلق على الأمثلة المضطربة بهذه الطريقة اسم "الأمثلة الخصامية".

من الطبيعي أن نتوقع أن التكوين الدقيق للاضطرابات الدنيا الضرورية هو نتيجة عشوائية للتباين الطبيعي الذي ينشأ في تشغيلات مختلفة لتعلم الانتشار العكسي. ومع ذلك، وجدنا أن الأمثلة الخصامية قوية نسبياً، ويتم مشاركتها بواسطة الشبكات العصبية ذات أعداد مختلفة من الطبقات والتنشيطات أو المدربة على مجموعات فرعية مختلفة من بيانات التدريب. أي، إذا استخدمنا شبكة عصبية واحدة لتوليد مجموعة من الأمثلة الخصامية، نجد أن هذه الأمثلة لا تزال صعبة إحصائياً على شبكة عصبية أخرى حتى عندما تم تدريبها بمعاملات فرط مختلفة أو، والأكثر إثارة للدهشة، عندما تم تدريبها على مجموعة مختلفة من الأمثلة.

تشير هذه النتائج إلى أن الشبكات العصبية العميقة التي يتم تعلمها بواسطة الانتشار العكسي لها خصائص غير بديهية ونقاط عمياء جوهرية، تكون بنيتها متصلة بتوزيع البيانات بطريقة غير واضحة.

---

### Translation Notes

- **Figures referenced:** Figure \ref{fig:alexnegative} (adversarial examples for AlexNet)
- **Key terms introduced:**
  - adversarial examples (أمثلة خصامية)
  - imperceptible perturbation (اضطراب غير محسوس)
  - blind spots (نقاط عمياء)
  - semantic meaning (معنى دلالي)
  - disentangle (تفصل)
  - activation space (فضاء التنشيطات)
  - hyperparameters (معاملات فرط)
- **Equations:** 0
- **Citations:** 8 references to prior work
- **Special handling:**
  - Used $\phi(x)$ notation throughout as it appears in original
  - Maintained section reference \ref{sec:image}
  - Preserved emphasis on "imperceptible" using \emph{}

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
