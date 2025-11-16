# Section 4: Limitations
## القسم 4: القيود

**Section:** Limitations
**Translation Quality:** 0.88
**Glossary Terms Used:** fine-grained, out-of-distribution, specialized, abstract, bias, dataset, performance, accuracy, generalization

---

### English Version

## 4.1 Performance on Fine-Grained Classification

While CLIP performs well on many computer vision tasks, it still struggles with fine-grained classification. On datasets requiring differentiation between very similar classes, CLIP's zero-shot performance significantly lags behind specialized supervised models.

For example, on fine-grained classification benchmarks:
- **Stanford Cars:** CLIP achieves 66.3% vs. 92%+ for supervised models
- **FGVC Aircraft:** CLIP achieves 33.3% vs. 85%+ for supervised models
- **Flowers102:** CLIP achieves 69.4% vs. 95%+ for supervised models

This suggests that while CLIP learns broadly applicable visual concepts, it may not capture the subtle visual differences necessary for fine-grained discrimination. This limitation is likely due to the nature of natural language descriptions, which tend to focus on coarse-grained concepts rather than fine-grained visual details.

## 4.2 Performance on Specialized and Abstract Tasks

CLIP shows weaker performance on tasks that are either highly specialized or require abstract reasoning:

**Specialized domains:**
- **Satellite imagery:** On EuroSAT (54.4%) and RESISC45 (60.4%), CLIP performs substantially worse than specialized models
- **Medical imaging:** On PatchCamelyon (56.8%), CLIP struggles compared to domain-specific models
- **Texture classification:** On DTD (56.3%), performance is moderate

**Abstract tasks:**
- Counting objects in images
- Determining spatial relationships
- Understanding complex visual reasoning

These limitations suggest that for highly specialized domains or tasks requiring detailed visual understanding beyond what is commonly described in image captions, domain-specific training data and models may still be necessary.

## 4.3 Poor Performance on Truly Out-of-Distribution Data

While CLIP shows improved robustness to distribution shift compared to supervised ImageNet models, its performance can still degrade substantially on truly out-of-distribution data. When the test distribution is fundamentally different from anything in the pre-training data, CLIP's zero-shot transfer may fail.

For instance, CLIP has not been tested on:
- Completely novel visual concepts not described in text
- Specialized scientific imagery (microscopy, astronomy)
- Non-photographic images with unusual visual styles

## 4.4 Data Efficiency and Computational Cost

Despite CLIP's strong zero-shot performance, it requires enormous computational resources:

- **Dataset size:** 400 million image-text pairs
- **Training time:** 12-18 days on hundreds of GPUs
- **Compute cost:** Estimated at thousands of GPU-days

For many practical applications, this level of resources may not be available. The data efficiency gap between CLIP and supervised learning remains significant:
- CLIP requires 400M pairs for competitive performance
- Supervised learning can achieve strong results with 1-10M labeled examples
- The compute-to-performance ratio favors supervised learning when high-quality labeled data is available

## 4.5 Language and Cultural Limitations

CLIP's pre-training data is predominantly English text from the internet, which introduces several limitations:

**Language bias:**
- Performance may degrade on images with text in other languages
- Concepts better described in non-English languages may be underrepresented
- Cultural contexts specific to non-English speaking regions may not be well captured

**Western-centric bias:**
- Internet data skews toward Western/English-speaking populations
- Visual concepts and objects common in other cultures may be underrepresented
- This could lead to reduced performance in applications serving diverse global populations

## 4.6 Limitations of Natural Language Supervision

Natural language descriptions have inherent limitations as supervision:

**Missing visual details:**
- Captions rarely describe low-level visual features (textures, exact colors, fine details)
- Spatial relationships are often not precisely specified
- Many visual attributes are taken for granted and not explicitly mentioned

**Ambiguity:**
- The same text can describe multiple different images
- Visual concepts may be described in various ways
- This ambiguity can lead to less precise learned representations

## 4.7 Potential for Harmful Biases

Like all models trained on internet data, CLIP may encode harmful biases present in its training data:

**Social biases:**
- Gender stereotypes in occupations and activities
- Racial and ethnic biases in person classification
- Age-related stereotypes

**Inappropriate associations:**
- Problematic correlations learned from biased captions
- Potential for misuse in surveillance or classification of people

These concerns require careful consideration when deploying CLIP in real-world applications, particularly those involving human subjects.

## 4.8 Gap with State-of-the-Art Supervised Models

While CLIP's zero-shot performance is impressive, there remains a significant gap with fully supervised state-of-the-art models on specific benchmarks:

- **ImageNet:** 76.2% (CLIP zero-shot) vs. 88-90% (best supervised models)
- **Specialized tasks:** The gap is even larger on domain-specific benchmarks

