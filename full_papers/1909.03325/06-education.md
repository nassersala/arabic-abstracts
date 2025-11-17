# Section 6: Education
## القسم 6: التعليم

**Section:** education
**Translation Quality:** 0.86
**Glossary Terms Used:** cybersecurity (الأمن السيبراني), security awareness (الوعي الأمني), cross-site request forgery (CSRF - تزوير الطلبات عبر المواقع), Stack Overflow (ستاك أوفرفلو)

---

### English Version

[57, Requirement 6.5] called for education of developers. Education of mainstream programmers, as opposed to CyberSecurity specialists, in CyberSecurity has been neglected until recently, and this neglect has been lamented as far as the Harvard Business Review [12]. Developments in professional accreditation are changing this [20]. However, there are limitations, even beyond errare humanum est, in relying on education.

1. There is experimental evidence that both trained students [48] and professional developers [47] will ignore security considerations unless explicitly instructed to take them into account. Lest this be thought to be a purely academic exercise with little relevance to the real world, consider the recent Y55M password problem described in [19].

2. There is field evidence that explicit requirements such as [57] are ignored in practice, e.g. the Forever 21 breach [7], or Macy's [8]. They may also not be communicated down the software supply chain, as in the Ticketmaster case [32].

3. Many educational resources, both formal textbooks [65] and informal resources such as Stack Overflow [22], pay very little attention to security, and indeed can be positively harmful. The discussion in Stack Overflow (analysed in [44, §4.3.1]) of cross-site request forgery (CSRF — this was in the OWASP top 10 in 2013 [53], but dropped from [54] "as many frameworks include CSRF defenses") is especially worrying. By default, Spring implicitly enables protection against this. But all the accepted answers to CSRF-related failures simply suggested disabling the check. There were no negative comments about this, and indeed a typical response is "Adding csrf().disable() solved the issue!!! I have no idea why it was enabled by default".

As we have noted, [57] both mandates education and does not rely solely on it.

However, as the safety-critical community laments (at least in the U.K. and U.S.A.: cultures do differ here), there is very little training in formal methods for most undergraduates.

---

### النسخة العربية

دعت [57، المتطلب 6.5] إلى تعليم المطورين. تم إهمال تعليم المبرمجين الرئيسيين، على عكس متخصصي الأمن السيبراني، في الأمن السيبراني حتى وقت قريب، وقد تم رثاء هذا الإهمال حتى في Harvard Business Review [12]. التطورات في الاعتماد المهني تغير هذا [20]. ومع ذلك، هناك قيود، حتى بعيداً عن الخطأ من طبيعة البشر (errare humanum est)، في الاعتماد على التعليم.

1. هناك دليل تجريبي على أن كلاً من الطلاب المدربين [48] والمطورين المحترفين [47] سيتجاهلون الاعتبارات الأمنية ما لم يُطلب منهم صراحةً أخذها في الاعتبار. لئلا يُعتقد أن هذا مجرد تمرين أكاديمي بحت له صلة قليلة بالعالم الحقيقي، انظر إلى مشكلة كلمة مرور Y55M الحديثة الموصوفة في [19].

2. هناك دليل ميداني على أن المتطلبات الصريحة مثل [57] يتم تجاهلها في الممارسة، مثل اختراق Forever 21 [7]، أو Macy's [8]. قد لا يتم أيضاً توصيلها عبر سلسلة توريد البرمجيات، كما في حالة Ticketmaster [32].

3. العديد من الموارد التعليمية، سواء الكتب المدرسية الرسمية [65] أو الموارد غير الرسمية مثل Stack Overflow [22]، تولي اهتماماً قليلاً جداً للأمن، بل يمكن أن تكون ضارة بشكل إيجابي. المناقشة في Stack Overflow (المحللة في [44، §4.3.1]) حول تزوير الطلبات عبر المواقع (CSRF — كان هذا في أعلى 10 لـ OWASP في عام 2013 [53]، لكنه أُسقط من [54] "حيث تتضمن العديد من الأطر دفاعات CSRF") مثيرة للقلق بشكل خاص. بشكل افتراضي، يمكّن Spring ضمنياً الحماية ضد هذا. لكن جميع الإجابات المقبولة على إخفاقات CSRF اقترحت ببساطة تعطيل الفحص. لم تكن هناك تعليقات سلبية حول هذا، وفي الواقع كانت استجابة نموذجية هي "إضافة csrf().disable() حلت المشكلة!!! ليس لدي أي فكرة لماذا تم تمكينها بشكل افتراضي".

كما لاحظنا، [57] تفرض التعليم ولا تعتمد عليه فقط.

ومع ذلك، كما يرثي مجتمع الأنظمة الحرجة من حيث السلامة (على الأقل في المملكة المتحدة والولايات المتحدة الأمريكية: تختلف الثقافات هنا)، هناك القليل جداً من التدريب على الأساليب الرسمية لمعظم الطلاب الجامعيين.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** professional accreditation, security considerations, supply chain, CSRF (Cross-Site Request Forgery), OWASP top 10, Spring framework
- **Equations:** 0
- **Citations:** [7], [8], [12], [19], [20], [22], [32], [44], [47], [48], [53], [54], [57], [65]
- **Special handling:** Real-world breach examples (Forever 21, Macy's, Ticketmaster) preserved; Stack Overflow quotes kept verbatim; code snippet (csrf().disable()) preserved in English; CSRF kept as acronym with Arabic translation in parentheses

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
