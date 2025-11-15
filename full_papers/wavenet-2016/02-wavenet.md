# Section 2: WaveNet
## القسم 2: WaveNet

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** autoregressive, convolutional neural network, dilated convolution, receptive field, gated activation units, residual connections, skip connections, softmax distribution, conditional generation, training

---

### English Version

## 2. WaveNet

In this section we describe the WaveNet architecture. We first present the basic building blocks of the model, and then discuss various architectural choices and training details.

### 2.1 Dilated Causal Convolutions

The main ingredient of WaveNet is the causal convolution. By using causal convolutions, we make sure the model cannot violate the ordering in which we model the data: the prediction $p(x_t | x_1, \ldots, x_{t-1})$ at time $t$ cannot depend on any of the future timesteps $x_{t+1}, x_{t+2}, \ldots$

At training time, the conditional predictions for all timesteps can be made in parallel because all timesteps of ground truth $x$ are known. When generating audio with the model, the predictions are sequential: after each sample is predicted, it is fed back into the network to predict the next sample.

Because audio signals have a very high temporal resolution (typically 16,000 samples per second), we need a very large receptive field to capture long-range dependencies. A simple solution would be to increase the number of layers or use larger filters, but this is computationally expensive and makes training difficult.

To address this, we use **dilated convolutions** (also known as atrous convolutions), which have been previously used in various contexts. A dilated convolution is a convolution where the filter is applied over an area larger than its length by skipping input values with a certain step. This is equivalent to a regular convolution with a filter that has been dilated by inserting zeros between the filter values, but is more efficient. The dilation factor $d$ controls the spacing between the filter elements.

More formally, for a 1-D sequence input $\mathbf{x}$ and a filter $f: \{0, \ldots, k-1\} \to \mathbb{R}$, the dilated convolution operation $\ast$ is defined as:

$$(\mathbf{x} \ast f)(t) = \sum_{i=0}^{k-1} f(i) \cdot x_{t-d \cdot i}$$

where $d$ is the dilation factor, $k$ is the filter size, and $t-d \cdot i$ accounts for the direction of the past. When $d = 1$, a dilated convolution reduces to a regular convolution.

Figure 1 illustrates this. Using dilated convolutions, the receptive field grows exponentially with depth. For example, with a filter size of 2 and dilation factors of 1, 2, 4, ..., $2^{n}$, the receptive field size is $2^{n+1}$. In our models, we stack multiple layers with exponentially increasing dilation factors. We repeat this stack multiple times to further increase the receptive field size.

### 2.2 Softmax Distributions

One approach to modeling the conditional distribution $p(x_t | x_1, \ldots, x_{t-1})$ would be to use a mixture model such as a mixture of Gaussians. However, van den Oord et al. (2016a) showed that a softmax distribution tends to work better, even when the data is implicitly continuous (such as image pixel values or audio sample values).

We thus apply a softmax over a finite set of values. For raw audio, this is challenging because audio samples are typically stored as 16-bit integer values, which means there are 65,536 possible values per timestep. To make this tractable, we first apply a μ-law companding transformation:

$$f(x_t) = \text{sign}(x_t) \frac{\ln(1 + \mu |x_t|)}{\ln(1 + \mu)}$$

where $-1 < x_t < 1$ and $\mu = 255$. We then quantize the resulting values to 256 possible values. This non-linear quantization produces a significantly better reconstruction than a simple linear quantization scheme, and is commonly used in digital audio processing.

The softmax distribution then models:

$$p(x_t | \mathbf{x}_{<t}) = \text{softmax}(h_{t,i})$$

where $h_t$ is the output of the network at timestep $t$, and $i$ indexes the 256 quantization levels. The model is trained to minimize the cross-entropy loss between the predicted distribution and the one-hot encoding of the actual quantized sample value.

### 2.3 Gated Activation Units

We use the same gated activation unit as used in PixelCNN (van den Oord et al., 2016b):

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x}) \odot \sigma(W_{g,k} \ast \mathbf{x})$$

