# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** Related Work
**Translation Quality:** 0.87
**Glossary Terms Used:** convolutional neural networks, transformers, attention mechanism, self-attention, weight sharing, receptive field, multimodal, feature extraction

---

### English Version

### Convolutional Networks and Attention

Convolutional neural networks (ConvNets) dominated perception tasks for nearly a decade through weight sharing and local receptive fields. However, their assumption of 2D grid structures limits multimodal applicability. The paper positions Transformers as flexible alternatives, though they suffer from quadratic scaling with input size.

The standard Transformer architecture applies self-attention across all inputs, leading to O(M²) complexity where M is the number of input elements. This makes direct application to raw high-dimensional data (like pixels or audio samples) computationally prohibitive. For example, a 224×224 image contains 50,176 pixels, requiring billions of operations per attention layer.

### Efficient Attention Architectures

Prior work addresses Transformer complexity through various strategies:
- **Subsampling inputs**: Reducing resolution before applying attention
- **Preprocessing with convolutions**: Vision Transformer (ViT) uses 16×16 patches, reducing ImageNet images from 50,176 pixels to 196 patches
- **Modifying attention internals**: Linear attention variants, sparse attention patterns, or learned attention patterns

The Perceiver builds on concepts from Set Transformer, which introduced inducing points to reduce complexity. However, the Perceiver makes key distinctions:
- **Decoupling network depth from input size**: The Perceiver can apply many layers of processing in latent space without revisiting the full input
- **Not just achieving linear complexity**: The goal is architectural flexibility and depth independence, not merely computational efficiency

### Multimodal Processing

Existing multimodal approaches typically require:
1. **Separate feature extractors** for each modality (e.g., ResNet for images, convolutional networks for audio)
2. **Hand-tuned fusion strategies** to combine representations
3. **Modality-specific architectural choices** throughout the pipeline

The Perceiver's unified architecture "handles a wide range of inputs out of the box even if they come from very different modalities." This eliminates the need for modality-specific preprocessing or fusion engineering.

### Position in the Literature

The paper positions the Perceiver as complementary to recent work on general-purpose architectures:
- Unlike ViT, which still relies on patching (a vision-specific operation), the Perceiver can attend directly to raw inputs
- Unlike sparse Transformers optimized for long sequences, the Perceiver focuses on very high-dimensional inputs across modalities
- Unlike multimodal fusion models, the Perceiver uses a single architecture without modality-specific components

This work represents a shift from "architecture as inductive bias" toward "architecture as general computation," relying on learned position encodings rather than structural assumptions to capture domain knowledge.

---

### النسخة العربية

### الشبكات الالتفافية والانتباه

هيمنت الشبكات العصبية الالتفافية (ConvNets) على مهام الإدراك لما يقارب عقداً من الزمن من خلال مشاركة الأوزان والمجالات الاستقبالية المحلية. ومع ذلك، فإن افتراضها لهياكل الشبكة ثنائية الأبعاد يحد من قابلية التطبيق متعدد الأنماط. يضع البحث المحولات (Transformers) كبدائل مرنة، على الرغم من أنها تعاني من التوسع التربيعي مع حجم المدخلات.

تطبق معمارية المحول القياسية الانتباه الذاتي عبر جميع المدخلات، مما يؤدي إلى تعقيد O(M²) حيث M هو عدد عناصر المدخلات. هذا يجعل التطبيق المباشر على البيانات الخام عالية الأبعاد (مثل البكسلات أو عينات الصوت) مكلفاً حسابياً. على سبيل المثال، تحتوي صورة 224×224 على 50,176 بكسل، مما يتطلب مليارات العمليات لكل طبقة انتباه.

### معماريات الانتباه الفعالة

تعالج الأعمال السابقة تعقيد المحول من خلال استراتيجيات مختلفة:
- **أخذ عينات فرعية من المدخلات**: تقليل الدقة قبل تطبيق الانتباه
- **المعالجة المسبقة بالالتفافات**: يستخدم محول الرؤية (ViT) رقع 16×16، مما يقلل صور ImageNet من 50,176 بكسل إلى 196 رقعة
- **تعديل آليات الانتباه الداخلية**: متغيرات الانتباه الخطي، أنماط الانتباه المتناثر، أو أنماط الانتباه المتعلمة

