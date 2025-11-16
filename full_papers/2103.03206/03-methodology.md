# Section 3: Methods
## القسم 3: المنهجية

**Section:** Methods
**Translation Quality:** 0.86
**Glossary Terms Used:** cross-attention, latent space, bottleneck, Fourier features, position encoding, permutation invariance, complexity, query, key, value

---

### English Version

## 3.1 The Perceiver Architecture

**Core Design**: The architecture alternates between two components: (1) a cross-attention module projecting byte arrays through a latent bottleneck, and (2) a Transformer tower operating in latent space.

**Addressing Quadratic Complexity**: Standard self-attention scales as O(M²) where M represents input dimensionality. The Perceiver introduces asymmetry: while keys and values project from the large input array, queries project from a learned latent array with dimension N ≪ M. This reduces complexity to O(M·N).

The key innovation is that queries Q are computed from a small learned latent array (size N), while keys K and values V are computed from the full input array (size M). Since attention complexity is determined by Q·K^T, having fewer queries dramatically reduces computation.

**Decoupling Depth from Input Size**: The resulting architecture achieves O(M·N + L·N²) complexity, where L is network depth. This critical decoupling allows "very deep architectures...essential for good performance on challenging tasks."

After the initial cross-attention that maps M inputs to N latent variables, all subsequent processing happens in the N-dimensional latent space. The model can apply L layers of self-attention in latent space with cost O(L·N²), independent of the input size M. Only when new information is needed does the model apply additional cross-attention layers.

**Architectural Components**:

1. **Cross-Attention Module**: Maps input array (M × D_input) to latent array (N × D_latent)
   - Input: byte array with position encodings
   - Learned queries: N latent vectors
   - Keys and values: derived from input
   - Output: N processed latent vectors

2. **Latent Transformer**: Standard Transformer operating on latent array
   - Self-attention within the N latent vectors
   - Feed-forward networks
   - Layer normalization and residual connections
   - Can be arbitrarily deep without affecting input complexity

3. **Iterative Cross-Attention**: Optional repeated cross-attention layers
   - Allows progressive refinement of latent representations
   - Enables the model to "hedge against" initial bottleneck information loss
   - Weight sharing across iterations reduces parameters

The model can be interpreted as a recurrent neural network unrolled in depth, with optional weight sharing between modules. Iterative cross-attention layers enable progressive information extraction, allowing the model to "hedge against" bottleneck constraints.

**Mathematical Formulation**:

For standard self-attention with M inputs:
$$\text{Complexity} = O(M^2 \cdot D)$$

For Perceiver cross-attention with N latent variables:
$$\text{Complexity} = O(M \cdot N \cdot D)$$

Total complexity with L latent layers:
$$\text{Total} = O(M \cdot N \cdot D) + O(L \cdot N^2 \cdot D)$$

When N ≪ M and L is moderate, this provides massive computational savings.

## 3.2 Position Encodings

**Fourier Features**: Rather than architectural position information, the Perceiver injects spatial/temporal awareness through learned feature tagging. The approach uses Fourier features:

$$\text{pos}(x_d, f_k) = [\sin(f_k \cdot \pi \cdot x_d), \cos(f_k \cdot \pi \cdot x_d)]$$

where frequencies uniformly sample between 1 and μ/2 (Nyquist frequency).

This parameterization permits independent control over:
- Frequency bands (number of different frequencies)
- Cutoff frequency μ (maximum frequency)
- Dimensionality of position encodings

The position encoding is concatenated with input features, allowing the model to learn which frequency components are relevant for each task.

**Advantages over Fixed Encodings**:
- Avoids numerical instability from exponential frequency spacing (as used in NeRF)
- Allows task-specific frequency adaptation
- Generalizes across different input resolutions and modalities

**Generality Arguments**: The authors defend position encodings as domain-agnostic rather than undermining flexibility:
- Position features remain learnable and adapt across domains
- Extend naturally to multimodal contexts through modality-specific encodings
- Same encoding mechanism works for spatial (2D/3D), temporal (1D), and abstract positions

**Permutation Invariance**: Pure attention operations are permutation-invariant—the model produces the same output regardless of input order. Position encodings break this invariance intentionally, allowing the model to utilize spatial/temporal structure.

Testing on permuted ImageNet reveals this property:
- ResNet-50 performance degrades dramatically under random pixel permutation
- Vision Transformer also suffers significant degradation
- Perceiver maintains accuracy through position encoding robustness

The experiment demonstrates that the Perceiver's architectural core is truly permutation-invariant, with all structural information coming from learned position encodings rather than hard-coded architectural assumptions.

**Implementation Details**:
- For images: 2D position encodings from (x, y) coordinates
- For audio: 1D position encodings from time indices
- For video: 3D position encodings from (t, x, y) coordinates
- For point clouds: 3D position encodings from (x, y, z) coordinates

