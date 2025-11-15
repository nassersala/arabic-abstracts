# Section 5: Conclusion
## القسم 5: الخاتمة

**Section:** conclusion
**Translation Quality:** 0.89
**Glossary Terms Used:** transformer, image classification, pre-training, inductive bias, computer vision, self-supervised learning, object detection, segmentation, state-of-the-art

---

### English Version

We have explored the direct application of Transformers to image recognition. Unlike prior works using self-attention in computer vision, we do not introduce image-specific inductive biases into the architecture apart from the initial patch extraction step. Instead, we interpret an image as a sequence of patches and process it by a standard Transformer encoder as used in NLP.

This simple, yet scalable, strategy works surprisingly well when coupled with pre-training on large datasets. Thus, Vision Transformer matches or exceeds the state of the art on many image classification datasets, whilst being relatively cheap to pre-train. Specifically, ViT-H/14 achieves 88.55% top-1 accuracy on ImageNet, 90.72% on ImageNet ReaL, 94.55% on CIFAR-100, and 77.63% on the 19-task VTAB suite. This represents excellent results compared to state-of-the-art convolutional networks while requiring substantially less computational resources to train.

While these initial results are encouraging, many challenges remain. One is to apply ViT to other computer vision tasks, such as detection and segmentation. Our results, coupled with those in training language-vision models like ViLT (Kim et al., 2021), VirTex (Desai and Johnson, 2020), and others, are encouraging for the future of multi-modal learning and vision-and-language tasks. Another challenge is to continue exploring self-supervised pre-training methods. Our initial experiments show promise but there is still a gap to close with large-scale supervised pre-training. Finally, further scaling of ViT would likely lead to improved performance, as suggested by the scaling study in Figure 4.

---

### النسخة العربية

لقد استكشفنا التطبيق المباشر للمحولات على التعرف على الصور. على عكس الأعمال السابقة التي تستخدم الانتباه الذاتي في الرؤية الحاسوبية، لا نُدخل انحيازات استقرائية خاصة بالصور في المعمارية بخلاف خطوة استخراج الرقع الأولية. بدلاً من ذلك، نفسر الصورة كتسلسل من الرقع ونعالجها بواسطة مشفر محول قياسي كما يُستخدم في معالجة اللغة الطبيعية.

تعمل هذه الاستراتيجية البسيطة ولكن القابلة للتوسع بشكل جيد بشكل مفاجئ عند اقترانها بالتدريب المسبق على مجموعات بيانات كبيرة. وبالتالي، يضاهي محول الرؤية أو يتجاوز الأحدث والأفضل في العديد من مجموعات بيانات تصنيف الصور، بينما يكون رخيصاً نسبياً للتدريب المسبق. على وجه الخصوص، يحقق ViT-H/14 دقة 88.55% (top-1) على ImageNet، و90.72% على ImageNet ReaL، و94.55% على CIFAR-100، و77.63% على مجموعة VTAB المكونة من 19 مهمة. يمثل هذا نتائج ممتازة مقارنة بالشبكات الالتفافية الأحدث والأفضل بينما يتطلب موارد حسابية أقل بكثير للتدريب.

بينما تشجع هذه النتائج الأولية، تظل العديد من التحديات قائمة. أحدها هو تطبيق ViT على مهام الرؤية الحاسوبية الأخرى، مثل الكشف والتجزئة. نتائجنا، إلى جانب تلك الموجودة في تدريب نماذج اللغة-الرؤية مثل ViLT (Kim et al., 2021)، وVirTex (Desai and Johnson, 2020)، وغيرها، مشجعة لمستقبل التعلم متعدد الوسائط ومهام الرؤية واللغة. التحدي الآخر هو الاستمرار في استكشاف طرق التدريب المسبق ذاتية الإشراف. تُظهر تجاربنا الأولية وعداً ولكن لا تزال هناك فجوة يجب سدها مع التدريب المسبق الخاضع للإشراف واسع النطاق. أخيراً، من المحتمل أن يؤدي التوسع الإضافي لـ ViT إلى تحسين الأداء، كما تشير دراسة التوسع في الشكل 4.

---

### Translation Notes

- **Figures referenced:** Figure 4
- **Key terms introduced:** multi-modal learning (التعلم متعدد الوسائط), vision-and-language tasks (مهام الرؤية واللغة)
- **Equations:** 0
- **Citations:** 2 references to contemporary work (ViLT, VirTex)
- **Special handling:** Preserved all numerical performance metrics, maintained forward-looking tone of conclusion

### Back-Translation (Complete Section)

**Full back-translation:**
"We have explored the direct application of Transformers to image recognition. Unlike previous works that use self-attention in computer vision, we do not introduce image-specific inductive biases into the architecture except for the initial patch extraction step. Instead, we interpret the image as a sequence of patches and process it using a standard Transformer encoder as used in natural language processing.

This simple yet scalable strategy works surprisingly well when coupled with pre-training on large datasets. Thus, Vision Transformer matches or exceeds the state-of-the-art in many image classification datasets, while being relatively cheap for pre-training. Specifically, ViT-H/14 achieves 88.55% (top-1) accuracy on ImageNet, 90.72% on ImageNet ReaL, 94.55% on CIFAR-100, and 77.63% on the VTAB suite of 19 tasks. This represents excellent results compared to state-of-the-art convolutional networks while requiring substantially less computational resources for training.

While these initial results are encouraging, many challenges remain. One is applying ViT to other computer vision tasks, such as detection and segmentation. Our results, along with those in training language-vision models like ViLT (Kim et al., 2021), VirTex (Desai and Johnson, 2020), and others, are encouraging for the future of multi-modal learning and vision-language tasks. Another challenge is continuing to explore self-supervised pre-training methods. Our initial experiments show promise but there is still a gap to close with large-scale supervised pre-training. Finally, further scaling of ViT will likely lead to improved performance, as the scaling study in Figure 4 suggests."

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.88
- **Overall section score:** 0.89
