# Section 4: Results
## القسم 4: النتائج

**Section:** results
**Translation Quality:** 0.87
**Glossary Terms Used:** downstream performance, baselines, ROC-AUC, PRC-AUC, class-imbalanced, scaling, pretraining data, robust representations, tokenization, Byte-Pair Encoder, BPE, character-level, word-level, vocabulary, subwords, regex, SELFIES, molecular string representation, attention visualization, attention heads, functional groups, aromatic rings, bracket closures, nested parentheses

---

### English Version

On the MoleculeNet tasks that we evaluated, ChemBERTa approaches, but does not beat, the strong baselines from Chemprop (Table 1).² Nevertheless, downstream performance of ChemBERTa scales well with more pretraining data (Fig. 1). On average, scaling from 100K to 10M resulted in ∆ROC-AUC = +0.110 and ∆PRC-AUC = +0.059. (HIV was omitted from this analysis due to resource constraints.) These results suggest that ChemBERTa learns more robust representations with additional data and is able to leverage this information when learning downstream tasks.

**Table 1:** Comparison of ChemBERTa pretrained on 10M PubChem compounds and Chemprop baselines on selected MoleculeNet tasks. We report both ROC-AUC and PRC-AUC to give a full picture of performance on class-imbalanced tasks.

| Dataset | Size | Model | ROC | PRC | ROC | PRC | ROC | PRC | ROC | PRC |
|---------|------|-------|-----|-----|-----|-----|-----|-----|-----|-----|
| BBBP | 2,039 | ChemBERTa 10M | 0.643 | 0.620 | - | - | - | - | - | - |
| | | D-MPNN | 0.708 | 0.697 | - | - | - | - | - | - |
| | | RF | 0.681 | 0.692 | - | - | - | - | - | - |
| | | SVM | 0.702 | 0.724 | - | - | - | - | - | - |
| ClinTox (CT_TOX) | 1,478 | ChemBERTa 10M | 0.733 | 0.975 | 0.622 | 0.119 | - | - | - | - |
| | | D-MPNN | 0.906 | 0.993 | 0.752 | 0.152 | - | - | - | - |
| | | RF | 0.693 | 0.968 | 0.780 | 0.383 | - | - | - | - |
| | | SVM | 0.833 | 0.986 | 0.763 | 0.364 | - | - | - | - |
| HIV | 41,127 | ChemBERTa 10M | - | - | - | - | 0.728 | 0.207 | - | - |
| | | D-MPNN | - | - | - | - | 0.688 | 0.429 | - | - |
| | | RF | - | - | - | - | 0.724 | 0.335 | - | - |
| | | SVM | - | - | - | - | 0.708 | 0.345 | - | - |

**Figure 1:** Scaling the pretraining size (100K, 250K, 1M, 10M) produces consistent improvements in downstream task performance on BBBP, ClinTox, and Tox21. Mean ∆AUC across all three tasks with a 68% confidence interval is shown in light blue.

**4.1 Tokenizers**

Our default tokenization strategy uses a Byte-Pair Encoder (BPE) from the HuggingFace tokenizers library [12]. BPE is a hybrid between character and word-level representations, which allows for the handling of large vocabularies in natural language corpora. Motivated by the intuition that rare and unknown words can often be decomposed into multiple known subwords, BPE finds the best word segmentation by iteratively and greedily merging frequent pairs of characters [32]. We compare this tokenization algorithm with a custom SmilesTokenizer based on a regex from [20], which we have released as part of DeepChem [31].³

To compare tokenizers, we pretrained two identical models on the PubChem-1M set. The pretrained models were evaluated on the Tox21 SR-p53 task. We found that the SmilesTokenizer narrowly outperformed BPE by ∆PRC-AUC = +0.015. Though this result suggests that a more semantically-relevant tokenization may provide performance benefits, further benchmarking on additional datasets is needed to validate this finding.

**4.2 SMILES vs. SELFIES**

In addition to SMILES, we pretrained ChemBERTA on SELFIES (SELF-referencing Embedded Strings) [15]. SELFIES is an alternate molecular string representation designed for machine learning. Because every valid SELFIES corresponds to a valid molecule, we hypothesized that SELFIES would lead to a more robust model. However, we found no significant difference in downstream performance on the Tox21 SR-p53 task. Further benchmarking is needed to validate this finding.

**4.3 Attention Visualization**

