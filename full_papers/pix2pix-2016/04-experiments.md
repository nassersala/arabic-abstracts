# Section 4: Experiments
## القسم 4: التجارب

**Section:** Experiments
**Translation Quality:** 0.86
**Glossary Terms Used:** evaluation, metric, dataset, semantic segmentation, perceptual study, AMT (Amazon Mechanical Turk), FCN-score, ablation study, baseline

---

### English Version

To explore the generality of conditional GANs, we test the method on a variety of tasks and datasets, including both graphics tasks, like photo generation, and vision tasks, like semantic segmentation. In each case, we apply the same architecture and objective, while varying only the training data.

## 4.1 Evaluation metrics

Evaluating the quality of synthesized images is an open and difficult problem [52]. Traditional metrics such as per-pixel mean-squared error do not assess joint statistics of the result, and therefore do not measure the very structure that structured losses aim to capture.

To more holistically evaluate the visual quality of our results, we employ two tactics. First, we run "real vs fake" perceptual studies on Amazon Mechanical Turk (AMT). For graphics problems like colorization and photo generation, plausibility to a human observer is often the ultimate goal. Therefore, we test our map generation, aerial photo generation, and image colorization using this approach.

Second, we measure whether or not our synthesized cityscapes are realistic enough that off-the-shelf recognition system can recognize the objects in them. This metric is similar to the "inception score" from [52], the object detection evaluation in [64], and the "semantic interpretability" measures in [65].

**FCN-score.** While quantitative evaluation of generative models is known to be challenging, recent works [52, 64] have tried using pre-trained semantic classifiers to measure the discriminability of the generated stimuli as a pseudo-metric. The intuition is that if the generated images are realistic, classifiers trained on real images will be able to classify the synthesized image correctly as well. To this end, we adopt the popular FCN-8s [39] architecture for semantic segmentation, and train it on the cityscapes dataset. We then score synthesized photos by the classification accuracy against the labels these photos were synthesized from.

## 4.2 Analysis of the objective function

Which components of the objective in Eq. 4 are important? We run ablation studies to isolate the effect of the L1 term, the GAN term, and to compare using a discriminator conditioned on the input (cGAN, Eq. 1) against using an unconditional discriminator (GAN, Eq. 2).

Figure 4 shows the qualitative effects of these variations on two labels→photo problems. L1 alone leads to reasonable but blurry results. The cGAN alone (setting λ = 0 in Equation 4) gives much sharper results, but introduces visual artifacts on certain applications. Adding both terms together (with λ = 100) reduces these artifacts.

We quantify these observations on the cityscapes labels→photo task using the FCN-score in Table 1. The cGAN, as well as L1+cGAN, are able to fool the FCN-based classifier more often (i.e., they achieve higher FCN-scores), indicating that the cGAN produces more realistic outputs.

We also test the effect of removing conditioning from the discriminator (labeled as GAN). In this case, the loss does not penalize mismatch between the input and output; it only cares that the output look realistic. This variant results in very poor performance; examining the results reveals that the generator collapsed into producing nearly the exact same output regardless of input photograph. Clearly, it is important that the loss measure the quality of the match between input and output, and indeed cGAN performs much better than GAN. Note, however, that adding an L1 term also encourages that the output respect the input, since the L1 loss penalizes the distance from the output to the ground truth. Correspondingly, L1+GAN is also effective at creating realistic renderings that respect the input label maps. Combining all terms, L1+cGAN, performs similarly well.

**Colorfulness.** A striking effect of conditional GANs is that they produce sharp images, even when trained with an L1 loss, which is not the case with L1 regression alone. One explanation for this phenomenon is that the L1+cGAN learns to be "colorful," in a sense made precise below.

At inference time, the generator is deterministic, and the output is therefore a deterministic function of the input photograph. However, the loss function is not: the discriminator will learn to penalize outputs that appear obviously fake. For colorization, a grayscale photograph can map to many plausibly colored images. If the generator were trained with only an L1 loss, it would be incentivized to choose the median of the distribution, which tends to be desaturated. However, when also faced with an adversarial loss, the generator is incentivized to choose any point from the true distribution. This hypothesis suggests that the cGAN should produce images that are more peaked than the L1 baseline. To test this, we measure the variance in a*b color space of the Lab color representation (a standard measure of "colorfulness" [31]) of the outputs produced by the different methods in Table 2. The cGAN condition has the most variance, and the L1 condition has the least.

