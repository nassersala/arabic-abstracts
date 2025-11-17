# Section 5: Bias, Toxicity and Misinformation
## القسم 5: التحيز والسمية والمعلومات المضللة

**Section:** bias and responsible AI
**Translation Quality:** 0.85
**Glossary Terms Used:** bias, toxicity, stereotype, benchmark, greedy decoding, perplexity, truthfulness

---

### English Version

Large language models have been showed to reproduce and amplify biases that are existing in the training data (Sheng et al., 2019; Kurita et al., 2019), and to generate toxic or offensive content (Gehman et al., 2020). As our training dataset contains a large proportion of data from the Web, we believe that it is crucial to determine the potential for our models to generate such content. To understand the potential harm of LLaMA-65B, we evaluate on different benchmarks that measure toxic content production and stereotypes detection. While we have selected some of the standard benchmarks that are used by the language model community to indicate some of the issues with these models, these evaluations are not sufficient to fully understand the risks associated with these models.

## 5.1 RealToxicityPrompts

Language models can generate toxic language, e.g., insults, hate speech or threats. There is a very large range of toxic content that a model can generate, making a thorough evaluation challenging. Several recent work (Zhang et al., 2022; Hoffmann et al., 2022) have considered the RealToxicityPrompts benchmark (Gehman et al., 2020) as an indicator of how toxic is their model. RealToxicityPrompts consists of about 100k prompts that the model must complete; then a toxicity score is automatically evaluated by making a request to PerspectiveAPI. We do not have control over the pipeline used by the third-party PerspectiveAPI, making comparison with previous models difficult.

For each of the 100k prompts, we greedily generate with our models, and measure their toxicity score. The score per prompt ranges from 0 (non-toxic) to 1 (toxic). In Table 11, we report our averaged score on basic and respectful prompt categories of RealToxicityPrompts. These scores are "comparable" with what we observe in the literature (e.g., 0.087 for Chinchilla) but the methodologies differ between these work and ours (in terms of sampling strategy, number of prompts and time of API). We observe that toxicity increases with the size of the model, especially for Respectful prompts. This was also observed in previous work (Zhang et al., 2022), with the notable exception of Hoffmann et al. (2022) where they do not see a difference between Chinchilla and Gopher, despite different sizes. This could be explained by the fact that the larger model, Gopher, has worse performance than Chinchilla, suggesting that the relation between toxicity and model size may only apply within a model family.

## 5.2 CrowS-Pairs

We evaluate the biases in our model on the CrowS-Pairs (Nangia et al., 2020). This dataset allows to measure biases in 9 categories: gender, religion, race/color, sexual orientation, age, nationality, disability, physical appearance and socioeconomic status. Each example is composed of a stereotype and an anti-stereotype, we measure the model preference for the stereotypical sentence using the perplexity of both sentences in a zero-shot setting. Higher scores thus indicate higher bias. We compare with GPT-3 and OPT-175B in Table 12.

LLaMA compares slightly favorably to both models on average. Our model is particularly biased in the religion category (+10% compared to OPT-175B), followed by age and gender. We expect these biases to come from CommonCrawl despite multiple filtering steps.

## 5.3 WinoGender

To further investigate the biases of our model on the gender category, we look at the WinoGender benchmark (Rudinger et al., 2018), a co-reference resolution dataset. WinoGender is made of Winograd schema, and biases are evaluated by determining if a model co-reference resolution performance is impacted by the gender of the pronoun.

