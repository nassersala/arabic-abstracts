# Section 8: Conclusion and Future Work
## القسم 8: الخلاصة والعمل المستقبلي

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** transformer, robustness, code intelligence, code transformation, abstract syntax tree, positional encoding, pre-trained models

---

### English Version

## 8 CONCLUSION AND FUTURE WORK

In this study, we have empirically investigated the robustness and limitations of Transformer on code intelligence. We implement 27 and 24 code transformation strategies for Java and Python languages respectively and apply the transformed code to three code intelligence tasks to study the effect on Transformer. Experimental results demonstrate that insertion / deletion transformation and identifier transformation have the great impact on Transformer's performance. Transformer based on ASTs shows more robust performance than the model based on only code sequence under most code transformations. Besides, the robustness of Transformer under code transformation is impacted by the design of positional encoding. Based on the findings, we summarize some future directions for improving the robustness of Transformer on code intelligence.

In the future, we plan to investigate the robustness of pre-trained models under code transformation. Moreover, we plan to collect more open-source projects to reproduce our experiments and to support more programming languages in our code transformation.

---

### النسخة العربية

## 8 الخلاصة والعمل المستقبلي

في هذه الدراسة، قمنا بالتحقيق التجريبي في متانة وقيود المحول في ذكاء الشفرة. قمنا بتنفيذ 27 و24 استراتيجية تحويل شفرة للغتي جافا وبايثون على التوالي وطبقنا الشفرة المُحولة على ثلاث مهام ذكاء شفرة لدراسة التأثير على المحول. تُظهر النتائج التجريبية أن تحويل الإدراج/الحذف وتحويل المعرف لهما تأثير كبير على أداء المحول. يُظهر المحول القائم على ASTs أداءً أكثر متانة من النموذج القائم على تسلسل الشفرة فقط تحت معظم تحويلات الشفرة. بالإضافة إلى ذلك، تتأثر متانة المحول تحت تحويل الشفرة بتصميم الترميز الموضعي. بناءً على النتائج، نلخص بعض الاتجاهات المستقبلية لتحسين متانة المحول في ذكاء الشفرة.

في المستقبل، نخطط للتحقيق في متانة النماذج المُدربة مسبقاً تحت تحويل الشفرة. علاوة على ذلك، نخطط لجمع المزيد من المشاريع مفتوحة المصدر لإعادة إنتاج تجاربنا ولدعم المزيد من لغات البرمجة في تحويل الشفرة الخاص بنا.

---

### Translation Notes

- **Key findings summarized:**
  - Insertion/deletion and identifier transformations have greatest impact
  - AST-based models more robust than sequence-only models
  - Positional encoding design impacts robustness

- **Future directions:**
  - Investigate pre-trained model robustness
  - Expand to more open-source projects
  - Support additional programming languages

- **Key terms used:**
  - Limitations (قيود)
  - Empirical investigation (تحقيق تجريبي)
  - Future directions (اتجاهات مستقبلية)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