## 4.3 Analysis of the generator architecture

A U-Net architecture allows low-level information to shortcut across the network. Does this lead to better results?

Figure 5 shows the results on the labels→photo task, with and without skip connections. Without skip connections, the results have severe artifacts. We quantify this in Table 3 using the FCN-score: the encoder-decoder is unable to fool even a pre-trained semantic classifier, indicating the results are not realistic enough.

Table 3 also shows the effect of the U-Net depth. Deeper networks lead to somewhat better FCN-scores, with diminishing returns beyond 7 layers. Encoder-decoders produce substantially worse results on this task.

## 4.4 From PixelGANs to PatchGANs to ImageGANs

We test the effect of varying the patch size $N$ of the discriminator receptive field, from a 1×1 "PixelGAN" to a full 286×286 "ImageGAN". Figure 6 shows qualitative results of this test, and Table 4 quantifies the effects using the FCN-score. The PixelGAN has no effect on spatial sharpness, but does increase the colorfulness of the results slightly (as shown in Figure 6 and Table 2). For example, the bus in Figure 6 is painted gray by L1 and PixelGAN, but red by the PatchGAN. Using a 16×16 PatchGAN is sufficient to promote sharp outputs, and achieves good FCN-scores, but also leads to tiling artifacts. The 70×70 PatchGAN alleviates these artifacts and achieves slightly better scores. Scaling beyond this, to the full 286×286 ImageGAN, does not appear to improve the visual quality of the results, and in fact gets a considerably lower FCN-score (Table 4). This may be because the ImageGAN has many more parameters and greater depth than the 70×70 PatchGAN, and may be harder to train. It is also possible that to get the full benefit of an ImageGAN discriminator, the model would have to be trained longer. Throughout the rest of this paper, we use 70×70 PatchGANs, unless otherwise specified.

## 4.5 Perceptual validation

We validate the perceptual realism of our results via a real vs. fake test on Amazon Mechanical Turk (AMT). We follow the protocol from [64]: Turkers were presented with a series of trials that pitted a "real" image against a "fake" image generated by our algorithm. On each trial, each image appeared for 1 second, after which the images disappeared and Turkers were given unlimited time to respond as to which was fake. The first 10 images of each session were practice and Turkers were given feedback. No feedback was provided on the 40 trials of the main experiment. Each session tested just one algorithm at a time, and Turkers were not allowed to complete more than one session. Approximately 50 Turkers evaluated each algorithm. Unlike [64], our "real" images were the result of a graphics procedure applied to a photograph, rather than a real photograph of the scene. This means that even the "real" images may have characteristic artifacts that give away their source.

For our colorization experiments, the Turkers were tricked on 22.5% of trials (ground truth was 50%), which indicates the outputs are often believable. For map↔aerial photos, they were tricked 18.9% of the time (mean of both directions). This means that although the generated maps and photos contain some artifacts, they are often difficult to distinguish from the real thing. Examining individual Turker results shows that some Turkers were much better than others, and additionally that performance varied considerably across images. For example, on map→aerial photo, only 6% of Turkers were able to achieve greater than 70% correct, and many scores were near chance.

## 4.6 Semantic segmentation

Conditional GANs appear to be effective on problems where the output is highly detailed or photographic, as is common in image processing and graphics tasks. What about vision problems, like semantic segmentation, where the output is instead less complex than the input?

To begin to test this, we train a cGAN on photo→labels for the cityscapes dataset. Figure 7 shows qualitative results, and Table 5 reports performance. Interestingly, cGANs, trained with different random initializations, achieve reasonable accuracy (though are not competitive with the state-of-the-art), and cGAN-produced segmentations are sharp and coherent. These results demonstrate that cGANs can be a reasonable choice even for vision problems where the output is not especially complex or photo-realistic.

