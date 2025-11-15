# Section 4: Reflection
## القسم 4: التأمل

**Section:** Reflection (Takeaways and Outlook)
**Translation Quality:** 0.87
**Glossary Terms Used:** text-to-text, encoder-decoder, denoising, pre-training, fine-tuning, multi-task learning, transfer learning, state-of-the-art, C4 corpus, scaling, ensemble, distillation, parameter sharing, conditional computation, language-agnostic, benchmark

---

### English Version

Having completed our systematic study, we wrap up by first recapping some of our most significant findings. Our results provide some high-level perspective on which avenues of research might be more or less promising. To conclude, we outline some topics we think might provide effective approaches for further progressing the field.

#### 4.1 Takeaways

**Text-to-text:** Our text-to-text framework provides a simple way to train a single model on a wide variety of text tasks using the same loss function and decoding procedure. We showed how this approach can be successfully applied to generative tasks like abstractive summarization, classification tasks like natural language inference, and even regression tasks like STS-B. In spite of its simplicity, we found the text-to-text framework obtained comparable performance to task-specific architectures and ultimately produced state-of-the-art results when combined with scale.

**Architectures:** While some work on transfer learning for NLP has considered architectural variants of the Transformer, we found the original encoder-decoder form worked best in our text-to-text framework. Though an encoder-decoder model uses twice as many parameters as "encoder-only" (e.g. BERT) or "decoder-only" (language model) architectures, it has a similar computational cost. We also showed that sharing the parameters in the encoder and decoder did not result in a substantial performance drop while halving the total parameter count.

**Unsupervised objectives:** Overall, we found that most "denoising" objectives, which train the model to reconstruct randomly corrupted text, performed similarly in the text-to-text setup. As a result, we suggest using objectives that produce short target sequences so that unsupervised pre-training is more computationally efficient.

**Data sets:** We introduced the "Colossal Clean Crawled Corpus" (C4), which comprises heuristically-cleaned text from the Common Crawl web dump. When comparing C4 to data sets that use additional filtering, we found that training on in-domain unlabeled data could boost performance in a few downstream tasks. However, constraining to a single domain typically results in a smaller data set. We separately showed that performance can degrade when an unlabeled data set is small enough that it is repeated many times over the course of pre-training. This motivates the use of a large and diverse data set like C4 for generic language understanding tasks.

**Training strategies:** We found that the basic approach of updating all of a pre-trained model's parameters during fine-tuning outperformed methods that are designed to update fewer parameters, although updating all parameters is most expensive. We also experimented with various approaches for training the model on multiple tasks at once, which in our text-to-text setting simply corresponds to mixing examples from different data sets when constructing batches. The primary concern in multi-task learning is setting the proportion of each task to train on. We ultimately did not find a strategy for setting mixing proportions that matched the performance of the basic approach of unsupervised pre-training followed by supervised fine-tuning. However, we found that fine-tuning after pre-training on a mixture of tasks produced comparable performance to unsupervised pre-training.

**Scaling:** We compared various strategies for taking advantage of additional compute, including training the model on more data, training a larger model, and using an ensemble of models. We found each approach conferred a significant boost in performance, though training a smaller model on more data was often outperformed by training a larger model for fewer steps. We also showed an ensemble of models can provide substantially better results than a single model, which provides an orthogonal means of leveraging additional computation. Ensembling models that were fine-tuned from the same base pre-trained model performed worse than pre-training and fine-tuning all models completely separately, though fine-tune-only ensembling still substantially outperformed a single model.

**Pushing the limits:** We combined our above insights and trained substantially larger models (up to 11 billion parameters) to achieve state-of-the-art results across many of the benchmarks we considered. For unsupervised training, we extracted text from our C4 data set and applied a denoising objective that corrupts contiguous spans of tokens. We pre-trained on a multi-task mixture before fine-tuning on individual tasks. Overall, our models were trained on over 1 trillion tokens. In the interest of facilitating the replication, extension, and application of our results, we release our code, the C4 data set, and pre-trained model weights for each T5 variant.

