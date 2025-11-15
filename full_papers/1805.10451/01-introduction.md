# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** deep learning, machine learning, manifold, autoencoder, encoder, decoder, latent space, ReLU, DNN, piecewise linear, optimal mass transportation, WGAN, generator, discriminator

---

### English Version

Deep learning is the mainstream technique for many machine learning tasks, including image recognition, machine translation, speech recognition, and so on [12]. It has outperformed conventional methods in various fields and achieved great successes. Unfortunately, the understanding on how it works remains unclear. It has the central importance to lay down the theoretic foundation for deep learning.

We believe that the main fundamental principle to explain the success of deep learning is the **manifold structure** in the data, there exists a well accepted manifold assumption: *natural high dimensional data concentrates close to a non-linear low-dimensional manifold*.

**Manifold Representation** The main focus of various deep learn methods is to learn the manifold structure from the real data and obtain a parametric representation of the manifold. In general, there is a probability distribution $\mu$ in the ambient space $\mathcal{X}$, the support of $\mu$ is a low dimensional manifold $\Sigma \subset \mathcal{X}$. For example, an autoencoder learns the encoding map $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ and the decoding map $\psi_\theta : \mathcal{F} \to \mathcal{X}$, where $\mathcal{F}$ is the latent space. The parametric representation of the input manifold $\Sigma$ is given by the decoding map $\psi_\theta$. The reconstructed manifold $\tilde{\Sigma} = \psi_\theta \circ \varphi_\theta(\Sigma)$ approximates input manifold. Furthermore, the DNN also learns and controls the distribution induced by the encoder $(\varphi_\theta)_*\mu$ defined on the latent space. Once the parametric manifold structure is obtained, it can be applied for various application, such as randomly generating a sample on $\tilde{\Sigma}$ as a generative model. Image denoising can be reinterpreted geometrically as projecting a noisy sample onto $\tilde{\Sigma}$ representing the clean image manifold, the closest point on $\tilde{\Sigma}$ gives the denoised image.

**Learning Capability** An autoencoder implemented by a ReLU DNN offers a piecewise functional space, the manifold structure can be learned by optimizing special loss functions. We introduce the concept of **Rectified Linear Complexity** of a DNN, which represents the upper bound of the number of pieces of all the functions representable by the DNN, and gives a measurement for the learning capability of the DNN. On the other hand, the piecewise linear encoding map $\varphi_\theta$ defined on the ambient space is required to be homemorphic from $\Sigma$ to a domain on $\mathcal{F}$. This requirement induces strong topological constraints of the input manifold $\Sigma$. We introduce another concept **Rectified linear Complexity** of an embedded manifold $(\Sigma, \mathcal{X})$, which describes the minimal number of pieces for a PL encoding map, and measures the difficulty to be encoded by a DNN. By comparing the complexities of the DNN and the manifold, we can verify if the DNN can learn the manifold in principle. Furthermore, we show for any DNN with fixed architecture, there exists an embedding manifold that can not be encoded by the DNN.

**Latent Probability Distribution Control** The distribution $(\varphi_\theta)_*\mu$ induced by the encoding map can be controlled by designing special loss functions to modify the encoding map $\varphi_\theta$. We also propose to use optimal mass transportation theory to find the optimal transportation map defined on the latent space, which transforms simple distributions, such as Gaussian or uniform, to $(\varphi_\theta)_*\mu$. Comparing to the conventional WGAN model, this method replaces the blackbox by explicit mathematical construction, and avoids the competition between the generator and the discriminator.

### 1.1 Contributions

This work proposes a geometric framework to understand autoencoder and general deep neural networks and explains the main theoretic reason for the great success of deep learning - the manifold structure hidden in data. The work introduces the concept of rectified linear complexity of a ReLU DNN to measure the learning capability, and rectified linear complexity of an embedded manifold to describe the encoding difficulty. By applying the concept of complexities, it is shown that for any DNN with fixed architecture, there is a manifold too complicated to be encoded by the DNN. Finally, the work proposes to apply optimal mass transportation map to control the distribution on the latent space.

