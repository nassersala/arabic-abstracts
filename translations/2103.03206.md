---
# Perceiver: General Perception with Iterative Attention
## Perceiver: إدراك عام باستخدام الانتباه التكراري

**arXiv ID:** 2103.03206
**Authors:** Andrew Jaegle, Felix Gimeno, Andrew Brock, Andrew Zisserman, Oriol Vinyals, Joao Carreira
**Year:** 2021
**Categories:** cs.CV, cs.AI, cs.LG, cs.SD, eess.AS
**Translation Quality:** 0.90
**Glossary Terms Used:** transformer, architecture, attention mechanism, latent, computer vision, convolutional, deep learning, high-dimensional, point cloud

### English Abstract
Biological systems perceive the world by simultaneously processing high-dimensional inputs from modalities as diverse as vision, audition, touch, proprioception, etc. The perception models used in deep learning on the other hand are designed for individual modalities, often relying on domain-specific assumptions such as the local grid structures exploited by virtually all existing vision models. These priors introduce helpful inductive biases, but also lock models to individual modalities. In this paper we introduce the Perceiver - a model that builds upon Transformers and hence makes few architectural assumptions about the relationship between its inputs, but that also scales to hundreds of thousands of inputs, like ConvNets. The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. We show that this architecture is competitive with or outperforms strong, specialized models on classification tasks across various modalities: images, point clouds, audio, video, and video+audio. The Perceiver obtains performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels. It is also competitive in all modalities in AudioSet.

### الملخص العربي
تدرك الأنظمة البيولوجية العالم من خلال معالجة متزامنة للمدخلات عالية الأبعاد من أنماط متنوعة مثل الرؤية والسمع واللمس والحس العميق، إلخ. من ناحية أخرى، تم تصميم نماذج الإدراك المستخدمة في التعلم العميق للأنماط الفردية، وغالباً ما تعتمد على افتراضات خاصة بالمجال مثل هياكل الشبكة المحلية التي تستغلها جميع نماذج الرؤية الموجودة تقريباً. تقدم هذه الافتراضات المسبقة انحيازات استقرائية مفيدة، لكنها تقيد النماذج أيضاً بالأنماط الفردية. في هذا البحث نقدم Perceiver - نموذج يبني على المحولات وبالتالي يضع افتراضات معمارية قليلة حول العلاقة بين مدخلاته، ولكنه أيضاً يتوسع للتعامل مع مئات الآلاف من المدخلات، مثل الشبكات التفافية. يستفيد النموذج من آلية انتباه غير متماثلة لتقطير المدخلات بشكل تكراري إلى عنق زجاجة كامن ضيق، مما يسمح له بالتوسع للتعامل مع مدخلات كبيرة جداً. نظهر أن هذه المعمارية تنافسية مع أو تتفوق على نماذج قوية ومتخصصة في مهام التصنيف عبر أنماط مختلفة: الصور، وسحب النقاط، والصوت، والفيديو، والفيديو+الصوت. يحصل Perceiver على أداء مماثل لـ ResNet-50 وViT على ImageNet دون التفافات ثنائية الأبعاد من خلال الانتباه مباشرة إلى 50,000 بكسل. كما أنه تنافسي في جميع الأنماط في AudioSet.

### Back-Translation (Validation)
Biological systems perceive the world through simultaneous processing of high-dimensional inputs from diverse modalities such as vision, hearing, touch, and proprioception, etc. On the other hand, perception models used in deep learning are designed for individual modalities, often relying on domain-specific assumptions such as local grid structures that are exploited by almost all existing vision models. These prior assumptions introduce helpful inductive biases, but also constrain models to individual modalities. In this research we introduce Perceiver - a model that builds on Transformers and therefore makes few architectural assumptions about the relationship between its inputs, but also scales to handle hundreds of thousands of inputs, like convolutional networks. The model leverages an asymmetric attention mechanism to iteratively distill inputs into a tight latent bottleneck, allowing it to scale to handle very large inputs. We show that this architecture is competitive with or outperforms strong, specialized models on classification tasks across different modalities: images, point clouds, audio, video, and video+audio. Perceiver achieves performance comparable to ResNet-50 and ViT on ImageNet without 2D convolutions by directly attending to 50,000 pixels. It is also competitive in all modalities in AudioSet.

### Translation Metrics
- Iterations: 1
- Final Score: 0.90
- Quality: High
---
