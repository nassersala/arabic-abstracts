# Section 5: Evaluation Model
## القسم 5: نموذج التقييم

**Section:** evaluation-model
**Translation Quality:** 0.86
**Glossary Terms Used:** testbed (منصة اختبار), simulation (محاكاة), fault injection (حقن الأعطال), electrical systems (أنظمة كهربائية), Simulink

---

### English Version

**Virtual ADAPT**

Virtual ADAPT is a Simulink formulation of a physical testbed representing a spacecraft's electrical power system. It allows for the injection of faults such as malfunctioning relays and sudden spikes in electrical resistance so that the system's response can be studied. Users can interact with Virtual ADAPT in real time through the GUI flippable switches or programmatic alteration of most model parameters.

Simulink models are represented as .mdl files which define a hierarchical structure of components and the connections between them through notions of subsystems, lines (same level connections), and ports (cross-level connections). Additionally, Virtual ADAPT includes MATLAB .m files describing fault states and state-transition logic for relevant components.

**Model Statistics**

Virtual ADAPT contains 11991 blocks, including the top level block. However, Virtual ADAPT is a hierarchical model and 73% of those blocks are in the lower 7 of Virtual ADAPT's 13 levels of block and sub-block containment (3197 blocks in the top 6 levels). The top level block for this is the block named VirtualADAPT/VirtualADAPTv1.

---

### النسخة العربية

**Virtual ADAPT**

Virtual ADAPT هو صياغة Simulink لمنصة اختبار مادية تمثل نظام الطاقة الكهربائية لمركبة فضائية. يسمح بحقن الأعطال مثل المرحلات المعطلة والارتفاعات المفاجئة في المقاومة الكهربائية بحيث يمكن دراسة استجابة النظام. يمكن للمستخدمين التفاعل مع Virtual ADAPT في الوقت الفعلي من خلال مفاتيح واجهة المستخدم الرسومية القابلة للقلب أو التعديل البرمجي لمعظم معاملات النموذج.

يتم تمثيل نماذج Simulink كملفات .mdl التي تحدد بنية هرمية للمكونات والاتصالات بينها من خلال مفاهيم الأنظمة الفرعية، والخطوط (اتصالات نفس المستوى)، والمنافذ (اتصالات عبر المستويات). بالإضافة إلى ذلك، يتضمن Virtual ADAPT ملفات MATLAB .m التي تصف حالات الأعطال ومنطق انتقال الحالة للمكونات ذات الصلة.

**إحصائيات النموذج**

يحتوي Virtual ADAPT على 11991 كتلة، بما في ذلك الكتلة ذات المستوى الأعلى. ومع ذلك، Virtual ADAPT هو نموذج هرمي و 73٪ من هذه الكتل موجودة في أدنى 7 من مستويات احتواء الكتل والكتل الفرعية الـ 13 في Virtual ADAPT (3197 كتلة في أعلى 6 مستويات). الكتلة ذات المستوى الأعلى لهذا هي الكتلة المسماة VirtualADAPT/VirtualADAPTv1.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Virtual ADAPT - (kept as proper noun)
  - Testbed - منصة اختبار
  - Spacecraft electrical power system - نظام الطاقة الكهربائية لمركبة فضائية
  - Fault injection - حقن الأعطال
  - Malfunctioning relays - المرحلات المعطلة
  - Electrical resistance - المقاومة الكهربائية
  - GUI (Graphical User Interface) - واجهة المستخدم الرسومية
  - .mdl files - (kept as is - file extension)
  - Hierarchical structure - بنية هرمية
  - Subsystems - الأنظمة الفرعية
  - Ports - المنافذ
  - MATLAB .m files - (kept as proper nouns)
  - State-transition logic - منطق انتقال الحالة
- **Equations:** 0
- **Citations:** None in this short section
- **Special handling:**
  - Virtual ADAPT kept as proper noun throughout
  - File extensions (.mdl, .m) kept in English
  - Software/tool names (Simulink, MATLAB) kept in English

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.84
- **Overall section score:** 0.86