where $\ast$ denotes a convolution operator, $\odot$ denotes element-wise multiplication, $\sigma(\cdot)$ is the sigmoid function, $k$ is the layer index, and $f$ and $g$ denote filter and gate, respectively. $W$ are learnable convolution filters.

We found that this non-linearity worked significantly better than the rectified linear activation function (ReLU) in our experiments. This gated activation is a form of learned feature interaction where the network can learn which parts of the input to emphasize or suppress.

### 2.4 Residual and Skip Connections

Both residual connections and parameterized skip connections are used throughout the network.

**Residual connections** (He et al., 2015) help the gradient flow through the network and allow training of much deeper models. For each layer, the input is added to the output:

$$\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{z}_k$$

where $\mathbf{z}_k$ is the output of the gated activation unit for layer $k$.

**Skip connections** gather information from all layers and sum them before applying the final softmax. This allows the network to use information from different temporal resolutions:

$$\sum_{k=1}^{N} \mathbf{skip}_k \to \text{ReLU} \to \text{1x1 conv} \to \text{ReLU} \to \text{1x1 conv} \to \text{softmax}$$

where each $\mathbf{skip}_k$ is the output of a 1×1 convolution applied to the gated activation output of layer $k$, and $N$ is the total number of layers.

The use of both residual and skip connections is illustrated in Figure 2. These connections are crucial for training very deep WaveNet models (we used up to 30 layers in our experiments).

### 2.5 Conditional WaveNets

Given an additional input $\mathbf{h}$ (e.g., a linguistic feature sequence for text-to-speech, or a speaker embedding for multi-speaker modeling), we can condition the predictions on this input. There are two types of conditioning:

**Global conditioning**: A single latent representation $\mathbf{h}$ conditions the entire output sequence. This is useful when the conditioning information is constant across time (e.g., speaker identity). The activation function becomes:

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x} + V_{f,k}^T \mathbf{h}) \odot \sigma(W_{g,k} \ast \mathbf{x} + V_{g,k}^T \mathbf{h})$$

where $V_{*,k}$ is a learnable linear projection.

**Local conditioning**: A time-series $\mathbf{h}_t$ conditions each timestep differently. This is used when the conditioning varies over time (e.g., linguistic features in TTS). If the time resolution of $\mathbf{h}$ is lower than that of the audio signal, we first upsample it using transposed convolutions (learned upsampling) to match the audio resolution. The activation function becomes:

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x} + V_{f,k} \ast \mathbf{h}) \odot \sigma(W_{g,k} \ast \mathbf{x} + V_{g,k} \ast \mathbf{h})$$

where $V_{*,k}$ now represents a 1×1 convolution.

### 2.6 Context Stacks

To further increase the receptive field while maintaining computational efficiency, we repeat the dilated convolution stack multiple times. For example, if we have a stack with dilation factors [1, 2, 4, ..., 512], we can repeat this stack 3 times to achieve a receptive field of more than 5000 timesteps (corresponding to over 300ms of audio at 16 kHz).

The full WaveNet architecture consists of:
- Causal convolutional input layer
- Multiple context stacks of dilated convolutions with gated activations
- Residual connections within each layer
- Skip connections from each layer to the output
- Two 1×1 convolutional layers with ReLU activation
- Final softmax layer over 256 classes

This architecture allows WaveNet to:
1. Model very long-range dependencies (thousands of timesteps)
2. Train efficiently in parallel during training
3. Generate high-quality audio sample by sample during inference
4. Condition on external information (text, speaker ID, etc.)

---

### النسخة العربية

## 2. WaveNet

في هذا القسم نصف معمارية WaveNet. نقدم أولاً الوحدات البنائية الأساسية للنموذج، ثم نناقش خيارات معمارية مختلفة وتفاصيل التدريب.

### 2.1 الالتفافات السببية الموسعة

المكون الرئيسي لـ WaveNet هو الالتفاف السببي. باستخدام الالتفافات السببية، نتأكد من أن النموذج لا يمكنه انتهاك الترتيب الذي ننمذج به البيانات: التنبؤ $p(x_t | x_1, \ldots, x_{t-1})$ في الوقت $t$ لا يمكن أن يعتمد على أي من الخطوات الزمنية المستقبلية $x_{t+1}, x_{t+2}, \ldots$

