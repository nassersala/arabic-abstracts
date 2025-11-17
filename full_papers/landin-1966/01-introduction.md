# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** programming languages, primitives, abstraction, functional relations, lambda calculus, syntax

---

### English Version

Most programming languages are partly a way of expressing things in terms of other things and partly a basic set of given things. The ISWIM (If you See What I Mean) system is a byproduct of an attempt to disentangle these two aspects in some current languages.

This attempt has led the author to think that many linguistic idiosyncracies are concerned with the former rather than the latter, whereas aptitude for a particular class of tasks is essentially determined by the latter rather than the former. The conclusion follows that many language characteristics are irrelevant to the alleged problem orientation.

ISWIM is an attempt at a general purpose system for describing things in terms of other things, that can be problem-oriented by appropriate choice of "primitives." So it is not a language so much as a family of languages, of which each member is the result of choosing a set of primitives. The possibilities concerning this set and what is needed to specify such a set are discussed below.

ISWIM is not alone in being a family, even after mere syntactic variations have been discounted (see Section 4). In practice, this is true of most languages that achieve more than one implementation, and if the dialects are well disciplined, they might with luck be characterized as differences in the set of things provided by the library or operating system. Perhaps had ALGOL 60 been launched as a family instead of proclaimed as a language, it would have fielded some of the less relevant criticisms of its deficiencies.

