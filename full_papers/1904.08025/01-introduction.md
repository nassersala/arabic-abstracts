# Section 1: Introduction
## القسم 1: المقدمة

**Section:** introduction
**Translation Quality:** 0.88
**Glossary Terms Used:** homomorphic encryption, feedback controller, cryptographic, El-Gamal, Paillier, LWE, bootstrapping, fully homomorphic, semi-homomorphic, somewhat-homomorphic

---

### English Version

Applications of homomorphic cryptography to the feedback controller are relatively new. To the authors' knowledge, the first contribution was made by Kogiso and Fujita [1] in 2015, followed by Farokhi et al. [2] and Kim et al. [3] both in 2016. Interestingly, each of them uses different homomorphic encryption schemes; El-Gamal [4], Paillier [5], and LWE [6] are employed, respectively. Because other two schemes are introduced in other chapters in this book, this chapter is written for introducing the LWE-based cryptosystem and its customization for building a dynamic feedback controller.

Homomorphic encryption implies a cryptographic scheme in which arithmetic operations can be performed directly on the encrypted data (i.e., ciphertexts) without decrypting them. When applied to the control systems, security increases because there is no need to keep the secret key inside the controller (see Fig. 1), which is supposed to be a vulnerable point in the feedback loop. After the idea of homomorphic encryption appeared in 1978 by Rivest el al. [7], two semi-homomorphic encryption schemes were developed. One is the multiplicatively homomorphic scheme by El-Gamal [4] developed in 1985, and the other is the additively homomorphic scheme by Paillier [5] developed in 1999. Homomorphic encryption schemes that allow both addition and multiplication appeared around 2000, and they are called somewhat-homomorphic because, even if both arithmetics are enabled, the arithmetic operations can be performed only finite times on an encrypted variable. In 2009, Gentry [6] developed an algorithm called 'bootstrapping' which finally overcame the restriction of finite number of operations. By performing the bootstrapping regularly on the encrypted variable, the variable becomes like a newborn ciphertext and so it allows more operations on it. The encryption scheme with this algorithm is called fully homomorphic. However, fully homomorphic encryption sometimes simply implies a scheme that allows both addition and multiplication, and we follow this convention.

In this chapter, we introduce the LWE-based fully homomorphic encryption scheme. We illustrate that, if the scheme is used with a stable closed-loop system then, interestingly, there is no need to employ the bootstrapping for infinite number of arithmetic operations as long as the system matrix of the controller consists of integer numbers, and the actuator and the sensor sacrifice their resolutions a little bit. Moreover, by utilizing the fully homomorphic arithmetics, we are able to encrypt all the parameters in the controller, as seen in Fig. 1.

This chapter consists of three parts. In the first part (Section 2), we present an introduction to the LWE-based encryption, discuss the homomorphic arithmetics, and illustrate the error growth in the ciphertexts. The second part (Section 3) is about customization of the LWE-based cryptosystem for the linear time-invariant dynamic feedback controllers. In the last part (Section 4), we show the error growth can be handled by the stability, so that the dynamic controller operates seamlessly with unlimited times fully homomorphic arithmetics. In Section 5, we conclude the chapter with a discussion on the need for integer system matrix of the controller, which is related to one of future research issues. For pedagogical purposes, we simplify many issues that should be considered in practice, and instead, focus on the key ingredients of homomorphic encryptions. In the same respect, the codes presented in this chapter consist of simple MATLAB commands that may not be used in real applications even if it works for simple examples.

---

### النسخة العربية

تُعتبر تطبيقات التشفير المتماثل على متحكمات التغذية الراجعة جديدة نسبياً. على حد علم المؤلفين، كانت أول مساهمة من قبل كوجيسو وفوجيتا [1] في عام 2015، تلاها فرخي وآخرون [2] وكيم وآخرون [3] كلاهما في عام 2016. ومن المثير للاهتمام أن كل منهم يستخدم مخططات تشفير متماثلة مختلفة؛ حيث تم استخدام مخططات إل-جمال [4]، وبايلير [5]، وLWE [6]، على التوالي. ولأن المخططين الآخرين يتم تقديمهما في فصول أخرى في هذا الكتاب، فقد كُتب هذا الفصل لتقديم النظام التشفيري القائم على LWE وتخصيصه لبناء متحكم تغذية راجعة ديناميكي.