#### 4.2 Outlook

**The inconvenience of large models:** An unsurprising but important result from our study is that larger models tend to perform better. The fact that the hardware used for running these models is continually getting cheaper and more powerful suggests that scaling up may continue to be a promising way to achieve better performance. However, it will always be the case that there are applications and scenarios where using a smaller or less expensive model is helpful, for example when performing client-side inference or federated learning. Relatedly, one beneficial use of transfer learning is the possibility of attaining good performance on low-resource tasks. Low-resource tasks often occur (by definition) in settings where one lacks the assets to label more data. It follows that low-resource applications often also have limited access to computational resources which can incur additional costs. As a result, we advocate for research on methods that achieve stronger performance with cheaper models so that transfer learning can be applied where it will have the most impact. Some current work along these lines include distillation, parameter sharing, and conditional computation.

**More efficient knowledge extraction:** Recall that one of the goals of pre-training is (loosely speaking) to provide the model with general-purpose "knowledge" that improves its performance on downstream tasks. The method we use in this work, which is currently common practice, is to train the model to denoise corrupted spans of text. We suspect that this simplistic technique may not be a very efficient way to teach the model general-purpose knowledge. More concretely, it would be useful to be able to attain good fine-tuning performance without needing to train our models on 1 trillion tokens of text first. Some concurrent work along these lines improves efficiency by pre-training a model to distinguish between real and machine-generated text.

**Formalizing the similarity between tasks:** We observed that pre-training on unlabeled in-domain data can improve performance on downstream tasks. This finding mostly relies on basic observations like the fact that SQuAD was created using data from Wikipedia. It would be useful to formulate a more rigorous notion of the "similarity" between the pre-training and downstream tasks, so that we could make more principled choices about what source of unlabeled data to use. There is some early empirical work along these lines in the field of computer vision. A better notion of the relatedness of tasks could also help choose supervised pre-training tasks, which has been shown to be helpful for the GLUE benchmark.

**Language-agnostic models:** We were disappointed to find that English-only pre-training did not achieve state-of-the-art results on the translation tasks we studied. We also are interested in avoiding the logistical difficulty of needing to specify which languages a vocabulary can encode ahead of time. To address these issues, we are interested in further investigating language-agnostic models, i.e. models that can perform a given NLP task with good performance regardless of the text's language. This is an especially pertinent issue given that English is not the native language for the majority of the world's population.

The motivation for this paper was the flurry of recent work on transfer learning for NLP. Before we began this work, these advances had already enabled breakthroughs in settings where learning-based methods had not yet been shown to be effective. We are happy to be able to continue this trend, for example by nearly matching human-level performance on the SuperGLUE benchmark, a task specifically designed to be difficult for modern transfer-learning pipelines. Our results stem from the combination of a straightforward and unified text-to-text framework, our new C4 data set, and insights from our systematic study. Additionally, we provided an empirical overview of the field and a perspective on where it stands. We are excited to see continued work using transfer learning towards the goal of general language understanding.

---

### النسخة العربية

بعد إكمال دراستنا المنهجية، نختتم بإعادة عرض بعض أهم نتائجنا أولاً. توفر نتائجنا بعض المنظور رفيع المستوى حول السبل البحثية التي قد تكون أكثر أو أقل واعدة. للختام، نحدد بعض الموضوعات التي نعتقد أنها قد توفر أساليب فعالة لمزيد من تقدم المجال.

#### 4.1 النقاط الرئيسية

