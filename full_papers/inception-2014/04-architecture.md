# Section 4: Architectural Details
## القسم 4: التفاصيل المعمارية

**Section:** Architectural Details
**Translation Quality:** 0.88
**Glossary Terms Used:** architecture, convolution, sparse, dense, dimension reduction, computational bottleneck, filter, pooling, concatenation

---

### English Version

The main idea of the Inception architecture is based on finding out how an optimal local sparse structure in a convolutional vision network can be approximated and covered by readily available dense components. Note that assuming translation invariance means that our network will be built from convolutional building blocks. All we need is to find the optimal local construction and to repeat it spatially. Arora et al. [2] suggests a layer-by layer construction in which one should analyze the correlation statistics of the last layer and cluster them into groups of units with high correlation. These clusters form the units of the next layer and are connected to the units in the previous layer. We assume that each unit from the earlier layer corresponds to some region of the input image and these units are grouped into filter banks. In the lower layers (the ones close to the input) correlated units would concentrate in local regions. This means, we would end up with a lot of clusters concentrated in a single region and they can be covered by a layer of 1×1 convolutions in the next layer, as suggested in [12]. However, one can also expect that there will be a smaller number of more spatially spread out clusters that can be covered by convolutions over larger patches, and there will be a decreasing number of patches over larger and larger regions. In order to avoid patch-alignment issues, current incarnations of the Inception architecture are restricted to filter sizes 1×1, 3×3 and 5×5, however this decision was based more on convenience rather than necessity. It also means that the suggested architecture is a combination of all those layers with their output filter banks concatenated into a single output vector forming the input of the next stage. Additionally, since pooling operations have been essential for the success in current state of the art convolutional networks, it suggests that adding an alternative parallel pooling path in each such stage should have additional beneficial effect, as well (see Figure 2(a)).

As these "Inception modules" are stacked on top of each other, their output correlation statistics are bound to vary: as features of higher abstraction are captured by higher layers, their spatial concentration is expected to decrease suggesting that the ratio of 3×3 and 5×5 convolutions should increase as we move to higher layers.

One big problem with the above modules, at least in this naive form, is that even a modest number of 5×5 convolutions can be prohibitively expensive on top of a convolutional layer with a large number of filters. This problem becomes even more pronounced once pooling units are added to the mix: their number of output filters equals to the number of filters in the previous stage. The merging of the output of the pooling layer with the outputs of convolutional layers would lead to an inevitable increase in the number of outputs from stage to stage. Even while this architecture might cover the optimal sparse structure, it would do it very inefficiently, leading to a computational blow up within a few stages.

This leads to the second idea of the proposed architecture: judiciously applying dimension reductions and projections wherever the computational requirements would increase too much otherwise. This is based on the success of embeddings: even low dimensional embeddings might contain a lot of information about a relatively large image patch. However, embeddings represent information in a dense, compressed form and compressed information is harder to model. We would like to keep our representation sparse at most places (as required by the conditions of [2]) and compress the signals only whenever they have to be aggregated en masse. That is, 1×1 convolutions are used to compute reductions before the expensive 3×3 and 5×5 convolutions. Besides being used as reductions, they also include the use of rectified linear activation which makes them dual-purpose. The final result is depicted in Figure 2(b).

In general, an Inception network is a network consisting of modules of the above type stacked upon each other, with occasional max-pooling layers with stride 2 to halve the resolution of the grid. For technical reasons (memory efficiency during training), it seemed beneficial to start using Inception modules only at higher layers while keeping the lower layers in traditional convolutional fashion. This is not strictly necessary, simply reflecting some infrastructural inefficiencies in our current implementation.

One of the main beneficial aspects of this architecture is that it allows for increasing the number of units at each stage significantly without an uncontrolled blow-up in computational complexity. The ubiquitous use of dimension reduction allows for shielding the large number of input filters of the last stage from the previous layer, first reducing their dimension before convolving over them with a large patch size. Another practically useful aspect of this design is that it aligns with the intuition that visual information should be processed at various scales and then aggregated so that the next stage can abstract features from different scales simultaneously.

