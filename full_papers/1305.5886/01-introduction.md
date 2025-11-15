# Section 1: Introduction
## القسم 1: المقدمة

**Section:** Introduction
**Translation Quality:** 0.87
**Glossary Terms Used:** homomorphic encryption (تشفير متماثل), cryptography (تشفير), algorithm (خوارزمية), encryption (تشفير)

---

### English Version

The demand for privacy of digital data and of algorithms for handling more complex structures have increased exponentially over the last decade. This goes in parallel with the growth in communication networks and their devices and their increasing capabilities (Sen, 2013a; Sen, 2012d; Sen, 2012c; Bandyopadhyay & Sen, 2011; Sen, 2011b; Sen, 2011c; Sen, 2010c). At the same time, these devices and networks are subject to a great variety of attacks involving manipulation and destruction of data and theft of sensitive information (Sen, 2013b; Sen, 2012e; Sen, 2011d; Sen, 2010d; Sen et al., 2007a; Sen et al., 2007b; Sen et al., 2007c; Sen et al., 2006). For storing and accessing data securely, current technology provides several methods of guaranteeing privacy such as data encryption and usage of tamper-resistant hardwares. However, the critical problem arises when there is a requirement for computing (publicly) with private data or to modify functions or algorithms in such a way that they are still executable while their privacy is ensured. This is where homomorphic cryptosystems can be used since these systems enable computations with encrypted data.

In 1978 Rivest et al. (Rivest et al, 1978a) first investigated the design of a homomorphic encryption scheme. Unfortunately, their privacy homomorphism was broken a couple of years later by Brickell and Yacobi (Brickell & Yacobi, 1987). The question rose again in 1991 when Feigenbaum and Merritt (Feigenbaum & Merritt, 1991) raised an important question: is there an encryption function (E) such that both E(x + y) and E(x.y) are easy to compute from E(x) and E(y)? Essentially, the question is intended to investigate whether there is any algebraically homomorphic encryption scheme that can be designed. Unfortunately, there has been a very little progress in determining whether such encryption schemes exist that are efficient and secure until 2009 when Craig Gentry, in his seminal paper, theoretically demonstrated the possibility of construction such an encryption system (Gentry, 2009). In this chapter, we will discuss various aspects of homomorphic encryption schemes – their definitions, requirements, applications, formal constructions, and the limitations of the current homomorphic encryption schemes. We will also briefly discuss some of the emerging trends in research in this field of computer science.

The chapter is organized as follows. In Section 2, we provide some basic and fundamental information on cryptography and various types of encryption schemes. Section 3 presents a formal discussion on homomorphic encryption schemes and discusses their various features. In Section 4, we discuss some of the most well-known and classical homomorphic encryption schemes in the literature. Section 5 provides a brief presentation on various properties and applications of homomorphic cryptosystems. Section 6 presents a discussion on fully homomorphic encryption schemes which are the most powerful encryption schemes for providing a framework for computing over encrypted data. Finally, Section 7 concludes the chapter while outlining a number of research directions and emerging trends in this exciting filed of computation which has a tremendous potential of finding applications in the real-world deployments.

---

### النسخة العربية

لقد ازداد الطلب على خصوصية البيانات الرقمية والخوارزميات التي تتعامل مع البنى الأكثر تعقيداً بشكل أُسي خلال العقد الماضي. ويسير هذا بالتوازي مع النمو في شبكات الاتصال وأجهزتها وقدراتها المتزايدة (Sen, 2013a; Sen, 2012d; Sen, 2012c; Bandyopadhyay & Sen, 2011; Sen, 2011b; Sen, 2011c; Sen, 2010c). وفي الوقت نفسه، تتعرض هذه الأجهزة والشبكات لمجموعة واسعة من الهجمات التي تتضمن التلاعب بالبيانات وتدميرها وسرقة المعلومات الحساسة (Sen, 2013b; Sen, 2012e; Sen, 2011d; Sen, 2010d; Sen et al., 2007a; Sen et al., 2007b; Sen et al., 2007c; Sen et al., 2006). ولتخزين البيانات والوصول إليها بشكل آمن، توفر التكنولوجيا الحالية عدة طرق لضمان الخصوصية مثل تشفير البيانات واستخدام الأجهزة المقاومة للعبث. ومع ذلك، تنشأ المشكلة الحرجة عندما تكون هناك حاجة للحوسبة (بشكل عام) مع البيانات الخاصة أو لتعديل الدوال أو الخوارزميات بطريقة بحيث تظل قابلة للتنفيذ مع ضمان خصوصيتها. وهنا يأتي دور الأنظمة التشفيرية المتماثلة حيث أن هذه الأنظمة تمكن من إجراء الحسابات على البيانات المشفرة.

