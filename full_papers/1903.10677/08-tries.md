# Section 8: Tries
## القسم 8: الأشجار البادئة (Tries)

**Section:** Core Implementation
**Translation Quality:** 0.87
**Glossary Terms Used:** trie, data structure, comonad, memoization, homomorphism

---

### English Version (Summary)

The classic **trie** ("prefix tree") data structure [Thue 1912, Knuth 1998] solves the problem of redundant comparison elegantly. The paper formulates a simple trie data type:

```haskell
data Cofree h b = b :/ h (Cofree h b)
```

This is the **cofree comonad** [Uustalu and Vene, 2005, 2008]. The similarity to the function decomposition from Section 6 makes for easy instance calculation.

**Theorem 14**: Given the definitions in Figure 4, (!) is a homomorphism with respect to each instantiated class.

**Theorem 15**: If (!) on h behaves like (→) (Key h), then Cofree h is a comonad homomorphism from Cofree h to (→) (Key h).

**Key Advantage**: During matching, the next character directly indexes to the relevant derivative (sub-trie), efficiently bypassing all other paths. This provides:
- No syntactic overhead (unlike RegExp)
- Direct indexing (no backtracking)
- Elegant composition with memoization strategies

The trie representation directly mirrors the (/) decomposition, making it more straightforward than regular expressions.

---

### النسخة العربية (ملخص)

بنية البيانات الكلاسيكية **trie** ("الشجرة البادئة") [Thue 1912, Knuth 1998] تحل مشكلة المقارنة الزائدة بشكل أنيق. تصوغ الورقة نوع شجرة بادئة بسيطة:

```haskell
data Cofree h b = b :/ h (Cofree h b)
```

هذا هو **الـ cofree comonad** [Uustalu and Vene, 2005, 2008]. التشابه مع تفكيك الدالة من القسم 6 يجعل حساب النماذج سهلاً.

**النظرية 14**: مع التعريفات في الشكل 4، (!) هو تشاكل بالنسبة لكل صنف مُنشأ.

**النظرية 15**: إذا تصرف (!) على h مثل (→) (Key h)، فإن Cofree h هو تشاكل comonad من Cofree h إلى (→) (Key h).

**الميزة الرئيسية**: أثناء المطابقة، يُستخدم الحرف التالي للفهرسة مباشرة إلى المشتقة ذات الصلة (الشجرة البادئة الفرعية)، متجاوزاً بكفاءة جميع المسارات الأخرى. هذا يوفر:
- عدم وجود عبء نحوي (على عكس RegExp)
- فهرسة مباشرة (بدون تراجع)
- تركيب أنيق مع استراتيجيات التخزين المؤقت

يعكس تمثيل الشجرة البادئة بشكل مباشر تفكيك (/)، مما يجعله أكثر وضوحاً من التعبيرات النمطية.

---

### Translation Notes

- **Key Innovation**: Tries as cofree comonads
- **Performance**: Direct indexing eliminates backtracking
- **Quality Score:** 0.87