في وقت التدريب، يمكن إجراء التنبؤات الشرطية لجميع الخطوات الزمنية بشكل متوازٍ لأن جميع الخطوات الزمنية للحقيقة الأرضية $x$ معروفة. عند توليد الصوت باستخدام النموذج، تكون التنبؤات تسلسلية: بعد التنبؤ بكل عينة، يتم إرجاعها إلى الشبكة للتنبؤ بالعينة التالية.

نظراً لأن الإشارات الصوتية لها دقة زمنية عالية جداً (عادةً 16,000 عينة في الثانية)، نحتاج إلى مجال استقبال كبير جداً لالتقاط التبعيات طويلة المدى. الحل البسيط هو زيادة عدد الطبقات أو استخدام مرشحات أكبر، لكن هذا مكلف حسابياً ويجعل التدريب صعباً.

لمعالجة هذا، نستخدم **الالتفافات الموسعة** (المعروفة أيضاً بالالتفافات المثقوبة)، والتي تم استخدامها سابقاً في سياقات مختلفة. الالتفاف الموسع هو التفاف حيث يتم تطبيق المرشح على منطقة أكبر من طوله عن طريق تخطي قيم المدخلات بخطوة معينة. هذا يعادل التفافاً منتظماً مع مرشح تم توسيعه عن طريق إدراج أصفار بين قيم المرشح، لكنه أكثر كفاءة. يتحكم عامل التوسيع $d$ في التباعد بين عناصر المرشح.

بشكل أكثر رسمية، لتسلسل مدخلات أحادي الأبعاد $\mathbf{x}$ ومرشح $f: \{0, \ldots, k-1\} \to \mathbb{R}$، يتم تعريف عملية الالتفاف الموسع $\ast$ على النحو التالي:

$$(\mathbf{x} \ast f)(t) = \sum_{i=0}^{k-1} f(i) \cdot x_{t-d \cdot i}$$

حيث $d$ هو عامل التوسيع، و $k$ هو حجم المرشح، و $t-d \cdot i$ يأخذ في الاعتبار اتجاه الماضي. عندما $d = 1$، يتحول الالتفاف الموسع إلى التفاف منتظم.

يوضح الشكل 1 هذا. باستخدام الالتفافات الموسعة، ينمو مجال الاستقبال بشكل أسي مع العمق. على سبيل المثال، مع حجم مرشح 2 وعوامل توسيع 1، 2، 4، ...، $2^{n}$، يكون حجم مجال الاستقبال $2^{n+1}$. في نماذجنا، نكدس طبقات متعددة بعوامل توسيع تزداد بشكل أسي. نكرر هذه المكدس عدة مرات لزيادة حجم مجال الاستقبال بشكل أكبر.

### 2.2 توزيعات Softmax

أحد الطرق لنمذجة التوزيع الشرطي $p(x_t | x_1, \ldots, x_{t-1})$ هو استخدام نموذج مزيج مثل مزيج من التوزيعات الغاوسية. ومع ذلك، أظهر van den Oord et al. (2016a) أن توزيع softmax يميل إلى العمل بشكل أفضل، حتى عندما تكون البيانات مستمرة ضمنياً (مثل قيم بكسلات الصور أو قيم عينات الصوت).

لذلك نطبق softmax على مجموعة منتهية من القيم. بالنسبة للصوت الخام، هذا يمثل تحدياً لأن عينات الصوت عادةً ما يتم تخزينها كقيم صحيحة 16 بت، مما يعني أن هناك 65,536 قيمة محتملة لكل خطوة زمنية. لجعل هذا قابلاً للمعالجة، نطبق أولاً تحويل ضغط μ-law:

$$f(x_t) = \text{sign}(x_t) \frac{\ln(1 + \mu |x_t|)}{\ln(1 + \mu)}$$

حيث $-1 < x_t < 1$ و $\mu = 255$. ثم نقوم بتكميم القيم الناتجة إلى 256 قيمة محتملة. ينتج هذا التكميم غير الخطي إعادة بناء أفضل بكثير من مخطط التكميم الخطي البسيط، ويُستخدم بشكل شائع في معالجة الصوت الرقمي.

