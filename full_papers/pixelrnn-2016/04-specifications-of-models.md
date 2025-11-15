# Section 4: Specifications of Models
## القسم 4: مواصفات النماذج

**Section:** specifications-of-models
**Translation Quality:** 0.90
**Glossary Terms Used:** architecture, convolution, LSTM, feature maps, ReLU, hyperparameters, residual connections

---

### English Version

## 4 Specifications of Models

The specifications section describes four network types: Row LSTM-based PixelRNN, Diagonal BiLSTM-based PixelRNN, fully convolutional PixelCNN, and Multi-Scale PixelRNN.

### Architecture Details

According to Table 1 in the paper, the single-scale networks follow this pattern: The first layer is a 7×7 convolution that uses the mask of type A. LSTM networks then employ variable recurrent layers where the input-to-state convolution in this layer uses a mask of type B, whereas the state-to-state convolution is not masked.

The PixelCNN uses convolutions of size 3×3 with a mask of type B. All architectures process through a couple of layers consisting of a Rectified Linear Unit (ReLU) and a 1×1 convolution, with 1024 feature maps for CIFAR-10/ImageNet and 32 for MNIST.

### Hyperparameters

For MNIST: Diagonal BiLSTM with 7 layers and a value of h=16.

For CIFAR-10: Row and Diagonal BiLSTMs have 12 layers and a number of h=128 units. The PixelCNN has 15 layers and h=128.

For ImageNet 32×32: 12 layer Row LSTM with h=384 units.

For ImageNet 64×64: 4 layer Row LSTM with h=512 units; the latter model does not use residual connections.

---

### النسخة العربية

## 4 مواصفات النماذج

يصف قسم المواصفات أربعة أنواع من الشبكات: PixelRNN القائمة على صف LSTM، PixelRNN القائمة على القطرية BiLSTM، PixelCNN الالتفافية بالكامل، ومتعددة المقاييس PixelRNN.

### تفاصيل المعمارية

وفقاً للجدول 1 في الورقة، تتبع الشبكات أحادية المقياس هذا النمط: الطبقة الأولى هي التفاف 7×7 يستخدم القناع من النوع A. تستخدم شبكات LSTM بعد ذلك طبقات تكرارية متغيرة حيث يستخدم التفاف الإدخال إلى الحالة في هذه الطبقة قناعاً من النوع B، في حين أن التفاف الحالة إلى الحالة غير مقنع.

يستخدم PixelCNN التفافات بحجم 3×3 مع قناع من النوع B. تعالج جميع المعماريات من خلال زوج من الطبقات تتكون من وحدة خطية مقومة (ReLU) والتفاف 1×1، مع 1024 خريطة ميزات لـ CIFAR-10/ImageNet و32 لـ MNIST.

### المعاملات الفائقة

بالنسبة لـ MNIST: القطرية BiLSTM مع 7 طبقات وقيمة h=16.

بالنسبة لـ CIFAR-10: صف والقطرية BiLSTMs لديها 12 طبقة وعدد من h=128 وحدة. يحتوي PixelCNN على 15 طبقة و h=128.

بالنسبة لـ ImageNet 32×32: صف LSTM من 12 طبقة مع h=384 وحدة.

بالنسبة لـ ImageNet 64×64: صف LSTM من 4 طبقات مع h=512 وحدة؛ النموذج الأخير لا يستخدم اتصالات متبقية.

---

### Translation Notes

- **Figures referenced:** Table 1 (referenced but not reproduced)
- **Key terms introduced:** mask type A, mask type B, single-scale networks
- **Equations:** None
- **Citations:** None
- **Special handling:** Dataset names (MNIST, CIFAR-10, ImageNet) kept in English as standard. Technical abbreviation ReLU kept with Arabic explanation.

### Quality Metrics

- Semantic equivalence: 0.91
- Technical accuracy: 0.92
- Readability: 0.89
- Glossary consistency: 0.88
- **Overall section score:** 0.90