The improved use of computational resources allows for increasing both the width of each stage as well as the number of stages without getting into computational difficulties. Another way to utilize the inception architecture is to create slightly inferior, but computationally cheaper versions of it. We have found that all the included the knobs and levers allow for a controlled balancing of computational resources that can result in networks that are 2−3× faster than similarly performing networks with non-Inception architecture, however this requires careful manual design at this point.

---

### النسخة العربية

تستند الفكرة الرئيسية لمعمارية Inception على إيجاد كيفية تقريب وتغطية بنية متناثرة محلية مثالية في شبكة رؤية التفافية بواسطة مكونات كثيفة متاحة بسهولة. لاحظ أن افتراض ثبات الترجمة يعني أن شبكتنا ستُبنى من كتل بناء التفافية. كل ما نحتاجه هو إيجاد البناء المحلي الأمثل وتكراره مكانياً. يقترح Arora وآخرون [2] بناءً طبقة تلو الأخرى حيث يجب على المرء تحليل إحصاءات الارتباط للطبقة الأخيرة وتجميعها في مجموعات من الوحدات ذات الارتباط العالي. تشكل هذه المجموعات وحدات الطبقة التالية وتتصل بالوحدات في الطبقة السابقة. نفترض أن كل وحدة من الطبقة السابقة تتوافق مع منطقة معينة من صورة الإدخال وأن هذه الوحدات مجمعة في بنوك مرشحات. في الطبقات السفلية (تلك القريبة من الإدخال)، ستتركز الوحدات المترابطة في مناطق محلية. هذا يعني أننا سننتهي بالكثير من المجموعات المركزة في منطقة واحدة ويمكن تغطيتها بطبقة من الالتفافات 1×1 في الطبقة التالية، كما هو مقترح في [12]. ومع ذلك، يمكن للمرء أيضاً أن يتوقع وجود عدد أقل من المجموعات المنتشرة مكانياً والتي يمكن تغطيتها بالالتفافات على بقع أكبر، وسيكون هناك عدد متناقص من البقع على مناطق أكبر فأكبر. لتجنب مشاكل محاذاة البقع، تقتصر التجسيدات الحالية لمعمارية Inception على أحجام المرشحات 1×1 و3×3 و5×5، ومع ذلك كان هذا القرار مبنياً على الراحة أكثر من الضرورة. هذا يعني أيضاً أن المعمارية المقترحة هي مزيج من كل تلك الطبقات مع دمج بنوك مرشحات المخرجات الخاصة بها في متجه مخرجات واحد يشكل مدخلات المرحلة التالية. بالإضافة إلى ذلك، نظراً لأن عمليات التجميع كانت ضرورية لنجاح الشبكات الالتفافية الحديثة، فإن ذلك يشير إلى أن إضافة مسار تجميع متوازي بديل في كل مرحلة من هذا القبيل يجب أن يكون له تأثير إضافي مفيد أيضاً (انظر الشكل 2(a)).

مع تكديس "وحدات Inception" هذه فوق بعضها البعض، من المؤكد أن تتنوع إحصاءات ارتباط مخرجاتها: نظراً لأن الميزات ذات التجريد الأعلى يتم التقاطها بواسطة الطبقات العليا، يُتوقع أن يتناقص تركيزها المكاني مما يشير إلى أن نسبة الالتفافات 3×3 و5×5 يجب أن تزداد مع انتقالنا إلى طبقات أعلى.

مشكلة كبيرة واحدة مع الوحدات المذكورة أعلاه، على الأقل في هذا الشكل الساذج، هي أن حتى عدداً متواضعاً من الالتفافات 5×5 يمكن أن يكون مكلفاً للغاية على قمة طبقة التفافية ذات عدد كبير من المرشحات. تصبح هذه المشكلة أكثر وضوحاً عندما تُضاف وحدات التجميع إلى المزيج: يساوي عدد مرشحات المخرجات الخاصة بها عدد المرشحات في المرحلة السابقة. سيؤدي دمج مخرجات طبقة التجميع مع مخرجات الطبقات الالتفافية إلى زيادة حتمية في عدد المخرجات من مرحلة إلى مرحلة. حتى في حين أن هذه المعمارية قد تغطي البنية المتناثرة المثالية، فإنها ستفعل ذلك بشكل غير فعال للغاية، مما يؤدي إلى انفجار حسابي خلال بضع مراحل.