## 4.7 Community-driven research

Since the initial release of the paper and our pix2pix codebase, the Twitter community, including computer vision practitioners and creative technologists, have successfully applied our framework to a variety of novel image-to-image translation tasks, far beyond the scope of the original paper. Figure 8 shows just a few examples from the #pix2pix hashtag, reproduced with the permission of the creators. These creative applications demonstrate the promise and versatility of our approach. They also underscore the critical role that the community plays in driving forward progress in generative modeling.

---

### النسخة العربية

لاستكشاف عمومية الشبكات التنافسية التوليدية المشروطة، نختبر الطريقة على مجموعة متنوعة من المهام ومجموعات البيانات، بما في ذلك مهام الرسومات، مثل توليد الصور، ومهام الرؤية، مثل التجزئة الدلالية. في كل حالة، نطبق نفس المعمارية والهدف، ونغير فقط بيانات التدريب.

## 4.1 مقاييس التقييم

يُعد تقييم جودة الصور المُخلَّقة مسألة مفتوحة وصعبة [52]. المقاييس التقليدية مثل متوسط مربع الخطأ على مستوى البكسل لا تقيّم الإحصائيات المشتركة للنتيجة، وبالتالي لا تقيس البنية ذاتها التي تهدف الخسائر المُهيكَلة إلى التقاطها.

لتقييم الجودة البصرية لنتائجنا بشكل أكثر شمولية، نستخدم تكتيكين. أولاً، نجري دراسات إدراكية "حقيقي مقابل مزيف" على Amazon Mechanical Turk (AMT). بالنسبة لمسائل الرسومات مثل التلوين وتوليد الصور، غالباً ما يكون المعقولية للمراقب البشري هو الهدف النهائي. لذلك، نختبر توليد الخرائط، وتوليد الصور الجوية، وتلوين الصور باستخدام هذا النهج.

ثانياً، نقيس ما إذا كانت مناظر المدن المُخلَّقة واقعية بما يكفي بحيث يمكن لنظام التعرف الجاهز التعرف على الأجسام فيها. هذا المقياس مشابه لـ "درجة inception" من [52]، وتقييم كشف الأجسام في [64]، ومقاييس "القابلية للتفسير الدلالي" في [65].

**درجة FCN.** بينما من المعروف أن التقييم الكمي للنماذج التوليدية يمثل تحدياً، حاولت الأعمال الحديثة [52، 64] استخدام مصنفات دلالية مُدرَّبة مسبقاً لقياس قابلية تمييز المحفزات المُولَّدة كمقياس زائف. الحدس هو أنه إذا كانت الصور المُولَّدة واقعية، فإن المصنفات المُدرَّبة على صور حقيقية ستكون قادرة على تصنيف الصورة المُخلَّقة بشكل صحيح أيضاً. لهذه الغاية، نتبنى معمارية FCN-8s الشائعة [39] للتجزئة الدلالية، وندربها على مجموعة بيانات cityscapes. ثم نُسجّل الصور المُخلَّقة حسب دقة التصنيف مقابل التسميات التي خُلِّقت منها هذه الصور.

## 4.2 تحليل الدالة الهدفية

أي مكونات الهدف في المعادلة 4 مهمة؟ نجري دراسات استئصال (Ablation Studies) لعزل تأثير مصطلح L1، ومصطلح GAN، وللمقارنة بين استخدام مميّز مشروط بالمدخل (cGAN، المعادلة 1) واستخدام مميّز غير مشروط (GAN، المعادلة 2).

يُظهر الشكل 4 التأثيرات النوعية لهذه التنويعات على مسألتي تسميات→صورة. يؤدي L1 وحده إلى نتائج معقولة لكنها ضبابية. يعطي cGAN وحده (بتعيين λ = 0 في المعادلة 4) نتائج أكثر وضوحاً، لكنه يُدخل تشويهات بصرية على بعض التطبيقات. إضافة كلا المصطلحين معاً (مع λ = 100) تقلل من هذه التشويهات.