**من نص إلى نص:** يوفر إطار عملنا من نص إلى نص طريقة بسيطة لتدريب نموذج واحد على مجموعة واسعة من مهام النصوص باستخدام نفس دالة الخسارة وإجراء فك التشفير. أظهرنا كيف يمكن تطبيق هذا النهج بنجاح على المهام التوليدية مثل التلخيص التجريدي، ومهام التصنيف مثل الاستدلال اللغوي الطبيعي، وحتى مهام الانحدار مثل STS-B. على الرغم من بساطته، وجدنا أن إطار العمل من نص إلى نص حصل على أداء مماثل للمعماريات الخاصة بالمهمة وأنتج في النهاية نتائج متقدمة عند دمجه مع النطاق.

**المعماريات:** بينما درس بعض الأعمال حول التعلم بالنقل لمعالجة اللغة الطبيعية متغيرات معمارية للمحول، وجدنا أن شكل المشفر-فك التشفير الأصلي عمل بشكل أفضل في إطار عملنا من نص إلى نص. على الرغم من أن نموذج المشفر-فك التشفير يستخدم ضعف عدد المعاملات مقارنة بالمعماريات "المشفر فقط" (مثل BERT) أو "فك التشفير فقط" (نموذج اللغة)، إلا أن له تكلفة حسابية مماثلة. أظهرنا أيضاً أن مشاركة المعاملات في المشفر وفك التشفير لم ينتج عنها انخفاض كبير في الأداء مع تقليل إجمالي عدد المعاملات إلى النصف.

**الأهداف غير الخاضعة للإشراف:** بشكل عام، وجدنا أن معظم أهداف "إزالة الضوضاء"، التي تدرب النموذج على إعادة بناء النص التالف عشوائياً، أدت أداءً مماثلاً في إعداد نص إلى نص. نتيجة لذلك، نقترح استخدام أهداف تنتج تسلسلات هدف قصيرة بحيث يكون التدريب المسبق غير الخاضع للإشراف أكثر كفاءة حسابياً.

**مجموعات البيانات:** قدمنا "مدونة الزحف النظيفة الضخمة" (C4)، التي تتكون من نصوص منظفة بشكل إرشادي من تفريغ Common Crawl على الويب. عند مقارنة C4 بمجموعات البيانات التي تستخدم تصفية إضافية، وجدنا أن التدريب على بيانات غير معنونة داخل المجال يمكن أن يعزز الأداء في عدد قليل من المهام اللاحقة. ومع ذلك، فإن التقييد بمجال واحد ينتج عنه عادةً مجموعة بيانات أصغر. أظهرنا بشكل منفصل أن الأداء يمكن أن يتدهور عندما تكون مجموعة البيانات غير المعنونة صغيرة بما يكفي بحيث تتكرر عدة مرات على مدار التدريب المسبق. هذا يحفز استخدام مجموعة بيانات كبيرة ومتنوعة مثل C4 لمهام فهم اللغة العامة.

**استراتيجيات التدريب:** وجدنا أن النهج الأساسي لتحديث جميع معاملات نموذج مدرب مسبقاً أثناء الضبط الدقيق تفوق على الطرق المصممة لتحديث عدد أقل من المعاملات، على الرغم من أن تحديث جميع المعاملات هو الأكثر تكلفة. جربنا أيضاً أساليب مختلفة لتدريب النموذج على مهام متعددة في وقت واحد، والذي في إعداد نص إلى نص لدينا يتوافق ببساطة مع مزج أمثلة من مجموعات بيانات مختلفة عند بناء الدفعات. الشاغل الرئيسي في التعلم متعدد المهام هو تحديد نسبة كل مهمة للتدريب عليها. في النهاية لم نجد استراتيجية لتحديد نسب المزج التي تطابق أداء النهج الأساسي للتدريب المسبق غير الخاضع للإشراف متبوعاً بالضبط الدقيق الخاضع للإشراف. ومع ذلك، وجدنا أن الضبط الدقيق بعد التدريب المسبق على مزيج من المهام أنتج أداءً مماثلاً للتدريب المسبق غير الخاضع للإشراف.