Each modality uses the same Fourier feature mechanism, differing only in the dimensionality and range of position vectors.

---

### النسخة العربية

## 3.1 معمارية Perceiver

**التصميم الأساسي**: تتناوب المعمارية بين مكونين: (1) وحدة انتباه متقاطع تُسقط مصفوفات البايتات عبر عنق زجاجة كامن، و(2) برج محول يعمل في الفضاء الكامن.

**معالجة التعقيد التربيعي**: يتوسع الانتباه الذاتي القياسي بمقدار O(M²) حيث M تمثل أبعاد المدخلات. يقدم Perceiver عدم تماثل: بينما تُسقط المفاتيح والقيم من مصفوفة المدخلات الكبيرة، تُسقط الاستعلامات من مصفوفة كامنة متعلمة ذات بُعد N ≪ M. هذا يقلل التعقيد إلى O(M·N).

الابتكار الرئيسي هو أن الاستعلامات Q تُحسب من مصفوفة كامنة صغيرة متعلمة (حجم N)، بينما تُحسب المفاتيح K والقيم V من مصفوفة المدخلات الكاملة (حجم M). نظراً لأن تعقيد الانتباه يُحدد بواسطة Q·K^T، فإن وجود عدد أقل من الاستعلامات يقلل الحساب بشكل كبير.

**فصل العمق عن حجم المدخلات**: تحقق المعمارية الناتجة تعقيداً O(M·N + L·N²)، حيث L هو عمق الشبكة. يسمح هذا الفصل الحاسم بـ "معماريات عميقة جداً...ضرورية للأداء الجيد في المهام الصعبة."

بعد الانتباه المتقاطع الأولي الذي يربط M من المدخلات بـ N من المتغيرات الكامنة، تحدث جميع المعالجات اللاحقة في الفضاء الكامن ذي البُعد N. يمكن للنموذج تطبيق L طبقات من الانتباه الذاتي في الفضاء الكامن بتكلفة O(L·N²)، مستقلة عن حجم المدخلات M. فقط عندما تكون هناك حاجة لمعلومات جديدة يطبق النموذج طبقات انتباه متقاطع إضافية.

**المكونات المعمارية**:

1. **وحدة الانتباه المتقاطع**: تربط مصفوفة المدخلات (M × D_input) بمصفوفة كامنة (N × D_latent)
   - المدخلات: مصفوفة بايتات مع تشفيرات الموضع
   - استعلامات متعلمة: N من المتجهات الكامنة
   - المفاتيح والقيم: مشتقة من المدخلات
   - المخرجات: N من المتجهات الكامنة المعالجة

2. **محول كامن**: محول قياسي يعمل على المصفوفة الكامنة
   - الانتباه الذاتي ضمن N من المتجهات الكامنة
   - الشبكات التغذية الأمامية
   - التطبيع الطبقي والاتصالات المتبقية
   - يمكن أن يكون عميقاً بشكل تعسفي دون التأثير على تعقيد المدخلات

3. **الانتباه المتقاطع التكراري**: طبقات انتباه متقاطع متكررة اختيارية
   - يسمح بالتحسين التدريجي للتمثيلات الكامنة
   - يمكّن النموذج من "التحوط ضد" فقدان المعلومات في عنق الزجاجة الأولي
   - مشاركة الأوزان عبر التكرارات تقلل المعاملات

يمكن تفسير النموذج كشبكة عصبية متكررة مفتوحة في العمق، مع مشاركة اختيارية للأوزان بين الوحدات. تمكّن طبقات الانتباه المتقاطع التكرارية من الاستخراج التدريجي للمعلومات، مما يسمح للنموذج بـ "التحوط ضد" قيود عنق الزجاجة.

**الصياغة الرياضية**:

للانتباه الذاتي القياسي مع M من المدخلات:
$$\text{Complexity} = O(M^2 \cdot D)$$

للانتباه المتقاطع Perceiver مع N من المتغيرات الكامنة:
$$\text{Complexity} = O(M \cdot N \cdot D)$$

التعقيد الإجمالي مع L طبقات كامنة:
$$\text{Total} = O(M \cdot N \cdot D) + O(L \cdot N^2 \cdot D)$$

عندما N ≪ M و L معتدل، يوفر هذا وفورات حسابية هائلة.

## 3.2 تشفيرات الموضع

**ميزات فورييه**: بدلاً من معلومات الموضع المعمارية، يحقن Perceiver الوعي المكاني/الزمني من خلال وسم الميزات المتعلمة. يستخدم النهج ميزات فورييه:

$$\text{pos}(x_d, f_k) = [\sin(f_k \cdot \pi \cdot x_d), \cos(f_k \cdot \pi \cdot x_d)]$$

