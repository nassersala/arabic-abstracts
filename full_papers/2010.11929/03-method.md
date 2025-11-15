# Section 3: Method
## القسم 3: المنهجية

**Section:** method
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, architecture, encoder, self-attention, multi-head attention, embedding, patch, image classification, inductive bias, translation equivariance, residual connection, pre-training, fine-tuning, feature map, convolutional neural network

---

### English Version

In model design we follow the original Transformer (Vaswani et al., 2017) as closely as possible. An advantage of this intentionally simple setup is that scalable NLP Transformer architectures – and their efficient implementations – can be used almost out of the box.

#### 3.1 Vision Transformer (ViT)

An overview of the model is depicted in Figure 1. The standard Transformer receives as input a 1D sequence of token embeddings. To handle 2D images, we reshape the image **x** ∈ ℝ^(H×W×C) into a sequence of flattened 2D patches **x**_p ∈ ℝ^(N×(P²·C)), where (H,W) is the resolution of the original image, C is the number of channels, (P,P) is the resolution of each image patch, and N = HW/P² is the resulting number of patches, which also serves as the effective input sequence length for the Transformer. The Transformer uses constant latent vector size D through all of its layers, so we flatten the patches and map to D dimensions with a trainable linear projection (Eq. 1). We refer to the output of this projection as the patch embeddings.

Similar to BERT's [class] token, we prepend a learnable embedding to the sequence of embedded patches (**z**₀⁰ = **x**_class), whose state at the output of the Transformer encoder (**z**_L⁰) serves as the image representation **y** (Eq. 4). Both during pre-training and fine-tuning, a classification head is attached to **z**_L⁰. The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time.

Position embeddings are added to the patch embeddings to retain positional information. We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings (Appendix D.4). The resulting sequence of embedding vectors serves as input to the encoder.

The Transformer encoder (Vaswani et al., 2017) consists of alternating layers of multiheaded self-attention (MSA, see Appendix A) and MLP blocks (Eq. 2, 3). Layernorm (LN) is applied before every block, and residual connections after every block (Wang et al., 2019; Baevski & Auli, 2019). The MLP contains two layers with a GELU non-linearity.

**Equations:**