يقوم توزيع softmax بعد ذلك بنمذجة:

$$p(x_t | \mathbf{x}_{<t}) = \text{softmax}(h_{t,i})$$

حيث $h_t$ هو مخرجات الشبكة عند الخطوة الزمنية $t$، و $i$ يشير إلى مستويات التكميم البالغة 256. يتم تدريب النموذج لتقليل خسارة الإنتروبيا المتقاطعة بين التوزيع المتنبأ به والترميز أحادي الفئة لقيمة العينة المكممة الفعلية.

### 2.3 وحدات التنشيط البوابية

نستخدم نفس وحدة التنشيط البوابية المستخدمة في PixelCNN (van den Oord et al., 2016b):

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x}) \odot \sigma(W_{g,k} \ast \mathbf{x})$$

حيث $\ast$ يشير إلى عملية الالتفاف، و $\odot$ يشير إلى الضرب العنصري، و $\sigma(\cdot)$ هي دالة السيجمويد، و $k$ هو رقم الطبقة، و $f$ و $g$ يشيران إلى المرشح والبوابة، على التوالي. $W$ هي مرشحات التفافية قابلة للتعلم.

وجدنا أن هذه اللاخطية عملت بشكل أفضل بكثير من دالة التنشيط الخطية المعدلة (ReLU) في تجاربنا. هذا التنشيط البوابي هو شكل من أشكال التفاعل المكتسب للميزات حيث يمكن للشبكة أن تتعلم أي أجزاء من المدخلات يجب التأكيد عليها أو قمعها.

### 2.4 الاتصالات المتبقية واتصالات التخطي

يتم استخدام كل من الاتصالات المتبقية واتصالات التخطي المحددة بمعاملات في جميع أنحاء الشبكة.

**الاتصالات المتبقية** (He et al., 2015) تساعد في تدفق التدرج عبر الشبكة وتسمح بتدريب نماذج أعمق بكثير. لكل طبقة، يتم إضافة المدخل إلى المخرج:

$$\mathbf{x}_{k+1} = \mathbf{x}_k + \mathbf{z}_k$$

حيث $\mathbf{z}_k$ هو مخرجات وحدة التنشيط البوابية للطبقة $k$.

**اتصالات التخطي** تجمع المعلومات من جميع الطبقات وتجمعها قبل تطبيق softmax النهائي. هذا يسمح للشبكة باستخدام المعلومات من دقات زمنية مختلفة:

$$\sum_{k=1}^{N} \mathbf{skip}_k \to \text{ReLU} \to \text{1x1 conv} \to \text{ReLU} \to \text{1x1 conv} \to \text{softmax}$$

حيث كل $\mathbf{skip}_k$ هو مخرجات التفاف 1×1 المطبق على مخرجات التنشيط البوابي للطبقة $k$، و $N$ هو العدد الإجمالي للطبقات.

يتم توضيح استخدام كل من الاتصالات المتبقية واتصالات التخطي في الشكل 2. هذه الاتصالات حاسمة لتدريب نماذج WaveNet العميقة جداً (استخدمنا ما يصل إلى 30 طبقة في تجاربنا).

### 2.5 نماذج WaveNet الشرطية

في ظل وجود مدخل إضافي $\mathbf{h}$ (على سبيل المثال، تسلسل ميزات لغوية لتحويل النص إلى كلام، أو تضمين متحدث لنمذجة متعددة المتحدثين)، يمكننا تكييف التنبؤات على هذا المدخل. هناك نوعان من التكييف:

**التكييف العام**: تمثيل كامن واحد $\mathbf{h}$ يكيف تسلسل المخرجات بالكامل. هذا مفيد عندما تكون معلومات التكييف ثابتة عبر الزمن (على سبيل المثال، هوية المتحدث). تصبح دالة التنشيط:

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x} + V_{f,k}^T \mathbf{h}) \odot \sigma(W_{g,k} \ast \mathbf{x} + V_{g,k}^T \mathbf{h})$$

حيث $V_{*,k}$ هو إسقاط خطي قابل للتعلم.