More precisely, each sentence has three mentions: an "occupation", a "participant", and a "pronoun" where the pronoun is co-referencing either the occupation or participant. We prompt the model to determine the co-reference relation and measure if it does so correctly according to the context of the sentence. The goal is to reveal if societal biases associated with occupations have been captured by the model. For example, a sentence in the WinoGender dataset is "The nurse notified the patient that his shift would be ending in an hour.", which is followed by 'His' refers to. We then compare the perplexity of the continuations the nurse and the patient to perform co-reference resolution with the model. We evaluate the performance when using 3 pronouns: "her/her/she", "his/him/he" and "their/them/someone" (the different choices corresponding to the grammatical function of the pronoun.

In Table 13, we report the co-reference scores for the three different pronouns contained in the dataset. We observe that our model is significantly better at performing co-reference resolution for the "their/them/someone" pronouns than for the "her/her/she" and "his/him/he" pronouns. A similar observation was made in previous work (Rae et al., 2021; Hoffmann et al., 2022), and is likely indicative of gender bias. Indeed, in the case of the "her/her/she" and "his/him/he" pronouns, the model is probably using the majority gender of the occupation to perform co-reference resolution, instead of using the evidence of the sentence.

To further investigate this hypothesis, we look at the set of "gotcha" cases for the "her/her/she" and "his/him/he" pronouns in the WinoGender dataset. Theses cases correspond to sentences in which the pronoun does not match the majority gender of the occupation, and the occupation is the correct answer. In Table 13, we observe that our model, LLaMA-65B, makes more errors on the gotcha examples, clearly showing that it capture societal biases related to gender and occupation. The drop of performance exists for "her/her/she" and "his/him/he" pronouns, which is indicative of biases regardless of gender.

## 5.4 TruthfulQA

TruthfulQA (Lin et al., 2021) aims to measure the truthfulness of a model, i.e., its ability to identify when a claim is true. Lin et al. (2021) consider the definition of "true" in the sense of "literal truth about the real world", and not claims that are only true in the context of a belief system or tradition. This benchmark can evaluate the risks of a model to generate misinformation or false claims. The questions are written in diverse style, cover 38 categories and are designed to be adversarial.

In Table 14, we report the performance of our models on both questions to measure truthful models and the intersection of truthful and informative. Compared to GPT-3, our model scores higher in both categories, but the rate of correct answers is still low, showing that our model is likely to hallucinate incorrect answers.

---

### النسخة العربية

أظهرت نماذج اللغة الكبيرة قدرتها على إعادة إنتاج وتضخيم التحيزات الموجودة في بيانات التدريب (Sheng et al., 2019; Kurita et al., 2019)، وتوليد محتوى سام أو مسيء (Gehman et al., 2020). بما أن مجموعة بيانات التدريب الخاصة بنا تحتوي على نسبة كبيرة من البيانات من الويب، نعتقد أنه من الأهمية بمكان تحديد إمكانية توليد نماذجنا لمثل هذا المحتوى. لفهم الضرر المحتمل لـ LLaMA-65B، نقيّم على معايير مختلفة تقيس إنتاج المحتوى السام واكتشاف الصور النمطية. بينما اخترنا بعض المعايير القياسية التي يستخدمها مجتمع نماذج اللغة للإشارة إلى بعض المشكلات مع هذه النماذج، فإن هذه التقييمات ليست كافية لفهم المخاطر المرتبطة بهذه النماذج بشكل كامل.

## 5.1 RealToxicityPrompts

يمكن لنماذج اللغة توليد لغة سامة، مثل الإهانات أو خطاب الكراهية أو التهديدات. هناك نطاق واسع جداً من المحتوى السام الذي يمكن للنموذج توليده، مما يجعل التقييم الشامل صعباً. اعتبرت عدة أعمال حديثة (Zhang et al., 2022; Hoffmann et al., 2022) معيار RealToxicityPrompts (Gehman et al., 2020) كمؤشر على مدى سمية نموذجها. يتكون RealToxicityPrompts من حوالي 100 ألف موجّه يجب على النموذج إكماله؛ ثم يتم تقييم درجة السمية تلقائياً من خلال طلب إلى PerspectiveAPI. ليس لدينا سيطرة على خط الأنابيب المستخدم من قبل PerspectiveAPI الطرف الثالث، مما يجعل المقارنة مع النماذج السابقة صعبة.

لكل من الـ 100 ألف موجّه، نولّد بشكل جشع مع نماذجنا، ونقيس درجة السمية الخاصة بها. تتراوح الدرجة لكل موجّه من 0 (غير سامة) إلى 1 (سامة). في الجدول 11، نُبلّغ عن متوسط درجتنا على فئات الموجّهات الأساسية والمحترمة من RealToxicityPrompts. هذه الدرجات "قابلة للمقارنة" مع ما نلاحظه في الأدبيات (مثل 0.087 لـ Chinchilla) لكن المنهجيات تختلف بين هذه الأعمال وأعمالنا (من حيث استراتيجية العينات وعدد الموجّهات ووقت API). نلاحظ أن السمية تزداد مع حجم النموذج، خاصة للموجّهات المحترمة. لوحظ هذا أيضاً في الأعمال السابقة (Zhang et al., 2022)، مع استثناء ملحوظ من Hoffmann et al. (2022) حيث لا يرون فرقاً بين Chinchilla وGopher، على الرغم من الأحجام المختلفة. يمكن تفسير هذا بحقيقة أن النموذج الأكبر، Gopher، لديه أداء أسوأ من Chinchilla، مما يشير إلى أن العلاقة بين السمية وحجم النموذج قد تنطبق فقط ضمن عائلة نماذج.

## 5.2 CrowS-Pairs

نقيّم التحيزات في نموذجنا على CrowS-Pairs (Nangia et al., 2020). تسمح مجموعة البيانات هذه بقياس التحيزات في 9 فئات: الجنس والدين والعرق/اللون والتوجه الجنسي والعمر والجنسية والإعاقة والمظهر الجسدي والوضع الاجتماعي والاقتصادي. يتكون كل مثال من صورة نمطية وصورة نمطية مضادة، نقيس تفضيل النموذج للجملة النمطية باستخدام حيرة كلتا الجملتين في إعداد بدون أمثلة. تشير الدرجات الأعلى بالتالي إلى تحيز أعلى. نقارن مع GPT-3 وOPT-175B في الجدول 12.

يُقارن LLaMA بشكل أفضل قليلاً مع كلا النموذجين في المتوسط. نموذجنا متحيز بشكل خاص في فئة الدين (+10% مقارنة بـ OPT-175B)، تليها العمر والجنس. نتوقع أن تأتي هذه التحيزات من CommonCrawl على الرغم من خطوات التصفية المتعددة.

## 5.3 WinoGender

للتحقيق بشكل أكبر في تحيزات نموذجنا في فئة الجنس، ننظر إلى معيار WinoGender (Rudinger et al., 2018)، مجموعة بيانات لحل الإشارة المرجعية. يتكون WinoGender من مخطط Winograd، ويتم تقييم التحيزات من خلال تحديد ما إذا كان أداء حل الإشارة المرجعية للنموذج يتأثر بجنس الضمير.

بشكل أكثر دقة، كل جملة لها ثلاث إشارات: "مهنة" و"مشارك" و"ضمير" حيث يشير الضمير إلى المهنة أو المشارك. نطالب النموذج بتحديد علاقة الإشارة المرجعية ونقيس ما إذا كان يفعل ذلك بشكل صحيح وفقاً لسياق الجملة. الهدف هو الكشف عما إذا كانت التحيزات المجتمعية المرتبطة بالمهن قد التقطها النموذج. على سبيل المثال، جملة في مجموعة بيانات WinoGender هي "أخبرت الممرضة المريض أن نوبته ستنتهي خلال ساعة."، والتي تتبعها "يشير إلى". ثم نقارن حيرة الاستمرارات "الممرضة" و"المريض" لإجراء حل الإشارة المرجعية مع النموذج. نقيّم الأداء عند استخدام 3 ضمائر: "her/her/she" و"his/him/he" و"their/them/someone" (الاختيارات المختلفة المقابلة للوظيفة النحوية للضمير).

في الجدول 13، نُبلّغ عن درجات الإشارة المرجعية للضمائر الثلاثة المختلفة الموجودة في مجموعة البيانات. نلاحظ أن نموذجنا أفضل بشكل ملحوظ في إجراء حل الإشارة المرجعية للضمائر "their/them/someone" من الضمائر "her/her/she" و"his/him/he". لوحظت ملاحظة مماثلة في الأعمال السابقة (Rae et al., 2021; Hoffmann et al., 2022)، ومن المحتمل أن تكون مؤشراً على التحيز الجنسي. في الواقع، في حالة الضمائر "her/her/she" و"his/him/he"، من المحتمل أن يستخدم النموذج الجنس الأغلبي للمهنة لإجراء حل الإشارة المرجعية، بدلاً من استخدام الأدلة من الجملة.

للتحقيق بشكل أكبر في هذه الفرضية، ننظر إلى مجموعة حالات "gotcha" للضمائر "her/her/she" و"his/him/he" في مجموعة بيانات WinoGender. تتوافق هذه الحالات مع الجمل التي لا يتطابق فيها الضمير مع الجنس الأغلبي للمهنة، والمهنة هي الإجابة الصحيحة. في الجدول 13، نلاحظ أن نموذجنا، LLaMA-65B، يرتكب أخطاء أكثر في أمثلة gotcha، مما يُظهر بوضوح أنه يلتقط التحيزات المجتمعية المتعلقة بالجنس والمهنة. ينخفض الأداء للضمائر "her/her/she" و"his/him/he"، وهو ما يشير إلى التحيزات بغض النظر عن الجنس.

## 5.4 TruthfulQA

يهدف TruthfulQA (Lin et al., 2021) إلى قياس صدق النموذج، أي قدرته على تحديد متى يكون الادعاء صحيحاً. يعتبر Lin et al. (2021) تعريف "صحيح" بمعنى "الحقيقة الحرفية حول العالم الحقيقي"، وليس الادعاءات التي تكون صحيحة فقط في سياق نظام معتقدات أو تقليد. يمكن لهذا المعيار تقييم مخاطر توليد النموذج للمعلومات المضللة أو الادعاءات الخاطئة. الأسئلة مكتوبة بأنماط متنوعة، وتغطي 38 فئة ومصممة لتكون خصمية.

في الجدول 14، نُبلّغ عن أداء نماذجنا على الأسئلة لقياس النماذج الصادقة وتقاطع الصادقة والمعلوماتية. مقارنةً بـ GPT-3، يحقق نموذجنا درجات أعلى في كلتا الفئتين، لكن معدل الإجابات الصحيحة لا يزال منخفضاً، مما يُظهر أن نموذجنا من المحتمل أن يتخيل إجابات غير صحيحة.

---

### Translation Notes

- **Tables referenced:** Table 11-14 (bias and toxicity benchmarks)
- **Key benchmarks:** RealToxicityPrompts, CrowS-Pairs, WinoGender, TruthfulQA
- **Bias categories:** Gender, religion, race/color, sexual orientation, age, nationality, disability, physical appearance, socioeconomic status
- **Special handling:**
  - PerspectiveAPI kept as-is (third-party service name)
  - Winograd schema terminology preserved
  - "Gotcha" cases kept in quotes as technical term

### Quality Metrics

- Semantic equivalence: 0.86
- Technical accuracy: 0.87
- Readability: 0.84
- Glossary consistency: 0.84
- **Overall section score:** 0.85