$$\mathbf{z}_0 = [\mathbf{x}_{class}; \mathbf{x}_p^1\mathbf{E}; \mathbf{x}_p^2\mathbf{E}; \cdots; \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{pos}$$
$$\mathbf{E} \in \mathbb{R}^{(P^2 \cdot C) \times D}, \mathbf{E}_{pos} \in \mathbb{R}^{(N+1) \times D}$$
(1)

$$\mathbf{z}'_\ell = \text{MSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \ell = 1 \ldots L$$
(2)

$$\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell, \quad \ell = 1 \ldots L$$
(3)

$$\mathbf{y} = \text{LN}(\mathbf{z}_L^0)$$
(4)

**Inductive bias.** We note that Vision Transformer has much less image-specific inductive bias than CNNs. In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer throughout the whole model. In ViT, only MLP layers are local and translationally equivariant, while the self-attention layers are global. The two-dimensional neighborhood structure is used very sparingly: in the beginning of the model by cutting the image into patches and at fine-tuning time for adjusting the position embeddings for images of different resolution (as described below). Other than that, the position embeddings at initialization time carry no information about the 2D positions of the patches and all spatial relations between the patches have to be learned from scratch.

**Hybrid Architecture.** As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (LeCun et al., 1989). In this hybrid model, the patch embedding projection **E** (Eq. 1) is applied to patches extracted from a CNN feature map. As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions of the feature map and projecting to the Transformer dimension. The classification input embedding and position embeddings are added as described above.

#### 3.2 Fine-tuning and Higher Resolution

Typically, we pre-train ViT on large datasets, and fine-tune to (smaller) downstream tasks. For this, we remove the pre-trained prediction head and attach a zero-initialized D×K feedforward layer, where K is the number of downstream classes. It is often beneficial to fine-tune at higher resolution than pre-training (Touvron et al., 2019; Kolesnikov et al., 2020). When feeding images of higher resolution, we keep the patch size the same, which results in a larger effective sequence length. The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful. We therefore perform 2D interpolation of the pre-trained position embeddings, according to their location in the original image. Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is manually injected into the Vision Transformer.

---

### النسخة العربية

في تصميم النموذج، نتبع المحول الأصلي (Vaswani et al., 2017) بأقرب قدر ممكن. تتمثل ميزة هذا الإعداد البسيط عمداً في أن معماريات المحولات لمعالجة اللغة الطبيعية القابلة للتوسع - وتطبيقاتها الفعالة - يمكن استخدامها تقريباً كما هي.

#### 3.1 محول الرؤية (ViT)

يُصوَّر نظرة عامة على النموذج في الشكل 1. يستقبل المحول القياسي كمدخل تسلسل أحادي البعد من تضمينات الرموز. للتعامل مع الصور ثنائية البعد، نعيد تشكيل الصورة **x** ∈ ℝ^(H×W×C) إلى تسلسل من الرقع ثنائية البعد المسطحة **x**_p ∈ ℝ^(N×(P²·C))، حيث (H,W) هي دقة الصورة الأصلية، وC هو عدد القنوات، و(P,P) هي دقة كل رقعة صورة، وN = HW/P² هو العدد الناتج من الرقع، والذي يعمل أيضاً كطول التسلسل الفعال للمدخل للمحول. يستخدم المحول حجم متجه كامن ثابت D عبر جميع طبقاته، لذا نقوم بتسطيح الرقع وتعيينها إلى أبعاد D باستخدام إسقاط خطي قابل للتدريب (المعادلة 1). نشير إلى مخرجات هذا الإسقاط باسم تضمينات الرقع.

على غرار رمز [class] في BERT، نُضيف تضميناً قابلاً للتعلم مسبقاً إلى تسلسل الرقع المضمنة (**z**₀⁰ = **x**_class)، التي تعمل حالتها عند مخرجات مشفر المحول (**z**_L⁰) كتمثيل للصورة **y** (المعادلة 4). خلال كل من التدريب المسبق والضبط الدقيق، يتم إرفاق رأس تصنيف بـ **z**_L⁰. يتم تنفيذ رأس التصنيف بواسطة شبكة متعددة الطبقات (MLP) بطبقة مخفية واحدة في وقت التدريب المسبق وبطبقة خطية واحدة في وقت الضبط الدقيق.

تُضاف تضمينات الموضع إلى تضمينات الرقع للحفاظ على المعلومات الموضعية. نستخدم تضمينات موضع أحادية البعد قياسية قابلة للتعلم، نظراً لأننا لم نلاحظ مكاسب أداء كبيرة من استخدام تضمينات موضع ثنائية البعد أكثر تقدماً (الملحق D.4). يعمل التسلسل الناتج من متجهات التضمين كمدخل للمشفر.

يتكون مشفر المحول (Vaswani et al., 2017) من طبقات متناوبة من الانتباه الذاتي متعدد الرؤوس (MSA، انظر الملحق A) وكتل الشبكة متعددة الطبقات (المعادلتان 2، 3). يُطبق التطبيع الطبقي (LN) قبل كل كتلة، والاتصالات المتبقية بعد كل كتلة (Wang et al., 2019; Baevski & Auli, 2019). تحتوي الشبكة متعددة الطبقات على طبقتين مع دالة لاخطية GELU.

**المعادلات:**

$$\mathbf{z}_0 = [\mathbf{x}_{class}; \mathbf{x}_p^1\mathbf{E}; \mathbf{x}_p^2\mathbf{E}; \cdots; \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{pos}$$
$$\mathbf{E} \in \mathbb{R}^{(P^2 \cdot C) \times D}, \mathbf{E}_{pos} \in \mathbb{R}^{(N+1) \times D}$$
(1)

$$\mathbf{z}'_\ell = \text{MSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \ell = 1 \ldots L$$
(2)

$$\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell, \quad \ell = 1 \ldots L$$
(3)

$$\mathbf{y} = \text{LN}(\mathbf{z}_L^0)$$
(4)

**الانحياز الاستقرائي.** نلاحظ أن محول الرؤية لديه انحياز استقرائي خاص بالصور أقل بكثير من الشبكات العصبية الالتفافية. في الشبكات العصبية الالتفافية، تكون المحلية وبنية الحي ثنائي البعد وثبات الإزاحة مدمجة في كل طبقة في جميع أنحاء النموذج بأكمله. في ViT، فقط طبقات الشبكة متعددة الطبقات محلية وثابتة الإزاحة، بينما طبقات الانتباه الذاتي عامة. تُستخدم بنية الحي ثنائي البعد بشكل محدود للغاية: في بداية النموذج عن طريق تقطيع الصورة إلى رقع وفي وقت الضبط الدقيق لضبط تضمينات الموضع للصور ذات الدقة المختلفة (كما هو موضح أدناه). بخلاف ذلك، لا تحمل تضمينات الموضع في وقت التهيئة أي معلومات حول المواضع ثنائية البعد للرقع ويجب تعلم جميع العلاقات المكانية بين الرقع من الصفر.

**المعمارية الهجينة.** كبديل لرقع الصور الخام، يمكن تشكيل تسلسل المدخلات من خرائط الخصائص للشبكة العصبية الالتفافية (LeCun et al., 1989). في هذا النموذج الهجين، يُطبق إسقاط تضمين الرقع **E** (المعادلة 1) على الرقع المستخرجة من خريطة خصائص الشبكة العصبية الالتفافية. كحالة خاصة، يمكن أن يكون للرقع حجم مكاني 1×1، مما يعني أن تسلسل المدخلات يُحصل عليه ببساطة عن طريق تسطيح الأبعاد المكانية لخريطة الخصائص والإسقاط إلى بُعد المحول. تُضاف تضمينات مدخل التصنيف وتضمينات الموضع كما هو موضح أعلاه.

#### 3.2 الضبط الدقيق والدقة الأعلى

عادة، نقوم بالتدريب المسبق لـ ViT على مجموعات بيانات كبيرة، ثم الضبط الدقيق لمهام لاحقة (أصغر). لهذا، نزيل رأس التنبؤ المدرب مسبقاً ونرفق طبقة أمامية D×K مهيأة بالصفر، حيث K هو عدد الفئات اللاحقة. غالباً ما يكون من المفيد الضبط الدقيق بدقة أعلى من التدريب المسبق (Touvron et al., 2019; Kolesnikov et al., 2020). عند إدخال صور بدقة أعلى، نحافظ على حجم الرقعة نفسه، مما ينتج عنه طول تسلسل فعال أكبر. يمكن لمحول الرؤية التعامل مع أطوال تسلسل تعسفية (حتى قيود الذاكرة)، ومع ذلك، قد لا تعود تضمينات الموضع المدربة مسبقاً ذات معنى. لذلك نقوم بإجراء استيفاء ثنائي البعد لتضمينات الموضع المدربة مسبقاً، وفقاً لموقعها في الصورة الأصلية. لاحظ أن تعديل الدقة واستخراج الرقع هذا هما النقطتان الوحيدتان اللتان يُحقن فيهما يدوياً انحياز استقرائي حول البنية ثنائية البعد للصور في محول الرؤية.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** patch embeddings (تضمينات الرقع), latent vector (متجه كامن), classification head (رأس تصنيف), layernorm (التطبيع الطبقي), residual connections (الاتصالات المتبقية), GELU non-linearity (دالة لاخطية GELU), 2D interpolation (استيفاء ثنائي البعد)
- **Equations:** 4 major equations with mathematical notation
- **Citations:** 6 references cited
- **Special handling:** All mathematical equations preserved in LaTeX format, technical terminology carefully translated while maintaining precision

### Back-Translation (Key Technical Paragraph)

**Inductive bias paragraph back-translation:**
"We note that Vision Transformer has much less image-specific inductive bias than CNNs. In CNNs, locality, two-dimensional neighborhood structure, and translation invariance are integrated into each layer throughout the entire model. In ViT, only MLP layers are local and translation-invariant, while self-attention layers are global. The two-dimensional neighborhood structure is used very sparingly: at the beginning of the model by cutting the image into patches and at fine-tuning time to adjust position embeddings for images of different resolutions (as explained below). Other than that, position embeddings at initialization time carry no information about the 2D positions of the patches and all spatial relationships between patches must be learned from scratch."

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.88
