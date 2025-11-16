# Section 6: Mechanising the Tokeneer Assurance Case
## القسم 6: أتمتة حالة ضمان Tokeneer

**Section:** mechanising-assurance-case
**Translation Quality:** 0.86
**Glossary Terms Used:** assurance case (حالة ضمان), formalization pattern (نمط الإضفاء الرسمي), claim (ادعاء), evidence (دليل), artifact (مصنوع)

---

### English Version

In the following, we mechanize an assurance argument with the claim that TIS satisfies SFR1. The assurance case fragment is shown in Figure 7, which is inspired by the formalisation pattern [9]. The latter shows how results from a formal method can be employed in an assurance case. This is contingent on the validation of both the formal model and the formal requirement. Consequently, the formalisation pattern breaks down a requirement into 3 claims stating that (1) the formal model is validated, (2) the formal requirement correctly characterises the informal requirement, and (3) the formal requirement is satisfied by the formal model. The former two claims will usually have an informal process argument.

The argument in Figure 7 justifies the link between the informal claim "TIS satisfies SFR1", which is in natural language, and the formal theorem FSRF1 from §5, which is expressed in HOL. The top-level claim, TIS-SFR1-C1, states that SFR1 is satisfied, which it references as a contextual element. This claim is decomposed by the use of the formalization strategy, TIS-SFR1-S1, which has the formal property (FSRF1) and TIS model from §5 as context. The satisfaction of the formal claim is expressed by TIS-SFR1-C4, and evidenced by SFR1-PROOF, which is the formal proof. The validation claims are encoded as justifications TIS-SFR1-C3 and TIS-SFR1-C4, which are not elaborated.

Figure 8 contains a mechanised version of the same argument in Isabelle/SACM. The structure is slightly different from the GSN diagram since justifications are particular kind of claims in SACM. The five claims are specified using the CLAIM command, with a name and content associated. The text in these claims integrate hyper-linked semi-formal and formal content; for example TIS-SFR1-C1 uses the antiquotation Expression to insert a formal link to the defined expression for SFR1. Similarly, TIS-SFR1-C3 contains a reference to the resource artifact TIS, which is a reference to the Tokeneer specification, and also an Isabelle constant TIS-model which contains the formal TIS model.

The inferences between these claims are specified by several instances of the ASSERTED_INFERENCE command, each of which links several premise claims to one or more conclusions. TIS-SFR-S1 shows that satisfaction of the informal requirement depends on the formal requirement, and the two validation claims.

Figure 7 does not elaborate further on the evidential artifacts required, for the verification, as GSN does not support this. This is functionality which SACM supports through the artifact meta-model, which allows us to record activities, participants, resources, and other assurance artifacts. Figure 9 supplements the argument in Figure 8 with the various evidential artifacts, and the relationships between them. For example, the evidence supporting the claim TIS_SFR1_C4 is a reference to the artifact TIS_FSFR1_SPEC_THY which is the Isabelle theory containing the proof of the theorem stated by TIS_SFR1_C4. TIS_FSFR1_SPEC_THY refers via the artifact relationship TIS_SFR1_PROOF_ACTIVITY_REL to the context of the proof which is the artifact Isabelle_IT and to the author of the proof which is Simon_Foster. This illustrates how Isabelle/SACM allows us to combine informal artifacts and activities with the formal results they produce.

---

### النسخة العربية

في ما يلي، نقوم بأتمتة حجة ضمان بادعاء أن TIS يفي بـ SFR1. يظهر جزء حالة الضمان في الشكل 7، المستوحى من نمط الإضفاء الرسمي [9]. يُظهر الأخير كيف يمكن استخدام نتائج من أسلوب رسمي في حالة ضمان. هذا يعتمد على التحقق من صحة كل من النموذج الرسمي والمتطلب الرسمي. وبالتالي، يفصل نمط الإضفاء الرسمي متطلباً إلى 3 ادعاءات تنص على أن (1) النموذج الرسمي متحقق من صحته، (2) المتطلب الرسمي يميز المتطلب غير الرسمي بشكل صحيح، و(3) المتطلب الرسمي راضٍ من قبل النموذج الرسمي. عادةً ما يكون للادعاءين الأولين حجة عملية غير رسمية.

