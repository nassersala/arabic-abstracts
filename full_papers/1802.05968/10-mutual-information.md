# Section 10: Mutual Information
## القسم 10: المعلومات المشتركة

**Section:** mutual-information
**Translation Quality:** 0.88
**Glossary Terms Used:** mutual information, entropy, conditional entropy, channel capacity

---

### English Version

The mutual information $I(x, y)$ between two variables, such as a channel input $x$ and output $y$, is the average amount of information that each value of $x$ provides about $y$

$$I(x, y) = H(y) - H(\eta) \text{ bits.}$$ (16)

Somewhat counter-intuitively, the average amount of information gained about the output when an input value is received is the same as the average amount of information gained about the input when an output value is received, $I(x, y) = I(y, x)$. This is why it did not matter when we pretended to reverse the direction of data through the channel. These quantities are summarised in Figure 8.

---

### النسخة العربية

المعلومات المشتركة $I(x, y)$ بين متغيرين، مثل دخل القناة $x$ والخرج $y$، هي متوسط كمية المعلومات التي توفرها كل قيمة من $x$ حول $y$

$$I(x, y) = H(y) - H(\eta) \text{ بتات.}$$ (16)

بشكل مخالف للحدس إلى حد ما، فإن متوسط كمية المعلومات المكتسبة حول الخرج عند استقبال قيمة دخل هو نفس متوسط كمية المعلومات المكتسبة حول الدخل عند استقبال قيمة خرج، $I(x, y) = I(y, x)$. لهذا السبب لم يكن مهماً عندما تظاهرنا بعكس اتجاه البيانات عبر القناة. يتم تلخيص هذه الكميات في الشكل 8.

---

### Quality Metrics
- **Overall section score:** 0.88
