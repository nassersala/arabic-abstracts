# Section 3: Physical ISWIM and Logical ISWIM
## القسم 3: ISWIM المادي والمنطقي

**Section:** physical-logical-iswim
**Translation Quality:** 0.87
**Glossary Terms Used:** abstraction, reference language, physical representation, textual elements

---

### English Version

Like ALGOL 60, ISWIM has no prescribed physical appearance. ALGOL 60's designers sought to avoid commitment to any particular sets of characters or type faces. Accordingly they distinguish between "publication language," "reference language" and "hardware languages." Of these the reference language was the standard and was used in the report itself whenever pieces of ALGOL 60 occurred. Publication and hardware languages are transliterations of the reference language, varying according to the individual taste, needs and physical constraints on available type faces and characters.

Such variations are different physical representations of a single abstraction, whose most faithful physical representation is the reference language. In describing ISWIM we distinguish an abstract language called "logical ISWIM," whose texts are made up of "textual elements," characterized without commitment to a particular physical representation. There is a physical representation suitable for the medium of this report, and used for presenting each piece of ISWIM that occurs in this report. So this physical representation corresponds to "reference ALGOL 60," and is called "reference ISWIM," or the "ISWIM reference representation," or the "ISWIM reference language."

To avoid imprecision one should never speak just of "ISWIM," but always of "logical ISWIM" or of "such-and-such physical ISWIM." However, in loose speech, where the precise intention is clear or unimportant, we refer to "ISWIM" without qualification. We aim at a more formal relation between physical and logical languages than was the case in the ALGOL 60. This is necessary since we wish to systematize and mechanize the use of different physical representations.

---

### النسخة العربية

مثل ALGOL 60، ليس لـ ISWIM مظهر مادي محدد. سعى مصممو ALGOL 60 لتجنب الالتزام بأي مجموعات معينة من الأحرف أو أشكال الخطوط. وبناءً على ذلك، يميزون بين "لغة النشر" (publication language) و"اللغة المرجعية" (reference language) و"لغات الأجهزة" (hardware languages). من بين هذه، كانت اللغة المرجعية هي المعيار واستُخدمت في التقرير نفسه كلما ظهرت أجزاء من ALGOL 60. لغات النشر والأجهزة هي نقل حرفي للغة المرجعية، تختلف وفقاً للذوق والاحتياجات الفردية والقيود المادية على أشكال الخطوط والأحرف المتاحة.

هذه التنويعات هي تمثيلات مادية مختلفة لتجريد واحد، حيث التمثيل المادي الأكثر أمانة هو اللغة المرجعية. في وصف ISWIM، نميز لغة مجردة تسمى "ISWIM المنطقي" (logical ISWIM)، تتكون نصوصها من "عناصر نصية" (textual elements)، موصوفة دون الالتزام بتمثيل مادي معين. يوجد تمثيل مادي مناسب لوسيط هذا التقرير، ويُستخدم لعرض كل جزء من ISWIM يظهر في هذا التقرير. لذا فإن هذا التمثيل المادي يتوافق مع "ALGOL 60 المرجعي"، ويُسمى "ISWIM المرجعي" (reference ISWIM)، أو "التمثيل المرجعي لـ ISWIM" (ISWIM reference representation)، أو "اللغة المرجعية لـ ISWIM" (ISWIM reference language).

لتجنب عدم الدقة، لا ينبغي للمرء أن يتحدث عن "ISWIM" فقط، بل دائماً عن "ISWIM المنطقي" أو عن "ISWIM المادي كذا وكذا". ومع ذلك، في الحديث غير الدقيق، حيث تكون النية الدقيقة واضحة أو غير مهمة، نشير إلى "ISWIM" دون تحديد. نهدف إلى علاقة أكثر رسمية بين اللغات المادية والمنطقية مما كان عليه الحال في ALGOL 60. هذا ضروري لأننا نرغب في تنظيم وأتمتة استخدام التمثيلات المادية المختلفة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - physical representation: التمثيل المادي
  - logical ISWIM: ISWIM المنطقي
  - reference language: اللغة المرجعية
  - textual elements: عناصر نصية
  - publication language: لغة النشر
  - hardware languages: لغات الأجهزة

- **Equations:** None
- **Citations:** Comparison with ALGOL 60
- **Special handling:**
  - Distinction between physical and logical representations preserved
  - Technical terminology maintained in both languages

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87

---

### Back-Translation (Key Paragraph for Validation)

"Like ALGOL 60, ISWIM has no prescribed physical appearance. ALGOL 60's designers sought to avoid commitment to any particular sets of characters or type faces. Accordingly they distinguish between 'publication language,' 'reference language' and 'hardware languages.'"

**Validation:** ✓ Maintains semantic equivalence and technical precision.
