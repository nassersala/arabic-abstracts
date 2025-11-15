# Section 2: Prior Work
## القسم 2: الأعمال السابقة

**Section:** prior-work
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, efficient, architecture, latency, compression, optimization, convolution, network

---

### English Version

There has been rising interest in building small and efficient neural networks in the recent literature, e.g. [16, 34, 12, 36, 22]. Many different approaches can be generally categorized into either compressing pretrained networks or training small networks directly. This paper proposes a class of network architectures that allows a model developer to specifically choose a small network that matches the resource restrictions (latency, size) for their application. MobileNets primarily focus on optimizing for latency but also yield small networks. Many papers on small networks focus only on size but do not consider speed.

MobileNets are built primarily from depthwise separable convolutions initially introduced in [26] and subsequently used in Inception models [13] to reduce the computation in the first few layers. Flattened networks [16] build a network out of fully factorized convolutions and showed the potential of extremely factorized networks. Independent of this current paper, Factorized Networks[34] introduces a similar factorized convolution as well as the use of topological connections. Subsequently, the Xception network [3] demonstrated how to scale up depthwise separable filters to out perform Inception V3 networks. Another small network is Squeezenet [12] which uses a bottleneck approach to design a very small network. Other reduced computation networks include structured transform networks [28] and deep fried convnets [37].

A different approach for obtaining small networks is shrinking, factorizing or compressing pretrained networks. Compression based on product quantization [36], hashing [2], and pruning, vector quantization and Huffman coding [5] have been proposed in the literature. Additionally various factorizations have been proposed to speed up pretrained networks [14, 20]. Another method for training small networks is distillation [9] which uses a larger network to teach a smaller network. It is complementary to our approach and is covered in some of our use cases in section 4. Another emerging approach is low bit networks [4, 22, 11].

---

### النسخة العربية

كان هناك اهتمام متزايد ببناء شبكات عصبية صغيرة وفعالة في الأدبيات الحديثة، على سبيل المثال [16، 34، 12، 36، 22]. يمكن تصنيف العديد من الأساليب المختلفة بشكل عام إما إلى ضغط الشبكات المدربة مسبقاً أو تدريب شبكات صغيرة مباشرة. تقترح هذه الورقة فئة من معماريات الشبكات التي تتيح لمطور النماذج اختيار شبكة صغيرة بشكل محدد تتطابق مع قيود الموارد (زمن الاستجابة، الحجم) لتطبيقهم. تركز MobileNets بشكل أساسي على التحسين لزمن الاستجابة ولكنها تنتج أيضاً شبكات صغيرة. تركز العديد من الأوراق البحثية حول الشبكات الصغيرة على الحجم فقط ولكنها لا تأخذ السرعة في الاعتبار.

تُبنى MobileNets بشكل أساسي من التفافات قابلة للفصل حسب العمق التي قُدمت في البداية في [26] واستُخدمت لاحقاً في نماذج Inception [13] لتقليل الحساب في الطبقات القليلة الأولى. تبني الشبكات المسطحة Flattened networks [16] شبكة من التفافات محللة بالكامل وأظهرت إمكانات الشبكات المحللة بشكل كبير. بشكل مستقل عن هذه الورقة الحالية، قدمت شبكات Factorized Networks [34] التفافاً محللاً مشابهاً بالإضافة إلى استخدام الاتصالات الطوبولوجية. لاحقاً، أظهرت شبكة Xception [3] كيفية توسيع نطاق المرشحات القابلة للفصل حسب العمق للتفوق على شبكات Inception V3. شبكة صغيرة أخرى هي Squeezenet [12] التي تستخدم نهج عنق الزجاجة لتصميم شبكة صغيرة جداً. تشمل الشبكات الأخرى ذات الحساب المخفض شبكات التحويل المنظمة [28] وشبكات deep fried convnets [37].

نهج مختلف للحصول على شبكات صغيرة هو تقليص أو تحليل أو ضغط الشبكات المدربة مسبقاً. تم اقتراح الضغط القائم على التكميم الحاصل الضربي [36]، والتجزئة [2]، والتقليم، والتكميم المتجه، وترميز هافمان [5] في الأدبيات. بالإضافة إلى ذلك، تم اقتراح تحليلات مختلفة لتسريع الشبكات المدربة مسبقاً [14، 20]. طريقة أخرى لتدريب الشبكات الصغيرة هي التقطير [9] التي تستخدم شبكة أكبر لتعليم شبكة أصغر. إنها مكملة لنهجنا ويتم تناولها في بعض حالات الاستخدام الخاصة بنا في القسم 4. نهج ناشئ آخر هو الشبكات منخفضة البت [4، 22، 11].

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** depthwise separable convolutions (التفافات قابلة للفصل حسب العمق), distillation (التقطير), product quantization (التكميم الحاصل الضربي), pruning (التقليم), vector quantization (التكميم المتجه), Huffman coding (ترميز هافمان), low bit networks (الشبكات منخفضة البت)
- **Equations:** 0
- **Citations:** [16], [34], [12], [36], [22], [26], [13], [3], [28], [37], [2], [5], [14], [20], [9], [4], [11]
- **Special handling:** Kept network names (Inception, Flattened networks, Factorized Networks, Xception, Squeezenet, deep fried convnets) as they appear in English as they are proper names

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
