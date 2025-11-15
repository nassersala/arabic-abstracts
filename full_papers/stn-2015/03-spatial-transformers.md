# Section 3: Spatial Transformers
## القسم 3: المحوّلات المكانية

**Section:** spatial-transformers (methodology)
**Translation Quality:** 0.87
**Glossary Terms Used:** localisation, feature map, transformation, parameters, affine, convolutional, fully-connected, regression, sampling, grid, bilinear interpolation, differentiable, gradient, backpropagation, cost function, feed-forward

---

### English Version

## 3.1 Localisation Network

The localisation network accepts an input feature map U∈ℝ^(H×W×C) with width W, height H, and C channels, outputting θ (transformation parameters): θ=f_loc(U). The parameter vector θ's dimensionality depends on the transformation type—for affine transformations, θ is 6-dimensional.

The localisation network function f_loc() can be fully-connected or convolutional, but must include a final regression layer to produce the transformation parameters θ.

## 3.2 Parameterised Sampling Grid

Output pixels form a regular grid G={G_i} of pixels G_i=(x_i^t, y_i^t), creating output feature map V∈ℝ^(H'×W'×C). For 2D affine transformation 𝙰_θ, the pointwise transformation is:

$$\\left[\\begin{matrix}x_i^s \\\\ y_i^s\\end{matrix}\\right]^T = \\mathcal{A}_\\theta \\left[\\begin{matrix}x_i^t \\\\ y_i^t \\\\ 1\\end{matrix}\\right]^T$$

where (x_i^t, y_i^t) are target coordinates and (x_i^s, y_i^s) are source coordinates. Using normalized coordinates where −1 ≤ coordinates ≤ 1 within spatial bounds.

The affine transformation enables cropping, translation, rotation, scale, and skew with only 6 parameters. Constrained transformations like attention use:

$$\\mathcal{A}_\\theta = \\begin{bmatrix}s & 0 & t_x \\\\ 0 & s & t_y\\end{bmatrix}$$

allowing scaling and translation. The framework supports plane projective transformations, piecewise affine, thin plate splines, or any parameterised form, provided that it is differentiable with respect to the parameters.

## 3.3 Differentiable Image Sampling

The sampler takes sampling points 𝒯_θ(G) and input feature map U, producing sampled output V. Each coordinate (x_i^s, y_i^s) defines the input location where a sampling kernel applies:

$$V_i^c = \\sum_n \\sum_m U_{nm}^c k(x_i^s - m; \\Phi_x) k(y_i^s - n; \\Phi_y)$$

where k() is a generic sampling kernel defining interpolation, and Φ_x, Φ_y are kernel parameters.

Using bilinear sampling:

$$V_i^c = \\sum_n \\sum_m U_{nm}^c \\max(0, 1-|x_i^s-m|) \\max(0, 1-|y_i^s-n|)$$

Gradients flow through the sampling mechanism via:

$$\\frac{\\partial V_i^c}{\\partial U_{nm}^c} = \\sum_n \\sum_m \\max(0, 1-|x_i^s-m|) \\max(0, 1-|y_i^s-n|)$$

$$\\frac{\\partial V_i^c}{\\partial x_i^s} = \\sum_n \\sum_m U_{nm}^c \\max(0, 1-|y_i^s-n|) \\times \\begin{cases}0 & \\text{if } |m-x_i^s|\\geq 1 \\\\ 1 & \\text{if } m\\geq x_i^s \\\\ -1 & \\text{if } m<x_i^s\\end{cases}$$

This differentiable mechanism allowing loss gradients to flow back enables end-to-end training.

## 3.4 Spatial Transformer Networks

The combination of localisation network, grid generator, and sampler forms a complete spatial transformer module—a self-contained module which can be dropped into a CNN architecture at any point, and in any number.

The network learns how to actively transform the feature maps to help minimise the overall cost function during training. Transformation knowledge is compressed and cached in the weights of the localisation network.

The framework supports multiple spatial transformers sequentially at increasing network depths or in parallel for multiple objects. A key limitation: the number of parallel spatial transformers limits the number of objects that the network can model in feed-forward architectures.

---

### النسخة العربية

## 3.1 شبكة التوطين

