# Section 2: Network Architecture
## القسم 2: معمارية الشبكة

**Section:** network-architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** architecture, convolutional network, contracting path, expansive path, convolution, ReLU, max pooling, downsampling, feature channels, upsampling, concatenation, feature vector, layer

---

### English Version

The network architecture is illustrated in Figure 1. It consists of a contracting path (left side) and an expansive path (right side). The contracting path follows the typical architecture of a convolutional network. It consists of the repeated application of two 3x3 convolutions (unpadded convolutions), each followed by a rectified linear unit (ReLU) and a 2x2 max pooling operation with stride 2 for downsampling. At each downsampling step we double the number of feature channels. Every step in the expansive path consists of an upsampling of the feature map followed by a 2x2 convolution ("up-convolution") that halves the number of feature channels, a concatenation with the correspondingly cropped feature map from the contracting path, and two 3x3 convolutions, each followed by a ReLU. The cropping is necessary due to the loss of border pixels in every convolution. At the final layer a 1x1 convolution is used to map each 64-component feature vector to the desired number of classes. In total the network has 23 convolutional layers.

To allow a seamless tiling of the output segmentation map (see Figure 2), it is important to select the input tile size such that all 2x2 max-pooling operations are applied to a layer with an even x- and y-size.

---

### النسخة العربية

معمارية الشبكة موضحة في الشكل 1. تتكون من مسار انكماش (الجانب الأيسر) ومسار توسع (الجانب الأيمن). يتبع مسار الانكماش المعمارية النموذجية للشبكة الالتفافية. يتكون من التطبيق المتكرر لالتفافين بحجم 3×3 (التفافات غير مبطنة)، يتبع كل منهما وحدة خطية مصححة (ReLU) وعملية تجميع أعظمي بحجم 2×2 مع خطوة 2 لتقليل العينات. في كل خطوة تقليل عينات نضاعف عدد قنوات الميزات. تتكون كل خطوة في المسار التوسعي من زيادة تردد لخريطة الميزات متبوعة بالتفاف 2×2 ("التفاف صاعد") يُنصِّف عدد قنوات الميزات، وربط مع خريطة الميزات المقطوعة المقابلة من مسار الانكماش، والتفافين بحجم 3×3، يتبع كل منهما ReLU. القص ضروري بسبب فقدان بكسلات الحدود في كل التفاف. في الطبقة النهائية، يُستخدم التفاف 1×1 لتعيين كل متجه ميزات من 64 مكوناً إلى العدد المطلوب من الأصناف. في المجمل، تحتوي الشبكة على 23 طبقة التفافية.

للسماح بتبليط سلس لخريطة التجزئة الناتجة (انظر الشكل 2)، من المهم اختيار حجم البلاطة المدخلة بحيث يتم تطبيق جميع عمليات التجميع الأعظمي 2×2 على طبقة ذات حجم x وy زوجي.

---

### Translation Notes

- **Figures referenced:**
  - Figure 1: U-net architecture illustration (main architectural diagram)
  - Figure 2: Overlap-tile strategy
- **Key terms introduced:**
  - Contracting path (مسار انكماش)
  - Expansive path (مسار توسع)
  - Unpadded convolutions (التفافات غير مبطنة)
  - Rectified linear unit / ReLU (وحدة خطية مصححة)
  - Max pooling (التجميع الأعظمي)
  - Stride (خطوة)
  - Downsampling (تقليل العينات)
  - Feature channels (قنوات الميزات)
  - Upsampling (زيادة التردد)
  - Up-convolution (التفاف صاعد)
  - Concatenation (ربط)
  - Cropped feature map (خريطة الميزات المقطوعة)
  - Border pixels (بكسلات الحدود)
  - Feature vector (متجه ميزات)
  - Convolutional layers (طبقات التفافية)
  - Tiling (تبليط)
- **Equations:** None in this section
- **Citations:** None in this section
- **Special handling:**
  - Kept "ReLU" as abbreviation after first mention with Arabic translation
  - Preserved specific dimensions (3x3, 2x2, 1x1, 64-component)
  - Used Arabic mathematical symbols (×) instead of English (x) for dimensions
  - Maintained technical precision in describing layer operations

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check

First two sentences back-translation:
Arabic → English: "The network architecture is illustrated in Figure 1. It consists of a contracting path (left side) and an expansive path (right side)."
Original: "The network architecture is illustrated in Figure 1. It consists of a contracting path (left side) and an expansive path (right side)."
✓ Exact semantic match

Technical description back-translation:
Arabic → English: "The contracting path follows the typical architecture of a convolutional network. It consists of repeated application of two 3×3 convolutions (unpadded convolutions), each followed by a rectified linear unit (ReLU) and a 2×2 max pooling operation with stride 2 for downsampling."
✓ Semantically equivalent with high technical accuracy
