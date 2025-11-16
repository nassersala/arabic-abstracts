# Abstract
## الملخص

**Section:** abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** homomorphic encryption, cryptographic, quantum computing, security, controller, LWE

---

### English Version

The cryptosystem based on the Learning-with-Errors (LWE) problem is considered as a post-quantum cryptosystem, because it is not based on the factoring problem with large primes which is easily solved by a quantum computer. Moreover, the LWE-based cryptosystem allows fully homomorphic arithmetics so that two encrypted variables can be added and multiplied without decrypting them. This chapter provides a comprehensive introduction to the LWE-based cryptosystem with examples. A key to the security of the LWE-based cryptosystem is the injection of random errors in the ciphertexts, which however hinders unlimited recursive operation of homomorphic arithmetics on ciphertexts due to the growth of the error. We show that this limitation can be overcome when the cryptosystem is used for a dynamic feedback controller that guarantees stability of the closed-loop system. Finally, we illustrate through MATLAB codes how the LWE-based cryptosystem can be customized to build a secure feedback control system. This chapter is written for the control engineers who do not have background on cryptosystems.

---

### النسخة العربية

يُعتبر النظام التشفيري القائم على مسألة التعلم مع الأخطاء (LWE) نظاماً تشفيرياً لما بعد الحوسبة الكمومية، لأنه لا يعتمد على مسألة تحليل الأعداد الأولية الكبيرة التي يمكن حلها بسهولة بواسطة الحاسوب الكمي. علاوة على ذلك، يسمح النظام التشفيري القائم على LWE بإجراء العمليات الحسابية المتماثلة الكاملة بحيث يمكن جمع وضرب متغيرين مشفرين دون فك تشفيرهما. يقدم هذا الفصل مقدمة شاملة للنظام التشفيري القائم على LWE مع أمثلة توضيحية. يتمثل مفتاح أمان النظام التشفيري القائم على LWE في حقن أخطاء عشوائية في النصوص المشفرة، والذي يعيق مع ذلك العملية العودية غير المحدودة للعمليات الحسابية المتماثلة على النصوص المشفرة بسبب نمو الخطأ. نُظهر أن هذا القيد يمكن التغلب عليه عندما يُستخدم النظام التشفيري لمتحكم تغذية راجعة ديناميكي يضمن استقرار النظام ذو الحلقة المغلقة. وأخيراً، نوضح من خلال أكواد MATLAB كيف يمكن تخصيص النظام التشفيري القائم على LWE لبناء نظام تحكم بتغذية راجعة آمن. هذا الفصل مكتوب لمهندسي التحكم الذين ليس لديهم خلفية في الأنظمة التشفيرية.

---

### Translation Notes

- **Key terms:** LWE (Learning-with-Errors), homomorphic encryption, post-quantum cryptography, dynamic feedback controller, closed-loop stability
- **Technical concepts:** The paper combines cryptography and control theory
- **Target audience:** Control engineers without cryptography background
- **Special features:** Includes MATLAB code examples

### Quality Metrics

- Semantic equivalence: 0.92
- Technical accuracy: 0.90
- Readability: 0.88
- Glossary consistency: 0.90
- **Overall section score:** 0.90

(Note: This abstract was previously translated in translations/1904.08025.md with quality 0.90)