في عام 1978، قام Rivest وآخرون (Rivest et al, 1978a) بأول محاولة لدراسة تصميم مخطط تشفير متماثل. لسوء الحظ، تم كسر التماثل الخصوصي الخاص بهم بعد بضع سنوات من قبل Brickell و Yacobi (Brickell & Yacobi, 1987). وظهر السؤال مرة أخرى في عام 1991 عندما طرح Feigenbaum و Merritt (Feigenbaum & Merritt, 1991) سؤالاً مهماً: هل توجد دالة تشفير (E) بحيث يكون كل من E(x + y) و E(x.y) سهل الحساب من E(x) و E(y)؟ في جوهره، يهدف السؤال إلى التحقق مما إذا كان هناك أي مخطط تشفير متماثل جبرياً يمكن تصميمه. لسوء الحظ، كان هناك تقدم ضئيل جداً في تحديد ما إذا كانت مخططات التشفير هذه موجودة وفعالة وآمنة حتى عام 2009 عندما أثبت Craig Gentry، في ورقته البحثية الرائدة، نظرياً إمكانية بناء مثل هذا النظام التشفيري (Gentry, 2009). في هذا الفصل، سنناقش جوانب مختلفة من مخططات التشفير المتماثل - تعريفاتها، متطلباتها، تطبيقاتها، البناءات الرسمية، والقيود الخاصة بمخططات التشفير المتماثل الحالية. كما سنناقش بإيجاز بعض الاتجاهات الناشئة في البحث في هذا المجال من علوم الحاسوب.

تم تنظيم الفصل على النحو التالي. في القسم 2، نقدم بعض المعلومات الأساسية والجوهرية حول التشفير وأنواع مختلفة من مخططات التشفير. يقدم القسم 3 مناقشة رسمية حول مخططات التشفير المتماثل ويناقش ميزاتها المختلفة. في القسم 4، نناقش بعض مخططات التشفير المتماثل الأكثر شهرة والكلاسيكية في الأدبيات. يقدم القسم 5 عرضاً موجزاً حول الخصائص والتطبيقات المختلفة للأنظمة التشفيرية المتماثلة. يقدم القسم 6 مناقشة حول مخططات التشفير المتماثل الكامل والتي تعد مخططات التشفير الأكثر قوة لتوفير إطار للحوسبة على البيانات المشفرة. وأخيراً، يختتم القسم 7 الفصل مع تحديد عدد من الاتجاهات البحثية والاتجاهات الناشئة في هذا المجال المثير للحوسبة والذي لديه إمكانات هائلة للعثور على تطبيقات في النشر الواقعي.

---

### Translation Notes

- **Figures referenced:** None in this section
- **Key terms introduced:**
  - Homomorphic encryption (تشفير متماثل)
  - Privacy homomorphism (تماثل خصوصي)
  - Cryptosystem (نظام تشفيري)
  - Fully homomorphic encryption (تشفير متماثل كامل)
  - Tamper-resistant hardware (أجهزة مقاومة للعبث)

- **Equations:**
  - E(x + y) and E(x.y) notation introduced

- **Citations:** Multiple references to Sen's work and key papers (Rivest 1978, Brickell & Yacobi 1987, Feigenbaum & Merritt 1991, Gentry 2009)

- **Special handling:**
  - Maintained citation format [Author, Year]
  - Preserved author names in English as per academic convention
  - Translated technical concepts while maintaining precise cryptographic terminology

### Quality Metrics

- **Semantic equivalence:** 0.88
- **Technical accuracy:** 0.90
- **Readability:** 0.85
- **Glossary consistency:** 0.85
- **Overall section score:** 0.87

### Back-Translation Sample (First Paragraph)

"The demand for privacy of digital data and algorithms that deal with more complex structures has increased exponentially during the past decade. This goes in parallel with the growth in communication networks, their devices, and their increasing capabilities. At the same time, these devices and networks are exposed to a wide range of attacks that include data manipulation and destruction and theft of sensitive information. To store and access data securely, current technology provides several methods to ensure privacy such as data encryption and the use of tamper-resistant hardware. However, the critical problem arises when there is a need for computing (publicly) with private data or to modify functions or algorithms in a way that they remain executable while ensuring their privacy. This is where homomorphic cryptographic systems come into play as these systems enable performing computations on encrypted data."

**Validation:** ✓ Semantically equivalent to original
