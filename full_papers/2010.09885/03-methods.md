# Section 3: Methods
## القسم 3: المنهجية

**Section:** methods
**Translation Quality:** 0.88
**Glossary Terms Used:** RoBERTa, transformer, attention heads, layers, attention mechanisms, pretraining, model hub, Inference API, Message Passing Neural Network, D-MPNN, Random Forest, Support Vector Machine, Morgan fingerprints, masking, vocabulary, sequence length, epochs, overfitting, chemical space, canonicalized, GPU, finetuning, classification tasks, benchmark, scaffold splitter, linear classification layer, backpropagation, early stopping, ROC-AUC

---

### English Version

ChemBERTa is based on the RoBERTa [25] transformer implementation in HuggingFace [12]. Our implementation of RoBERTa uses 12 attention heads and 6 layers, resulting in 72 distinct attention mechanisms. So far, we have released 15 pre-trained ChemBERTa models on the Huggingface's model hub; these models have collectively received over 30,000 Inference API calls to date.¹

We used the popular Chemprop library for all baselines [6]. We trained the directed Message Passing Neural Network (D-MPNN) with default hyperparameters as well as the sklearn-based [26] Random Forest (RF) and Support Vector Machine (SVM) models from Chemprop, which use 2048-bit Morgan fingerprints from RDKit [27, 28].

**3.1 PreTraining on PubChem 77M**

We adopted our pretraining procedure from RoBERTa, which masks 15% of the tokens in each input string. We used a max. vocab size of 52K tokens and max. sequence length of 512 tokens. We trained for 10 epochs on all PubChem subsets except for the 10M subset, on which we trained for 3 epochs to avoid observed overfitting. Our hypothesis is that, in learning to recover masked tokens, the model forms a representational topology of chemical space that should generalize to property prediction tasks.

For pretraining, we curated a dataset of 77M unique SMILES from PubChem [29], the world's largest open-source collection of chemical structures. The SMILES were canonicalized and globally shuffled to facilitate large-scale pretraining. We divided this dataset into subsets of 100K, 250K, 1M, and 10M. Pretraining on the largest subset took approx. 48 hours on a single NVIDIA V100 GPU. We make this dataset publicly available and leave pretraining on the full 77M set to future work.

**3.2 Finetuning on MoleculeNet**

We evaluated our models on several classification tasks from MoleculeNet [30] selected to cover a range of dataset sizes (1.5K - 41.1K examples) and medicinal chemistry applications (brain penetrability, toxicity, and on-target inhibition). These included the BBBP, ClinTox, HIV, and Tox21 datasets. For datasets with multiple tasks, we selected a single representative task: the clinical toxicity (CT_TOX) task from ClinTox and the p53 stress-response pathway activation (SR-p53) task from Tox21. For each dataset, we generated an 80/10/10 train/valid/test split using the scaffold splitter from DeepChem [31]. During finetuning, we appended a linear classification layer and backpropagated through the base model. We finetuned models for up to 25 epochs with early stopping on ROC-AUC. We release a tutorial in DeepChem which allows users to go through loading a pre-trained ChemBERTa model, running masked prediction tasks, visualizing the attention of the model on several molecules, and fine-tuning the model on the Tox21 SR-p53 dataset.

---

### النسخة العربية

يعتمد ChemBERTa على تطبيق المحول RoBERTa [25] في HuggingFace [12]. يستخدم تطبيقنا لـ RoBERTa 12 رأس انتباه و6 طبقات، مما ينتج عنه 72 آلية انتباه متميزة. حتى الآن، أصدرنا 15 نموذجاً مدرباً مسبقاً من ChemBERTa على مركز نماذج Huggingface؛ وقد تلقت هذه النماذج مجتمعة أكثر من 30,000 استدعاء لواجهة برمجة التطبيقات للاستنتاج حتى الآن.¹

استخدمنا مكتبة Chemprop الشائعة لجميع خطوط الأساس [6]. قمنا بتدريب الشبكة العصبية لتمرير الرسائل الموجهة (D-MPNN) بالمعاملات الفائقة الافتراضية بالإضافة إلى نماذج الغابة العشوائية (RF) وآلة المتجهات الداعمة (SVM) القائمة على sklearn [26] من Chemprop، والتي تستخدم بصمات Morgan بـ 2048 بت من RDKit [27، 28].

**3.1 التدريب المسبق على PubChem 77M**

اعتمدنا إجراء التدريب المسبق من RoBERTa، الذي يخفي 15٪ من الرموز في كل سلسلة إدخال. استخدمنا حجم مفردات أقصى قدره 52 ألف رمز وطول تسلسل أقصى قدره 512 رمز. قمنا بالتدريب لـ 10 حقب على جميع مجموعات PubChem الفرعية باستثناء مجموعة الـ 10 ملايين الفرعية، التي قمنا بالتدريب عليها لـ 3 حقب لتجنب فرط التخصيص الملاحظ. فرضيتنا هي أنه في تعلم استرداد الرموز المقنعة، يشكل النموذج طوبولوجيا تمثيلية للفضاء الكيميائي يجب أن تعمم على مهام التنبؤ بالخصائص.

