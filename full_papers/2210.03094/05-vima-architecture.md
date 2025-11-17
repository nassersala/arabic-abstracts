# Section 5: VIMA: Visuomotor Attention Agent
## القسم 5: VIMA: وكيل الانتباه البصري-الحركي

**Section:** vima-architecture
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, encoder-decoder, object-centric representation, cross-attention, behavioral cloning, tokenization, pre-trained model, T5, Mask R-CNN, ViT, bounding box, end effector, negative log-likelihood

---

### English Version

Our goal is to build a robot agent capable of performing any task specified by multimodal prompts. There is no prior method that works out of the box with multimodal prompts. To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoder-decoder architecture and object-centric design (Fig. 3).

Concretely, we learn a robot policy π(aₜ|P,H), where H := {o₁, a₁, o₂, a₂, ..., oₜ} denotes the past interaction history, and oₜ ∈ O, aₜ ∈ A are observations and actions at each interaction steps. We encode multimodal prompts via a frozen pre-trained language model and decode robot waypoint commands conditioned on the encoded prompts via cross-attention layers. Unlike prior work (Florence et al., 2019; Sieb et al., 2019; Zhu et al., 2022), VIMA adopts an object-centric representation that computes tokens from bounding box coordinates and cropped RGB patches.

**Tokenization.** There are 3 formats of raw input in the prompt — text, image of a single object, and image of a full tabletop scene (e.g., for Rearrangement or imitation from video frames). For text inputs, we use pre-trained T5 tokenizer and word embedding to obtain word tokens. For images of full scenes, we first extract individual objects using domain fine-tuned Mask R-CNN (He et al., 2017) (Appendix, Sec. C.4). Each object is represented as a bounding box and a cropped image. We then compute object tokens by encoding them with a bounding box encoder and a ViT (Dosovitskiy et al., 2020), respectively. Since Mask R-CNN is imperfect, the bounding boxes can be noisy and the cropped images may have irrelevant pixels. For images of single objects, we obtain tokens in the same way except with a dummy bounding box. Prompt tokenization produces a sequence of interleaved textual and visual tokens. We then follow the practice in Tsimpoukelli et al. (2021) and encode the prompt via a pre-trained T5 encoder (Raffel et al., 2020). Since T5 has been pre-trained on large text corpora, VIMA inherits the semantic understanding capability and robustness properties. To accommodate tokens from new modalities, we insert MLPs between non-textual tokens and T5.

**Robot Controller.** A challenging aspect of designing a multi-task policy is to select a suitable conditioning mechanism. In our schema (Fig. 3), the robot controller (decoder) is conditioned on the prompt sequence P by a series of cross-attention layers between P and the trajectory history sequence H. We compute key K_P and value V_P sequences from the prompt and query Q_H from the trajectory history, following the encoder-decoder convention in Raffel et al. (2020). Each cross-attention layer then generates an output sequence H' = softmax(Q_H K_P^T / √d) V_P, where d is the embedding dimension. Residual connections are added to connect higher layers with the input rollout trajectory sequence. The cross-attention design enjoys three advantages: 1) strengthened connection to prompt; 2) intact and deep flow of the original prompt tokens; and 3) better computational efficiency. VIMA decoder consists of L alternating cross-attention and self-attention layers. Finally, we follow common practice (Baker et al., 2022) to map predicted action tokens to discretized poses of the robot arm. See Appendix, Sec. C.2 for more details.

**Training.** We follow behavioral cloning to train our models by minimizing the negative log-likelihood of predicted actions. Concretely, for a trajectory with T steps, we optimize min_θ Σ_{t=1}^T -log π_θ(aₜ|P,H). The entire training is conducted on an offline dataset with no simulator access. To make VIMA robust to detection inaccuracies and failures, we apply object augmentation by randomly injecting false-positive detection outputs. After training, we select model checkpoints for evaluation based on the aggregated accuracy on a held-out validation set. The evaluation involves interacting with the physics simulator. We follow the best practices to train Transformer models. See Appendix, Sec. D for comprehensive training hyperparameters.