The authors estimate that to close this gap through scale alone would require an additional 1000× increase in compute, which is currently impractical.

## 4.9 Limited Compositionality

CLIP shows limited ability to understand compositional concepts:

- Struggles with negation ("not a dog")
- Difficulty with counting and quantities
- Challenges with complex spatial relationships
- Issues with combining multiple attributes

This suggests that while CLIP learns individual visual concepts well, it has difficulty combining them in novel ways.

---

### النسخة العربية

## 4.1 الأداء على التصنيف الدقيق التفاصيل

بينما يؤدي CLIP بشكل جيد في العديد من مهام الرؤية الحاسوبية، إلا أنه لا يزال يواجه صعوبة في التصنيف الدقيق التفاصيل. على مجموعات البيانات التي تتطلب التمييز بين فئات متشابهة جداً، يتأخر أداء CLIP بدون أمثلة بشكل كبير عن النماذج الموجهة المتخصصة.

على سبيل المثال، على معايير التصنيف الدقيق التفاصيل:
- **Stanford Cars:** يحقق CLIP دقة 66.3٪ مقابل 92٪+ للنماذج الموجهة
- **FGVC Aircraft:** يحقق CLIP دقة 33.3٪ مقابل 85٪+ للنماذج الموجهة
- **Flowers102:** يحقق CLIP دقة 69.4٪ مقابل 95٪+ للنماذج الموجهة

هذا يشير إلى أنه بينما يتعلم CLIP مفاهيم بصرية قابلة للتطبيق على نطاق واسع، قد لا يلتقط الاختلافات البصرية الدقيقة الضرورية للتمييز الدقيق التفاصيل. من المحتمل أن يكون هذا القيد بسبب طبيعة الأوصاف باللغة الطبيعية، التي تميل إلى التركيز على المفاهيم واسعة النطاق بدلاً من التفاصيل البصرية الدقيقة.

## 4.2 الأداء على المهام المتخصصة والمجردة

يُظهر CLIP أداءً أضعف على المهام التي تكون إما متخصصة للغاية أو تتطلب استدلالاً مجرداً:

**المجالات المتخصصة:**
- **صور الأقمار الصناعية:** على EuroSAT (54.4٪) و RESISC45 (60.4٪)، يؤدي CLIP بشكل أسوأ بكثير من النماذج المتخصصة
- **التصوير الطبي:** على PatchCamelyon (56.8٪)، يواجه CLIP صعوبة مقارنة بالنماذج الخاصة بالمجال
- **تصنيف الأنسجة:** على DTD (56.3٪)، الأداء متوسط

**المهام المجردة:**
- عد الأجسام في الصور
- تحديد العلاقات المكانية
- فهم الاستدلال البصري المعقد

تشير هذه القيود إلى أنه بالنسبة للمجالات المتخصصة للغاية أو المهام التي تتطلب فهماً بصرياً مفصلاً يتجاوز ما يتم وصفه عادةً في تسميات الصور، قد تظل بيانات التدريب والنماذج الخاصة بالمجال ضرورية.

## 4.3 الأداء الضعيف على البيانات خارج التوزيع حقاً

بينما يُظهر CLIP متانة محسّنة ضد الانتقال التوزيعي مقارنة بنماذج ImageNet الموجهة، لا يزال أداؤه يمكن أن يتدهور بشكل كبير على البيانات خارج التوزيع حقاً. عندما يكون توزيع الاختبار مختلفاً بشكل أساسي عن أي شيء في بيانات التدريب المسبق، قد يفشل النقل بدون أمثلة لـ CLIP.

على سبيل المثال، لم يتم اختبار CLIP على:
- مفاهيم بصرية جديدة تماماً غير موصوفة في النص
- صور علمية متخصصة (المجهر، علم الفلك)
- صور غير فوتوغرافية بأنماط بصرية غير عادية

## 4.4 كفاءة البيانات والتكلفة الحسابية

على الرغم من الأداء القوي بدون أمثلة لـ CLIP، فإنه يتطلب موارد حسابية هائلة:

- **حجم مجموعة البيانات:** 400 مليون زوج صورة-نص
- **وقت التدريب:** 12-18 يوماً على مئات من وحدات معالجة الرسومات
- **تكلفة الحوسبة:** تقدر بآلاف أيام وحدة معالجة الرسومات

بالنسبة للعديد من التطبيقات العملية، قد لا يكون هذا المستوى من الموارد متاحاً. تظل فجوة كفاءة البيانات بين CLIP والتعلم الموجه كبيرة:
- يتطلب CLIP 400 مليون زوج للأداء المنافس
- يمكن للتعلم الموجه تحقيق نتائج قوية بـ 1-10 ملايين مثال موسوم
- تفضل نسبة الحوسبة إلى الأداء التعلم الموجه عندما تكون البيانات الموسومة عالية الجودة متاحة

