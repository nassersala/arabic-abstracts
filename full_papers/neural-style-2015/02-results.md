# Section 2: Results
## القسم 2: النتائج

**Section:** results
**Translation Quality:** 0.88
**Glossary Terms Used:** convolutional neural network (الشبكة العصبية الالتفافية), content representation (تمثيل المحتوى), style representation (تمثيل الأسلوب), loss function (دالة الخسارة), optimization (التحسين)

---

### English Version

The key finding of this paper is that the representations of content and style in the Convolutional Neural Network are separable. That is, we can manipulate both representations independently to produce new, perceptually meaningful images. To demonstrate this finding, we generate images that mix the content and style representation from two different source images. In particular, we match the content representation of a photograph depicting the "Neckarfront" in Tübingen, Germany and the style representations of several well-known artworks taken from different periods of art (Fig 2).

The images are synthesised by finding an image that simultaneously matches the content representation of the photograph and the style representation of the respective piece of art (see Methods for details). While the global arrangement of the original photograph is preserved, the colours and local structures that compose the global scenery are provided by the artwork. Effectively, this renders the photograph in the style of the artwork, such that the appearance of the synthesised image resembles the work of art, even though it shows the same content as the photograph.

As outlined above, the style representation is a multi-scale representation that includes multiple layers of the neural network. In the images we have shown in Fig 2, the style representation included layers from the whole network hierarchy. Style can also be defined more locally by including only a smaller number of lower layers, leading to different visual experiences (Fig 3, along the rows). When matching the style representations up to higher layers in the network, local images structures are matched on an increasingly large scale, leading to a smoother and more continuous visual experience. Thus, the visually most appealing images are usually created by matching the style representation up to the highest layers in the network (Fig 3, last row).

Of course, image content and style cannot be completely disentangled. When synthesising an image that combines the content of one image with the style of another, there usually does not exist an image that perfectly matches both constraints at the same time. However, the loss function we minimise during image synthesis contains two terms for content and style respectively, that are well separated (see Methods). We can therefore smoothly regulate the emphasis on either reconstructing the content or the style (Fig 3, along the columns). A strong emphasis on style will result in images that match the appearance of the artwork, effectively giving a texturised version of it, but hardly show any of the photograph's content (Fig 3, first column). When placing strong emphasis on content, one can clearly identify the photograph, but the style of the painting is not as well-matched (Fig 3, last column). For a specific pair of source images one can adjust the trade-off between content and style to create visually appealing images.

**Figure 2 Caption:**

Images that combine the content of a photograph with the style of several well-known artworks. The images were created by finding an image that simultaneously matches the content representation of the photograph and the style representation of the artwork (see Methods). The original photograph depicting the Neckarfront in Tübingen, Germany, is shown in **A** (Photo: Andreas Praefcke). The painting that provided the style for the respective generated image is shown in the bottom left corner of each panel.
- **B** *The Shipwreck of the Minotaur* by J.M.W. Turner, 1805.
- **C** *The Starry Night* by Vincent van Gogh, 1889.
- **D** *Der Schrei* by Edvard Munch, 1893.
- **E** *Femme nue assise* by Pablo Picasso, 1910.
- **F** *Composition VII* by Wassily Kandinsky, 1913.

**Figure 3 Caption:**

Detailed results for the style of the painting *Composition VII* by Wassily Kandinsky. The rows show the result of matching the style representation of increasing subsets of the CNN layers (see Methods). We find that the local image structures captured by the style representation increase in size and complexity when including style features from higher layers of the network. This can be explained by the increasing receptive field sizes and feature complexity along the network's processing hierarchy. The columns show different relative weightings between the content and style reconstruction. The number above each column indicates the ratio α/β between the emphasis on matching the content of the photograph and the style of the artwork (see Methods).

---

### النسخة العربية