يشير التشفير المتماثل إلى مخطط تشفيري يمكن فيه إجراء العمليات الحسابية مباشرة على البيانات المشفرة (أي النصوص المشفرة) دون فك تشفيرها. عند تطبيقه على أنظمة التحكم، يزداد الأمان لأنه لا حاجة للاحتفاظ بالمفتاح السري داخل المتحكم (انظر الشكل 1)، والذي يُفترض أنه نقطة ضعف في حلقة التغذية الراجعة. بعد ظهور فكرة التشفير المتماثل في عام 1978 من قبل ريفست وآخرين [7]، تم تطوير مخططي تشفير شبه متماثلين. أحدهما هو المخطط المتماثل الضربي من قبل إل-جمال [4] المطور في عام 1985، والآخر هو المخطط المتماثل الجمعي من قبل بايلير [5] المطور في عام 1999. ظهرت مخططات التشفير المتماثلة التي تسمح بكل من الجمع والضرب حوالي عام 2000، وتُسمى شبه متماثلة لأنه حتى لو كانت كلتا العمليتين الحسابيتين ممكنتين، يمكن إجراء العمليات الحسابية عدداً محدوداً فقط من المرات على متغير مشفر. في عام 2009، طور جنتري [6] خوارزمية تسمى "التمهيد الذاتي" (bootstrapping) التي تغلبت أخيراً على قيد العدد المحدود من العمليات. من خلال إجراء التمهيد الذاتي بانتظام على المتغير المشفر، يصبح المتغير مثل نص مشفر حديث الولادة وبالتالي يسمح بمزيد من العمليات عليه. يُسمى مخطط التشفير مع هذه الخوارزمية بالتشفير المتماثل الكامل. ومع ذلك، يشير التشفير المتماثل الكامل أحياناً ببساطة إلى مخطط يسمح بكل من الجمع والضرب، ونحن نتبع هذا الاصطلاح.

في هذا الفصل، نقدم مخطط التشفير المتماثل الكامل القائم على LWE. نوضح أنه إذا تم استخدام المخطط مع نظام حلقة مغلقة مستقر، فمن المثير للاهتمام أنه لا حاجة لاستخدام التمهيد الذاتي لعدد لا نهائي من العمليات الحسابية طالما أن مصفوفة النظام للمتحكم تتكون من أعداد صحيحة، ويضحي المشغل والمستشعر بدقتهما قليلاً. علاوة على ذلك، من خلال استخدام العمليات الحسابية المتماثلة الكاملة، نستطيع تشفير جميع المعاملات في المتحكم، كما هو موضح في الشكل 1.

يتكون هذا الفصل من ثلاثة أجزاء. في الجزء الأول (القسم 2)، نقدم مقدمة للتشفير القائم على LWE، ونناقش العمليات الحسابية المتماثلة، ونوضح نمو الخطأ في النصوص المشفرة. الجزء الثاني (القسم 3) يتعلق بتخصيص النظام التشفيري القائم على LWE لمتحكمات التغذية الراجعة الديناميكية الخطية الثابتة زمنياً. في الجزء الأخير (القسم 4)، نُظهر أن نمو الخطأ يمكن التعامل معه من خلال الاستقرار، بحيث يعمل المتحكم الديناميكي بسلاسة مع عمليات حسابية متماثلة كاملة غير محدودة. في القسم 5، نختتم الفصل بمناقشة حول الحاجة إلى مصفوفة نظام صحيحة للمتحكم، والتي ترتبط بإحدى قضايا البحث المستقبلية. لأغراض تعليمية، نبسّط العديد من القضايا التي ينبغي أخذها في الاعتبار في الممارسة العملية، وبدلاً من ذلك، نركز على المكونات الرئيسية للتشفير المتماثل. بنفس الروح، تتكون الأكواد المقدمة في هذا الفصل من أوامر MATLAB بسيطة قد لا تُستخدم في التطبيقات الحقيقية حتى لو كانت تعمل للأمثلة البسيطة.

---

### Translation Notes

- **Figures referenced:** Figure 1 (control system configuration)
- **Key terms introduced:** homomorphic encryption (متماثل), bootstrapping (التمهيد الذاتي), semi-homomorphic (شبه متماثل), somewhat-homomorphic (شبه متماثل), fully homomorphic (متماثل كامل)
- **Historical context:** Timeline of homomorphic encryption development (1978-2009)
- **Citations:** 7 references cited [1-7]
- **Special handling:** Author names kept in English, mathematical concepts preserved

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88