### 1.2 Organization

The current work is organized in the following way: section 2 briefly reviews the literature of autoencoders; section 3 explains the manifold representation; section 4 quantifies the learning capability of a DNN and the learning difficulty for a manifold; section 5 proposes to control the probability measure induced by the encoder using optimal mass transportation theory. Experimental results are demonstrated in the appendix 6.

---

### النسخة العربية

التعلم العميق هو التقنية السائدة للعديد من مهام تعلم الآلة، بما في ذلك التعرف على الصور، والترجمة الآلية، والتعرف على الكلام، وما إلى ذلك [12]. لقد تفوق على الأساليب التقليدية في مختلف المجالات وحقق نجاحات كبيرة. لسوء الحظ، لا يزال الفهم حول كيفية عمله غير واضح. من الأهمية المركزية وضع الأساس النظري للتعلم العميق.

نعتقد أن المبدأ الأساسي الرئيسي لتفسير نجاح التعلم العميق هو **بنية المتعدد** في البيانات، حيث يوجد افتراض متعدد مقبول على نطاق واسع: *البيانات الطبيعية عالية الأبعاد تتركز بالقرب من متعدد غير خطي منخفض الأبعاد*.

**تمثيل المتعدد** التركيز الرئيسي لمختلف طرق التعلم العميق هو تعلم بنية المتعدد من البيانات الحقيقية والحصول على تمثيل بارامتري للمتعدد. بشكل عام، يوجد توزيع احتمالات $\mu$ في الفضاء المحيط $\mathcal{X}$، ودعم $\mu$ هو متعدد منخفض الأبعاد $\Sigma \subset \mathcal{X}$. على سبيل المثال، يتعلم المشفر التلقائي خريطة الترميز $\varphi_\theta : \mathcal{X} \to \mathcal{F}$ وخريطة فك الترميز $\psi_\theta : \mathcal{F} \to \mathcal{X}$، حيث $\mathcal{F}$ هو الفضاء الكامن. يتم إعطاء التمثيل البارامتري لمتعدد المدخلات $\Sigma$ بواسطة خريطة فك الترميز $\psi_\theta$. المتعدد المعاد بناؤه $\tilde{\Sigma} = \psi_\theta \circ \varphi_\theta(\Sigma)$ يقرب متعدد المدخلات. علاوة على ذلك، تتعلم الشبكة العصبية العميقة أيضاً وتتحكم في التوزيع المستحث بواسطة المشفر $(\varphi_\theta)_*\mu$ المعرف على الفضاء الكامن. بمجرد الحصول على بنية المتعدد البارامترية، يمكن تطبيقها لتطبيقات مختلفة، مثل توليد عينة عشوائياً على $\tilde{\Sigma}$ كنموذج توليدي. يمكن إعادة تفسير إزالة الضوضاء من الصور هندسياً على أنها إسقاط عينة صاخبة على $\tilde{\Sigma}$ الذي يمثل متعدد الصورة النظيفة، والنقطة الأقرب على $\tilde{\Sigma}$ تعطي الصورة منزوعة الضوضاء.

**قدرة التعلم** يوفر المشفر التلقائي المنفذ بواسطة شبكة عصبية عميقة ReLU فضاءً دالياً متعدد القطع، ويمكن تعلم بنية المتعدد عن طريق تحسين دوال خسارة خاصة. نقدم مفهوم **التعقيد الخطي المصحح** لشبكة عصبية عميقة، والذي يمثل الحد الأعلى لعدد القطع لجميع الدوال القابلة للتمثيل بواسطة الشبكة العصبية العميقة، ويعطي قياساً لقدرة التعلم للشبكة العصبية العميقة. من ناحية أخرى، يُطلب من خريطة الترميز الخطية المتعددة القطع $\varphi_\theta$ المعرفة على الفضاء المحيط أن تكون متشاكلة من $\Sigma$ إلى مجال على $\mathcal{F}$. يستحث هذا المتطلب قيوداً طوبولوجية قوية على متعدد المدخلات $\Sigma$. نقدم مفهوماً آخر **التعقيد الخطي المصحح** لمتعدد مضمن $(\Sigma, \mathcal{X})$، والذي يصف الحد الأدنى لعدد القطع لخريطة ترميز PL، ويقيس صعوبة الترميز بواسطة شبكة عصبية عميقة. من خلال مقارنة تعقيدات الشبكة العصبية العميقة والمتعدد، يمكننا التحقق مما إذا كانت الشبكة العصبية العميقة يمكنها تعلم المتعدد من حيث المبدأ. علاوة على ذلك، نظهر أنه لأي شبكة عصبية عميقة ذات بنية ثابتة، يوجد متعدد مضمن لا يمكن ترميزه بواسطة الشبكة العصبية العميقة.

