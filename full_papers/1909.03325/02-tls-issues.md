# Section 2: TLS and its issues
## القسم 2: بروتوكول TLS ومشاكله

**Section:** tls-issues
**Translation Quality:** 0.87
**Glossary Terms Used:** TLS (أمن طبقة النقل), SSL (طبقة المقابس الآمنة), encryption (التشفير), hashing (التجزئة), implementation (التنفيذ), bounds checking (فحص الحدود), static analysis (التحليل الساكن), protocol (بروتوكول)

---

### English Version

The TLS protocol (and its predecessor SSL) are the basis of most Internet security, underpinning, for example, https. They also have displayed some of the most prominent problems.

**Correctness** Paulson [56] "Proved TLS Secure", according to folklore. More precisely, the abstract states "All the obvious security goals can be proved", but the paper itself is more more nuanced.

> Is TLS really secure? My proofs suggest that it is, but one should draw no conclusions without reading the rest of this paper, which describes how the protocol was modelled and what properties were proved. I have analyzed a much simplified form of TLS; I assume hashing and encryption to be secure.

There has been much work on TLS security since, e.g. [28, 37]. In particular, the latter used 'real' encryption, the RSA PKCS #1 v1.5, recommended, rather than 'ideal' encryption. Again, these all focus on the idealised protocol, rather than implementations.

**Heartbleed [49]** This, arguably the most serious security issue of 2014, at least as perceived by the media (for example [4]) and the public (for example [63]), was a bug in a particular, but very widely used, implementation (OpenSSL) of TLS, and hence instantly falls outside the scope of [56]. Furthermore, it was a bug in an extension [61] which postdates [56]. [61] states "This document does not introduce any new security considerations", which is also true.

The bug itself was a bounds checking bug, and thus could have been flagged by even relatively weak static analysis tools. Looking a bit deeper, it was caused by assuming that the other end was behaving correctly. This seems to be a general class of errors, oddly missing from [1].

**Poodle [46, 50]** This also appeared in 2014. It requires two "features" to operate.

1. Many TLS implementations contain ways to downgrade to SSL 3.0 if the other end doesn't support TLS itself. However this downgrade (again, a feature of implementations, so outside the scope of [56]) is typically not a proper protocol negotiation, and can be subverted by an active attacker. As [1] state "where the identity of a principal is essential to the meaning of a message, it should be mentioned explicitly in the message", and indeed should be authenticated.

2. Once downgraded to SSL 3.0, the attacker can exploit this.
   > The most severe problem of CBC encryption in SSL 3.0 is that its block cipher padding is not deterministic, and not covered by the MAC (Message Authentication Code): thus, the integrity of padding cannot be fully verified when decrypting. [46]

Paulson [56] states, not unreasonably, "I assume hashing and encryption to be secure", as this is a separate set of proof technologies, and generally only produces relative security proofs.

Hence we have a proof of correctness of a (simplified, but in fact the simplification is irrelevant here) version of an abstract protocol, and major bugs in implementations. One is a "coding" bug, while the other is a combination of a protocol bug and a cryptography bug. Though not directly relevant to this paper, [60] demonstrates that Heartbleed (and Poodle) had a major positive effect on the OpenSSL project.

---

### النسخة العربية

يشكل بروتوكول TLS (وسلفه SSL) أساس معظم الأمن على الإنترنت، حيث يدعم، على سبيل المثال، https. كما أظهرا بعض المشاكل الأكثر بروزاً.

**الصحة** أثبت Paulson [56] "أمان TLS"، وفقاً للمعرفة الشائعة. بشكل أدق، ينص الملخص على أن "جميع أهداف الأمان الواضحة يمكن إثباتها"، لكن الورقة نفسها أكثر دقة.

> هل TLS آمن حقاً؟ تشير براهيني إلى ذلك، لكن لا ينبغي استخلاص أي استنتاجات دون قراءة بقية هذه الورقة، التي تصف كيفية نمذجة البروتوكول والخصائص التي تم إثباتها. لقد حللت شكلاً مبسطاً للغاية من TLS؛ أفترض أن التجزئة والتشفير آمنان.