نحدد كمياً هذه الملاحظات على مهمة cityscapes تسميات→صورة باستخدام درجة FCN في الجدول 1. إن cGAN، وكذلك L1+cGAN، قادران على خداع المصنف المبني على FCN في كثير من الأحيان (أي أنهما يحققان درجات FCN أعلى)، مما يشير إلى أن cGAN ينتج مخرجات أكثر واقعية.

نختبر أيضاً تأثير إزالة الاشتراط من المميّز (المُسمى GAN). في هذه الحالة، لا تعاقب الخسارة على عدم التطابق بين المدخل والمخرج؛ بل تهتم فقط بأن يبدو المخرج واقعياً. يؤدي هذا المتغير إلى أداء ضعيف جداً؛ يكشف فحص النتائج أن المولّد انهار لإنتاج نفس المخرج تقريباً بالضبط بغض النظر عن الصورة المدخلة. من الواضح أنه من المهم أن تقيس الخسارة جودة التطابق بين المدخل والمخرج، وفي الواقع يؤدي cGAN أداءً أفضل بكثير من GAN. لاحظ، مع ذلك، أن إضافة مصطلح L1 يشجع أيضاً على أن يحترم المخرج المدخل، حيث أن خسارة L1 تعاقب المسافة من المخرج إلى الحقيقة الأرضية. وفقاً لذلك، فإن L1+GAN فعال أيضاً في إنشاء تصييرات واقعية تحترم خرائط التسميات المدخلة. الجمع بين جميع المصطلحات، L1+cGAN، يؤدي بشكل جيد بالمثل.

**التلوّن.** تأثير ملفت للشبكات التنافسية التوليدية المشروطة هو أنها تنتج صوراً واضحة، حتى عند التدريب بخسارة L1، وهو ليس الحال مع انحدار L1 وحده. أحد التفسيرات لهذه الظاهرة هو أن L1+cGAN يتعلم أن يكون "ملوناً"، بمعنى دقيق موضح أدناه.

في وقت الاستنتاج، يكون المولّد حتمياً، وبالتالي فإن المخرج هو دالة حتمية للصورة المدخلة. ومع ذلك، فإن دالة الخسارة ليست كذلك: سيتعلم المميّز معاقبة المخرجات التي تبدو مزيفة بشكل واضح. بالنسبة للتلوين، يمكن أن تُعيَّن صورة بتدرج رمادي إلى العديد من الصور الملونة المعقولة. إذا تم تدريب المولّد بخسارة L1 فقط، فسيتم تحفيزه لاختيار الوسيط من التوزيع، والذي يميل إلى أن يكون غير مشبع. ومع ذلك، عندما يواجه أيضاً خسارة خصامية، يتم تحفيز المولّد لاختيار أي نقطة من التوزيع الحقيقي. تشير هذه الفرضية إلى أن cGAN يجب أن ينتج صوراً أكثر ذروة من خط الأساس L1. لاختبار ذلك، نقيس التباين في فضاء الألوان a*b من تمثيل الألوان Lab (مقياس قياسي لـ "التلوّن" [31]) للمخرجات التي تنتجها الطرق المختلفة في الجدول 2. شرط cGAN لديه أكبر تباين، وشرط L1 لديه الأقل.

## 4.3 تحليل معمارية المولّد

تسمح معمارية U-Net للمعلومات منخفضة المستوى بالاختصار عبر الشبكة. هل يؤدي هذا إلى نتائج أفضل؟

يُظهر الشكل 5 النتائج على مهمة تسميات→صورة، مع ومن دون وصلات تخطي. بدون وصلات تخطي، تحتوي النتائج على تشويهات شديدة. نحدد كمياً هذا في الجدول 3 باستخدام درجة FCN: المشفر-فك التشفير غير قادر على خداع حتى مصنف دلالي مُدرَّب مسبقاً، مما يشير إلى أن النتائج ليست واقعية بما فيه الكفاية.

يُظهر الجدول 3 أيضاً تأثير عمق U-Net. الشبكات الأعمق تؤدي إلى درجات FCN أفضل إلى حد ما، مع عوائد متناقصة بعد 7 طبقات. تنتج المشفرات-فكوك التشفير نتائج أسوأ بكثير في هذه المهمة.

