# Section 9: Performance
## القسم 9: الأداء

**Section:** Evaluation
**Translation Quality:** 0.84
**Glossary Terms Used:** benchmark, memoization, performance, optimization

---

### English Version (Summary)

This section provides empirical performance evaluation comparing different implementations.

**Test Examples (Figure 6):**
```haskell
a = single "a"
b = single "b"
atoz = sum [single [c] | c ← ['a'..'z']]
fishy = atoz∗ ∗ single "fish" ∗ atoz∗
anbn = 1 + a ∗ anbn ∗ b
dyck = (single "[" ∗ dyck ∗ single "]")∗
```

**Performance Results (Figure 7):**

Tests run on matching strings of length 100 with four interpretations:
- RegExp ((→) Char) ℕ
- RegExp (Map Char) ℕ
- Cofree ((→) Char) ℕ
- Cofree (Map Char) ℕ

**Key Findings:**

1. **Memoization Impact:**
   - For RegExp: Moderate benefit (sometimes harmful)
   - For Cofree: Dramatic benefit (2K-230K times faster)

2. **Cofree vs RegExp:**
   - Memoized Cofree: 8.5-485× faster than memoized RegExp
   - Memoized Cofree: 11.5-1075× faster than non-memoized RegExp

3. **Recursive Examples:**
   - `anbn` and `dyck` fail to terminate with RegExp Map
   - All examples work with Cofree Map

**Example Timings:**
- `a∗`: RegExp→ 30.56µs, CofreeMap 2.624µs
- `fishy`: RegExp→ 1.276ms, CofreeMap 4.233µs
- `anbn`: RegExp→ 1.293ms, CofreeMap 2.770µs

**Caveats:** Implementation has had no performance tuning and only rudimentary benchmarking. Further optimizations may narrow or widen the gaps.

---

### النسخة العربية (ملخص)

يوفر هذا القسم تقييم أداء تجريبي يقارن التطبيقات المختلفة.

**أمثلة الاختبار (الشكل 6):**
```haskell
a = single "a"
b = single "b"
atoz = sum [single [c] | c ← ['a'..'z']]
fishy = atoz∗ ∗ single "fish" ∗ atoz∗
anbn = 1 + a ∗ anbn ∗ b
dyck = (single "[" ∗ dyck ∗ single "]")∗
```

**نتائج الأداء (الشكل 7):**

اختبارات على سلاسل نصية بطول 100 مع أربع تفسيرات:
- RegExp ((→) Char) ℕ
- RegExp (Map Char) ℕ
- Cofree ((→) Char) ℕ
- Cofree (Map Char) ℕ

**النتائج الرئيسية:**

1. **تأثير التخزين المؤقت:**
   - لـ RegExp: فائدة معتدلة (أحياناً ضارة)
   - لـ Cofree: فائدة كبيرة (أسرع 2K-230K مرة)

2. **Cofree مقابل RegExp:**
   - Cofree المخزن مؤقتاً: أسرع 8.5-485× من RegExp المخزن مؤقتاً
   - Cofree المخزن مؤقتاً: أسرع 11.5-1075× من RegExp غير المخزن مؤقتاً

3. **الأمثلة العودية:**
   - `anbn` و `dyck` تفشل في الإنهاء مع RegExp Map
   - جميع الأمثلة تعمل مع Cofree Map

**أمثلة التوقيتات:**
- `a∗`: RegExp→ 30.56µs، CofreeMap 2.624µs
- `fishy`: RegExp→ 1.276ms، CofreeMap 4.233µs
- `anbn`: RegExp→ 1.293ms، CofreeMap 2.770µs

**التحذيرات:** لم يحصل التطبيق على ضبط أداء ولديه معايير قياس أولية فقط. قد تضيق أو توسع التحسينات الإضافية الفجوات.

---

### Translation Notes

- **Empirical Evaluation**: Real performance measurements
- **Key Finding**: Cofree with memoization dramatically faster
- **Quality Score:** 0.84
