# Section 6: Conclusion and Future Work
## القسم 6: الخاتمة والأعمال المستقبلية

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** neural network, collaborative filtering, deep learning, matrix factorization, framework, recommendation, multi-layer perceptron, generalization, pairwise learning, recurrent neural network, hashing

---

### English Version

In this work, we explored neural network architectures for collaborative filtering. We devised a general framework NCF and proposed three instantiations — GMF, MLP and NeuMF — that model the user-item interaction with neural networks. Our framework is simple yet effective. It nicely unifies and generalizes existing work of MF and obviates the need to handcraft a feature-based or kernel-based interaction function. Being generic, we believe it can be applied to other domains and tasks beyond recommendation.

Through extensive experiments on two real-world datasets, we show the effectiveness of the proposed NCF framework. To enable the wider adoption of NCF, we have released our implementation code at https://github.com/hexiangnan/neural_collaborative_filtering. Empirical results show that using deeper layers of neural networks offers better recommendation performance. Although the focus of this work is on implicit feedback, our methods can be straightforwardly extended to model explicit feedback data (i.e., ratings). To this end, one can use the NCF to predict the rating score, for which the network parameters are learned by minimizing the regression loss (e.g., square loss) between the predicted rating score and the target value.

Our future work will focus on the following directions. Firstly, we plan to investigate pairwise learners (e.g., BPR and margin-based loss) for NCF models. As we adopt pointwise log loss for learning NCF in this work, it is worthwhile to compare the performance with a pairwise learner which has been shown effective for implicit feedback. Secondly, we will explore to incorporate auxiliary information, such as user reviews and knowledge graphs, into our NCF models to make the recommendation performance more robust. Moreover, we plan to extend NCF for other important recommendation tasks, such as group recommendation for social decision support and multi-media recommendation that leverages the visual semantics in images and videos to make better recommendations. Our work has opened up a new avenue of research possibilities for recommendation based on deep learning. As such, we believe our work will spur more research on deep learning based recommendation systems.

**Acknowledgements.** This work was supported in part by the National Natural Science Foundation of China (Grant No. 61672308 and 61672191). NExT research is supported by the National Research Foundation, Prime Minister's Office, Singapore under its IRC@SG Funding Initiative.

---

### النسخة العربية

في هذا العمل، استكشفنا معماريات الشبكات العصبية للتصفية التعاونية. ابتكرنا إطار عمل عام NCF واقترحنا ثلاثة تطبيقات — GMF و MLP و NeuMF — تقوم بنمذجة تفاعل المستخدم والعنصر بالشبكات العصبية. إطار عملنا بسيط لكنه فعال. إنه يوحد ويعمم بشكل جيد العمل الحالي لتحليل المصفوفات ويلغي الحاجة إلى صياغة يدوية لدالة تفاعل قائمة على الميزات أو النواة. نظراً لكونه عاماً، نعتقد أنه يمكن تطبيقه على مجالات ومهام أخرى خارج نطاق التوصية.

من خلال تجارب واسعة على مجموعتي بيانات من العالم الحقيقي، نُظهر فعالية إطار عمل NCF المقترح. لتمكين اعتماد أوسع لـ NCF، أصدرنا شفرة التنفيذ الخاصة بنا على https://github.com/hexiangnan/neural_collaborative_filtering. تُظهر النتائج التجريبية أن استخدام طبقات أعمق من الشبكات العصبية يقدم أداء توصية أفضل. على الرغم من أن تركيز هذا العمل هو على التغذية الراجعة الضمنية، إلا أن طرقنا يمكن تمديدها بشكل مباشر لنمذجة بيانات التغذية الراجعة الصريحة (أي التقييمات). لهذه الغاية، يمكن للمرء استخدام NCF للتنبؤ بدرجة التقييم، والتي يتم تعلم معاملات الشبكة لها من خلال تقليل خسارة الانحدار (على سبيل المثال، الخسارة التربيعية) بين درجة التقييم المتوقعة والقيمة المستهدفة.

سيركز عملنا المستقبلي على الاتجاهات التالية. أولاً، نخطط للتحقيق في متعلمي الأزواج (على سبيل المثال، BPR وخسارة قائمة على الهامش) لنماذج NCF. نظراً لأننا نتبنى خسارة اللوغاريتم النقطية لتعلم NCF في هذا العمل، فمن المفيد مقارنة الأداء بمتعلم الأزواج الذي ثبت أنه فعال للتغذية الراجعة الضمنية. ثانياً، سنستكشف دمج المعلومات المساعدة، مثل مراجعات المستخدمين والرسوم البيانية المعرفية، في نماذج NCF الخاصة بنا لجعل أداء التوصية أكثر قوة. علاوة على ذلك، نخطط لتوسيع NCF لمهام التوصية المهمة الأخرى، مثل التوصية الجماعية لدعم القرار الاجتماعي والتوصية متعددة الوسائط التي تستفيد من الدلالات المرئية في الصور ومقاطع الفيديو لإجراء توصيات أفضل. لقد فتح عملنا طريقاً جديداً من إمكانيات البحث للتوصية القائمة على التعلم العميق. على هذا النحو، نعتقد أن عملنا سيحفز المزيد من البحث في أنظمة التوصية القائمة على التعلم العميق.

**شكر وتقدير.** تم دعم هذا العمل جزئياً من قبل المؤسسة الوطنية للعلوم الطبيعية في الصين (رقم المنحة 61672308 و 61672191). يتم دعم بحث NExT من قبل المؤسسة الوطنية للبحوث، مكتب رئيس الوزراء، سنغافورة في إطار مبادرة التمويل IRC@SG الخاصة بها.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Pairwise learner
  - Knowledge graphs
  - Group recommendation
  - Multi-media recommendation
  - Visual semantics
  - Social decision support
- **Equations:** None
- **Citations:** Reference to BPR
- **Special handling:**
  - GitHub URL kept in English (standard for code repositories)
  - Grant numbers preserved in original format
  - Acknowledgements section translated maintaining institutional names in English
  - Technical terms like "regression loss" translated as "خسارة الانحدار"
  - Future directions listed systematically in both languages

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