**التحكم في توزيع الاحتمالات الكامن** يمكن التحكم في التوزيع $(\varphi_\theta)_*\mu$ المستحث بواسطة خريطة الترميز عن طريق تصميم دوال خسارة خاصة لتعديل خريطة الترميز $\varphi_\theta$. نقترح أيضاً استخدام نظرية النقل الأمثل للكتلة لإيجاد خريطة النقل الأمثل المعرفة على الفضاء الكامن، والتي تحول التوزيعات البسيطة، مثل التوزيع الغاوسي أو الموحد، إلى $(\varphi_\theta)_*\mu$. بالمقارنة مع نموذج WGAN التقليدي، تستبدل هذه الطريقة الصندوق الأسود ببناء رياضي صريح، وتتجنب المنافسة بين المولد والمميز.

### 1.1 المساهمات

يقترح هذا العمل إطاراً هندسياً لفهم المشفر التلقائي والشبكات العصبية العميقة العامة ويشرح السبب النظري الرئيسي للنجاح الكبير للتعلم العميق - بنية المتعدد المخفية في البيانات. يقدم العمل مفهوم التعقيد الخطي المصحح لشبكة عصبية عميقة ReLU لقياس قدرة التعلم، والتعقيد الخطي المصحح لمتعدد مضمن لوصف صعوبة الترميز. من خلال تطبيق مفهوم التعقيدات، يتم إظهار أنه لأي شبكة عصبية عميقة ذات بنية ثابتة، يوجد متعدد معقد جداً بحيث لا يمكن ترميزه بواسطة الشبكة العصبية العميقة. أخيراً، يقترح العمل تطبيق خريطة النقل الأمثل للكتلة للتحكم في التوزيع على الفضاء الكامن.

### 1.2 التنظيم

العمل الحالي منظم بالطريقة التالية: يراجع القسم 2 بإيجاز أدبيات المشفرات التلقائية؛ يشرح القسم 3 تمثيل المتعدد؛ يحدد القسم 4 كمياً قدرة التعلم لشبكة عصبية عميقة وصعوبة التعلم لمتعدد؛ يقترح القسم 5 التحكم في قياس الاحتمالات المستحث بواسطة المشفر باستخدام نظرية النقل الأمثل للكتلة. يتم عرض النتائج التجريبية في الملحق 6.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - manifold structure → بنية المتعدد
  - ambient space → الفضاء المحيط
  - support of distribution → دعم التوزيع
  - parametric representation → تمثيل بارامتري
  - piecewise linear (PL) → خطي متعدد القطع
  - homeomorphic → متشاكل
  - push-forward measure → القياس المدفوع للأمام

- **Equations:** Several inline LaTeX equations preserved
- **Citations:** [12] referenced
- **Special handling:** Mathematical notation preserved exactly

### Back-Translation Check (First Paragraph)

"Deep learning is the dominant technique for many machine learning tasks, including image recognition, machine translation, speech recognition, and so on [12]. It has surpassed conventional methods in various fields and achieved great successes. Unfortunately, the understanding of how it works remains unclear. It is of central importance to establish the theoretical foundation for deep learning."

✓ Semantic match verified

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