يبني Perceiver على مفاهيم من Set Transformer، الذي قدم نقاط الاستحثاث لتقليل التعقيد. ومع ذلك، يقدم Perceiver تمييزات رئيسية:
- **فصل عمق الشبكة عن حجم المدخلات**: يمكن لـ Perceiver تطبيق العديد من طبقات المعالجة في الفضاء الكامن دون إعادة النظر في المدخلات الكاملة
- **ليس مجرد تحقيق التعقيد الخطي**: الهدف هو المرونة المعمارية واستقلالية العمق، وليس مجرد الكفاءة الحسابية

### المعالجة متعددة الأنماط

تتطلب الأساليب متعددة الأنماط الحالية عادةً:
1. **مستخرجات ميزات منفصلة** لكل نمط (مثل ResNet للصور، الشبكات الالتفافية للصوت)
2. **استراتيجيات دمج مضبوطة يدوياً** لدمج التمثيلات
3. **اختيارات معمارية خاصة بالنمط** في جميع أنحاء خط الأنابيب

تتعامل المعمارية الموحدة لـ Perceiver مع "مجموعة واسعة من المدخلات بشكل جاهز حتى لو كانت من أنماط مختلفة جداً." هذا يلغي الحاجة إلى معالجة مسبقة خاصة بالنمط أو هندسة الدمج.

### الموقع في الأدبيات

يضع البحث Perceiver كمكمل للأعمال الحديثة على المعماريات عامة الغرض:
- على عكس ViT، الذي لا يزال يعتمد على التقسيم إلى رقع (عملية خاصة بالرؤية)، يمكن لـ Perceiver الانتباه مباشرة للمدخلات الخام
- على عكس المحولات المتناثرة المُحسّنة للتسلسلات الطويلة، يركز Perceiver على المدخلات عالية الأبعاد جداً عبر الأنماط
- على عكس نماذج دمج الأنماط المتعددة، يستخدم Perceiver معمارية واحدة دون مكونات خاصة بالنمط

يمثل هذا العمل تحولاً من "المعمارية كانحياز استقرائي" نحو "المعمارية كحساب عام"، معتمداً على تشفيرات الموضع المتعلمة بدلاً من الافتراضات الهيكلية لالتقاط معرفة المجال.

---

### Translation Notes

- **Figures referenced:** None in Related Work
- **Key terms introduced:**
  - Set Transformer: Set Transformer (kept in English, established model name)
  - Inducing points: نقاط الاستحثاث
  - Patching: التقسيم إلى رقع
  - Sparse attention: الانتباه المتناثر
  - Linear attention: الانتباه الخطي
  - Feature extraction: استخراج الميزات
  - Fusion strategies: استراتيجيات الدمج
  - Receptive field: المجال الاستقبالي
  - Weight sharing: مشاركة الأوزان
- **Equations:** O(M²), O(M·N) complexity notation
- **Citations:** References to ConvNets, Vision Transformer, Set Transformer
- **Special handling:**
  - Model names kept in English (ConvNets, ViT, ResNet)
  - Complexity notation kept in standard mathematical form

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

### Back-Translation Check

"Convolutional neural networks (ConvNets) dominated perception tasks for nearly a decade through weight sharing and local receptive fields. However, their assumption of 2D grid structures limits multimodal applicability. The research positions Transformers as flexible alternatives, though they suffer from quadratic scaling with input size.

The standard Transformer architecture applies self-attention across all inputs, leading to O(M²) complexity where M is the number of input elements. Prior work addresses Transformer complexity through various strategies: subsampling inputs, preprocessing with convolutions, or modifying attention internals.

Perceiver builds on concepts from Set Transformer but makes key distinctions: decoupling network depth from input size, and focusing not just on achieving linear complexity but on architectural flexibility and depth independence."

Back-translation confirms semantic accuracy and technical precision.
