# Section 3: Deployment and dissemination
## القسم 3: الانتشار والتبني

**Section:** evaluation/deployment
**Translation Quality:** 0.87
**Glossary Terms Used:** formal methods (الأساليب الرسمية), B method (أسلوب B), safety-critical (حرجة من حيث السلامة), automated proof (البرهان الآلي), Domain Specific Language (لغة خاصة بالمجال)

---

### English Version

## 3.1 Research and development

CSSP was initially an in-house development project before being funded⁶ by the R&D project LCHIP⁷ to obtain a generic version of the platform. This project is aimed at allowing any engineer to develop a function by using its usual Domain Specific Language and to obtain this function running safely on a hardware platform. With the automatic development process, the B formal method will remain "behind the curtain" in order to avoid expert transactions. As the safety demonstration does not require any specific feature for the input B model, it could be handwritten or the by-product of a translation process.

**Figure 5:** On-the-fly automatic model extraction from relay-based schematics and B model generation.

⁶ The project is partly funded by BPI France, Région PACA, and Métropole Aix-Marseille, with a strong support from the "Pôles de compétitivité" I-Trans (Lille), SCS (Aix en Provence) and Systematic (Paris).
⁷ Low Cost High Integrity Platform.

Several DSL are planned to be supported at once (relays schematic, grafcet) based on an Open API (Bxml). The translation from relays schematic is being studied for the French Railways. The whole process, starting from the B model and finishing with the software running on the hardware platform, is expected to be fully automatic⁸, even with "not so simple models" with the integration of the results obtained from some R&D projects⁹.

⁸ "Push button" - the Graal of industry.
⁹ to improve automatic proof performances (ANR-BWARE)

## 3.2 Education

The IDE is based on Atelier B 4.5.3, providing a simplified process-oriented GUI.

**Figure 6:** Starter kits for education.

A first starter kit, SK0, containing the IDE and the execution platform, was released by the end of 2017¹⁰, presented and experimented at the occasion of several hands-on sessions organised at university sites in Europe, North and South America. Audience was diverse, ranging from automation to embedded systems, mecatronics, computer science and formal methods. Results obtained are very encouraging:
– teaching formal methods is eased as students are able to see their model running in and interacting with the physical world,
– less theoretic profiles may be introduced/educated to more abstract aspects of computation,
– the platform has demonstrated a certain robustness during all these manipulations and has been enriched with the feedback collected so far.
– CSSP is yet used to teach in M2 in universities and engineering schools.

¹⁰ https://www.clearsy.com/en/our-tools/clearsy-safety-platform/

**Figure 7:** Exploitation and dissemination.

## 3.3 Deployment

CSSP building blocks are operating platform-screen doors in São Paulo L15 metro (certified in 2018 at level SIL3 by CERTIFER on the inopportune opening failure of the doors), in Stockholm City line (certified in 2019), and in New York city (to be certified in 2019).

A new starter kit, SK1, released end of 2018 and aimed at prototyping¹¹, has been experimented by the French Railways for transforming wired logic into programmed ones [1] (track side signal control, wrong way temporary signalling system). This starter kit definitely attracts a lot of attention from industry, from railways but also robotics and autonomous vehicles. With the forthcoming CSSP Core (safety programmable logic controller) by the end of 2019, more deployments in industry are expected.

¹¹ It embeds 20 inputs and 8 outputs, all digital.

---

### النسخة العربية

## 3.1 البحث والتطوير

كانت CSSP في البداية مشروع تطوير داخلي قبل أن يتم تمويلها⁶ من قبل مشروع البحث والتطوير LCHIP⁷ للحصول على نسخة عامة من المنصة. يهدف هذا المشروع إلى السماح لأي مهندس بتطوير دالة باستخدام لغته الخاصة بالمجال المعتادة والحصول على هذه الدالة تعمل بأمان على منصة أجهزة. مع عملية التطوير التلقائي، سيبقى أسلوب B الرسمي "خلف الستار" من أجل تجنب المعاملات التي تتطلب خبراء. بما أن إثبات السلامة لا يتطلب أي ميزة محددة لنموذج B المُدخل، يمكن أن يكون مكتوباً يدوياً أو ناتجاً ثانوياً لعملية ترجمة.

**الشكل 5:** استخراج نموذج تلقائي فوري من المخططات القائمة على المُرحِّلات وتوليد نموذج B.

⁶ المشروع ممول جزئياً من قبل BPI France و Région PACA و Métropole Aix-Marseille، مع دعم قوي من "أقطاب التنافسية" I-Trans (ليل)، SCS (إكس أون بروفانس) و Systematic (باريس).
⁷ منصة منخفضة التكلفة عالية النزاهة (Low Cost High Integrity Platform).

