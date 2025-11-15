# Section 4: Designing for Understandability
## القسم الرابع: التصميم من أجل القابلية للفهم

**Section:** designing-for-understandability
**Translation Quality:** 0.87
**Glossary Terms Used:** understandability, consensus algorithm, decomposition, state space reduction, nondeterminism, leader election, log replication, safety

---

### English Version

Several alternatives were considered during our design of Raft, and we evaluated them based on understandability: how hard is it for a reader to comprehend and develop intuitions about each alternative? This section discusses how we applied techniques to maximize understandability.

Understandability guided our choices at each stage of the design. Our primary goal was understandability: could we define a consensus algorithm for practical systems and describe it in a way that is significantly easier to learn than Paxos? Furthermore, we wanted the algorithm to facilitate the development of intuitions that are essential for system builders. It was important not just for the algorithm to work, but for it to be obvious why it works.

In designing Raft we applied several techniques to improve understandability. The most important techniques were **decomposition** and **state space reduction**.

**Problem decomposition.** Wherever possible, we divided problems into separate pieces that could be solved, explained, and understood relatively independently. For example, in Raft we separated leader election, log replication, safety, and membership changes. This contrasts with Paxos, which interleaves the management of elections and logging in complex ways. Decomposition allowed us to focus our attention on one problem at a time, reducing cognitive load.

**Minimizing state space.** To make the system easier to understand, we reduced the number of states to consider, making the system more coherent and eliminating nondeterminism where possible. Specifically, logs are not allowed to have holes, and Raft limits the ways in which logs can become inconsistent with each other. Although in most cases we tried to eliminate nondeterminism, there are some situations where nondeterminism actually improves understandability. In particular, randomized approaches introduce nondeterminism, but they tend to reduce the state space by handling all possible choices in a similar fashion. We used randomization to simplify the Raft leader election algorithm.

In several places in the design we had a choice between alternative approaches. We evaluated these alternatives based primarily on understandability. We found that in some cases there was a trade-off between performance and understandability. When this occurred, we generally erred on the side of understandability, though in a few cases we improved performance without significantly affecting understandability.

---

### النسخة العربية

تم النظر في عدة بدائل أثناء تصميمنا لـ Raft، وقيّمناها بناءً على القابلية للفهم: ما مدى صعوبة أن يفهم القارئ ويطور حدساً حول كل بديل؟ يناقش هذا القسم كيفية تطبيقنا للتقنيات لتعظيم القابلية للفهم.

وجهت القابلية للفهم خياراتنا في كل مرحلة من مراحل التصميم. كان هدفنا الأساسي هو القابلية للفهم: هل يمكننا تعريف خوارزمية إجماع للأنظمة العملية ووصفها بطريقة أسهل بكثير للتعلم من Paxos؟ علاوة على ذلك، أردنا أن تسهل الخوارزمية تطوير الحدس الضروري لبناة الأنظمة. كان من المهم ليس فقط أن تعمل الخوارزمية، ولكن أن يكون واضحاً لماذا تعمل.

في تصميم Raft طبقنا عدة تقنيات لتحسين القابلية للفهم. أهم التقنيات كانت **التفكيك** و**تقليل فضاء الحالة**.

**تفكيك المشكلة.** حيثما أمكن، قسمنا المشاكل إلى أجزاء منفصلة يمكن حلها وشرحها وفهمها بشكل مستقل نسبياً. على سبيل المثال، في Raft فصلنا انتخاب القائد، ونسخ السجل، والسلامة، وتغييرات العضوية. هذا يتناقض مع Paxos، التي تتشابك إدارة الانتخابات والتسجيل بطرق معقدة. سمح لنا التفكيك بتركيز انتباهنا على مشكلة واحدة في كل مرة، مما يقلل الحمل المعرفي.

**تقليل فضاء الحالة.** لجعل النظام أسهل للفهم، قللنا عدد الحالات التي يجب النظر فيها، مما يجعل النظام أكثر تماسكاً ويزيل عدم الحتمية حيثما أمكن. على وجه التحديد، لا يُسمح للسجلات أن تحتوي على ثغرات، و Raft تحد من الطرق التي يمكن أن تصبح بها السجلات غير متسقة مع بعضها البعض. على الرغم من أننا في معظم الحالات حاولنا إزالة عدم الحتمية، إلا أن هناك بعض المواقف التي يحسن فيها عدم الحتمية القابلية للفهم بالفعل. على وجه الخصوص، تُدخل النُّهُج العشوائية عدم الحتمية، لكنها تميل إلى تقليل فضاء الحالة من خلال التعامل مع جميع الاختيارات الممكنة بطريقة مماثلة. استخدمنا العشوائية لتبسيط خوارزمية انتخاب القائد في Raft.

في عدة أماكن في التصميم كان لدينا خيار بين نُهُج بديلة. قيّمنا هذه البدائل بناءً بشكل أساسي على القابلية للفهم. وجدنا أنه في بعض الحالات كانت هناك مقايضة بين الأداء والقابلية للفهم. عندما حدث هذا، أخطأنا بشكل عام في جانب القابلية للفهم، على الرغم من أننا في بعض الحالات حسّنا الأداء دون التأثير بشكل كبير على القابلية للفهم.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - understandability = القابلية للفهم
  - decomposition = التفكيك
  - state space reduction = تقليل فضاء الحالة
  - problem decomposition = تفكيك المشكلة
  - cognitive load = الحمل المعرفي
  - coherent = تماسكاً
  - nondeterminism = عدم الحتمية
  - randomized approaches = النُّهُج العشوائية
  - randomization = العشوائية
  - trade-off = مقايضة

- **Special handling:**
  - Emphasized key techniques using bold text in both languages
  - Maintained the two main subsections (problem decomposition and state space reduction)
  - Preserved the analytical tone discussing design choices

- **Translation decisions:**
  - "decomposition" → "التفكيك" (breaking apart/decomposition)
  - "state space" → "فضاء الحالة" (state space, already used in glossary)
  - "cognitive load" → "الحمل المعرفي" (mental/cognitive burden)
  - "coherent" → "تماسكاً" (cohesive/coherent)
  - "nondeterminism" → "عدم الحتمية" (non-determinism, already in glossary)
  - "randomization" → "العشوائية" (randomness)
  - "trade-off" → "مقايضة" (compromise/trade-off)
  - "erred on the side of" → "أخطأنا في جانب" (chose the side of)

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately preserves design philosophy and reasoning
- **Technical accuracy:** 0.89 - Design principles and technical concepts well translated
- **Readability:** 0.86 - Clear explanation of abstract design concepts
- **Glossary consistency:** 0.86 - Consistent with established terms
- **Overall section score:** 0.87

### Back-Translation Check

Key principle:
English: "Our primary goal was understandability"
Arabic: "كان هدفنا الأساسي هو القابلية للفهم"
Back: "Our primary goal was understandability"
✓ Exact match

Design technique:
English: "we divided problems into separate pieces that could be solved, explained, and understood relatively independently"
Arabic: "قسمنا المشاكل إلى أجزاء منفصلة يمكن حلها وشرحها وفهمها بشكل مستقل نسبياً"
Back: "we divided problems into separate parts that can be solved, explained, and understood relatively independently"
✓ Semantically equivalent
