# Section 4: VIMA-BENCH: Benchmark for Multimodal Robot Learning
## القسم 4: VIMA-BENCH: معيار للتعلم الروبوتي متعدد الوسائط

**Section:** vima-bench
**Translation Quality:** 0.87
**Glossary Terms Used:** benchmark, simulation, procedurally-generated, imitation learning, expert trajectories, zero-shot generalization, evaluation protocol, object segmentation, bounding boxes, motor actions

---

### English Version

**Simulation Environment.** Existing benchmarks are generally geared towards a particular task specification. To our knowledge, there is no benchmark that provides a rich suite of multimodal tasks and a comprehensive testbed for targeted probing of agent capabilities. To this end, we introduce a new benchmark suite for multimodal robot learning called VIMA-BENCH. We build our benchmark by extending the Ravens robot simulator (Zeng et al., 2020). VIMA-BENCH supports extensible collections of objects and textures to compose multimodal prompts and to procedurally generate a large number of tasks. Specifically, we provide 17 tasks with multimodal prompt templates, which can be instantiated into thousands of task instances. Each task belongs to one or more of the 6 task categories mentioned above. VIMA-BENCH can generate large quantities of imitation learning data via scripted oracle agents. More details are elaborated in Appendix, Sec. A.

**Observation and Actions.** The observation space of our simulator includes RGB images rendered from both frontal view and top-down view. Ground-truth object segmentation and bounding boxes are also provided for training object-centric models (Sec. 4). We inherit the high-level action space from Zeng et al. (2020), which consists of primitive motor skills like "pick and place" and "wipe". These are parameterized by poses of the end effector. Our simulator also features scripted oracle programs that can generate expert demonstrations by using privileged simulator state information, such as the precise location of all objects, and the ground-truth interpretation of the multimodal instruction.

**Training Dataset.** We leverage oracles to generate a large offline dataset of expert trajectories for imitation learning. Our dataset includes 50K trajectories per task, and 650K successful trajectories in total. We hold out a subset of objects and textures for evaluation and designate 4 out of 17 tasks as a testbed for zero-shot generalization.

**Evaluating Zero-Shot Generalization.** Each task in VIMA-BENCH has a binary success criterion and does not provide partial reward. During test time, we execute agent policies in the simulator for multiple episodes to compute a percentage success rate. The average success rate over all evaluated tasks will be the final reported metric.

We design a four-level evaluation protocol (Fig. 2) to systematically probe the generalization capabilities of learned agents. Each level deviates more from the training distribution, and is thus strictly harder than the previous one.

1. **Placement generalization.** All prompts are seen verbatim during training, but only the placement of objects on the tabletop is randomized at testing;

2. **Combinatorial generalization.** All textures and objects are seen during training, but new combinations of them appear in testing;

3. **Novel object generalization.** Test prompts and the simulated workspace include novel textures and objects;

4. **Novel task generalization.** New tasks with novel prompt templates at test time.

---

### النسخة العربية

**بيئة المحاكاة.** تركز المعايير الموجودة بشكل عام على تحديد مهمة معينة. على حد علمنا، لا يوجد معيار يوفر مجموعة غنية من المهام متعددة الوسائط ومنصة اختبار شاملة للفحص المستهدف لقدرات الوكيل. تحقيقاً لهذه الغاية، نقدم مجموعة معايير جديدة للتعلم الروبوتي متعدد الوسائط تسمى VIMA-BENCH. نبني معيارنا بتوسيع محاكي الروبوت Ravens (Zeng et al., 2020). يدعم VIMA-BENCH مجموعات قابلة للتوسيع من الأشياء والأنسجة لتأليف موجهات متعددة الوسائط وتوليد عدد كبير من المهام بشكل إجرائي. على وجه التحديد، نوفر 17 مهمة مع قوالب موجهات متعددة الوسائط، والتي يمكن إنشاؤها في آلاف حالات المهام. تنتمي كل مهمة إلى واحدة أو أكثر من فئات المهام الستة المذكورة أعلاه. يمكن لـ VIMA-BENCH توليد كميات كبيرة من بيانات التعلم بالتقليد عبر وكلاء أوراكل مبرمجة. يتم توضيح المزيد من التفاصيل في الملحق، القسم A.

