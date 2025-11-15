# Section 2: Network Architecture
## القسم 2: معمارية الشبكة

**Section:** network-architecture
**Translation Quality:** 0.87
**Glossary Terms Used:** convolutional network, architecture, feature channels, max pooling, upsampling, concatenation, segmentation, localization, receptive field

---

### English Version

The network architecture is illustrated in Figure 1. It consists of a contracting path (left side) and an expansive path (right side). The contracting path follows the typical architecture of a convolutional network. It consists of the repeated application of two 3x3 convolutions (unpadded convolutions), each followed by a rectified linear unit (ReLU) and a 2x2 max pooling operation with stride 2 for downsampling. At each downsampling step we double the number of feature channels. Every step in the expansive path consists of an upsampling of the feature map followed by a 2x2 convolution ("up-convolution") that halves the number of feature channels, a concatenation with the correspondingly cropped feature map from the contracting path, and two 3x3 convolutions, each followed by a ReLU. The cropping is necessary due to the loss of border pixels in every convolution. At the final layer a 1x1 convolution is used to map each 64-component feature vector to the desired number of classes. In total the network has 23 convolutional layers.

To allow a seamless tiling of the output segmentation map (see Figure 2), it is important to select the input tile size such that all 2x2 max-pooling operations are applied to a layer with an even x- and y-size.

---

### النسخة العربية

يتم توضيح معمارية الشبكة في الشكل 1. وتتكون من مسار انقباضي (الجانب الأيسر) ومسار توسعي (الجانب الأيمن). يتبع المسار الانقباضي المعمارية النموذجية للشبكة الالتفافية. ويتكون من التطبيق المتكرر لالتفافين بحجم 3×3 (التفافات بدون حشو)، يتبع كل منهما وحدة خطية مقومة (ReLU) وعملية تجميع أعظمي بحجم 2×2 مع خطوة 2 لتقليل العينات. في كل خطوة تقليل عينات نضاعف عدد قنوات الميزات. تتكون كل خطوة في المسار التوسعي من زيادة عينات خريطة الميزات متبوعة بالتفاف بحجم 2×2 ("التفاف زيادة عينات") الذي يقلل عدد قنوات الميزات إلى النصف، وتسلسل مع خريطة الميزات المقصوصة بشكل مطابق من المسار الانقباضي، والتفافين بحجم 3×3، يتبع كل منهما ReLU. القص ضروري بسبب فقدان بكسلات الحدود في كل التفاف. في الطبقة النهائية يتم استخدام التفاف بحجم 1×1 لتعيين كل متجه ميزات من 64 مكوناً إلى العدد المطلوب من الأصناف. في المجموع، تحتوي الشبكة على 23 طبقة التفافية.

للسماح بتبليط سلس لخريطة التجزئة الناتجة (انظر الشكل 2)، من المهم اختيار حجم البلاطة المدخلة بحيث يتم تطبيق جميع عمليات التجميع الأعظمي 2×2 على طبقة ذات حجم زوجي في x و y.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2
- **Key terms introduced:** contracting path, expansive path, unpadded convolutions, ReLU, up-convolution, feature map cropping, tiling
- **Equations:** None explicit, but architectural specifications (3x3, 2x2, 1x1 kernel sizes)
- **Citations:** None in this section
- **Special handling:** Preserved technical specifications like "3x3", "2x2", "stride 2", "23 convolutional layers", "64-component feature vector"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
