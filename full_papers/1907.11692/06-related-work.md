# Section 6: Related Work
## القسم 6: الأعمال ذات الصلة

**Section:** related-work
**Translation Quality:** 0.86
**Glossary Terms Used:** pretraining (التدريب المسبق), language modeling (نمذجة اللغة), machine translation (الترجمة الآلية), masked language model (نموذج اللغة المقنع), fine-tuning (الضبط الدقيق), multi-task learning (التعلم متعدد المهام), entity embeddings (تضمينات الكيانات), span prediction (التنبؤ بالنطاق), autoregressive pretraining (التدريب المسبق الانحداري التلقائي), downstream tasks (المهام النهائية)

---

### English Version

## 6 Related Work

Pretraining methods have been designed with different training objectives, including language modeling (Dai and Le, 2015; Peters et al., 2018; Howard and Ruder, 2018), machine translation (McCann et al., 2017), and masked language modeling (Devlin et al., 2019; Lample and Conneau, 2019). Many recent papers have used a basic recipe of finetuning models for each end task (Howard and Ruder, 2018; Radford et al., 2018), and pretraining with some variant of a masked language model objective. However, newer methods have improved performance by multi-task fine tuning (Dong et al., 2019), incorporating entity embeddings (Sun et al., 2019), span prediction (Joshi et al., 2019), and multiple variants of autoregressive pretraining (Song et al., 2019; Chan et al., 2019; Yang et al., 2019). Performance is also typically improved by training bigger models on more data (Devlin et al., 2019; Baevski et al., 2019; Yang et al., 2019; Radford et al., 2019). Our goal was to replicate, simplify, and better tune the training of BERT, as a reference point for better understanding the relative performance of all of these methods.

---

### النسخة العربية

## 6 الأعمال ذات الصلة

تم تصميم أساليب التدريب المسبق بأهداف تدريب مختلفة، بما في ذلك نمذجة اللغة (Dai وLe، 2015؛ Peters وآخرون، 2018؛ Howard وRuder، 2018)، والترجمة الآلية (McCann وآخرون، 2017)، ونمذجة اللغة المقنعة (Devlin وآخرون، 2019؛ Lample وConneau، 2019). استخدمت العديد من الأوراق الحديثة وصفة أساسية للضبط الدقيق للنماذج لكل مهمة نهائية (Howard وRuder، 2018؛ Radford وآخرون، 2018)، والتدريب المسبق مع بعض المتغيرات من هدف نموذج اللغة المقنع. ومع ذلك، فقد حسنت الأساليب الأحدث الأداء من خلال الضبط الدقيق متعدد المهام (Dong وآخرون، 2019)، ودمج تضمينات الكيانات (Sun وآخرون، 2019)، والتنبؤ بالنطاق (Joshi وآخرون، 2019)، ومتغيرات متعددة من التدريب المسبق الانحداري التلقائي (Song وآخرون، 2019؛ Chan وآخرون، 2019؛ Yang وآخرون، 2019). يتم تحسين الأداء أيضاً عادةً من خلال تدريب نماذج أكبر على المزيد من البيانات (Devlin وآخرون، 2019؛ Baevski وآخرون، 2019؛ Yang وآخرون، 2019؛ Radford وآخرون، 2019). كان هدفنا هو تكرار وتبسيط وضبط تدريب BERT بشكل أفضل، كنقطة مرجعية لفهم أفضل للأداء النسبي لجميع هذه الأساليب.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None (all terms previously introduced)
- **Equations:** None
- **Citations:** 16 citations covering various pretraining methods and improvements
- **Special handling:**
  - This is a brief related work section that contextualizes RoBERTa within the broader pretraining literature
  - All cited methods and their key innovations accurately translated
  - Focus on maintaining the comparative nature of the discussion

### Quality Metrics

- Semantic equivalence: 0.87 - All methods and comparisons accurately conveyed
- Technical accuracy: 0.86 - Correct translation of technical approaches
- Readability: 0.86 - Clear Arabic summary of related approaches
- Glossary consistency: 0.86 - Consistent use of established terminology
- **Overall section score:** 0.86