We used BertViz [13] to inspect the attention heads of ChemBERTa (SmilesTokenizer version) on Tox21, and contrast them to the molecular graph visualization of an attention-based GNN. We found certain neurons that were selective for chemically-relevant functional groups, and aromatic rings. We also observed other neurons that tracked bracket closures – a finding in keeping with results on attention-based RNNs showing the ability to track nested parentheses [33, 34].

**Figure 2:** (a) Attention in GNNs highlights a problematic ketone in a Tox21 compound. (b) Attention over SMILES tokens in ChemBERTa provides a close analogue to graph attention. (c) Neural stack trace enables fine-grained introspection of neuron behavior. (b - c) produced via BertViz [13].

---

### النسخة العربية

على مهام MoleculeNet التي قيمناها، يقترب ChemBERTa من خطوط الأساس القوية من Chemprop، لكنه لا يتفوق عليها (الجدول 1).² ومع ذلك، يتوسع الأداء النهائي لـ ChemBERTa بشكل جيد مع المزيد من بيانات التدريب المسبق (الشكل 1). في المتوسط، أدى التوسع من 100 ألف إلى 10 ملايين إلى ∆ROC-AUC = +0.110 و∆PRC-AUC = +0.059. (تم حذف HIV من هذا التحليل بسبب قيود الموارد.) تشير هذه النتائج إلى أن ChemBERTa يتعلم تمثيلات أكثر قوة مع بيانات إضافية وقادر على الاستفادة من هذه المعلومات عند تعلم المهام النهائية.

**الجدول 1:** مقارنة بين ChemBERTa المدرب مسبقاً على 10 ملايين مركب من PubChem وخطوط الأساس من Chemprop على مهام MoleculeNet المختارة. نبلغ عن كل من ROC-AUC وPRC-AUC لإعطاء صورة كاملة عن الأداء على المهام غير المتوازنة من حيث الفئات.

**الشكل 1:** توسيع حجم التدريب المسبق (100 ألف، 250 ألف، 1 مليون، 10 ملايين) ينتج تحسينات متسقة في أداء المهمة النهائية على BBBP وClinTox وTox21. يظهر متوسط ∆AUC عبر جميع المهام الثلاث مع فاصل ثقة 68٪ باللون الأزرق الفاتح.

**4.1 المرمّزات**

تستخدم استراتيجية الترميز الافتراضية لدينا مرمّز أزواج البايت (BPE) من مكتبة المرمّزات في HuggingFace [12]. يعتبر BPE مزيجاً بين تمثيلات مستوى الأحرف ومستوى الكلمات، مما يسمح بالتعامل مع مفردات كبيرة في مجموعات النصوص باللغة الطبيعية. مدفوعاً بالحدس أن الكلمات النادرة وغير المعروفة يمكن في كثير من الأحيان تحليلها إلى كلمات فرعية معروفة متعددة، يجد BPE أفضل تقسيم للكلمات من خلال دمج أزواج الأحرف المتكررة بشكل تكراري وجشع [32]. نقارن خوارزمية الترميز هذه مع SmilesTokenizer مخصص يعتمد على تعبير نمطي من [20]، والذي أصدرناه كجزء من DeepChem [31].³

لمقارنة المرمّزات، قمنا بالتدريب المسبق لنموذجين متطابقين على مجموعة PubChem-1M. تم تقييم النماذج المدربة مسبقاً على مهمة Tox21 SR-p53. وجدنا أن SmilesTokenizer تفوق بفارق ضئيل على BPE بمقدار ∆PRC-AUC = +0.015. على الرغم من أن هذه النتيجة تشير إلى أن الترميز الأكثر صلة من الناحية الدلالية قد يوفر فوائد في الأداء، إلا أن هناك حاجة إلى مزيد من المعايرة على مجموعات بيانات إضافية للتحقق من صحة هذه النتيجة.

**4.2 SMILES مقابل SELFIES**

بالإضافة إلى SMILES، قمنا بالتدريب المسبق لـ ChemBERTA على SELFIES (سلاسل مضمنة ذاتية الإشارة) [15]. SELFIES هو تمثيل سلسلة جزيئية بديل مصمم للتعلم الآلي. نظراً لأن كل SELFIES صالح يقابل جزيئاً صالحاً، افترضنا أن SELFIES سيؤدي إلى نموذج أكثر قوة. ومع ذلك، لم نجد فرقاً كبيراً في الأداء النهائي على مهمة Tox21 SR-p53. هناك حاجة إلى مزيد من المعايرة للتحقق من صحة هذه النتيجة.

**4.3 تصور الانتباه**

