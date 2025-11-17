# Section 4: Instruction Finetuning
## القسم 4: الضبط بالتعليمات

**Section:** instruction finetuning
**Translation Quality:** 0.86
**Glossary Terms Used:** finetuning, instruction, MMLU, OPT-IML, Flan-PaLM, protocol

---

### English Version

In this section, we show that briefly finetuning on instructions data rapidly leads to improvements on MMLU. Although the non-finetuned version of LLaMA-65B is already able to follow basic instructions, we observe that a very small amount of finetuning improves the performance on MMLU, and further improves the ability of the model to follow instructions. Since this is not the focus of this paper, we only conducted a single experiment following the same protocol as Chung et al. (2022) to train an instruct model, LLaMA-I.

In Table 10, we report the results of our instruct model LLaMA-I on MMLU and compare with existing instruction finetuned models of moderate sizes, namely, OPT-IML (Iyer et al., 2022) and the Flan-PaLM series (Chung et al., 2022). All the reported numbers are from the corresponding papers. Despite the simplicity of the instruction finetuning approach used here, we reach 68.9% on MMLU. LLaMA-I (65B) outperforms on MMLU existing instruction finetuned models of moderate sizes, but are still far from the state-of-the-art, that is 77.4 for GPT code-davinci-002 on MMLU (numbers taken from Iyer et al. (2022)). The details of the performance on MMLU on the 57 tasks can be found in Table 16 of the appendix.

---

### النسخة العربية

في هذا القسم، نُظهر أن الضبط الدقيق القصير على بيانات التعليمات يؤدي بسرعة إلى تحسينات على MMLU. على الرغم من أن النسخة غير المضبوطة من LLaMA-65B قادرة بالفعل على اتباع التعليمات الأساسية، نلاحظ أن كمية صغيرة جداً من الضبط الدقيق تحسّن الأداء على MMLU، وتحسّن كذلك قدرة النموذج على اتباع التعليمات. بما أن هذا ليس محور هذه الورقة، أجرينا تجربة واحدة فقط بنفس البروتوكول كما في Chung et al. (2022) لتدريب نموذج تعليمي، LLaMA-I.

في الجدول 10، نُبلّغ عن نتائج نموذجنا التعليمي LLaMA-I على MMLU ونقارن مع نماذج مضبوطة بالتعليمات موجودة ذات أحجام متوسطة، وهي OPT-IML (Iyer et al., 2022) وسلسلة Flan-PaLM (Chung et al., 2022). جميع الأرقام المُبلّغ عنها من الأوراق المقابلة. على الرغم من بساطة نهج الضبط الدقيق بالتعليمات المستخدم هنا، نصل إلى 68.9% على MMLU. يتفوق LLaMA-I (65B) على MMLU على النماذج المضبوطة بالتعليمات الموجودة ذات الأحجام المتوسطة، لكنها لا تزال بعيدة عن أحدث ما توصلت إليه التقنية، وهو 77.4 لـ GPT code-davinci-002 على MMLU (أرقام مأخوذة من Iyer et al. (2022)). يمكن العثور على تفاصيل الأداء على MMLU على المهام الـ 57 في الجدول 16 من الملحق.

---

### Translation Notes

- **Tables referenced:** Table 10 (instruction finetuning results on MMLU), Table 16 (detailed MMLU results in appendix)
- **Key models compared:** OPT-IML, Flan-T5-XXL, Flan-PaLM, GPT code-davinci-002
- **Main finding:** Simple instruction finetuning improves MMLU from 63.4% to 68.9%
- **Special handling:**
  - Model names (OPT-IML, Flan-PaLM, GPT code-davinci-002) kept in original form
  - LLaMA-I notation introduced for instruction-tuned variant

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