النتيجة الأساسية لهذا البحث هي أن تمثيلات المحتوى والأسلوب في الشبكة العصبية الالتفافية قابلة للفصل. أي أننا يمكننا التلاعب بكلا التمثيلين بشكل مستقل لإنتاج صور جديدة ذات معنى إدراكي. لإثبات هذه النتيجة، نولد صوراً تمزج تمثيل المحتوى والأسلوب من صورتين مصدر مختلفتين. على وجه الخصوص، نطابق تمثيل المحتوى لصورة فوتوغرافية تصور "نيكارفرونت" في توبنغن، ألمانيا وتمثيلات الأسلوب لعدة أعمال فنية معروفة مأخوذة من فترات مختلفة من الفن (الشكل 2).

يتم تصنيع الصور من خلال إيجاد صورة تطابق في نفس الوقت تمثيل المحتوى للصورة الفوتوغرافية وتمثيل الأسلوب للعمل الفني المعني (انظر قسم الطرق للحصول على التفاصيل). بينما يتم الحفاظ على الترتيب العام للصورة الفوتوغرافية الأصلية، فإن الألوان والبنى الموضعية التي تكوّن المشهد العام يتم توفيرها بواسطة العمل الفني. بشكل فعال، يؤدي هذا إلى عرض الصورة الفوتوغرافية بأسلوب العمل الفني، بحيث يشبه مظهر الصورة المصنعة العمل الفني، على الرغم من أنها تُظهر نفس محتوى الصورة الفوتوغرافية.

كما هو موضح أعلاه، تمثيل الأسلوب هو تمثيل متعدد المقاييس يتضمن طبقات متعددة من الشبكة العصبية. في الصور التي أظهرناها في الشكل 2، تضمن تمثيل الأسلوب طبقات من التسلسل الهرمي الكامل للشبكة. يمكن أيضاً تعريف الأسلوب بشكل أكثر موضعية من خلال تضمين عدد أقل فقط من الطبقات السفلى، مما يؤدي إلى تجارب بصرية مختلفة (الشكل 3، على طول الصفوف). عند مطابقة تمثيلات الأسلوب حتى الطبقات العليا في الشبكة، تتم مطابقة البنى الصورية الموضعية على نطاق أكبر بشكل متزايد، مما يؤدي إلى تجربة بصرية أكثر سلاسة واستمرارية. وبالتالي، فإن الصور الأكثر جاذبية بصرياً عادة ما يتم إنشاؤها من خلال مطابقة تمثيل الأسلوب حتى الطبقات العليا في الشبكة (الشكل 3، الصف الأخير).

بالطبع، لا يمكن فصل محتوى الصورة وأسلوبها بشكل كامل. عند تصنيع صورة تجمع بين محتوى صورة وأسلوب أخرى، عادة لا توجد صورة تطابق كلا القيدين بشكل مثالي في نفس الوقت. ومع ذلك، فإن دالة الخسارة التي نقلّلها أثناء تصنيع الصورة تحتوي على حدين للمحتوى والأسلوب على التوالي، وهما مفصولان جيداً (انظر قسم الطرق). يمكننا لذلك تنظيم التركيز بسلاسة على إعادة بناء المحتوى أو الأسلوب (الشكل 3، على طول الأعمدة). سيؤدي التركيز القوي على الأسلوب إلى صور تطابق مظهر العمل الفني، مما يعطي بشكل فعال نسخة منسجة منه، ولكن بالكاد تُظهر أياً من محتوى الصورة الفوتوغرافية (الشكل 3، العمود الأول). عند وضع تركيز قوي على المحتوى، يمكن للمرء تحديد الصورة الفوتوغرافية بوضوح، لكن أسلوب اللوحة لا يتطابق بشكل جيد (الشكل 3، العمود الأخير). لزوج محدد من الصور المصدر، يمكن للمرء ضبط المفاضلة بين المحتوى والأسلوب لإنشاء صور جذابة بصرياً.

**شرح الشكل 2:**