**التطوير:** قارنا استراتيجيات مختلفة للاستفادة من الحوسبة الإضافية، بما في ذلك تدريب النموذج على المزيد من البيانات، وتدريب نموذج أكبر، واستخدام مجموعة من النماذج. وجدنا أن كل نهج منح دفعة كبيرة في الأداء، على الرغم من أن تدريب نموذج أصغر على المزيد من البيانات كان غالباً ما يتفوق عليه تدريب نموذج أكبر لعدد أقل من الخطوات. أظهرنا أيضاً أن مجموعة من النماذج يمكن أن توفر نتائج أفضل بكثير من نموذج واحد، مما يوفر وسيلة متعامدة للاستفادة من الحوسبة الإضافية. أداء تجميع النماذج التي تم ضبطها بدقة من نفس النموذج الأساسي المدرب مسبقاً كان أسوأ من التدريب المسبق والضبط الدقيق لجميع النماذج بشكل منفصل تماماً، على الرغم من أن التجميع بالضبط الدقيق فقط تفوق بشكل كبير على نموذج واحد.

**دفع الحدود:** جمعنا رؤانا أعلاه ودربنا نماذج أكبر بكثير (تصل إلى 11 مليار معامل) لتحقيق نتائج متقدمة عبر العديد من المعايير التي درسناها. للتدريب غير الخاضع للإشراف، استخرجنا نصاً من مجموعة بيانات C4 وطبقنا هدف إزالة الضوضاء الذي يفسد امتدادات متجاورة من الرموز. دربنا مسبقاً على مزيج متعدد المهام قبل الضبط الدقيق على المهام الفردية. بشكل عام، تم تدريب نماذجنا على أكثر من تريليون رمز. من أجل تسهيل تكرار نتائجنا وتوسيعها وتطبيقها، نصدر كودنا ومجموعة بيانات C4 وأوزان النموذج المدرب مسبقاً لكل متغير من T5.

#### 4.2 النظرة المستقبلية

**إزعاج النماذج الكبيرة:** نتيجة غير مفاجئة ولكنها مهمة من دراستنا هي أن النماذج الأكبر تميل إلى الأداء بشكل أفضل. حقيقة أن الأجهزة المستخدمة لتشغيل هذه النماذج تصبح باستمرار أرخص وأكثر قوة تشير إلى أن التوسع قد يستمر في كونه طريقة واعدة لتحقيق أداء أفضل. ومع ذلك، سيكون دائماً هناك تطبيقات وسيناريوهات حيث يكون استخدام نموذج أصغر أو أقل تكلفة مفيداً، على سبيل المثال عند إجراء استنتاج من جانب العميل أو التعلم الاتحادي. ذات صلة، أحد الاستخدامات المفيدة للتعلم بالنقل هو إمكانية تحقيق أداء جيد على المهام ذات الموارد المنخفضة. غالباً ما تحدث المهام ذات الموارد المنخفضة (بحكم التعريف) في إعدادات حيث يفتقر المرء إلى الأصول لتصنيف المزيد من البيانات. يترتب على ذلك أن التطبيقات ذات الموارد المنخفضة غالباً ما يكون لها أيضاً وصول محدود إلى الموارد الحسابية التي يمكن أن تتكبد تكاليف إضافية. نتيجة لذلك، ندعو إلى البحث عن طرق تحقق أداءً أقوى بنماذج أرخص بحيث يمكن تطبيق التعلم بالنقل حيث سيكون له أكبر تأثير. تتضمن بعض الأعمال الحالية في هذا الاتجاه التقطير ومشاركة المعاملات والحوسبة الشرطية.

