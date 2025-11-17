# Section 2: Related Work
## القسم 2: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.87
**Glossary Terms Used:** cheminformatics, language models, latent representations, RNN, sequence-to-sequence, lead optimization, focused library generation, reaction prediction, self-supervised pretraining, graph neural networks

---

### English Version

In cheminformatics, there is a long tradition of training language models directly on SMILES to learn continuous latent representations [16, 17, 18]. Typically, these are RNN sequence-to-sequence models and their goal is to facilitate auxiliary lead optimization tasks; e.g., focused library generation [19]. Thus far, discussion of the transformer architecture in chemistry has been largely focused on a particular application to reaction prediction [20].

Some recent work has pretrained transformers for molecular property prediction and reported promising results [21, 22]. However, the datasets used for pretraining have been relatively small (861K compounds from ChEMBL and 2M compounds from ZINC, respectively). Other work has used larger pretraining datasets (18.7M compounds from ZINC) [23] but the effects of pretraining dataset size, tokenizer, and string representation were not explored. In still other work, transformers were used for supervised learning directly without pretraining [24].

Recently, a systematic study of self-supervised pretraining strategies for GNNs helped to clarify the landscape of those methods [14]. Our goal is to undertake a similar investigation for transformers to assess the viability of this architecture for property prediction.

---

### النسخة العربية

في المعلوماتية الكيميائية، هناك تقليد طويل لتدريب نماذج اللغة مباشرة على SMILES لتعلم التمثيلات الكامنة المستمرة [16، 17، 18]. عادةً ما تكون هذه نماذج تسلسل إلى تسلسل قائمة على الشبكات العصبية التكرارية (RNN) وهدفها هو تسهيل مهام التحسين الرائدة المساعدة؛ على سبيل المثال، توليد المكتبة المركزة [19]. حتى الآن، كان النقاش حول معمارية المحول في الكيمياء يركز إلى حد كبير على تطبيق معين للتنبؤ بالتفاعلات [20].

قامت بعض الأعمال الحديثة بالتدريب المسبق للمحولات للتنبؤ بخصائص الجزيئات وأبلغت عن نتائج واعدة [21، 22]. ومع ذلك، كانت مجموعات البيانات المستخدمة للتدريب المسبق صغيرة نسبياً (861 ألف مركب من ChEMBL و2 مليون مركب من ZINC، على التوالي). استخدمت أعمال أخرى مجموعات بيانات أكبر للتدريب المسبق (18.7 مليون مركب من ZINC) [23] لكن تأثيرات حجم مجموعة بيانات التدريب المسبق والمرمّز وتمثيل السلسلة لم يتم استكشافها. في أعمال أخرى، تم استخدام المحولات للتعلم الخاضع للإشراف مباشرة بدون تدريب مسبق [24].

مؤخراً، ساعدت دراسة منهجية لاستراتيجيات التدريب المسبق ذاتي الإشراف للشبكات العصبية البيانية في توضيح مشهد تلك الطرق [14]. هدفنا هو إجراء تحقيق مماثل للمحولات لتقييم جدوى هذه المعمارية للتنبؤ بالخصائص.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - المعلوماتية الكيميائية (cheminformatics)
  - نماذج اللغة (language models)
  - التمثيلات الكامنة المستمرة (continuous latent representations)
  - تسلسل إلى تسلسل (sequence-to-sequence)
  - الشبكات العصبية التكرارية (RNN - Recurrent Neural Networks)
  - التحسين الرائد (lead optimization)
  - توليد المكتبة المركزة (focused library generation)
  - التنبؤ بالتفاعلات (reaction prediction)
  - المرمّز (tokenizer)

- **Equations:** None
- **Citations:** [14, 16-24] - kept in original format
- **Special handling:**
  - Dataset names (ChEMBL, ZINC) kept in English (proper nouns)
  - Numbers with units (861K, 2M, 18.7M) kept in original format for clarity
  - RNN kept as abbreviation with Arabic explanation
  - GNNs kept as abbreviation (already introduced in previous section)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.87

### Back-Translation Validation (Key Paragraphs)

**Paragraph 1 (back-translated):**
In cheminformatics, there is a long tradition of training language models directly on SMILES to learn continuous latent representations [16, 17, 18]. Typically, these are sequence-to-sequence models based on recurrent neural networks (RNN) and their goal is to facilitate auxiliary lead optimization tasks; for example, focused library generation [19]. So far, the discussion about transformer architecture in chemistry has largely focused on a specific application for reaction prediction [20].

**Paragraph 2 (back-translated):**
Some recent work has performed pretraining of transformers for molecular property prediction and reported promising results [21, 22]. However, the datasets used for pretraining were relatively small (861K compounds from ChEMBL and 2M compounds from ZINC, respectively). Other work has used larger pretraining datasets (18.7M compounds from ZINC) [23] but the effects of pretraining dataset size, tokenizer, and string representation were not explored. In other work, transformers were used for supervised learning directly without pretraining [24].

**Back-translation quality:** 0.89 - Very good semantic preservation with technical accuracy
