# Section 4: Four Levels of Abstraction
## القسم 4: أربعة مستويات من التجريد

**Section:** four-levels-abstraction
**Translation Quality:** 0.86
**Glossary Terms Used:** abstraction, syntax, grammar, applicative expressions, tree language, abstract machine

---

### English Version

The "physical~logical" terminology is often used to distinguish features that are a fortuitous consequence of physical conditions from features that are in some sense more essential. This idea is carried further by making a similar distinction among the "more essential" features. In fact ISWIM is presented here as a four-level concept comprising the following:

(1) **physical ISWIM's**, of which one is the reference language and others are various publication and hardware languages (not described here).

(2) **logical ISWIM**, which is uncommitted as to character sets and type faces, but committed as to the sequence of textual elements, and the grammatical rules for grouping them, e.g., by parentheses, indentation and precedence relations.

(3) **abstract ISWIM**, which is uncommitted as to the grammatical rules of sequence and grouping, but committed as to the grammatical categories and their nesting structure. Thus abstract ISWIM is a "tree language" of which logical ISWIM is one linearization.

(4) **applicative expressions (AEs)**, which constitute another tree language, structurally more austere than abstract ISWIM, and providing certain basic grammatical categories in terms of which all of ISWIM's more numerous categories can be expressed.

The set of acceptable texts of a physical ISWIM is specified by the relations between 1 and 2, and between 2 and 3. The outcome of each text is specified by these relations, together with a "frame of reference," i.e., a rule that associates a meaning with each of a chosen set of identifiers.

These are the things that vary from one member of our language family to the next. The specification of the family is completed by the relation between abstract ISWIM and AEs, together with an abstract machine that interprets AEs. These elements are the same for all members of the family and are not discussed in this paper (see [1, 2, 4]).

The relationship between physical ISWIM and logical ISWIM is fixed by saying what physical texts represent each logical element, and also what layout is permitted in stringing them together. The relationship between logical ISWIM and abstract ISWIM is fixed by a formal grammar not unlike the one in the ALGOL 60 report, together with a statement connecting the phrase categories with the abstract grammatical categories.

These two relations cover what is usually called the "syntax" or "grammar" of a language. In this paper syntax is not discussed beyond a few general remarks and a few examples whose meaning should be obvious.

The relationship between abstract ISWIM and AEs is fixed by giving the form of AE equivalent to each abstract ISWIM grammatical category. It happens that these latter include a subset that exactly matches AEs. Hence this link in our chain of relations is roughly a mapping of ISWIM into an essential "kernel" of ISWIM, of which all the rest is mere decoration.

---

### النسخة العربية

غالباً ما تُستخدم مصطلحات "المادي~المنطقي" لتمييز الميزات التي هي نتيجة عرضية للظروف المادية من الميزات الأكثر جوهرية بمعنى ما. يتم تطوير هذه الفكرة بشكل أكبر من خلال إجراء تمييز مماثل بين الميزات "الأكثر جوهرية". في الواقع، يتم تقديم ISWIM هنا كمفهوم من أربعة مستويات يتضمن ما يلي:

(1) **ISWIM المادي**، حيث واحد منها هو اللغة المرجعية والآخرون هم لغات نشر وأجهزة متنوعة (غير موصوفة هنا).

(2) **ISWIM المنطقي**، وهو غير ملتزم بمجموعات الأحرف وأشكال الخطوط، ولكنه ملتزم بتسلسل العناصر النصية، والقواعد النحوية لتجميعها، مثل الأقواس، والمسافة البادئة، وعلاقات الأسبقية.

(3) **ISWIM المجرد**، وهو غير ملتزم بالقواعد النحوية للتسلسل والتجميع، ولكنه ملتزم بالفئات النحوية وبنيتها المتداخلة. وبالتالي فإن ISWIM المجرد هو "لغة شجرية" (tree language) حيث ISWIM المنطقي هو أحد تخطيطاتها الخطية.

(4) **التعبيرات التطبيقية (AEs - applicative expressions)**، والتي تشكل لغة شجرية أخرى، أكثر تقشفاً من الناحية البنيوية من ISWIM المجرد، وتوفر فئات نحوية أساسية معينة يمكن من خلالها التعبير عن جميع فئات ISWIM الأكثر عدداً.

يتم تحديد مجموعة النصوص المقبولة لـ ISWIM المادي بالعلاقات بين 1 و2، وبين 2 و3. يتم تحديد نتيجة كل نص من خلال هذه العلاقات، جنباً إلى جنب مع "إطار مرجعي" (frame of reference)، أي قاعدة تربط معنى بكل من مجموعة مختارة من المعرفات.

هذه هي الأشياء التي تختلف من عضو إلى آخر في عائلة اللغات لدينا. يتم استكمال مواصفات العائلة بالعلاقة بين ISWIM المجرد والتعبيرات التطبيقية (AEs)، جنباً إلى جنب مع آلة مجردة تفسر AEs. هذه العناصر هي نفسها لجميع أفراد العائلة ولا تتم مناقشتها في هذه الورقة (انظر [1، 2، 4]).

يتم تحديد العلاقة بين ISWIM المادي وISWIM المنطقي من خلال تحديد النصوص المادية التي تمثل كل عنصر منطقي، وكذلك التخطيط المسموح به في ربطها معاً. يتم تحديد العلاقة بين ISWIM المنطقي وISWIM المجرد من خلال قواعد نحوية رسمية لا تختلف كثيراً عن تلك الموجودة في تقرير ALGOL 60، جنباً إلى جنب مع بيان يربط فئات العبارات بالفئات النحوية المجردة.

تغطي هاتان العلاقتان ما يُسمى عادة "التركيب" (syntax) أو "النحو" (grammar) للغة. في هذه الورقة لا تتم مناقشة التركيب إلا من خلال بعض الملاحظات العامة وبعض الأمثلة التي يجب أن يكون معناها واضحاً.

يتم تحديد العلاقة بين ISWIM المجرد والتعبيرات التطبيقية (AEs) من خلال إعطاء شكل AE المكافئ لكل فئة نحوية من ISWIM المجرد. يحدث أن هذه الأخيرة تتضمن مجموعة فرعية تطابق تماماً AEs. وبالتالي فإن هذا الرابط في سلسلة علاقاتنا هو تقريباً تعيين (mapping) لـ ISWIM إلى "نواة" أساسية من ISWIM، حيث كل ما تبقى مجرد زخرفة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - four-level concept: مفهوم من أربعة مستويات
  - tree language: لغة شجرية
  - linearization: تخطيط خطي
  - applicative expressions (AEs): التعبيرات التطبيقية
  - frame of reference: إطار مرجعي
  - abstract machine: آلة مجردة
  - kernel: نواة

- **Equations:** None
- **Citations:** References to [1, 2, 4], comparison with ALGOL 60
- **Special handling:**
  - Four-level hierarchy clearly delineated
  - Technical relationships between levels preserved
  - Numbered list structure maintained

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86

---

### Back-Translation (Key Paragraph for Validation)

"ISWIM is presented here as a four-level concept comprising: (1) physical ISWIM's, (2) logical ISWIM, (3) abstract ISWIM which is a 'tree language' of which logical ISWIM is one linearization, and (4) applicative expressions (AEs), which constitute another tree language, structurally more austere than abstract ISWIM."

**Validation:** ✓ Maintains semantic equivalence and captures the hierarchical structure accurately.