من المخطط دعم العديد من اللغات الخاصة بالمجال دفعة واحدة (مخطط المُرحِّلات، grafcet) بناءً على واجهة برمجة تطبيقات مفتوحة (Bxml). تتم دراسة الترجمة من مخطط المُرحِّلات للسكك الحديدية الفرنسية. من المتوقع أن تكون العملية بأكملها، بدءاً من نموذج B وانتهاءً بالبرنامج الذي يعمل على منصة الأجهزة، تلقائية بالكامل⁸، حتى مع "النماذج غير البسيطة" مع دمج النتائج التي تم الحصول عليها من بعض مشاريع البحث والتطوير⁹.

⁸ "ضغطة زر" - الكأس المقدسة للصناعة.
⁹ لتحسين أداء البرهان التلقائي (ANR-BWARE)

## 3.2 التعليم

تعتمد بيئة التطوير المتكاملة على Atelier B 4.5.3، وتوفر واجهة مستخدم رسومية مبسطة موجهة نحو العمليات.

**الشكل 6:** مجموعات البدء للتعليم.

تم إصدار مجموعة البدء الأولى، SK0، التي تحتوي على بيئة التطوير المتكاملة ومنصة التنفيذ، بحلول نهاية عام 2017¹⁰، وتم تقديمها وتجربتها بمناسبة العديد من الجلسات العملية المنظمة في مواقع جامعية في أوروبا وأمريكا الشمالية والجنوبية. كان الجمهور متنوعاً، يتراوح من الأتمتة إلى الأنظمة المدمجة، والميكاترونيكس، وعلوم الحاسوب والأساليب الرسمية. النتائج التي تم الحصول عليها مشجعة للغاية:
– يتم تسهيل تعليم الأساليب الرسمية حيث يستطيع الطلاب رؤية نموذجهم يعمل ويتفاعل مع العالم المادي،
– يمكن تقديم/تعليم الملفات الأقل نظرية للجوانب الأكثر تجريداً للحساب،
– أظهرت المنصة متانة معينة خلال كل هذه المعالجات وتم إثراؤها بالتعليقات التي تم جمعها حتى الآن.
– يتم استخدام CSSP حالياً للتدريس في ماجستير السنة الثانية (M2) في الجامعات والمدارس الهندسية.

¹⁰ https://www.clearsy.com/en/our-tools/clearsy-safety-platform/

**الشكل 7:** الاستغلال والانتشار.

## 3.3 الانتشار

تعمل الوحدات البنائية لـ CSSP في أبواب الشاشة المنصة في مترو ساو باولو L15 (معتمد في 2018 عند مستوى SIL3 من قبل CERTIFER على فشل الفتح غير المناسب للأبواب)، في خط مدينة ستوكهولم (معتمد في 2019)، وفي مدينة نيويورك (سيتم اعتماده في 2019).

تم تجربة مجموعة بدء جديدة، SK1، تم إصدارها في نهاية عام 2018 وتهدف إلى النماذج الأولية¹¹، من قبل السكك الحديدية الفرنسية لتحويل المنطق السلكي إلى منطق مبرمج [1] (التحكم في إشارات جانب المسار، نظام الإشارات المؤقت للاتجاه الخاطئ). تجذب مجموعة البدء هذه بالتأكيد الكثير من الاهتمام من الصناعة، من السكك الحديدية ولكن أيضاً من الروبوتات والمركبات ذاتية القيادة. مع CSSP Core القادمة (وحدة التحكم المنطقية القابلة للبرمجة الآمنة) بحلول نهاية عام 2019، من المتوقع المزيد من الانتشار في الصناعة.

¹¹ تحتوي على 20 مدخلاً و 8 مخرجات، جميعها رقمية.

---

### Translation Notes

- **Figures referenced:** Figure 5 (relay schematics to B model), Figure 6 (starter kits), Figure 7 (exploitation and dissemination)
- **Key terms introduced:** Domain Specific Language (DSL), LCHIP, starter kit, SIL3 certification, programmable logic controller
- **Equations:** None
- **Citations:** Reference [1] for French Railways application
- **Special handling:**
  - Multiple footnotes explaining funding sources, acronyms, technical details
  - Geographic locations: São Paulo, Stockholm, New York, France
  - Certification standards: SIL3 by CERTIFER
  - Product names: SK0, SK1, CSSP Core
  - References to real-world deployments

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.87

---

### Back-Translation (Validation)

## 3.1 Research and Development

CSSP was initially an internal development project before being funded⁶ by the LCHIP⁷ R&D project to obtain a generic version of the platform. This project aims to allow any engineer to develop a function using their usual Domain Specific Language and obtain this function running safely on a hardware platform. With the automatic development process, the B formal method will remain "behind the curtain" to avoid transactions requiring experts. Since the safety proof does not require any specific feature for the input B model, it can be handwritten or a by-product of a translation process...

[The back-translation confirms preservation of technical content, certifications, and deployment details]