**الملاحظة والإجراءات.** يتضمن فضاء الملاحظة لمحاكينا صور RGB مُقدمة من كل من المنظر الأمامي والمنظر من أعلى لأسفل. يتم أيضاً توفير تجزئة الأشياء الحقيقية والصناديق المحيطة لتدريب النماذج المركزة على الأشياء (القسم 4). نرث فضاء الإجراءات عالي المستوى من Zeng et al. (2020)، والذي يتكون من مهارات حركية بدائية مثل "الالتقاط والوضع" و "المسح". يتم تحديد هذه بواسطة أوضاع المُؤَثِّر النهائي. يتميز محاكينا أيضاً ببرامج أوراكل مبرمجة يمكنها توليد عروض توضيحية من الخبراء باستخدام معلومات حالة المحاكي المميزة، مثل الموقع الدقيق لجميع الأشياء، والتفسير الحقيقي للتعليمات متعددة الوسائط.

**مجموعة بيانات التدريب.** نستفيد من الأوراكل لتوليد مجموعة بيانات كبيرة غير متصلة بالإنترنت من مسارات الخبراء للتعلم بالتقليد. تتضمن مجموعة بياناتنا 50 ألف مسار لكل مهمة، و650 ألف مسار ناجح في المجموع. نحتفظ بمجموعة فرعية من الأشياء والأنسجة للتقييم ونخصص 4 من أصل 17 مهمة كمنصة اختبار للتعميم بدون أمثلة.

**تقييم التعميم بدون أمثلة.** كل مهمة في VIMA-BENCH لديها معيار نجاح ثنائي ولا توفر مكافأة جزئية. خلال وقت الاختبار، ننفذ سياسات الوكيل في المحاكي لحلقات متعددة لحساب نسبة النجاح المئوية. سيكون متوسط معدل النجاح عبر جميع المهام المقيَّمة هو المقياس النهائي المُبَلَّغ عنه.

نصمم بروتوكول تقييم من أربعة مستويات (الشكل 2) للفحص المنهجي لقدرات التعميم للوكلاء المتعلمين. كل مستوى ينحرف أكثر عن توزيع التدريب، وبالتالي يكون أكثر صعوبة بشكل صارم من المستوى السابق.

1. **تعميم الوضع.** يتم رؤية جميع الموجهات حرفياً أثناء التدريب، لكن فقط وضع الأشياء على سطح المكتب يكون عشوائياً عند الاختبار؛

2. **التعميم التوافقي.** يتم رؤية جميع الأنسجة والأشياء أثناء التدريب، ولكن تظهر توليفات جديدة منها في الاختبار؛

3. **تعميم الأشياء الجديدة.** تتضمن موجهات الاختبار ومساحة العمل المحاكاة أنسجة وأشياء جديدة؛

4. **تعميم المهام الجديدة.** مهام جديدة مع قوالب موجهات جديدة في وقت الاختبار.

---

### Translation Notes

- **Figures referenced:** Figure 2 (evaluation protocol with 4 levels)
- **Key terms introduced:** Ravens simulator, oracle agents, scripted demonstrations, binary success criterion, four-level evaluation protocol
- **Equations:** None
- **Citations:** Zeng et al. 2020 (Ravens simulator)
- **Special handling:**
  - Preserved technical terms like "pick and place", "end effector"
  - Maintained numbered list for 4 generalization levels
  - Kept dataset statistics (50K, 650K, 17 tasks, 4 tasks)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Validation

**Simulation Environment.** Existing benchmarks generally focus on a specific task specification. To our knowledge, there is no benchmark that provides a rich suite of multimodal tasks and a comprehensive testing platform for targeted examination of agent capabilities. To this end, we introduce a new benchmark suite for multimodal robot learning called VIMA-BENCH. We build our benchmark by extending the Ravens robot simulator (Zeng et al., 2020). VIMA-BENCH supports extensible collections of objects and textures to compose multimodal prompts and procedurally generate a large number of tasks. Specifically, we provide 17 tasks with multimodal prompt templates, which can be instantiated into thousands of task instances. Each task belongs to one or more of the six task categories mentioned above. VIMA-BENCH can generate large quantities of imitation learning data via scripted oracle agents. More details are elaborated in Appendix, Section A.

[Rest follows similar pattern...]