استخدمنا BertViz [13] لفحص رؤوس الانتباه في ChemBERTa (إصدار SmilesTokenizer) على Tox21، ومقارنتها بتصور الرسم البياني الجزيئي للشبكة العصبية البيانية القائمة على الانتباه. وجدنا خلايا عصبية معينة كانت انتقائية للمجموعات الوظيفية ذات الصلة الكيميائية، والحلقات العطرية. لاحظنا أيضاً خلايا عصبية أخرى تتبعت إغلاقات الأقواس - وهي نتيجة تتوافق مع النتائج على الشبكات العصبية التكرارية القائمة على الانتباه التي تظهر القدرة على تتبع الأقواس المتداخلة [33، 34].

**الشكل 2:** (أ) يسلط الانتباه في الشبكات العصبية البيانية الضوء على كيتون إشكالي في مركب Tox21. (ب) يوفر الانتباه على رموز SMILES في ChemBERTa نظيراً قريباً لانتباه الرسم البياني. (ج) يتيح تتبع المكدس العصبي فحصاً دقيقاً لسلوك الخلايا العصبية. (ب - ج) تم إنتاجهما عبر BertViz [13].

---

### Translation Notes

- **Figures referenced:**
  - Figure 1: Scaling pretraining size chart
  - Figure 2: Attention visualization comparison (3 subfigures a, b, c)
- **Tables referenced:**
  - Table 1: Performance comparison across models and datasets

- **Key terms introduced:**
  - الأداء النهائي (downstream performance)
  - خطوط الأساس (baselines)
  - ROC-AUC (kept as-is, standard metric abbreviation)
  - PRC-AUC (kept as-is, standard metric abbreviation)
  - غير المتوازنة من حيث الفئات (class-imbalanced)
  - التوسع (scaling)
  - تمثيلات أكثر قوة (robust representations)
  - مرمّز أزواج البايت (Byte-Pair Encoder/BPE)
  - مستوى الأحرف (character-level)
  - مستوى الكلمات (word-level)
  - كلمات فرعية (subwords)
  - تعبير نمطي (regex)
  - سلاسل مضمنة ذاتية الإشارة (SELF-referencing Embedded Strings/SELFIES)
  - تصور الانتباه (attention visualization)
  - رؤوس الانتباه (attention heads)
  - المجموعات الوظيفية (functional groups)
  - الحلقات العطرية (aromatic rings)
  - إغلاقات الأقواس (bracket closures)
  - الأقواس المتداخلة (nested parentheses)
  - كيتون (ketone)
  - تتبع المكدس العصبي (neural stack trace)

- **Equations:**
  - ∆ROC-AUC = +0.110
  - ∆PRC-AUC = +0.059
  - ∆PRC-AUC = +0.015

- **Citations:** [12, 13, 15, 20, 31, 32, 33, 34] - kept in original format
- **Special handling:**
  - Table 1 described but not fully reproduced (referenced in text)
  - Figure captions translated
  - Statistical notation (∆, %, etc.) preserved
  - Footnote markers (², ³) preserved
  - Dataset sizes (100K, 250K, 1M, 10M) kept as-is
  - Confidence interval (68%) preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.89
- **Overall section score:** 0.87

### Back-Translation Validation (Key Paragraphs)

**First paragraph (back-translated):**
On the MoleculeNet tasks we evaluated, ChemBERTa approaches the strong baselines from Chemprop, but does not surpass them (Table 1).² However, the downstream performance of ChemBERTa scales well with more pretraining data (Figure 1). On average, scaling from 100K to 10M resulted in ∆ROC-AUC = +0.110 and ∆PRC-AUC = +0.059. (HIV was removed from this analysis due to resource constraints.) These results indicate that ChemBERTa learns more robust representations with additional data and is able to leverage this information when learning downstream tasks.

**Tokenizers paragraph (back-translated):**
Our default tokenization strategy uses a Byte-Pair Encoder (BPE) from the tokenizers library in HuggingFace [12]. BPE is a hybrid between character-level and word-level representations, allowing for handling large vocabularies in natural language text collections. Driven by the intuition that rare and unknown words can often be decomposed into multiple known subwords, BPE finds the best word segmentation by iteratively and greedily merging frequent character pairs [32]. We compare this tokenization algorithm with a custom SmilesTokenizer based on a regular expression from [20], which we released as part of DeepChem [31].³

**Back-translation quality:** 0.89 - Very good technical accuracy and semantic preservation