**التكييف المحلي**: سلسلة زمنية $\mathbf{h}_t$ تكيف كل خطوة زمنية بشكل مختلف. يُستخدم هذا عندما يتغير التكييف عبر الزمن (على سبيل المثال، الميزات اللغوية في TTS). إذا كانت الدقة الزمنية لـ $\mathbf{h}$ أقل من دقة الإشارة الصوتية، نقوم أولاً بزيادة العينات باستخدام الالتفافات المنقولة (زيادة العينات المكتسبة) لمطابقة دقة الصوت. تصبح دالة التنشيط:

$$\mathbf{z} = \tanh(W_{f,k} \ast \mathbf{x} + V_{f,k} \ast \mathbf{h}) \odot \sigma(W_{g,k} \ast \mathbf{x} + V_{g,k} \ast \mathbf{h})$$

حيث $V_{*,k}$ الآن يمثل التفافاً 1×1.

### 2.6 مكدسات السياق

لزيادة مجال الاستقبال بشكل أكبر مع الحفاظ على الكفاءة الحسابية، نكرر مكدس الالتفاف الموسع عدة مرات. على سبيل المثال، إذا كان لدينا مكدس بعوامل توسيع [1، 2، 4، ...، 512]، يمكننا تكرار هذا المكدس 3 مرات لتحقيق مجال استقبال يزيد عن 5000 خطوة زمنية (أي ما يقابل أكثر من 300 ميلي ثانية من الصوت عند 16 كيلوهرتز).

تتكون معمارية WaveNet الكاملة من:
- طبقة مدخلات التفافية سببية
- مكدسات سياق متعددة من الالتفافات الموسعة مع تنشيطات بوابية
- اتصالات متبقية داخل كل طبقة
- اتصالات تخطي من كل طبقة إلى المخرج
- طبقتان التفافيتان 1×1 مع تنشيط ReLU
- طبقة softmax النهائية على 256 فئة

تسمح هذه المعمارية لـ WaveNet بما يلي:
1. نمذجة التبعيات طويلة المدى جداً (آلاف الخطوات الزمنية)
2. التدريب بكفاءة بالتوازي أثناء التدريب
3. توليد صوت عالي الجودة عينة تلو الأخرى أثناء الاستدلال
4. التكييف على معلومات خارجية (نص، معرف المتحدث، إلخ)

---

### Translation Notes

- **Figures referenced:** Figure 1 (dilated convolutions visualization), Figure 2 (residual and skip connections)
- **Key terms introduced:**
  - Causal convolution (الالتفاف السببي)
  - Dilated convolution (الالتفاف الموسع)
  - Atrous convolution (الالتفاف المثقوب) - alternative name
  - Receptive field (مجال الاستقبال)
  - μ-law companding (ضغط μ-law)
  - Gated activation units (وحدات التنشيط البوابية)
  - Residual connections (الاتصالات المتبقية)
  - Skip connections (اتصالات التخطي)
  - Global conditioning (التكييف العام)
  - Local conditioning (التكييف المحلي)
  - Transposed convolution (الالتفاف المنقول)
  - Context stacks (مكدسات السياق)
  - One-hot encoding (الترميز أحادي الفئة)

- **Equations:** 7 major equations
  - Dilated convolution formula
  - μ-law companding transformation
  - Softmax distribution
  - Gated activation function
  - Residual connection formula
  - Skip connection architecture
  - Global and local conditioning formulas

- **Citations:**
  - van den Oord et al. (2016a, 2016b) - PixelCNN and related work
  - He et al. (2015) - ResNet residual connections

- **Special handling:**
  - All mathematical notation preserved in LaTeX format
  - "Causal" translated as "سببي" (maintaining causality constraint)
  - "Dilated" as "موسع" (expanded/widened)
  - "Gated" as "بوابية" (gate-based)
  - "Skip connections" as "اتصالات التخطي" (bypass connections)
  - Technical parameters (256 levels, 16 kHz, etc.) preserved
  - "Context stacks" as "مكدسات السياق" (stacked layers with context)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.93
- Readability: 0.86
- Glossary consistency: 0.85
- **Overall section score:** 0.88