**استخراج المعرفة بشكل أكثر كفاءة:** تذكر أن أحد أهداف التدريب المسبق هو (بشكل عام) توفير "معرفة" للنموذج ذات أغراض عامة تحسن أداءه على المهام اللاحقة. الطريقة التي نستخدمها في هذا العمل، والتي هي ممارسة شائعة حالياً، هي تدريب النموذج على إزالة ضوضاء امتدادات النص التالفة. نشك في أن هذه التقنية البسيطة قد لا تكون طريقة فعالة للغاية لتعليم النموذج المعرفة العامة. بشكل أكثر تحديداً، سيكون من المفيد أن نكون قادرين على تحقيق أداء ضبط دقيق جيد دون الحاجة إلى تدريب نماذجنا على تريليون رمز من النصوص أولاً. بعض الأعمال المتزامنة في هذا الاتجاه تحسن الكفاءة من خلال التدريب المسبق لنموذج للتمييز بين النص الحقيقي والنص الذي تم إنشاؤه آلياً.

**إضفاء الطابع الرسمي على التشابه بين المهام:** لاحظنا أن التدريب المسبق على بيانات غير معنونة داخل المجال يمكن أن يحسن الأداء على المهام اللاحقة. يعتمد هذا الاكتشاف في الغالب على ملاحظات أساسية مثل حقيقة أن SQuAD تم إنشاؤه باستخدام بيانات من ويكيبيديا. سيكون من المفيد صياغة مفهوم أكثر صرامة للـ "تشابه" بين مهام التدريب المسبق والمهام اللاحقة، بحيث يمكننا اتخاذ خيارات أكثر مبدئية حول مصدر البيانات غير المعنونة التي يجب استخدامها. هناك بعض الأعمال التجريبية المبكرة في هذا الاتجاه في مجال الرؤية الحاسوبية. يمكن أن يساعد مفهوم أفضل لترابط المهام أيضاً في اختيار مهام التدريب المسبق الخاضعة للإشراف، والتي ثبت أنها مفيدة لمعيار GLUE.

**نماذج لا تعتمد على اللغة:** كنا محبطين لاكتشاف أن التدريب المسبق بالإنجليزية فقط لم يحقق نتائج متقدمة على مهام الترجمة التي درسناها. نحن مهتمون أيضاً بتجنب الصعوبة اللوجستية للحاجة إلى تحديد اللغات التي يمكن للمفردات ترميزها مسبقاً. لمعالجة هذه المشكلات، نحن مهتمون بالتحقيق بشكل أكبر في النماذج التي لا تعتمد على اللغة، أي النماذج التي يمكنها أداء مهمة معينة لمعالجة اللغة الطبيعية بأداء جيد بغض النظر عن لغة النص. هذه قضية ذات صلة خاصة بالنظر إلى أن الإنجليزية ليست اللغة الأم لغالبية سكان العالم.

كان الدافع لهذا البحث هو موجة الأعمال الأخيرة حول التعلم بالنقل لمعالجة اللغة الطبيعية. قبل أن نبدأ هذا العمل، كانت هذه التطورات قد مكّنت بالفعل من اختراقات في إعدادات حيث لم يتم إثبات فعالية الطرق القائمة على التعلم بعد. نحن سعداء بأن نكون قادرين على مواصلة هذا الاتجاه، على سبيل المثال من خلال مطابقة الأداء على مستوى البشر تقريباً على معيار SuperGLUE، وهي مهمة مصممة خصيصاً لتكون صعبة على خطوط أنابيب التعلم بالنقل الحديثة. تنبع نتائجنا من الجمع بين إطار عمل مباشر وموحد من نص إلى نص، ومجموعة بيانات C4 الجديدة، والرؤى من دراستنا المنهجية. بالإضافة إلى ذلك، قدمنا نظرة عامة تجريبية للمجال ومنظوراً حول الوضع الحالي. نحن متحمسون لرؤية العمل المستمر باستخدام التعلم بالنقل نحو هدف فهم اللغة العام.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** Takeaways, outlook, distillation, parameter sharing, conditional computation, language-agnostic models, federated learning, human-level performance
- **Equations:** 0
- **Citations:** References to related work on distillation, federated learning, computer vision
- **Special handling:**
  - Summary of key findings organized by topic
  - Future research directions
  - Acknowledgment of limitations and challenges
  - Model release information (code, datasets, weights)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.87