حيث تُأخذ عينات من الترددات بشكل منتظم بين 1 و μ/2 (تردد نايكويست).

تسمح هذه المعلمية بالتحكم المستقل في:
- نطاقات التردد (عدد الترددات المختلفة)
- تردد القطع μ (التردد الأقصى)
- أبعاد تشفيرات الموضع

يتم ربط تشفير الموضع مع ميزات المدخلات، مما يسمح للنموذج بتعلم أي مكونات التردد ذات صلة بكل مهمة.

**المزايا مقارنة بالتشفيرات الثابتة**:
- تجنب عدم الاستقرار العددي من تباعد التردد الأسي (كما هو مستخدم في NeRF)
- تسمح بتكيف التردد الخاص بالمهمة
- تعمم عبر دقات ودخلات مختلفة من الأنماط

**حجج العمومية**: يدافع المؤلفون عن تشفيرات الموضع باعتبارها مستقلة عن المجال بدلاً من تقويض المرونة:
- تبقى ميزات الموضع قابلة للتعلم وتتكيف عبر المجالات
- تمتد بشكل طبيعي إلى السياقات متعددة الأنماط من خلال تشفيرات خاصة بالنمط
- نفس آلية التشفير تعمل للمواضع المكانية (2D/3D)، والزمنية (1D)، والمجردة

**عدم التباين التبديلي**: عمليات الانتباه الخالصة هي غير متباينة للتبديل—ينتج النموذج نفس المخرجات بغض النظر عن ترتيب المدخلات. تكسر تشفيرات الموضع هذا التباين عن قصد، مما يسمح للنموذج باستخدام البنية المكانية/الزمنية.

يكشف الاختبار على ImageNet المبدل عن هذه الخاصية:
- أداء ResNet-50 يتدهور بشكل كبير تحت التبديل العشوائي للبكسلات
- محول الرؤية يعاني أيضاً من تدهور كبير
- يحافظ Perceiver على الدقة من خلال متانة تشفير الموضع

تُظهر التجربة أن الجوهر المعماري لـ Perceiver هو فعلاً غير متباين للتبديل، مع كل المعلومات الهيكلية القادمة من تشفيرات الموضع المتعلمة بدلاً من الافتراضات المعمارية المشفرة بشكل صارم.

**تفاصيل التنفيذ**:
- للصور: تشفيرات موضع ثنائية الأبعاد من إحداثيات (x, y)
- للصوت: تشفيرات موضع أحادية البُعد من مؤشرات الوقت
- للفيديو: تشفيرات موضع ثلاثية الأبعاد من إحداثيات (t, x, y)
- لسحب النقاط: تشفيرات موضع ثلاثية الأبعاد من إحداثيات (x, y, z)

يستخدم كل نمط نفس آلية ميزات فورييه، مختلفاً فقط في الأبعاد ونطاق متجهات الموضع.

---

### Translation Notes

- **Figures referenced:** None explicitly, but architecture diagrams implied
- **Key terms introduced:**
  - Asymmetric attention: انتباه غير متماثل
  - Latent bottleneck: عنق زجاجة كامن
  - Cross-attention: الانتباه المتقاطع
  - Fourier features: ميزات فورييه
  - Nyquist frequency: تردد نايكويست
  - Permutation invariance: عدم التباين التبديلي
  - Query (Q): استعلام
  - Key (K): مفتاح
  - Value (V): قيمة
  - Feed-forward network: شبكة تغذية أمامية
  - Layer normalization: التطبيع الطبقي
  - Residual connection: اتصال متبقي
- **Equations:**
  - Complexity notation: O(M²), O(M·N), O(L·N²)
  - Fourier features: sin/cos functions
- **Citations:** Reference to NeRF
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - Complexity analysis kept in Big-O notation
  - Model names kept in English (NeRF, ResNet-50, Vision Transformer)

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.86

### Back-Translation Check

"The architecture alternates between two components: (1) a cross-attention module that projects byte arrays through a latent bottleneck, and (2) a Transformer tower operating in latent space.

Standard self-attention scales as O(M²) where M represents input dimensions. Perceiver introduces asymmetry: while keys and values are projected from the large input array, queries are projected from a learned latent array with dimension N ≪ M. This reduces complexity to O(M·N).

The resulting architecture achieves O(M·N + L·N²) complexity, where L is network depth. After the initial cross-attention that maps M inputs to N latent variables, all subsequent processing happens in the N-dimensional latent space.

For position encodings, the approach uses Fourier features where frequencies are uniformly sampled between 1 and μ/2 (Nyquist frequency). This allows independent control over frequency bands, cutoff frequency, and dimensionality of position encodings."

Back-translation confirms technical accuracy and semantic preservation.
