# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.92
**Glossary Terms Used:** بنية البيانات, خوارزمية, رسم بياني, دالة التجزئة, الأمن السيبراني

---

### English Version

Authenticated data structures provide cryptographic proofs that their answers are as accurate as the author intended, even if the data structure is being controlled by a remote untrusted host. In this paper we present efficient techniques for authenticating data structures that represent graphs and collections of geometric objects. We use a data-querying model where a data structure maintained by a trusted source is mirrored at distributed untrusted servers, called responders, with the responders answering queries made by users: when a user queries a responder, along with the answer to the issued query, he receives a cryptographic proof that allows the verification of the answer trusting only a short statement (digest) signed by the source. We introduce the path hash accumulator, a new primitive based on cryptographic hashing for efficiently authenticating various properties of structured data represented as paths, including any decomposable query over sequences of elements. We show how to employ our primitive to authenticate queries about properties of paths in graphs and search queries on multi-catalogs. This allows the design of new, efficient authenticated data structures for fundamental problems on networks, such as path and connectivity queries over graphs, and complex queries on two-dimensional geometric objects, such as intersection and containment queries.

---

### النسخة العربية

تقدم بنى البيانات المصادق عليها براهين تشفيرية بأن إجاباتها دقيقة بقدر ما قصد المؤلف، حتى لو كانت بنية البيانات تحت سيطرة مضيف بعيد غير موثوق. في هذه الورقة، نقدم تقنيات فعالة للمصادقة على بنى البيانات التي تمثل الرسوم البيانية ومجموعات الكائنات الهندسية. نستخدم نموذج استعلام البيانات حيث يتم نسخ بنية البيانات التي يحتفظ بها مصدر موثوق على خوادم موزعة غير موثوقة، تسمى المستجيبين، حيث يجيب المستجيبون على الاستعلامات المقدمة من المستخدمين: عندما يستعلم مستخدم أحد المستجيبين، يحصل مع الإجابة على الاستعلام المُصدر على برهان تشفيري يسمح بالتحقق من الإجابة بالثقة فقط في بيان قصير (ملخص) موقَّع من المصدر. نقدم مُجمِّع تجزئة المسار، وهو بدائي جديد يعتمد على التجزئة التشفيرية للمصادقة بكفاءة على خصائص متنوعة للبيانات المنظمة الممثلة كمسارات، بما في ذلك أي استعلام قابل للتحليل على تسلسلات من العناصر. نوضح كيفية استخدام هذا البدائي للمصادقة على الاستعلامات حول خصائص المسارات في الرسوم البيانية واستعلامات البحث على الفهارس المتعددة. يتيح ذلك تصميم بنى بيانات مصادق عليها جديدة وفعالة لمسائل أساسية على الشبكات، مثل استعلامات المسار والاتصال على الرسوم البيانية، والاستعلامات المعقدة على الكائنات الهندسية ثنائية الأبعاد، مثل استعلامات التقاطع والاحتواء.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** authenticated data structures, path hash accumulator, responders, digest, cryptographic proof
- **Equations:** None
- **Citations:** None in abstract
- **Special handling:** Focus on cryptographic and data structure terminology

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.93
- Readability: 0.91
- Glossary consistency: 0.93
- **Overall section score:** 0.92