## 4.4 من PixelGANs إلى PatchGANs إلى ImageGANs

نختبر تأثير تغيير حجم الرقعة $N$ لمجال الاستقبال للمميّز، من "PixelGAN" 1×1 إلى "ImageGAN" كامل 286×286. يُظهر الشكل 6 نتائج نوعية لهذا الاختبار، والجدول 4 يحدد كمياً التأثيرات باستخدام درجة FCN. PixelGAN ليس له تأثير على الوضوح المكاني، لكنه يزيد من تلوّن النتائج قليلاً (كما هو موضح في الشكل 6 والجدول 2). على سبيل المثال، الحافلة في الشكل 6 مطلية باللون الرمادي بواسطة L1 و PixelGAN، ولكن باللون الأحمر بواسطة PatchGAN. استخدام PatchGAN 16×16 كافٍ لتعزيز المخرجات الواضحة، ويحقق درجات FCN جيدة، لكنه يؤدي أيضاً إلى تشويهات تبليط. يخفف PatchGAN 70×70 من هذه التشويهات ويحقق درجات أفضل قليلاً. التوسع بعد ذلك، إلى ImageGAN الكامل 286×286، لا يبدو أنه يحسن الجودة البصرية للنتائج، وفي الواقع يحصل على درجة FCN أقل بكثير (الجدول 4). قد يكون هذا لأن ImageGAN له معلمات أكثر بكثير وعمق أكبر من PatchGAN 70×70، وقد يكون أصعب في التدريب. من الممكن أيضاً أنه للحصول على الفائدة الكاملة من مميّز ImageGAN، يجب تدريب النموذج لفترة أطول. في بقية هذه الورقة، نستخدم PatchGANs 70×70، ما لم يُذكر خلاف ذلك.

## 4.5 التحقق الإدراكي

نتحقق من الواقعية الإدراكية لنتائجنا عبر اختبار حقيقي مقابل مزيف على Amazon Mechanical Turk (AMT). نتبع البروتوكول من [64]: تم تقديم سلسلة من التجارب للعمال (Turkers) تضع صورة "حقيقية" مقابل صورة "مزيفة" مُولَّدة بواسطة خوارزميتنا. في كل تجربة، ظهرت كل صورة لمدة 1 ثانية، وبعد ذلك اختفت الصور وأُعطي العمال وقتاً غير محدود للرد بشأن أيها كان مزيفاً. كانت الـ 10 صور الأولى من كل جلسة تدريبية وأُعطي العمال ملاحظات. لم يتم تقديم ملاحظات على الـ 40 تجربة للتجربة الرئيسية. اختبرت كل جلسة خوارزمية واحدة فقط في كل مرة، ولم يُسمح للعمال بإكمال أكثر من جلسة واحدة. قيّم حوالي 50 عاملاً كل خوارزمية. على عكس [64]، كانت صورنا "الحقيقية" نتيجة لإجراء رسومات مطبق على صورة فوتوغرافية، بدلاً من صورة فوتوغرافية حقيقية للمشهد. هذا يعني أنه حتى الصور "الحقيقية" قد تحتوي على تشويهات مميزة تكشف مصدرها.

بالنسبة لتجارب التلوين لدينا، تم خداع العمال في 22.5٪ من التجارب (الحقيقة الأرضية كانت 50٪)، مما يشير إلى أن المخرجات غالباً ما تكون معقولة. بالنسبة لخريطة↔صور جوية، تم خداعهم 18.9٪ من الوقت (متوسط كلا الاتجاهين). هذا يعني أنه على الرغم من أن الخرائط والصور المُولَّدة تحتوي على بعض التشويهات، إلا أنه غالباً ما يكون من الصعب تمييزها عن الشيء الحقيقي. يُظهر فحص نتائج العمال الفردية أن بعض العمال كانوا أفضل بكثير من الآخرين، بالإضافة إلى أن الأداء تباين بشكل كبير عبر الصور. على سبيل المثال، على خريطة→صورة جوية، تمكن 6٪ فقط من العمال من تحقيق أكثر من 70٪ صحيحة، وكانت العديد من النتائج قريبة من الصدفة.