تقبل شبكة التوطين خريطة ميزات إدخال U∈ℝ^(H×W×C) بعرض W وارتفاع H وعدد قنوات C، وتُخرج θ (معاملات التحويل): θ=f_loc(U). تعتمد أبعاد متجه المعاملات θ على نوع التحويل—بالنسبة للتحويلات الأفينية، تكون θ سداسية الأبعاد.

يمكن أن تكون دالة شبكة التوطين f_loc() متصلة بالكامل أو التفافية، لكن يجب أن تتضمن طبقة انحدار نهائية لإنتاج معاملات التحويل θ.

## 3.2 شبكة العينات ذات المعاملات

تشكل بكسلات الإخراج شبكة منتظمة G={G_i} من البكسلات G_i=(x_i^t, y_i^t)، مما يخلق خريطة ميزات إخراج V∈ℝ^(H'×W'×C). بالنسبة للتحويل الأفيني ثنائي الأبعاد 𝙰_θ، يكون التحويل النقطي:

$$\\left[\\begin{matrix}x_i^s \\\\ y_i^s\\end{matrix}\\right]^T = \\mathcal{A}_\\theta \\left[\\begin{matrix}x_i^t \\\\ y_i^t \\\\ 1\\end{matrix}\\right]^T$$

حيث (x_i^t, y_i^t) هي إحداثيات الهدف و(x_i^s, y_i^s) هي إحداثيات المصدر. باستخدام إحداثيات معيارية حيث −1 ≤ إحداثيات ≤ 1 ضمن الحدود المكانية.

يُمكّن التحويل الأفيني القص والإزاحة والدوران والتحجيم والانحراف باستخدام 6 معاملات فقط. تستخدم التحويلات المقيدة مثل الانتباه:

$$\\mathcal{A}_\\theta = \\begin{bmatrix}s & 0 & t_x \\\\ 0 & s & t_y\\end{bmatrix}$$

مما يسمح بالتحجيم والإزاحة. يدعم الإطار تحويلات الإسقاط المستوي، والتحويلات الأفينية القطعية، وشرائح الصفيحة الرقيقة، أو أي شكل ذي معاملات، بشرط أن يكون قابلاً للاشتقاق بالنسبة للمعاملات.

## 3.3 أخذ عينات الصور القابل للاشتقاق

يأخذ جهاز أخذ العينات نقاط العينات 𝒯_θ(G) وخريطة ميزات الإدخال U، لإنتاج إخراج معيّن V. كل إحداثية (x_i^s, y_i^s) تحدد موقع الإدخال حيث تُطبق نواة أخذ العينات:

$$V_i^c = \\sum_n \\sum_m U_{nm}^c k(x_i^s - m; \\Phi_x) k(y_i^s - n; \\Phi_y)$$

حيث k() هي نواة أخذ عينات عامة تحدد الاستيفاء، وΦ_x وΦ_y هي معاملات النواة.

باستخدام أخذ العينات ثنائي الخطي:

$$V_i^c = \\sum_n \\sum_m U_{nm}^c \\max(0, 1-|x_i^s-m|) \\max(0, 1-|y_i^s-n|)$$

تتدفق التدرجات من خلال آلية أخذ العينات عبر:

$$\\frac{\\partial V_i^c}{\\partial U_{nm}^c} = \\sum_n \\sum_m \\max(0, 1-|x_i^s-m|) \\max(0, 1-|y_i^s-n|)$$

$$\\frac{\\partial V_i^c}{\\partial x_i^s} = \\sum_n \\sum_m U_{nm}^c \\max(0, 1-|y_i^s-n|) \\times \\begin{cases}0 & \\text{إذا } |m-x_i^s|\\geq 1 \\\\ 1 & \\text{إذا } m\\geq x_i^s \\\\ -1 & \\text{إذا } m<x_i^s\\end{cases}$$

تُمكّن هذه الآلية القابلة للاشتقاق التي تسمح بتدفق تدرجات الخسارة للخلف التدريب من البداية للنهاية.

## 3.4 شبكات المحوّل المكاني

