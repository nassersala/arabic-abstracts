# Section 7: Loops or Functionals?
## القسم 7: حلقات أم وظائف عليا؟

**Section:** loops-vs-functionals
**Translation Quality:** 0.86
**Glossary Terms Used:** higher-order functional, loop, imperative programming, functional programming, map, fold

---

### English Version

With Mini Babel-17, you can freely choose between a programming style that uses loops and a programming style that puts its emphasis on the use of higher-order functionals. If you have an imperative background, you might start out with using loops everywhere, and then migrate slowly to the use of functionals like map or fold as your understanding of functional programming increases.

But even after your functional programming skills have matured, you might still choose to use loops in appropriate situations. Let us for example look at a function that takes a list of integers [a₀, ..., aₙ] and an integer x as arguments and returns the list

[q₀, ..., qₙ]  where  qₖ = Σᵢ₌₀ᵏ aᵢxⁱ

The implementation in Mini Babel-17 via a loop is straightforward, efficient and even elegant:

```
m => x => begin
            val y = 0
            val p = 1
            for a in m do
              y = y + a*p
              p = p * x
              yield y
            end
          end
```

---

### النسخة العربية

مع Mini Babel-17، يمكنك الاختيار بحرية بين أسلوب برمجة يستخدم الحلقات وأسلوب برمجة يركز على استخدام الوظائف العليا. إذا كانت لديك خلفية أمرية، فقد تبدأ باستخدام الحلقات في كل مكان، ثم تنتقل ببطء إلى استخدام وظائف مثل map أو fold مع زيادة فهمك للبرمجة الوظيفية.

لكن حتى بعد نضوج مهاراتك في البرمجة الوظيفية، قد لا تزال تختار استخدام الحلقات في المواقف المناسبة. دعونا على سبيل المثال ننظر إلى دالة تأخذ قائمة من الأعداد الصحيحة [a₀, ..., aₙ] وعدداً صحيحاً x كمعاملات وتُعيد القائمة

[q₀, ..., qₙ]  حيث  qₖ = Σᵢ₌₀ᵏ aᵢxⁱ

التنفيذ في Mini Babel-17 عبر حلقة هو مباشر وفعال وحتى أنيق:

```
m => x => begin
            val y = 0
            val p = 1
            for a in m do
              y = y + a*p
              p = p * x
              yield y
            end
          end
```

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Higher-order functionals (وظائف عليا)
  - Map (map - kept in English as standard term)
  - Fold (fold - kept in English as standard term)
  - Imperative background (خلفية أمرية)
- **Equations:** Mathematical summation qₖ = Σᵢ₌₀ᵏ aᵢxⁱ
- **Citations:** None
- **Special handling:**
  - Code block preserved with original syntax
  - Mathematical notation preserved
  - Function names (map, fold) kept in English as they are standard FP terminology

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