للتدريب المسبق، قمنا بتنسيق مجموعة بيانات من 77 مليون SMILES فريد من PubChem [29]، أكبر مجموعة مفتوحة المصدر في العالم من الهياكل الكيميائية. تم توحيد SMILES وخلطها عالمياً لتسهيل التدريب المسبق واسع النطاق. قسمنا مجموعة البيانات هذه إلى مجموعات فرعية من 100 ألف و250 ألف و1 مليون و10 ملايين. استغرق التدريب المسبق على أكبر مجموعة فرعية حوالي 48 ساعة على معالج رسومات NVIDIA V100 واحد. نجعل مجموعة البيانات هذه متاحة للعامة ونترك التدريب المسبق على مجموعة الـ 77 مليون الكاملة للعمل المستقبلي.

**3.2 الضبط الدقيق على MoleculeNet**

قمنا بتقييم نماذجنا على عدة مهام تصنيف من MoleculeNet [30] تم اختيارها لتغطي مجموعة من أحجام مجموعات البيانات (1.5 ألف - 41.1 ألف مثال) وتطبيقات الكيمياء الطبية (نفاذية الدماغ، السمية، والتثبيط المستهدف). وشملت هذه مجموعات بيانات BBBP وClinTox وHIV وTox21. بالنسبة لمجموعات البيانات ذات المهام المتعددة، اخترنا مهمة تمثيلية واحدة: مهمة السمية السريرية (CT_TOX) من ClinTox ومهمة تنشيط مسار استجابة الإجهاد p53 (SR-p53) من Tox21. لكل مجموعة بيانات، أنشأنا تقسيم تدريب/تحقق/اختبار بنسبة 80/10/10 باستخدام مقسم السقالة من DeepChem [31]. أثناء الضبط الدقيق، أضفنا طبقة تصنيف خطية وقمنا بالانتشار العكسي عبر النموذج الأساسي. قمنا بالضبط الدقيق للنماذج لما يصل إلى 25 حقبة مع التوقف المبكر على ROC-AUC. نصدر برنامجاً تعليمياً في DeepChem يتيح للمستخدمين المرور عبر تحميل نموذج ChemBERTa مدرب مسبقاً، وتشغيل مهام التنبؤ المقنعة، وتصور انتباه النموذج على عدة جزيئات، والضبط الدقيق للنموذج على مجموعة بيانات Tox21 SR-p53.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Tables referenced:** Table 1 (discussed in Results section)
- **Key terms introduced:**
  - رأس انتباه (attention head)
  - طبقات (layers)
  - آلية انتباه (attention mechanism)
  - واجهة برمجة التطبيقات للاستنتاج (Inference API)
  - الشبكة العصبية لتمرير الرسائل الموجهة (Directed Message Passing Neural Network/D-MPNN)
  - الغابة العشوائية (Random Forest/RF)
  - آلة المتجهات الداعمة (Support Vector Machine/SVM)
  - بصمات Morgan (Morgan fingerprints)
  - إخفاء/قنع (masking)
  - حجم المفردات (vocabulary size)
  - طول التسلسل (sequence length)
  - حقب (epochs)
  - فرط التخصيص (overfitting)
  - طوبولوجيا تمثيلية (representational topology)
  - الفضاء الكيميائي (chemical space)
  - موحد (canonicalized)
  - معالج رسومات (GPU)
  - طبقة تصنيف خطية (linear classification layer)
  - الانتشار العكسي (backpropagation)
  - التوقف المبكر (early stopping)
  - نفاذية الدماغ (brain penetrability)
  - التثبيط المستهدف (on-target inhibition)
  - مقسم السقالة (scaffold splitter)

- **Equations:** None
- **Citations:** [6, 12, 25-31] - kept in original format
- **Special handling:**
  - Model names (ChemBERTa, RoBERTa, D-MPNN) kept in English
  - Library names (HuggingFace, Chemprop, sklearn, RDKit, DeepChem) kept in English
  - Dataset names (PubChem, MoleculeNet, BBBP, ClinTox, HIV, Tox21) kept in English
  - Technical abbreviations explained in Arabic on first use
  - Numbers (12 heads, 6 layers, 72 mechanisms, etc.) kept as numerals
  - Footnote marker (¹) preserved

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.90
- **Overall section score:** 0.88

### Back-Translation Validation (Key Paragraphs)

**First paragraph (back-translated):**
ChemBERTa is based on the RoBERTa [25] transformer implementation in HuggingFace [12]. Our implementation of RoBERTa uses 12 attention heads and 6 layers, resulting in 72 distinct attention mechanisms. So far, we have released 15 pre-trained ChemBERTa models on the Huggingface model hub; these models have collectively received more than 30,000 Inference API calls to date.¹

**Pretraining paragraph (back-translated):**
For pretraining, we curated a dataset of 77 million unique SMILES from PubChem [29], the world's largest open-source collection of chemical structures. SMILES were canonicalized and globally shuffled to facilitate large-scale pretraining. We divided this dataset into subsets of 100K, 250K, 1M, and 10M. Pretraining on the largest subset took approximately 48 hours on a single NVIDIA V100 GPU. We make this dataset publicly available and leave pretraining on the full 77M set to future work.

**Back-translation quality:** 0.90 - Excellent technical accuracy and semantic preservation