صور تجمع بين محتوى صورة فوتوغرافية وأسلوب عدة أعمال فنية معروفة. تم إنشاء الصور من خلال إيجاد صورة تطابق في نفس الوقت تمثيل المحتوى للصورة الفوتوغرافية وتمثيل الأسلوب للعمل الفني (انظر قسم الطرق). يتم عرض الصورة الفوتوغرافية الأصلية التي تصور نيكارفرونت في توبنغن، ألمانيا في **أ** (تصوير: أندرياس برايفكه). يتم عرض اللوحة التي وفرت الأسلوب للصورة المولدة المعنية في الزاوية السفلية اليسرى من كل لوحة.
- **ب** *حطام سفينة المينوتور* لـ J.M.W. تيرنر، 1805.
- **ج** *الليلة المرصعة بالنجوم* لـ فينسنت فان جوخ، 1889.
- **د** *الصرخة* لـ إدفارد مونك، 1893.
- **هـ** *امرأة عارية جالسة* لـ بابلو بيكاسو، 1910.
- **و** *التكوين السابع* لـ فاسيلي كاندينسكي، 1913.

**شرح الشكل 3:**

نتائج مفصلة لأسلوب لوحة *التكوين السابع* لـ فاسيلي كاندينسكي. توضح الصفوف نتيجة مطابقة تمثيل الأسلوب لمجموعات فرعية متزايدة من طبقات الشبكة العصبية الالتفافية (انظر قسم الطرق). نجد أن البنى الصورية الموضعية التي يلتقطها تمثيل الأسلوب تزداد في الحجم والتعقيد عند تضمين ميزات الأسلوب من الطبقات العليا من الشبكة. يمكن تفسير ذلك بزيادة أحجام الحقول الاستقبالية وتعقيد الميزات على طول التسلسل الهرمي لمعالجة الشبكة. توضح الأعمدة الأوزان النسبية المختلفة بين إعادة بناء المحتوى والأسلوب. يشير الرقم أعلى كل عمود إلى النسبة α/β بين التركيز على مطابقة محتوى الصورة الفوتوغرافية وأسلوب العمل الفني (انظر قسم الطرق).

---

### Translation Notes

- **Figures referenced:** Figure 2 (style transfer examples), Figure 3 (detailed analysis with Kandinsky)

- **Key terms introduced:**
  - Separable representations (تمثيلات قابلة للفصل)
  - Perceptually meaningful (ذات معنى إدراكي)
  - Image synthesis (تصنيع الصور)
  - Trade-off (مفاضلة)
  - Weighting (أوزان / توزين)

- **Artworks mentioned:**
  - The Shipwreck of the Minotaur (حطام سفينة المينوتور)
  - The Starry Night (الليلة المرصعة بالنجوم)
  - Der Schrei / The Scream (الصرخة)
  - Femme nue assise (امرأة عارية جالسة)
  - Composition VII (التكوين السابع)

- **Translation choices:**
  - "Separable" → "قابلة للفصل" (can be separated)
  - "Manipulate" → "التلاعب" (manipulate/control)
  - "Synthesised" → "مصنعة" (synthesized/generated)
  - "Disentangled" → "فصل" (separated/disentangled)
  - "Trade-off" → "مفاضلة" (trade-off/balance)
  - "Texturised version" → "نسخة منسجة" (textured version)
  - "Visually appealing" → "جذابة بصرياً" (visually attractive)

- **Artist names:** Kept in English transliteration with Arabic pronunciation where applicable

- **Mathematical notation:** α/β ratio mentioned and preserved

- **Citations:** Multiple references to "see Methods"

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-translation Check

Key sentence: "The key finding of this paper is that the representations of content and style in the Convolutional Neural Network are separable."

Arabic: "النتيجة الأساسية لهذا البحث هي أن تمثيلات المحتوى والأسلوب في الشبكة العصبية الالتفافية قابلة للفصل."

Back to English: "The fundamental finding of this research is that the content and style representations in the Convolutional Neural Network are separable."

✓ Semantic match confirmed