كان هناك الكثير من العمل على أمان TLS منذ ذلك الحين، مثل [28، 37]. على وجه الخصوص، استخدمت الأخيرة التشفير "الحقيقي"، RSA PKCS #1 v1.5، الموصى به، بدلاً من التشفير "المثالي". مرة أخرى، تركز كل هذه على البروتوكول المثالي، وليس على التنفيذات.

**Heartbleed [49]** هذه، القضية الأمنية الأكثر خطورة في عام 2014، على الأقل كما يُنظر إليها من قبل وسائل الإعلام (على سبيل المثال [4]) والجمهور (على سبيل المثال [63])، كانت خطأ في تنفيذ معين، ولكن مستخدم على نطاق واسع جداً، (OpenSSL) من TLS، وبالتالي تقع على الفور خارج نطاق [56]. علاوة على ذلك، كان خطأ في امتداد [61] جاء بعد [56]. تنص [61] على أن "هذه الوثيقة لا تقدم أي اعتبارات أمنية جديدة"، وهو أيضاً صحيح.

كان الخطأ نفسه خطأ في فحص الحدود، وبالتالي كان يمكن الإشارة إليه حتى بواسطة أدوات التحليل الساكن الضعيفة نسبياً. بالنظر بشكل أعمق قليلاً، كان ناتجاً عن افتراض أن الطرف الآخر يتصرف بشكل صحيح. يبدو أن هذه فئة عامة من الأخطاء، غائبة بشكل غريب عن [1].

**Poodle [46، 50]** ظهر هذا أيضاً في عام 2014. يتطلب "ميزتين" للعمل.

1. تحتوي العديد من تنفيذات TLS على طرق للتخفيض إلى SSL 3.0 إذا كان الطرف الآخر لا يدعم TLS نفسه. ومع ذلك، فإن هذا التخفيض (مرة أخرى، ميزة من التنفيذات، وبالتالي خارج نطاق [56]) عادةً ليس تفاوضاً صحيحاً للبروتوكول، ويمكن تخريبه من قبل مهاجم نشط. كما تنص [1] "حيث تكون هوية الجهة الأساسية ضرورية لمعنى الرسالة، يجب ذكرها صراحةً في الرسالة"، ويجب بالفعل مصادقتها.

2. بمجرد التخفيض إلى SSL 3.0، يمكن للمهاجم استغلال هذا.
   > المشكلة الأكثر خطورة في تشفير CBC في SSL 3.0 هي أن حشو كتلة الشفرة الخاص بها ليس حتمياً، وغير مغطى بواسطة MAC (كود مصادقة الرسالة): وبالتالي، لا يمكن التحقق بشكل كامل من سلامة الحشو عند فك التشفير. [46]

ينص Paulson [56]، بشكل معقول، "أفترض أن التجزئة والتشفير آمنان"، حيث أن هذه مجموعة منفصلة من تقنيات الإثبات، وعموماً تنتج فقط إثباتات أمان نسبية.

وبالتالي لدينا إثبات لصحة نسخة (مبسطة، ولكن في الواقع التبسيط غير ذي صلة هنا) من بروتوكول مجرد، وأخطاء رئيسية في التنفيذات. أحدها خطأ "برمجة"، بينما الآخر هو مزيج من خطأ بروتوكول وخطأ تشفير. على الرغم من أنه ليس ذا صلة مباشرة بهذه الورقة، توضح [60] أن Heartbleed (و Poodle) كان لهما تأثير إيجابي كبير على مشروع OpenSSL.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** TLS protocol, SSL, Heartbleed vulnerability, Poodle vulnerability, bounds checking, OpenSSL, CBC encryption, MAC (Message Authentication Code)
- **Equations:** 0
- **Citations:** [1], [4], [28], [37], [46], [49], [50], [56], [60], [61], [63]
- **Special handling:** Quoted passages preserved with block quotes; technical vulnerability names (Heartbleed, Poodle) kept in English as they are proper names

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