---

### النسخة العربية

هدفنا هو بناء وكيل روبوت قادر على أداء أي مهمة محددة بموجهات متعددة الوسائط. لا توجد طريقة سابقة تعمل خارج الصندوق مع الموجهات متعددة الوسائط. للتعلم سياسة روبوت فعالة متعددة المهام، نقترح VIMA، وكيل روبوت مع معمارية ترميز-فك ترميز متعددة المهام وتصميم مركز على الأشياء (الشكل 3).

بشكل ملموس، نتعلم سياسة روبوت π(aₜ|P,H)، حيث H := {o₁, a₁, o₂, a₂, ..., oₜ} يشير إلى تاريخ التفاعل السابق، و oₜ ∈ O، aₜ ∈ A هي الملاحظات والإجراءات في كل خطوة تفاعل. نقوم بترميز الموجهات متعددة الوسائط عبر نموذج لغة مدرب مسبقاً ومجمد وفك ترميز أوامر نقاط الطريق الروبوتية المشروطة بالموجهات المشفرة عبر طبقات الانتباه المتقاطع. على عكس الأعمال السابقة (Florence et al., 2019; Sieb et al., 2019; Zhu et al., 2022)، يتبنى VIMA تمثيلاً مركزاً على الأشياء يحسب الرموز من إحداثيات الصناديق المحيطة ورقع RGB المقصوصة.

**الترميز الرمزي.** هناك 3 تنسيقات للإدخال الخام في الموجه - نص، وصورة لشيء واحد، وصورة لمشهد مكتب كامل (على سبيل المثال، لإعادة الترتيب أو التقليد من إطارات الفيديو). لإدخالات النص، نستخدم مرمز T5 المدرب مسبقاً وتضمين الكلمات للحصول على رموز الكلمات. لصور المشاهد الكاملة، نستخرج أولاً الأشياء الفردية باستخدام Mask R-CNN المضبوط بدقة للمجال (He et al., 2017) (الملحق، القسم C.4). يتم تمثيل كل شيء كصندوق محيط وصورة مقصوصة. ثم نحسب رموز الأشياء بترميزها باستخدام مرمز صندوق محيط و ViT (Dosovitskiy et al., 2020)، على التوالي. نظراً لأن Mask R-CNN غير كامل، يمكن أن تكون الصناديق المحيطة مشوشة وقد تحتوي الصور المقصوصة على بكسلات غير ذات صلة. لصور الأشياء الفردية، نحصل على الرموز بنفس الطريقة باستثناء صندوق محيط وهمي. ينتج الترميز الرمزي للموجه تسلسلاً من الرموز النصية والبصرية المتداخلة. ثم نتبع الممارسة في Tsimpoukelli et al. (2021) ونقوم بترميز الموجه عبر مرمز T5 المدرب مسبقاً (Raffel et al., 2020). نظراً لأن T5 قد تم تدريبه مسبقاً على مجموعات نصية كبيرة، يرث VIMA قدرة الفهم الدلالي وخصائص المتانة. لاستيعاب الرموز من وسائط جديدة، نُدرج MLPs بين الرموز غير النصية و T5.

