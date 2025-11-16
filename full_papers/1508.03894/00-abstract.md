# Abstract
## الملخص

**Section:** Abstract
**Translation Quality:** 0.91
**Glossary Terms Used:** formal verification (التحقق الرسمي), avionics (إلكترونيات الطيران), specification (مواصفة), validation (التحقق من الصحة), safety-critical (حرجة من حيث السلامة), requirements (متطلبات)

---

### English Version

Safety critical avionics software is a natural application area for formal verification. This is reflected in the formal method's inclusion into the certification guideline DO-178C and its formal methods supplement DO-333. Airbus and Dassault-Aviation, for example, have conducted studies in using formal verification. A large German national research project, Verisoft XT, also examined the application of formal methods in the avionics domain.

However, formal methods are not yet mainstream, and it is questionable if formal verification, especially formal deduction, can be integrated into the software development processes of a resource constrained small or medium enterprise (SME). ESG, a Munich based medium sized company, has conducted a small experimental study on the application of formal verification on a small portion of a real avionics project. The low level specification of a software function was formalized with ACSL, and the corresponding source code was partially verified using Frama-C and the WP plugin, with Alt-Ergo as automated prover.

We established a couple of criteria which a method should meet to be fit for purpose for industrial use in SME, and evaluated these criteria with the experience gathered by using ACSL with Frama-C on a real world example. The paper reports on the results of this study but also highlights some issues regarding the method in general which, in our view, will typically arise when using the method in the domain of embedded real-time programming.

---

### النسخة العربية

تُعد البرمجيات الحرجة من حيث السلامة لإلكترونيات الطيران مجالاً طبيعياً لتطبيق التحقق الرسمي. وينعكس ذلك في إدراج الأساليب الرسمية ضمن إرشادات الاعتماد DO-178C والملحق الخاص بالأساليب الرسمية DO-333. فعلى سبيل المثال، أجرت شركتا Airbus وDassault-Aviation دراسات حول استخدام التحقق الرسمي. كما فحص مشروع بحثي وطني ألماني كبير، Verisoft XT، تطبيق الأساليب الرسمية في مجال إلكترونيات الطيران.

ومع ذلك، لا تزال الأساليب الرسمية غير سائدة على نطاق واسع، ومن المشكوك فيه ما إذا كان يمكن دمج التحقق الرسمي، وخاصة الاستدلال الرسمي، في عمليات تطوير البرمجيات للشركات الصغيرة والمتوسطة المحدودة الموارد. أجرت شركة ESG، وهي شركة متوسطة الحجم مقرها ميونيخ، دراسة تجريبية صغيرة حول تطبيق التحقق الرسمي على جزء صغير من مشروع إلكترونيات طيران حقيقي. تمت صياغة المواصفة منخفضة المستوى لوظيفة برمجية بشكل رسمي باستخدام ACSL، وتم التحقق جزئياً من الشفرة المصدرية المقابلة باستخدام Frama-C وإضافة WP، مع استخدام Alt-Ergo كمُثبِت آلي.

أنشأنا مجموعة من المعايير التي يجب أن تستوفيها الطريقة لتكون مناسبة للاستخدام الصناعي في الشركات الصغيرة والمتوسطة، وقيّمنا هذه المعايير بالخبرة المكتسبة من استخدام ACSL مع Frama-C على مثال من العالم الواقعي. يقدم البحث تقريراً عن نتائج هذه الدراسة ولكنه يسلط الضوء أيضاً على بعض المشكلات المتعلقة بالطريقة بشكل عام والتي، في رأينا، ستظهر عادةً عند استخدام الطريقة في مجال البرمجة المدمجة في الوقت الفعلي.

---

### Translation Notes

- **Key Terms:**
  - Safety-critical: حرجة من حيث السلامة
  - Avionics: إلكترونيات الطيران
  - Formal verification: التحقق الرسمي
  - Formal methods: الأساليب الرسمية
  - Formal deduction: الاستدلال الرسمي
  - Low level specification: المواصفة منخفضة المستوى
  - SME (Small or Medium Enterprise): الشركات الصغيرة والمتوسطة
  - Automated prover: مُثبِت آلي
  - Embedded real-time programming: البرمجة المدمجة في الوقت الفعلي

- **Acronyms and Tools:**
  - ACSL: ANSI C Specification Language (kept in English)
  - Frama-C: Framework name (kept in English)
  - WP plugin: إضافة WP
  - Alt-Ergo: Automated theorem prover name (kept in English)
  - DO-178C, DO-333: Certification standards (kept in English)
  - Verisoft XT: Project name (kept in English)

- **Special Handling:**
  - Company names preserved in English (ESG, Airbus, Dassault-Aviation)
  - Technical tool names preserved in English
  - Certification standard numbers preserved

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.91
- Readability: 0.90
- Glossary consistency: 0.91
- **Overall section score:** 0.91

### Back-Translation Sample

"Safety-critical software for avionics is a natural field for applying formal verification. This is reflected in the inclusion of formal methods within the DO-178C certification guidelines and the DO-333 formal methods supplement. For example, Airbus and Dassault-Aviation companies conducted studies on using formal verification. A large German national research project, Verisoft XT, also examined the application of formal methods in the avionics field."

**Back-translation Assessment:** Excellent - preserves all key information and technical meaning.