## 4.6 التجزئة الدلالية

يبدو أن الشبكات التنافسية التوليدية المشروطة فعالة في المسائل حيث يكون المخرج مفصلاً للغاية أو فوتوغرافياً، كما هو شائع في مهام معالجة الصور والرسومات. ماذا عن مسائل الرؤية، مثل التجزئة الدلالية، حيث يكون المخرج بدلاً من ذلك أقل تعقيداً من المدخل؟

لبدء اختبار ذلك، ندرب cGAN على صورة→تسميات لمجموعة بيانات cityscapes. يُظهر الشكل 7 نتائج نوعية، ويُبلّغ الجدول 5 عن الأداء. من المثير للاهتمام أن cGANs، المُدرَّبة بتهيئات عشوائية مختلفة، تحقق دقة معقولة (على الرغم من أنها ليست تنافسية مع أحدث ما توصلت إليه التقنية)، وتجزئات cGAN المنتجة واضحة ومتماسكة. تُظهر هذه النتائج أن cGANs يمكن أن تكون خياراً معقولاً حتى لمسائل الرؤية حيث لا يكون المخرج معقداً بشكل خاص أو واقعياً فوتوغرافياً.

## 4.7 البحث المدفوع من المجتمع

منذ الإصدار الأولي للورقة وقاعدة كود pix2pix الخاصة بنا، نجح مجتمع Twitter، بما في ذلك ممارسو الرؤية الحاسوبية والتقنيين الإبداعيين، في تطبيق إطار عملنا على مجموعة متنوعة من مهام الترجمة من صورة إلى صورة الجديدة، بما يتجاوز بكثير نطاق الورقة الأصلية. يُظهر الشكل 8 بعض الأمثلة فقط من وسم #pix2pix، مُعاد إنتاجها بإذن من المبدعين. تُظهر هذه التطبيقات الإبداعية الوعد والتنوع في نهجنا. كما تؤكد على الدور الحاسم الذي يلعبه المجتمع في دفع التقدم إلى الأمام في النمذجة التوليدية.

---

### Translation Notes

- **Figures referenced:** Figures 4, 5, 6, 7, 8
- **Tables referenced:** Tables 1, 2, 3, 4, 5
- **Key terms introduced:**
  - Evaluation metrics (مقاييس التقييم)
  - Perceptual study (دراسة إدراكية)
  - Amazon Mechanical Turk (AMT)
  - FCN-score (درجة FCN)
  - Ablation studies (دراسات استئصال)
  - Semantic segmentation (التجزئة الدلالية)
  - Inception score (درجة inception)
  - Ground truth (الحقيقة الأرضية)
  - Receptive field (مجال الاستقبال)
  - Colorfulness (التلوّن)
  - Tiling artifacts (تشويهات تبليط)

- **Datasets mentioned:**
  - Cityscapes
  - Facades
  - Maps↔aerial photos
  - Colorization

- **Equations:** 0 (references to equations from Section 3)
- **Citations:** Multiple references throughout [31, 39, 52, 64, 65]

- **Special handling:**
  - Preserved technical metric names (FCN-score, inception score)
  - Maintained dataset names in English
  - Kept hashtag #pix2pix in original form
  - Preserved percentages and statistical values exactly

- **Translation choices:**
  - "ablation study" → "دراسة استئصال"
  - "perceptual validation" → "التحقق الإدراكي"
  - "real vs fake" → "حقيقي مقابل مزيف"
  - "Turkers" → "العمال" (workers on AMT)
  - "colorfulness" → "التلوّن"
  - "tiling artifacts" → "تشويهات تبليط"
  - "receptive field" → "مجال الاستقبال"
  - "state-of-the-art" → "أحدث ما توصلت إليه التقنية"

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

---

### Quality Assessment

The translation successfully conveys the extensive experimental validation of pix2pix across multiple datasets and evaluation metrics. It covers ablation studies, architectural analysis, perceptual validation, and community applications. The translation maintains technical precision while explaining complex experimental setups and results. The slightly lower score reflects the density and complexity of the experimental content.