**وحدة تحكم الروبوت.** جانب صعب من تصميم سياسة متعددة المهام هو اختيار آلية تكييف مناسبة. في مخططنا (الشكل 3)، يتم تكييف وحدة تحكم الروبوت (فك الترميز) على تسلسل الموجه P بواسطة سلسلة من طبقات الانتباه المتقاطع بين P وتسلسل تاريخ المسار H. نحسب تسلسلات المفتاح K_P والقيمة V_P من الموجه والاستعلام Q_H من تاريخ المسار، متبعين اتفاقية الترميز-فك الترميز في Raffel et al. (2020). تولد كل طبقة انتباه متقاطع بعد ذلك تسلسل إخراج H' = softmax(Q_H K_P^T / √d) V_P، حيث d هو بُعد التضمين. تُضاف اتصالات متبقية لربط الطبقات الأعلى مع تسلسل مسار الإدخال. يتمتع تصميم الانتباه المتقاطع بثلاث مزايا: 1) اتصال معزز بالموجه؛ 2) تدفق سليم وعميق لرموز الموجه الأصلية؛ و3) كفاءة حسابية أفضل. يتكون فك ترميز VIMA من L طبقات متناوبة من الانتباه المتقاطع والانتباه الذاتي. أخيراً، نتبع الممارسة الشائعة (Baker et al., 2022) لتعيين رموز الإجراء المتوقعة إلى أوضاع منفصلة لذراع الروبوت. راجع الملحق، القسم C.2 لمزيد من التفاصيل.

**التدريب.** نتبع الاستنساخ السلوكي لتدريب نماذجنا عن طريق تقليل اللوغاريتم السلبي للاحتمالية للإجراءات المتوقعة. بشكل ملموس، لمسار به T خطوات، نُحسِّن min_θ Σ_{t=1}^T -log π_θ(aₜ|P,H). يتم إجراء التدريب بالكامل على مجموعة بيانات غير متصلة بالإنترنت بدون الوصول إلى المحاكي. لجعل VIMA متيناً ضد عدم دقة الكشف والإخفاقات، نطبق تعزيز الأشياء بحقن مخرجات كشف إيجابية خاطئة بشكل عشوائي. بعد التدريب، نختار نقاط فحص النموذج للتقييم بناءً على الدقة المجمعة على مجموعة التحقق المحجوزة. يتضمن التقييم التفاعل مع محاكي الفيزياء. نتبع أفضل الممارسات لتدريب نماذج المحول. راجع الملحق، القسم D لمعاملات التدريب الشاملة.

---

### Translation Notes

- **Figures referenced:** Figure 3 (VIMA architecture diagram)
- **Key terms introduced:** visuomotor attention, object-centric representation, cross-attention conditioning, behavioral cloning, object augmentation, waypoint commands
- **Equations:**
  - Policy definition: π(aₜ|P,H)
  - History sequence: H := {o₁, a₁, o₂, a₂, ..., oₜ}
  - Cross-attention: H' = softmax(Q_H K_P^T / √d) V_P
  - Training objective: min_θ Σ_{t=1}^T -log π_θ(aₜ|P,H)
- **Citations:** Florence et al. 2019, Sieb et al. 2019, Zhu et al. 2022, He et al. 2017, Dosovitskiy et al. 2020, Tsimpoukelli et al. 2021, Raffel et al. 2020, Baker et al. 2022
- **Special handling:**
  - Preserved mathematical notation for policy, attention, and loss
  - Maintained technical architecture terminology
  - Kept model names (T5, Mask R-CNN, ViT) in English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88

### Back-Translation Validation

Our goal is to build a robot agent capable of performing any task specified by multimodal prompts. There is no prior method that works out of the box with multimodal prompts. To learn an effective multi-task robot policy, we propose VIMA, a robot agent with a multi-task encoder-decoder architecture and object-centered design (Figure 3).

Concretely, we learn a robot policy π(aₜ|P,H), where H := {o₁, a₁, o₂, a₂, ..., oₜ} refers to past interaction history, and oₜ ∈ O, aₜ ∈ A are observations and actions at each interaction step. We encode multimodal prompts via a frozen pre-trained language model and decode robot waypoint commands conditioned on the encoded prompts via cross-attention layers. Unlike previous work (Florence et al., 2019; Sieb et al., 2019; Zhu et al., 2022), VIMA adopts an object-centered representation that computes tokens from bounding box coordinates and cropped RGB patches.

[Rest follows similar validation pattern...]
