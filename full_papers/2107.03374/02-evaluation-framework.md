# Section 2: Evaluation Framework
## القسم 2: إطار التقييم

**Section:** methodology
**Translation Quality:** 0.87
**Glossary Terms Used:** معيار, الصحة الوظيفية, مجموعة بيانات, اختبار, دالة, خوارزمية

---

### English Version

In this section, we discuss the details of our evaluation framework. We begin by defining the pass@k metric, and explain its advantages over standard match-based metrics. Next, we describe the dataset of hand-written problems, called "HumanEval," which we created in order to benchmark our models. Finally, we discuss the sandbox environment we used to safely execute model-generated code.

#### 2.1. Functional Correctness

Generative models for code are predominantly benchmarked by matching samples against a reference solution, where the match can be exact or fuzzy (as in BLEU score). However, recent work has surfaced deficiencies in match-based metrics for code. For instance, Ren et al. (2020) finds that BLEU has problems capturing semantic features specific to code, and suggests several semantic modifications to the score.

More fundamentally, match-based metrics are unable to account for the large and complex space of programs functionally equivalent to a reference solution. As a consequence, recent works in unsupervised code translation (Lachaux et al., 2020) and pseudocode-to-code translation (Kulal et al., 2019) have turned to functional correctness instead, where a sample is considered correct if it passes a set of unit tests. We argue that this metric should be applied to docstring-conditional code generation as well.

Perhaps the most convincing reason to evaluate functional correctness is that it is used by human developers to judge code. A framework known as test-driven development dictates that software requirements be converted into test cases before any implementation begins, and success is defined by a program that passes these tests. While few organizations employ full test-driven development, integration of new code is usually dependent on creating and passing unit tests.

Kulal et al. (2019) evaluate functional correctness using the pass@k metric, where k code samples are generated per problem, a problem is considered solved if any sample passes the unit tests, and the total fraction of problems solved is reported. However, computing pass@k in this way can have high variance. Instead, to evaluate pass@k, we generate n ≥ k samples per task (in this paper, we use n = 200 and k ≤ 100), count the number of correct samples c ≤ n which pass unit tests, and calculate the unbiased estimator:

$$\text{pass}@k := \mathbb{E}_{\text{Problems}} \left[1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\right]$$

#### 2.2. HumanEval: Hand-Written Evaluation Set

We evaluate functional correctness on a set of 164 hand-written programming problems, which we call the HumanEval dataset. Each problem includes a function signature, docstring, body, and several unit tests, with an average of 7.7 tests per problem. It is important for these tasks to be hand-written, since our models are trained on a large fraction of GitHub, which already contains solutions to problems from a variety of sources. For example, there are more than ten public repositories containing solutions to Codeforces problems, which make up part of the recently proposed APPS dataset (Hendrycks et al., 2021).

Programming tasks in the HumanEval dataset assess language comprehension, reasoning, algorithms, and simple mathematics. We release the HumanEval dataset so that others can evaluate functional correctness and measure the problem-solving capabilities of their models. The dataset can be found at https://www.github.com/openai/human-eval.

#### 2.3. Sandbox for Executing Generated Programs

Since publicly available programs have unknown intent and generated programs are often incorrect, executing these programs poses a security risk. Indeed, GitHub is known to contain malicious programs that alter or change their environments (Rokon et al., 2020).

Therefore, we developed a sandbox environment to safely run untrusted programs against unit tests. Our goals were to prevent these programs from modifying, gaining persistence on, accessing sensitive resources on, or exfiltrating data from a host or network. Since OpenAI's training infrastructure is built on Kubernetes and cloud services, we designed our sandbox to address the limitations of these environments while remaining idiomatic with their patterns of use.

We selected the gVisor container runtime (Lacasse, 2018) as the main host protection component. Since container runtimes like Docker can share host resources with containers, a malicious container could potentially compromise a host. gVisor protects the host by emulating its resources to introduce a security boundary between the host and its containers. Network-adjacent hosts and services are protected by eBPF-based firewall rules that prevent inbound and outbound connections except for those required for experiment control.

---

### النسخة العربية

في هذا القسم، نناقش تفاصيل إطار التقييم الخاص بنا. نبدأ بتعريف معيار pass@k، ونشرح مزاياه على المقاييس القياسية القائمة على المطابقة. بعد ذلك، نصف مجموعة البيانات من المشكلات المكتوبة يدوياً، المسماة "HumanEval"، والتي أنشأناها من أجل قياس أداء نماذجنا. أخيراً، نناقش بيئة الحماية التي استخدمناها لتنفيذ الشفرة البرمجية المولدة بواسطة النموذج بأمان.

#### 2.1. الصحة الوظيفية

يتم قياس أداء النماذج التوليدية للشفرة البرمجية بشكل أساسي من خلال مطابقة العينات مع حل مرجعي، حيث يمكن أن تكون المطابقة دقيقة أو تقريبية (كما في درجة BLEU). ومع ذلك، كشفت الأعمال الحديثة عن أوجه قصور في المقاييس القائمة على المطابقة للشفرة البرمجية. على سبيل المثال، يجد Ren et al. (2020) أن BLEU لديه مشاكل في التقاط الميزات الدلالية الخاصة بالشفرة البرمجية، ويقترح العديد من التعديلات الدلالية على الدرجة.

بشكل أكثر جوهرية، المقاييس القائمة على المطابقة غير قادرة على مراعاة المساحة الكبيرة والمعقدة من البرامج المكافئة وظيفياً للحل المرجعي. ونتيجة لذلك، تحولت الأعمال الحديثة في ترجمة الشفرة البرمجية غير الخاضعة للإشراف (Lachaux et al., 2020) وترجمة الشفرة الزائفة إلى شفرة برمجية (Kulal et al., 2019) إلى الصحة الوظيفية بدلاً من ذلك، حيث تُعتبر العينة صحيحة إذا اجتازت مجموعة من اختبارات الوحدة. نحن نجادل بأن هذا المعيار يجب أن يُطبق على توليد الشفرة البرمجية المشروطة بسلاسل التوثيق أيضاً.