تبرر الحجة في الشكل 7 الرابط بين الادعاء غير الرسمي "TIS يفي بـ SFR1"، الذي باللغة الطبيعية، والنظرية الرسمية FSRF1 من §5، المعبر عنها في HOL. الادعاء من المستوى الأعلى، TIS-SFR1-C1، ينص على أن SFR1 راضٍ، والذي يشير إليه كعنصر سياقي. يتم تحليل هذا الادعاء باستخدام استراتيجية الإضفاء الرسمي، TIS-SFR1-S1، التي تحتوي على الخاصية الرسمية (FSRF1) ونموذج TIS من §5 كسياق. يتم التعبير عن رضا الادعاء الرسمي بواسطة TIS-SFR1-C4، ويُدلل عليه بواسطة SFR1-PROOF، وهو الإثبات الرسمي. يتم ترميز ادعاءات التحقق من الصحة كتبريرات TIS-SFR1-C3 و TIS-SFR1-C4، التي لا يتم توضيحها.

يحتوي الشكل 8 على نسخة مؤتمتة من نفس الحجة في Isabelle/SACM. البنية مختلفة قليلاً عن مخطط GSN حيث أن التبريرات هي نوع معين من الادعاءات في SACM. يتم تحديد الادعاءات الخمسة باستخدام أمر CLAIM، مع اسم ومحتوى مرتبطين. يدمج النص في هذه الادعاءات محتوى شبه رسمي ورسمي مرتبطاً بروابط فائقة؛ على سبيل المثال يستخدم TIS-SFR1-C1 الاقتباس القديم Expression لإدراج رابط رسمي إلى التعبير المحدد لـ SFR1. وبالمثل، يحتوي TIS-SFR1-C3 على مرجع لمصنوع المورد TIS، وهو مرجع لمواصفات Tokeneer، وأيضاً ثابت Isabelle TIS-model الذي يحتوي على نموذج TIS الرسمي.

يتم تحديد الاستنتاجات بين هذه الادعاءات بواسطة عدة مثيلات من أمر ASSERTED_INFERENCE، كل منها يربط عدة ادعاءات مقدمة بواحد أو أكثر من الاستنتاجات. يُظهر TIS-SFR-S1 أن رضا المتطلب غير الرسمي يعتمد على المتطلب الرسمي، وادعاءي التحقق من الصحة.

الشكل 7 لا يوضح بشكل أكبر المصنوعات الإثباتية المطلوبة، للتحقق، حيث أن GSN لا يدعم هذا. هذه وظيفة يدعمها SACM من خلال النموذج الفوقي للمصنوعات، الذي يسمح لنا بتسجيل الأنشطة، والمشاركين، والموارد، ومصنوعات الضمان الأخرى. يكمل الشكل 9 الحجة في الشكل 8 بالمصنوعات الإثباتية المختلفة، والعلاقات بينها. على سبيل المثال، الدليل الداعم للادعاء TIS_SFR1_C4 هو مرجع للمصنوع TIS_FSFR1_SPEC_THY وهو نظرية Isabelle التي تحتوي على إثبات النظرية المذكورة بواسطة TIS_SFR1_C4. يشير TIS_FSFR1_SPEC_THY عبر علاقة المصنوع TIS_SFR1_PROOF_ACTIVITY_REL إلى سياق الإثبات وهو المصنوع Isabelle_IT وإلى مؤلف الإثبات وهو Simon_Foster. هذا يوضح كيف يسمح لنا Isabelle/SACM بدمج المصنوعات والأنشطة غير الرسمية مع النتائج الرسمية التي تنتجها.

---

### Translation Notes

- **Figures referenced:** Figure 7 (TIS Claim Formalization), Figure 8 (TIS argument: Claims and their relations in Isabelle/SACM), Figure 9 (TIS argument: Artifacts and their relations in Isabelle/SACM)
- **Key terms introduced:**
  - Formalisation pattern (نمط الإضفاء الرسمي)
  - Justification (تبرير)
  - Evidential artifact (مصنوع إثباتي)
  - Artifact meta-model (النموذج الفوقي للمصنوعات)
  - Antiquotation (الاقتباس القديم)
- **Equations:** 0
- **Citations:** [9]
- **Special handling:**
  - Claim identifiers (TIS-SFR1-C1, etc.) kept in English
  - Command names (CLAIM, ASSERTED_INFERENCE) kept in English
  - Artifact names (TIS_FSFR1_SPEC_THY, etc.) kept in English
  - Author names (Simon_Foster) kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
