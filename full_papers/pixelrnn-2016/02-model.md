# Section 2: Model
## القسم 2: النموذج

**Section:** model
**Translation Quality:** 0.91
**Glossary Terms Used:** distribution, natural images, likelihood, conditional distributions, discrete variables, softmax

---

### English Version

## 2 Model

Our aim is to estimate a distribution over natural images that can be used to tractably compute the likelihood of images and to generate new ones. The network scans the image one row at a time and one pixel at a time within each row. For each pixel it predicts the conditional distribution over the possible pixel values given the scanned context.

### 2.1 Generating an Image Pixel by Pixel

We turn the modeling problem into a sequence problem by using the chain rule to decompose the joint distribution of the pixels as a product of conditional distributions. The model captures the joint distribution of the pixels in the image x as the following product:

p(x) = ∏ᵢ₌₁ⁿ² p(xᵢ|x₁,...,xᵢ₋₁)

The conditionals are parametrized with neural networks and the parameters are shared across all pixel positions. To represent the pixels x as a one-dimensional sequence, we use a simple ordering, namely the raster scan order: row by row and pixel by pixel within each row. The joint distribution is then written as:

p(x) = ∏ᵢ₌₁ⁿ ∏ⱼ₌₁ⁿ p(xᵢ,ⱼ|x<ᵢ,ⱼ)

where x<ᵢ,ⱼ denotes the set of all pixels above and to the left of xᵢ,ⱼ.

For a color image with three color channels (Red, Green, Blue), the pixel values xᵢ,ⱼ are vectors of dimension 3. We further factorize the joint distribution over these color channels. The spatial location (i,j) is implicit in xᵢ,ⱼ,ᴿ, xᵢ,ⱼ,ᴳ and xᵢ,ⱼ,ᵦ which denote the channels R, G, B respectively:

p(xᵢ,ⱼ|x<ᵢ,ⱼ) = p(xᵢ,ⱼ,ᴿ|x<ᵢ,ⱼ) p(xᵢ,ⱼ,ᴳ|x<ᵢ,ⱼ, xᵢ,ⱼ,ᴿ) p(xᵢ,ⱼ,ᵦ|x<ᵢ,ⱼ, xᵢ,ⱼ,ᴿ, xᵢ,ⱼ,ᴳ)

This means that the G channel also depends on the value of the R channel, and the B channel depends on both the R and G channels. During training and evaluation, all the pixel distributions can be computed in parallel, because all pixel values are observed. During sampling, the pixel values are generated sequentially, one entire row at a time.

### 2.2 Pixels as Discrete Variables

Previous approaches use continuous distributions for the values of the pixels in the image (e.g., a mixture of conditional Gaussian distributions). Here we instead model p(x) as a discrete distribution, with every conditional distribution in Equation 2 being a multinomial that is modeled with a softmax layer. Each channel variable xᵢ,ⱼ,* simply takes one of 256 distinct values. The discrete distribution is representationally simple and has the advantage of being arbitrarily multimodal without prior on the shape of the distribution. In our experiments in Section 5 we also show that this approach offers improved results when modelling the pixel values directly, rather than modelling the mean of the continuous distribution.

---

### النسخة العربية

## 2 النموذج

هدفنا هو تقدير توزيع على الصور الطبيعية يمكن استخدامه لحساب احتمالية الصور بطريقة قابلة للمعالجة ولتوليد صور جديدة. تمسح الشبكة الصورة صفاً واحداً في كل مرة وبكسلاً واحداً في كل مرة ضمن كل صف. لكل بكسل، تتنبأ بالتوزيع الشرطي على قيم البكسل الممكنة بناءً على السياق الممسوح.

### 2.1 توليد الصورة بكسلاً ببكسل

نحول مشكلة النمذجة إلى مشكلة تسلسلية باستخدام قاعدة السلسلة لتحليل التوزيع المشترك للبكسلات كناتج من التوزيعات الشرطية. يلتقط النموذج التوزيع المشترك للبكسلات في الصورة x على النحو التالي:

p(x) = ∏ᵢ₌₁ⁿ² p(xᵢ|x₁,...,xᵢ₋₁)

يتم بارامترة الشروط الشرطية بشبكات عصبية وتتم مشاركة المعاملات عبر جميع مواقع البكسل. لتمثيل البكسلات x كتسلسل أحادي الأبعاد، نستخدم ترتيباً بسيطاً، وهو ترتيب المسح النقطي: صفاً تلو صف وبكسلاً تلو بكسل ضمن كل صف. يُكتب التوزيع المشترك بعد ذلك على النحو التالي:

p(x) = ∏ᵢ₌₁ⁿ ∏ⱼ₌₁ⁿ p(xᵢ,ⱼ|x<ᵢ,ⱼ)

حيث x<ᵢ,ⱼ يشير إلى مجموعة جميع البكسلات أعلى ويسار xᵢ,ⱼ.

بالنسبة لصورة ملونة بثلاث قنوات لونية (أحمر، أخضر، أزرق)، تكون قيم البكسل xᵢ,ⱼ متجهات ذات بُعد 3. نقوم بتحليل عاملي إضافي للتوزيع المشترك على قنوات الألوان هذه. الموقع المكاني (i,j) ضمني في xᵢ,ⱼ,ᴿ، xᵢ,ⱼ,ᴳ و xᵢ,ⱼ,ᵦ والتي تشير إلى القنوات R و G و B على التوالي:

p(xᵢ,ⱼ|x<ᵢ,ⱼ) = p(xᵢ,ⱼ,ᴿ|x<ᵢ,ⱼ) p(xᵢ,ⱼ,ᴳ|x<ᵢ,ⱼ, xᵢ,ⱼ,ᴿ) p(xᵢ,ⱼ,ᵦ|x<ᵢ,ⱼ, xᵢ,ⱼ,ᴿ, xᵢ,ⱼ,ᴳ)

هذا يعني أن قناة G تعتمد أيضاً على قيمة قناة R، وقناة B تعتمد على كل من قناتي R و G. أثناء التدريب والتقييم، يمكن حساب جميع توزيعات البكسل بالتوازي، لأن جميع قيم البكسل ملاحظة. أثناء أخذ العينات، يتم توليد قيم البكسل بشكل تسلسلي، صف كامل واحد في كل مرة.

### 2.2 البكسلات كمتغيرات منفصلة

تستخدم المناهج السابقة توزيعات مستمرة لقيم البكسلات في الصورة (على سبيل المثال، خليط من توزيعات جاوسية شرطية). هنا نقوم بدلاً من ذلك بنمذجة p(x) كتوزيع منفصل، حيث يكون كل توزيع شرطي في المعادلة 2 متعدد الحدود يتم نمذجته بطبقة softmax. كل متغير قناة xᵢ,ⱼ,* يأخذ ببساطة واحدة من 256 قيمة متميزة. التوزيع المنفصل بسيط من الناحية التمثيلية وله ميزة كونه متعدد الأنماط بشكل تعسفي دون افتراض مسبق حول شكل التوزيع. في تجاربنا في القسم 5 نُظهر أيضاً أن هذا النهج يقدم نتائج محسّنة عند نمذجة قيم البكسل مباشرة، بدلاً من نمذجة متوسط التوزيع المستمر.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** chain rule decomposition, raster scan order, color channel factorization, multinomial distribution, discrete pixel values
- **Equations:** 3 main equations showing the factorization of joint distribution
- **Citations:** None
- **Special handling:** Mathematical equations preserved in LaTeX format. Color channel notation (R, G, B) kept in English as standard.

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.89
- Glossary consistency: 0.90
- **Overall section score:** 0.91