ربما السبب الأكثر إقناعاً لتقييم الصحة الوظيفية هو أنه يُستخدم من قبل المطورين البشريين للحكم على الشفرة البرمجية. إطار عمل يُعرف بالتطوير الموجه بالاختبار يملي أن متطلبات البرمجيات يجب أن تُحول إلى حالات اختبار قبل بدء أي تنفيذ، ويُعرّف النجاح ببرنامج يجتاز هذه الاختبارات. في حين أن قلة من المنظمات تستخدم التطوير الموجه بالاختبار الكامل، فإن دمج الشفرة البرمجية الجديدة يعتمد عادةً على إنشاء واجتياز اختبارات الوحدة.

يقيّم Kulal et al. (2019) الصحة الوظيفية باستخدام معيار pass@k، حيث يتم توليد k عينة من الشفرة البرمجية لكل مشكلة، وتُعتبر المشكلة محلولة إذا اجتازت أي عينة اختبارات الوحدة، ويتم الإبلاغ عن النسبة الإجمالية للمشكلات المحلولة. ومع ذلك، يمكن أن يكون لحساب pass@k بهذه الطريقة تباين كبير. بدلاً من ذلك، لتقييم pass@k، نولد n ≥ k عينة لكل مهمة (في هذه الورقة، نستخدم n = 200 و k ≤ 100)، ونحسب عدد العينات الصحيحة c ≤ n التي تجتاز اختبارات الوحدة، ونحسب المقدر غير المتحيز:

$$\text{pass}@k := \mathbb{E}_{\text{المشكلات}} \left[1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}\right]$$

#### 2.2. HumanEval: مجموعة التقييم المكتوبة يدوياً

نقيّم الصحة الوظيفية على مجموعة من 164 مشكلة برمجة مكتوبة يدوياً، نسميها مجموعة بيانات HumanEval. تتضمن كل مشكلة توقيع دالة، وسلسلة توثيق، ومتن، والعديد من اختبارات الوحدة، بمتوسط 7.7 اختبار لكل مشكلة. من المهم أن تكون هذه المهام مكتوبة يدوياً، حيث أن نماذجنا مدربة على جزء كبير من GitHub، والذي يحتوي بالفعل على حلول لمشكلات من مصادر متنوعة. على سبيل المثال، هناك أكثر من عشرة مستودعات عامة تحتوي على حلول لمشكلات Codeforces، والتي تشكل جزءاً من مجموعة بيانات APPS المقترحة مؤخراً (Hendrycks et al., 2021).

تقيّم مهام البرمجة في مجموعة بيانات HumanEval الفهم اللغوي والاستدلال والخوارزميات والرياضيات البسيطة. نطلق مجموعة بيانات HumanEval حتى يتمكن الآخرون من تقييم الصحة الوظيفية وقياس قدرات حل المشكلات لنماذجهم. يمكن العثور على مجموعة البيانات في https://www.github.com/openai/human-eval.

#### 2.3. بيئة الحماية لتنفيذ البرامج المولدة

نظراً لأن البرامج المتاحة للعامة لها نوايا غير معروفة والبرامج المولدة غالباً ما تكون غير صحيحة، فإن تنفيذ هذه البرامج يشكل خطراً أمنياً. في الواقع، من المعروف أن GitHub يحتوي على برامج ضارة تُغير أو تُعدل بيئاتها (Rokon et al., 2020).

لذلك، طورنا بيئة حماية لتشغيل البرامج غير الموثوق بها بأمان ضد اختبارات الوحدة. كانت أهدافنا هي منع هذه البرامج من التعديل، أو الحصول على ثبات على، أو الوصول إلى موارد حساسة على، أو استخراج البيانات من مضيف أو شبكة. نظراً لأن بنية التدريب الخاصة بـ OpenAI مبنية على Kubernetes والخدمات السحابية، صممنا بيئة الحماية الخاصة بنا لمعالجة قيود هذه البيئات مع البقاء متسقة مع أنماط استخدامها.

اخترنا وقت تشغيل الحاوية gVisor (Lacasse, 2018) كمكون حماية المضيف الرئيسي. نظراً لأن أوقات تشغيل الحاويات مثل Docker يمكن أن تشارك موارد المضيف مع الحاويات، فإن الحاوية الضارة يمكن أن تُعرض المضيف للخطر بشكل محتمل. يحمي gVisor المضيف من خلال محاكاة موارده لإدخال حد أمني بين المضيف وحاوياته. تُحمى المضيفات والخدمات المجاورة للشبكة بقواعد جدار الحماية المستندة إلى eBPF التي تمنع الاتصالات الواردة والصادرة باستثناء تلك المطلوبة للتحكم في التجربة.

---

### Translation Notes

- **Key terms introduced:** pass@k (kept as pass@k), functional correctness (الصحة الوظيفية), unit tests (اختبارات الوحدة), test-driven development (التطوير الموجه بالاختبار), sandbox (بيئة الحماية), unbiased estimator (المقدر غير المتحيز)
- **Figures referenced:** Figure 3 (code snippet for pass@k calculation)
- **Equations:** 1 mathematical equation for pass@k metric
- **Citations:** Multiple references to related work
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - HumanEval kept as proper noun
  - URLs kept as-is
  - Technical terms like gVisor, Docker, Kubernetes, eBPF kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.90
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.87