يُشكّل الجمع بين شبكة التوطين ومولد الشبكة وجهاز أخذ العينات وحدة محوّل مكاني كاملة—وحدة مستقلة يمكن إدراجها في معمارية الشبكة العصبية الالتفافية في أي نقطة، وبأي عدد.

تتعلم الشبكة كيفية تحويل خرائط الميزات بشكل نشط للمساعدة في تقليل دالة التكلفة الإجمالية أثناء التدريب. يتم ضغط معرفة التحويل وتخزينها مؤقتاً في أوزان شبكة التوطين.

يدعم الإطار محوّلات مكانية متعددة بشكل تسلسلي عند أعماق شبكة متزايدة أو بشكل متوازي لأجسام متعددة. قيد رئيسي: يحدد عدد المحوّلات المكانية المتوازية عدد الأجسام التي يمكن للشبكة نمذجتها في معماريات التغذية الأمامية.

---

### Translation Notes

- **Figures referenced:** Implicit reference to Figure 1 (module architecture)
- **Key terms introduced:**
  - Localisation network (شبكة التوطين)
  - Parameterised sampling grid (شبكة العينات ذات المعاملات)
  - Grid generator (مولد الشبكة)
  - Sampler (جهاز أخذ العينات)
  - Bilinear sampling (أخذ العينات ثنائي الخطي)
  - Affine transformation (التحويل الأفيني)
  - Thin plate splines (شرائح الصفيحة الرقيقة)
  - Plane projective transformations (تحويلات الإسقاط المستوي)
  - Piecewise affine (أفينية قطعية)

- **Equations:** 7 major equations with LaTeX notation preserved
- **Citations:** 0
- **Special handling:**
  - All mathematical equations preserved in LaTeX format
  - Variable names kept in English (U, V, θ, etc.)
  - Mathematical notation maintained throughout
  - "Self-contained module" translated as "وحدة مستقلة"
  - "Dropped into" translated as "إدراجها في"
  - "Cached in the weights" translated as "تخزينها مؤقتاً في أوزان"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation

## 3.1 Localization Network

The localization network accepts an input feature map U∈ℝ^(H×W×C) with width W, height H, and number of channels C, and outputs θ (transformation parameters): θ=f_loc(U). The dimensions of parameter vector θ depend on the transformation type—for affine transformations, θ is six-dimensional.

The localization network function f_loc() can be fully-connected or convolutional, but must include a final regression layer to produce transformation parameters θ.

## 3.2 Parameterized Sampling Grid

Output pixels form a regular grid G={G_i} of pixels G_i=(x_i^t, y_i^t), creating output feature map V∈ℝ^(H'×W'×C). For 2D affine transformation 𝙰_θ, the pointwise transformation is: [equations preserved]

where (x_i^t, y_i^t) are target coordinates and (x_i^s, y_i^s) are source coordinates. Using normalized coordinates where −1 ≤ coordinates ≤ 1 within spatial bounds.

The affine transformation enables cropping, translation, rotation, scaling, and skew using only 6 parameters. Constrained transformations like attention use: [equation] allowing scaling and translation. The framework supports plane projective transformations, piecewise affine, thin plate splines, or any parameterized form, provided it is differentiable with respect to parameters.

## 3.3 Differentiable Image Sampling

The sampler takes sampling points 𝒯_θ(G) and input feature map U, to produce sampled output V. Each coordinate (x_i^s, y_i^s) defines the input location where a sampling kernel is applied: [equations preserved]

where k() is a general sampling kernel that defines interpolation, and Φ_x and Φ_y are kernel parameters.

Using bilinear sampling: [equations] Gradients flow through the sampling mechanism via: [equations]

This differentiable mechanism that allows loss gradients to flow backward enables end-to-end training.

## 3.4 Spatial Transformer Networks

The combination of localization network, grid generator, and sampler forms a complete spatial transformer module—an independent module that can be inserted into a CNN architecture at any point, and in any number.

The network learns how to actively transform feature maps to help minimize the overall cost function during training. Transformation knowledge is compressed and cached in the localization network weights.

The framework supports multiple spatial transformers sequentially at increasing network depths or in parallel for multiple objects. A key limitation: the number of parallel spatial transformers limits the number of objects the network can model in feed-forward architectures.
