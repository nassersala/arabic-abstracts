# Section 3: Running Example: Tokeneer
## القسم 3: مثال تشغيلي: Tokeneer

**Section:** running-example
**Translation Quality:** 0.87
**Glossary Terms Used:** security (أمان), authentication (مصادقة), verification (التحقق), formal methods (الأساليب الرسمية), certification (الاعتماد)

---

### English Version

To demonstrate our approach, we use the Tokeneer Identification Station (TIS) illustrated in Figure 4, a system that guards entry to a secure enclave by ensuring that only authorised users are admitted.

The relevant physical infrastructure consists of a door, a fingerprint reader, a display, and a card (token) reader. The main function of the TIS is to check the stored credentials on a presented token, read a fingerprint if necessary, and then either unlatches the door, or denies entry. Entry is permitted when the token holds at least three data items: (1) an ID certificate, which identifies the user, (2) a privilege certificate, which stores a clearance level, and (3) an identification and authentication (I&A) certificate, which assigns a fingerprint template. When the user first presents their token the three certificates are read and cross-checked. If the token is valid, then a fingerprint is taken, which if validated against the I&A certificate, allows the door to be unlocked once the token is removed. An optional authorisation certificate is also written upon successful authentication which allows the fingerprint check to be skipped.

The TIS has a variety of other functions related to its administration. Before use, a TIS must be enrolled, meaning it is loaded with a public key chain and certificate, which are needed to check token certificates. Moreover, the TIS stores audit data which can be used to check previously occurred entries. The TIS therefore also has a keyboard, floppy drive, and screen to configure it. Administrators are granted access to these functions. The TIS also has an alarm which will sound if the door is left open for too long.

Our objective is to construct an assurance case that argues that the TIS fulfils its security properties and complies to the Common Criteria (CC) standard [4]. CC supports a vendor in delivering a system compliant to a security level while a certification authority confirms compliance and further qualities. The standard defines seven Evaluation Assurance Levels (EALs), each a collection of Security Functional Requirements (SFRs) and Security Assurance Requirements (SARs) the system would have to meet. Formal Methods (FMs) are strongly recommended for EAL 5 and above. Now, one can either (a) use a pre-specified set of general security properties, or (b) develop an application-specific set with the potential of additional effort due to requirements analysis. The security of the TIS is assured according to (b) by demonstrating six SFRs [6], of which the first four are shown here and detailed below in section 5:

**SFR1** If the latch is unlocked by TIS, then TIS must be in possession of either a User Token or an Admin Token. The User Token must either have a valid Authorisation Certificate, or must have valid ID, Privilege, and I&A Certificates, together with a template that allowed TIS to successfully validate the user's fingerprint. Or, if the User Token does not meet this, the Admin Token must have a valid Authorisation Certificate, with role of "guard".

**SFR2** If the latch is unlocked automatically by TIS, then the current time must be close to being within the allowed entry period defined for the User requesting access.

**SFR3** An alarm will be raised whenever the door/latch is insecure.

**SFR4** No audit data is lost without an audit alarm being raised.

The pioneering work on the assurance of the TIS according to option (b) was carried out by Praxis High Integrity Systems and SPRE Inc. [1]. Barnes et al. performed security analysis, specification using Z, implementation in SPARK, and verification and test of the security properties. After independent assessment EAL 5 was achieved. This way, Tokeneer became a successful example of the use of FMs in assuring a system against CC.

---

### النسخة العربية

لتوضيح نهجنا، نستخدم محطة التعريف Tokeneer (TIS) الموضحة في الشكل 4، وهو نظام يحرس الدخول إلى حاوية آمنة من خلال ضمان قبول المستخدمين المصرح لهم فقط.

تتكون البنية التحتية المادية ذات الصلة من باب، وقارئ بصمات الأصابع، وشاشة عرض، وقارئ بطاقة (رمز مميز). الوظيفة الرئيسية لـ TIS هي التحقق من بيانات الاعتماد المخزنة على رمز مميز مقدم، وقراءة بصمة الإصبع إذا لزم الأمر، ثم إما فتح قفل الباب، أو رفض الدخول. يُسمح بالدخول عندما يحتوي الرمز المميز على ثلاثة عناصر بيانات على الأقل: (1) شهادة الهوية، التي تحدد المستخدم، (2) شهادة الامتياز، التي تخزن مستوى التخليص، و(3) شهادة التعريف والمصادقة (I&A)، التي تعيّن قالب بصمة الإصبع. عندما يقدم المستخدم رمزه المميز لأول مرة، يتم قراءة الشهادات الثلاث والتحقق المتقاطع منها. إذا كان الرمز المميز صالحاً، فإنه يتم أخذ بصمة الإصبع، والتي إذا تم التحقق من صحتها مقابل شهادة I&A، تسمح بفتح قفل الباب بمجرد إزالة الرمز المميز. تُكتب أيضاً شهادة ترخيص اختيارية عند المصادقة الناجحة والتي تسمح بتخطي فحص بصمة الإصبع.