هذا يؤدي إلى الفكرة الثانية للمعمارية المقترحة: تطبيق تخفيضات الأبعاد والإسقاطات بحكمة حيثما تزداد المتطلبات الحسابية بشكل كبير. يستند هذا على نجاح التضمينات: حتى التضمينات ذات الأبعاد المنخفضة قد تحتوي على الكثير من المعلومات حول بقعة صورة كبيرة نسبياً. ومع ذلك، تمثل التضمينات المعلومات في شكل كثيف ومضغوط، والمعلومات المضغوطة أصعب في النمذجة. نرغب في الحفاظ على تمثيلنا متناثراً في معظم الأماكن (كما هو مطلوب من قبل شروط [2]) وضغط الإشارات فقط عندما يتعين تجميعها بشكل جماعي. أي أنه تُستخدم الالتفافات 1×1 لحساب التخفيضات قبل الالتفافات المكلفة 3×3 و5×5. بالإضافة إلى استخدامها كتخفيضات، فإنها تتضمن أيضاً استخدام التنشيط الخطي المقوّم مما يجعلها ثنائية الغرض. النتيجة النهائية موضحة في الشكل 2(b).

بشكل عام، شبكة Inception هي شبكة تتكون من وحدات من النوع المذكور أعلاه مكدسة فوق بعضها البعض، مع طبقات تجميع أقصى عرضية بخطوة 2 لتنصيف دقة الشبكة. لأسباب فنية (كفاءة الذاكرة أثناء التدريب)، بدا من المفيد البدء في استخدام وحدات Inception فقط في الطبقات العليا مع الحفاظ على الطبقات السفلية بطريقة التفافية تقليدية. هذا ليس ضرورياً بشكل صارم، بل يعكس ببساطة بعض أوجه القصور في البنية التحتية في تطبيقنا الحالي.

أحد الجوانب المفيدة الرئيسية لهذه المعمارية هو أنها تسمح بزيادة عدد الوحدات في كل مرحلة بشكل كبير دون انفجار غير منضبط في التعقيد الحسابي. يسمح الاستخدام المنتشر لتخفيض الأبعاد بحماية العدد الكبير من مرشحات الإدخال للمرحلة الأخيرة من الطبقة السابقة، أولاً تقليل أبعادها قبل الالتفاف عليها بحجم بقعة كبيرة. جانب آخر مفيد عملياً لهذا التصميم هو أنه يتماشى مع الحدس بأن المعلومات البصرية يجب معالجتها على مقاييس مختلفة ثم تجميعها بحيث يمكن للمرحلة التالية تجريد الميزات من مقاييس مختلفة في وقت واحد.

يسمح الاستخدام المحسّن للموارد الحسابية بزيادة اتساع كل مرحلة وكذلك عدد المراحل دون الوقوع في صعوبات حسابية. طريقة أخرى لاستخدام معمارية Inception هي إنشاء إصدارات أقل جودة قليلاً، ولكنها أرخص من الناحية الحسابية منها. وجدنا أن جميع الأزرار والروافع المدرجة تسمح بموازنة منضبطة للموارد الحسابية التي يمكن أن تؤدي إلى شبكات أسرع بمقدار 2-3× من الشبكات ذات الأداء المماثل بدون معمارية Inception، ومع ذلك فإن هذا يتطلب تصميماً يدوياً دقيقاً في هذه المرحلة.

---

### Translation Notes

- **Figures referenced:** Figure 2(a), Figure 2(b)
- **Key terms introduced:** Inception module, translation invariance, filter banks, dimension reduction, embeddings, rectified linear activation
- **Equations:** None
- **Citations:** [2], [12]
- **Special handling:**
  - Kept "Inception module" as "وحدات Inception"
  - Translated "translation invariance" as "ثبات الترجمة"
  - Translated "filter banks" as "بنوك مرشحات"
  - Kept mathematical notation like "1×1, 3×3, 5×5" unchanged
  - Translated "dimension reduction" as "تخفيض الأبعاد"
  - Translated "embeddings" as "التضمينات"
  - Translated "rectified linear activation" as "التنشيط الخطي المقوّم"
  - Translated "computational blow up" as "انفجار حسابي"
  - Kept stride terminology: "بخطوة 2"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