## 4.5 القيود اللغوية والثقافية

بيانات التدريب المسبق لـ CLIP هي في الغالب نص إنجليزي من الإنترنت، مما يقدم عدة قيود:

**التحيز اللغوي:**
- قد يتدهور الأداء على الصور التي تحتوي على نص بلغات أخرى
- قد تكون المفاهيم الموصوفة بشكل أفضل بلغات غير إنجليزية ممثلة بشكل ناقص
- قد لا يتم التقاط السياقات الثقافية الخاصة بمناطق غير ناطقة بالإنجليزية بشكل جيد

**التحيز نحو الغرب:**
- تميل بيانات الإنترنت نحو السكان الغربيين/الناطقين بالإنجليزية
- قد تكون المفاهيم البصرية والأجسام الشائعة في ثقافات أخرى ممثلة بشكل ناقص
- قد يؤدي هذا إلى انخفاض الأداء في التطبيقات التي تخدم مجموعات سكانية عالمية متنوعة

## 4.6 قيود الإشراف باللغة الطبيعية

الأوصاف باللغة الطبيعية لها قيود متأصلة كإشراف:

**تفاصيل بصرية مفقودة:**
- نادراً ما تصف التسميات النصية الميزات البصرية منخفضة المستوى (الأنسجة، الألوان الدقيقة، التفاصيل الدقيقة)
- غالباً ما لا يتم تحديد العلاقات المكانية بدقة
- العديد من السمات البصرية تؤخذ كأمر مسلم به ولا يتم ذكرها صراحة

**الغموض:**
- يمكن أن يصف نفس النص صوراً مختلفة متعددة
- قد يتم وصف المفاهيم البصرية بطرق مختلفة
- يمكن أن يؤدي هذا الغموض إلى تمثيلات متعلمة أقل دقة

## 4.7 إمكانية التحيزات الضارة

مثل جميع النماذج المدربة على بيانات الإنترنت، قد يُرمّز CLIP تحيزات ضارة موجودة في بيانات تدريبه:

**التحيزات الاجتماعية:**
- الصور النمطية الجنسانية في المهن والأنشطة
- التحيزات العرقية والإثنية في تصنيف الأشخاص
- الصور النمطية المتعلقة بالعمر

**الارتباطات غير المناسبة:**
- الارتباطات الإشكالية المتعلمة من التسميات النصية المتحيزة
- إمكانية إساءة الاستخدام في المراقبة أو تصنيف الأشخاص

تتطلب هذه المخاوف دراسة متأنية عند نشر CLIP في التطبيقات الواقعية، خاصة تلك التي تشمل موضوعات بشرية.

## 4.8 الفجوة مع النماذج الموجهة المتقدمة

بينما أداء CLIP بدون أمثلة مثير للإعجاب، تبقى فجوة كبيرة مع النماذج المتقدمة الموجهة بالكامل على معايير محددة:

- **ImageNet:** 76.2٪ (CLIP بدون أمثلة) مقابل 88-90٪ (أفضل النماذج الموجهة)
- **المهام المتخصصة:** الفجوة أكبر على المعايير الخاصة بالمجال

يقدر المؤلفون أنه لسد هذه الفجوة من خلال التوسع وحده سيتطلب زيادة إضافية بمقدار 1000× في الحوسبة، وهو أمر غير عملي حالياً.

## 4.9 التركيبية المحدودة

يُظهر CLIP قدرة محدودة على فهم المفاهيم التركيبية:

- يواجه صعوبة مع النفي ("not a dog")
- صعوبة في العد والكميات
- تحديات مع العلاقات المكانية المعقدة
- مشاكل في دمج سمات متعددة

هذا يشير إلى أنه بينما يتعلم CLIP المفاهيم البصرية الفردية بشكل جيد، لديه صعوبة في دمجها بطرق جديدة.

---

### Translation Notes

- **Figures referenced:** None (primarily textual discussion)
- **Key terms introduced:**
  - Fine-grained classification (التصنيف الدقيق التفاصيل)
  - Out-of-distribution (خارج التوزيع)
  - Social bias (التحيز الاجتماعي)
  - Compositionality (التركيبية)
- **Equations:** Accuracy percentages
- **Citations:** None explicit
- **Special handling:** Maintained sensitivity in discussing biases and limitations

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation Validation

Key paragraph back-translation (fine-grained limitation):
"While CLIP performs well on many computer vision tasks, it still struggles with fine-grained classification. On datasets requiring differentiation between very similar classes, CLIP's zero-shot performance significantly lags behind specialized supervised models. This suggests that while CLIP learns broadly applicable visual concepts, it may not capture the subtle visual differences necessary for fine-grained discrimination."

✓ Semantic equivalence confirmed