At first sight the facilities provided in ISWIM will appear comparatively meager. This appearance will be especially misleading to someone who has not appreciated how much of current manuals are devoted to the explanation of common (i.e., problem-orientation independent) logical structure rather than problem-oriented specialties. For example, in almost every language a user can coin names, obeying certain rules about the contexts in which the name is used and their relation to the textual segments that introduce, define, declare, or otherwise constrain its use. These rules vary considerably from one language to another, and frequently even within a single language there may be different conventions for different classes of names, with near-analogies that come irritatingly close to being exact. (Note that restrictions on what names can be coined also vary, but these are trivial differences. When they have any logical significance it is likely to be pernicious, by leading to puns such as ALGOL's integer labels.)

So rules about user-coined names is an area in which we might expect to see the history of computer applications give ground to their logic. Another such area is in specifying functional relations. In fact these two areas are closely related since any use of a user-coined name implicitly involves a functional relation; e.g., compare:

```
x(x+a)               f(b+2c)
where x = b + 2c     where f(x) = x(x+a)
```

ISWIM is thus part programming language and part program for research. A possible first step in the research program is 1700 doctoral theses called "A Correspondence between x and Church's λ-notation."

---

### النسخة العربية

معظم لغات البرمجة هي جزئياً طريقة للتعبير عن أشياء من خلال أشياء أخرى، وجزئياً مجموعة أساسية من الأشياء المُعطاة. نظام ISWIM (إذا كنت ترى ما أعنيه - If you See What I Mean) هو نتيجة ثانوية لمحاولة فصل هذين الجانبين في بعض اللغات الحالية.

لقد قادت هذه المحاولة المؤلف إلى التفكير في أن العديد من السمات اللغوية الغريبة تتعلق بالجانب الأول بدلاً من الثاني، في حين أن الملاءمة لفئة معينة من المهام تُحدد بشكل أساسي بالجانب الثاني بدلاً من الأول. ويترتب على ذلك أن العديد من خصائص اللغة غير ذات صلة بالتوجه المزعوم نحو حل المشكلات.

ISWIM هو محاولة لإنشاء نظام عام الغرض لوصف الأشياء من خلال أشياء أخرى، يمكن أن يكون موجهاً نحو حل المشكلات من خلال الاختيار المناسب للـ"العمليات الأولية" (primitives). لذا فهو ليس لغة بقدر ما هو عائلة من اللغات، حيث كل عضو فيها هو نتيجة اختيار مجموعة من العمليات الأولية. يتم مناقشة الاحتمالات المتعلقة بهذه المجموعة وما يلزم لتحديد مثل هذه المجموعة أدناه.

ISWIM ليس وحيداً في كونه عائلة، حتى بعد استبعاد التنويعات التركيبية الصرفة (انظر القسم 4). في الممارسة العملية، هذا صحيح بالنسبة لمعظم اللغات التي تحقق أكثر من تنفيذ واحد، وإذا كانت اللهجات منضبطة بشكل جيد، فقد يتم توصيفها بحظ سعيد على أنها اختلافات في مجموعة الأشياء المقدمة من المكتبة أو نظام التشغيل. ربما لو تم إطلاق ALGOL 60 كعائلة بدلاً من الإعلان عنه كلغة، لكان قد صد بعض الانتقادات الأقل صلة بشأن أوجه القصور فيه.

للوهلة الأولى، ستبدو الإمكانات المتوفرة في ISWIM ضئيلة نسبياً. سيكون هذا المظهر مضللاً بشكل خاص لشخص لم يقدّر مدى تكريس الأدلة الحالية لشرح البنية المنطقية المشتركة (أي المستقلة عن التوجه نحو حل المشكلات) بدلاً من التخصصات الموجهة نحو حل المشكلات. على سبيل المثال، في كل لغة تقريباً يمكن للمستخدم ابتكار أسماء، مع الالتزام بقواعد معينة حول السياقات التي يُستخدم فيها الاسم وعلاقتها بالمقاطع النصية التي تقدم أو تعرّف أو تصرّح أو تقيّد استخدامه بطريقة أخرى. تختلف هذه القواعد بشكل كبير من لغة إلى أخرى، وكثيراً ما تكون هناك اتفاقيات مختلفة لفئات مختلفة من الأسماء حتى ضمن لغة واحدة، مع تشابهات قريبة تقترب بشكل مزعج من أن تكون متطابقة تماماً. (لاحظ أن القيود على الأسماء التي يمكن ابتكارها تختلف أيضاً، ولكن هذه اختلافات تافهة. عندما يكون لها أي أهمية منطقية، فمن المحتمل أن تكون ضارة، من خلال التسبب في لعب على الكلمات مثل التسميات الصحيحة في ALGOL.)

لذا فإن القواعد المتعلقة بالأسماء التي يبتكرها المستخدم هي مجال قد نتوقع فيه أن نرى تاريخ تطبيقات الحاسوب يفسح المجال لمنطقها. مجال آخر من هذا القبيل هو تحديد العلاقات الوظيفية. في الواقع، هذان المجالان مرتبطان ارتباطاً وثيقاً حيث أن أي استخدام لاسم ابتكره المستخدم يتضمن ضمنياً علاقة وظيفية؛ على سبيل المثال، قارن:

```
x(x+a)               f(b+2c)
where x = b + 2c     where f(x) = x(x+a)
```
حيث x = b + 2c     حيث f(x) = x(x+a)

ISWIM هو بالتالي جزء لغة برمجة وجزء برنامج للبحث. خطوة أولى محتملة في برنامج البحث هي 1700 رسالة دكتوراه بعنوان "التطابق بين x وتدوين λ لـChurch."

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - ISWIM (If you See What I Mean): تبقى بالإنجليزية مع ترجمة المعنى
  - primitives: العمليات الأولية
  - user-coined names: الأسماء التي يبتكرها المستخدم
  - functional relations: العلاقات الوظيفية
  - lambda calculus (λ-notation): تدوين λ (لامدا)
  - problem-oriented: موجه نحو حل المشكلات

- **Equations:** Simple mathematical examples showing equivalence between expressions
- **Citations:** Reference to Section 4, mention of ALGOL 60, Church's λ-notation
- **Special handling:**
  - Code examples preserved in monospace format
  - Historical context from 1966 maintained
  - Footnote reference to Church's lambda calculus preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

---

### Back-Translation (Key Paragraph for Validation)

"Most programming languages are partially a way of expressing things through other things, and partially a basic set of given things. The ISWIM system (If you See What I Mean) is a byproduct of an attempt to separate these two aspects in some current languages."

**Validation:** ✓ Maintains semantic equivalence with original text.