لدى TIS مجموعة متنوعة من الوظائف الأخرى المتعلقة بإدارته. قبل الاستخدام، يجب تسجيل TIS، مما يعني تحميله بسلسلة مفاتيح عامة وشهادة، والتي تكون مطلوبة للتحقق من شهادات الرموز المميزة. علاوة على ذلك، يخزن TIS بيانات التدقيق التي يمكن استخدامها للتحقق من الإدخالات التي حدثت سابقاً. لذلك يحتوي TIS أيضاً على لوحة مفاتيح، ومحرك أقراص مرنة، وشاشة لتكوينه. يُمنح المسؤولون الوصول إلى هذه الوظائف. يحتوي TIS أيضاً على إنذار سيصدر صوتاً إذا تُرك الباب مفتوحاً لفترة طويلة جداً.

هدفنا هو إنشاء حالة ضمان تجادل بأن TIS يفي بخصائص الأمان الخاصة به ويتوافق مع معيار المعايير المشتركة (CC) [4]. يدعم CC البائع في تسليم نظام متوافق مع مستوى أمان بينما تؤكد سلطة الاعتماد الامتثال والصفات الإضافية. يحدد المعيار سبعة مستويات ضمان التقييم (EALs)، كل منها مجموعة من متطلبات الأمان الوظيفية (SFRs) ومتطلبات ضمان الأمان (SARs) التي يجب على النظام تلبيتها. يوصى بشدة بالأساليب الرسمية (FMs) لـ EAL 5 وما فوق. الآن، يمكن للمرء إما (أ) استخدام مجموعة محددة مسبقاً من خصائص الأمان العامة، أو (ب) تطوير مجموعة خاصة بالتطبيق مع إمكانية الجهد الإضافي بسبب تحليل المتطلبات. يتم ضمان أمان TIS وفقاً لـ (ب) من خلال إظهار ستة SFRs [6]، والتي يتم عرض الأربعة الأولى منها هنا وتفصيلها أدناه في القسم 5:

**SFR1** إذا تم فتح قفل المزلاج بواسطة TIS، فيجب أن يكون TIS في حيازة إما رمز مميز للمستخدم أو رمز مميز للمسؤول. يجب أن يحتوي رمز المستخدم المميز إما على شهادة ترخيص صالحة، أو يجب أن يحتوي على شهادات هوية وامتياز و I&A صالحة، جنباً إلى جنب مع قالب سمح لـ TIS بالتحقق من صحة بصمة إصبع المستخدم بنجاح. أو، إذا لم يستوف رمز المستخدم المميز ذلك، فيجب أن يحتوي رمز المسؤول المميز على شهادة ترخيص صالحة، بدور "حارس".

**SFR2** إذا تم فتح قفل المزلاج تلقائياً بواسطة TIS، فيجب أن يكون الوقت الحالي قريباً من أن يكون ضمن فترة الدخول المسموح بها المحددة للمستخدم الذي يطلب الوصول.

**SFR3** سيتم رفع إنذار كلما كان الباب/المزلاج غير آمن.

**SFR4** لا تُفقد بيانات التدقيق دون رفع إنذار تدقيق.

تم تنفيذ العمل الرائد على ضمان TIS وفقاً للخيار (ب) بواسطة Praxis High Integrity Systems و SPRE Inc. [1]. أجرى Barnes وآخرون تحليل الأمان، والمواصفات باستخدام Z، والتنفيذ في SPARK، والتحقق واختبار خصائص الأمان. بعد التقييم المستقل، تم تحقيق EAL 5. بهذه الطريقة، أصبح Tokeneer مثالاً ناجحاً على استخدام الأساليب الرسمية في ضمان نظام ضد CC.

---

### Translation Notes

- **Figures referenced:** Figure 4 (Tokeneer System Overview)
- **Key terms introduced:**
  - Tokeneer Identification Station - TIS (محطة التعريف Tokeneer)
  - Token (رمز مميز)
  - ID certificate (شهادة الهوية)
  - Privilege certificate (شهادة الامتياز)
  - I&A certificate - Identification and Authentication (شهادة التعريف والمصادقة)
  - Fingerprint template (قالب بصمة الإصبع)
  - Authorisation certificate (شهادة ترخيص)
  - Common Criteria - CC (المعايير المشتركة)
  - Evaluation Assurance Levels - EALs (مستويات ضمان التقييم)
  - Security Functional Requirements - SFRs (متطلبات الأمان الوظيفية)
  - Security Assurance Requirements - SARs (متطلبات ضمان الأمان)
  - Z notation (تدوين Z)
  - SPARK
- **Equations:** 0
- **Citations:** [1,4,6]
- **Special handling:**
  - Technical system names (TIS, Tokeneer, SPARK, Z) kept in English
  - SFR1-SFR4 kept as is (standard requirement labels)
  - Company names (Praxis High Integrity Systems, SPRE Inc.) kept in English
  - Standard names (Common Criteria, ISO, EAL) kept in English

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
