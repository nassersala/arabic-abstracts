# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.90
**Glossary Terms Used:** generative image modeling, unsupervised learning, image compression, autoregressive, recurrent neural networks, deep learning

---

### English Version

Generative image modeling is a central problem in unsupervised learning. Probabilistic density models can be applied in a wide variety of tasks, from image compression and forms of reconstruction such as image inpainting and deblurring, to generation of new images. When the models are conditioned on external information, a large variety of other tasks can be addressed, such as generating images from text descriptions or simulating the future frames in a planning task.

Building complex and expressive models that are also tractable and scalable has proved to be difficult. The previous approaches can be divided into two categories. Non-parametric models are very flexible as they directly use the training data at test time, but may not scale well to larger datasets and may not capture the full structure in the data. On the other hand, parametric approaches such as Variational Autoencoders (VAEs) can learn good latent representations, but often rely on intractable inference steps or heuristics.

To tractably model the joint distribution of the pixels in the image, we use a well-known decomposition of the joint distribution as a product of conditional distributions. The joint distribution p(x) is written as the following product:

p(x) = ∏ᵢ₌₁ⁿ² p(xᵢ|x₁,...,xᵢ₋₁)

where x is an image represented as an n×n×3 tensor of pixel values, and xᵢ is a single pixel. The factorization turns the modeling problem into a sequence problem, where one learns to predict the next pixel given all the previously generated pixels. But to model the conditional distributions we need a highly expressive sequence model that can capture the complex dependencies in the images.

Recurrent Neural Networks (RNNs) are powerful models that offer a compact and shared parametrization of the conditional distributions. RNNs have been very successful in modelling other kinds of data sequences such as handwriting generation, character prediction and machine translation. Moreover, two-dimensional RNNs have previously been used for generating images (Graves, 2013) and, more recently, conditional generation of images for grayscale or binary images (Gregor et al., 2015). In our current work we advance two-dimensional RNNs by using a novel architecture based on twelve-layer deep networks. We use two types of LSTM layers: Row LSTMs and Diagonal BiLSTMs. The networks incorporate residual connections (He et al., 2015) around LSTM layers; to our knowledge this is the first time that residual connections have been used in recurrent networks.

We also significantly improve the PixelCNN architecture from (van den Oord et al., 2016a) by introducing masked convolutions and using it to generate multi-scale models. We achieve state-of-the-art log-likelihood results on natural images and provide benchmarks on the ImageNet dataset. The generated samples from the PixelRNN capture both local and long-range correlations in the images and appear crisp, varied and globally coherent.

---

### النسخة العربية

يُعد النمذجة التوليدية للصور مسألة محورية في التعلم غير الموجه. يمكن تطبيق نماذج الكثافة الاحتمالية في مجموعة واسعة من المهام، من ضغط الصور وأشكال إعادة البناء مثل ملء الصور وإزالة التشويش، إلى توليد صور جديدة. عندما تكون النماذج مشروطة بمعلومات خارجية، يمكن معالجة مجموعة كبيرة من المهام الأخرى، مثل توليد الصور من الأوصاف النصية أو محاكاة الإطارات المستقبلية في مهمة التخطيط.

أثبت بناء نماذج معقدة ومعبرة وقابلة للمعالجة والتوسع في الوقت نفسه أنه أمر صعب. يمكن تقسيم المناهج السابقة إلى فئتين. النماذج غير البارامترية مرنة للغاية حيث تستخدم بيانات التدريب مباشرة في وقت الاختبار، ولكنها قد لا تتوسع بشكل جيد إلى مجموعات بيانات أكبر وقد لا تلتقط البنية الكاملة في البيانات. من ناحية أخرى، يمكن للمناهج البارامترية مثل المشفرات التلقائية التباينية (VAEs) تعلم تمثيلات كامنة جيدة، ولكنها غالباً ما تعتمد على خطوات استدلال غير قابلة للمعالجة أو طرق استدلالية.

لنمذجة التوزيع المشترك للبكسلات في الصورة بطريقة قابلة للمعالجة، نستخدم تحليلاً معروفاً للتوزيع المشترك كناتج من التوزيعات الشرطية. يُكتب التوزيع المشترك p(x) على النحو التالي:

p(x) = ∏ᵢ₌₁ⁿ² p(xᵢ|x₁,...,xᵢ₋₁)

حيث x هي صورة ممثلة كموتر n×n×3 من قيم البكسل، و xᵢ هو بكسل واحد. يحول التحليل العاملي مشكلة النمذجة إلى مشكلة تسلسلية، حيث يتعلم المرء التنبؤ بالبكسل التالي بناءً على جميع البكسلات المولدة سابقاً. ولكن لنمذجة التوزيعات الشرطية نحتاج إلى نموذج تسلسلي معبر للغاية يمكنه التقاط التبعيات المعقدة في الصور.

الشبكات العصبية التكرارية (RNNs) هي نماذج قوية توفر بارامترية مدمجة ومشتركة للتوزيعات الشرطية. كانت الشبكات العصبية التكرارية ناجحة للغاية في نمذجة أنواع أخرى من تسلسلات البيانات مثل توليد الكتابة اليدوية والتنبؤ بالحروف والترجمة الآلية. علاوة على ذلك، تم استخدام الشبكات العصبية التكرارية ثنائية الأبعاد سابقاً لتوليد الصور (Graves، 2013) ومؤخراً، التوليد الشرطي للصور بالرماديات أو الصور الثنائية (Gregor et al.، 2015). في عملنا الحالي نتقدم بالشبكات العصبية التكرارية ثنائية الأبعاد باستخدام معمارية جديدة قائمة على شبكات عميقة من اثنتي عشرة طبقة. نستخدم نوعين من طبقات LSTM: طبقات LSTM الصفية وطبقات BiLSTM القطرية. تتضمن الشبكات اتصالات متبقية (He et al.، 2015) حول طبقات LSTM؛ حسب علمنا هذه هي المرة الأولى التي يتم فيها استخدام الاتصالات المتبقية في الشبكات التكرارية.

كما نحسن بشكل كبير معمارية PixelCNN من (van den Oord et al.، 2016a) من خلال تقديم الالتفافات المقنعة واستخدامها لتوليد نماذج متعددة المقاييس. نحقق نتائج اللوغاريتم الاحتمالي الأفضل على الصور الطبيعية ونوفر معايير مرجعية على مجموعة بيانات ImageNet. تلتقط العينات المولدة من PixelRNN كلاً من الارتباطات المحلية والطويلة المدى في الصور وتظهر واضحة ومتنوعة ومتماسكة عالمياً.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** generative image modeling, autoregressive factorization, Row LSTM, Diagonal BiLSTM, masked convolution, multi-scale models
- **Equations:** 1 (product of conditional distributions)
- **Citations:** 4 references cited (Graves 2013, Gregor et al. 2015, He et al. 2015, van den Oord et al. 2016a)
- **Special handling:** Mathematical equation preserved in original LaTeX format. Proper names and citations kept in English.

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.88
- Glossary consistency: 0.89
- **Overall section score:** 0.90
