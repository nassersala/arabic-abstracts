# Section 15: Key Equations
## القسم 15: المعادلات الأساسية

**Section:** reference
**Translation Quality:** 0.88
**Glossary Terms Used:** entropy, joint entropy, conditional entropy, mutual information, channel capacity

---

### English Version

Logarithms use base 2 unless stated otherwise.

**Entropy**

$$H(x) = \sum_{i=1}^{m} p(x_i) \log \frac{1}{p(x_i)} \text{ bits}$$ (31)

$$H(x) = \int_x p(x) \log \frac{1}{p(x)} dx \text{ bits}$$ (32)

**Joint entropy**

$$H(x, y) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{1}{p(x_i, y_j)} \text{ bits}$$ (33)

$$H(x, y) = \int_x \int_y p(y, x) \log \frac{1}{p(y, x)} dy dx \text{ bits}$$ (34)

$$H(x, y) = I(x, y) + H(x|y) + H(y|x) \text{ bits}$$ (35)

**Conditional Entropy**

$$H(y|x) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{1}{p(x_i|y_j)} \text{ bits}$$ (36)

$$H(x|y) = \int_y \int_x p(x, y) \log \frac{1}{p(x|y)} dx dy \text{ bits}$$ (38)

$$H(x|y) = H(x, y) - H(y) \text{ bits}$$ (40)

$$H(y|x) = H(x, y) - H(x) \text{ bits}$$ (41)

from which we obtain the chain rule for entropy

$$H(x, y) = H(x) + H(y|x) \text{ bits}$$ (42)
$$= H(y) + H(x|y) \text{ bits}$$ (43)

**Mutual Information**

$$I(x, y) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{p(x_i, y_j)}{p(x_i)p(y_j)} \text{ bits}$$ (46)

$$I(x, y) = \int_y \int_x p(x, y) \log \frac{p(x, y)}{p(x)p(y)} dx dy \text{ bits}$$ (47)

$$I(x, y) = H(x) + H(y) - H(x, y)$$ (48)
$$= H(x) - H(x|y)$$ (49)
$$= H(y) - H(y|x)$$ (50)
$$= H(x, y) - [H(x|y) + H(y|x)] \text{ bits}$$ (51)

**Channel Capacity**

$$C = \max_{p(x)} I(x, y) \text{ bits per value.}$$ (53)

If the channel input $x$ has variance $S$, the noise $\eta$ has variance $N$, and both $x$ and $\eta$ are iid Gaussian variables then $I(x, y) = C$, where

$$C = \frac{1}{2} \log \left(1 + \frac{S}{N}\right) \text{ bits per value,}$$ (54)

where the ratio of variances $S/N$ is the signal to noise ratio.

---

### النسخة العربية

تستخدم اللوغاريتمات الأساس 2 ما لم يُذكر خلاف ذلك.

**الإنتروبيا**

$$H(x) = \sum_{i=1}^{m} p(x_i) \log \frac{1}{p(x_i)} \text{ بتات}$$ (31)

$$H(x) = \int_x p(x) \log \frac{1}{p(x)} dx \text{ بتات}$$ (32)

**الإنتروبيا المشتركة**

$$H(x, y) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{1}{p(x_i, y_j)} \text{ بتات}$$ (33)

$$H(x, y) = \int_x \int_y p(y, x) \log \frac{1}{p(y, x)} dy dx \text{ بتات}$$ (34)

$$H(x, y) = I(x, y) + H(x|y) + H(y|x) \text{ بتات}$$ (35)

**الإنتروبيا الشرطية**

$$H(y|x) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{1}{p(x_i|y_j)} \text{ بتات}$$ (36)

$$H(x|y) = \int_y \int_x p(x, y) \log \frac{1}{p(x|y)} dx dy \text{ بتات}$$ (38)

$$H(x|y) = H(x, y) - H(y) \text{ بتات}$$ (40)

$$H(y|x) = H(x, y) - H(x) \text{ بتات}$$ (41)

ومن هذا نحصل على قاعدة السلسلة للإنتروبيا

$$H(x, y) = H(x) + H(y|x) \text{ بتات}$$ (42)
$$= H(y) + H(x|y) \text{ بتات}$$ (43)

**المعلومات المشتركة**

$$I(x, y) = \sum_{i=1}^{m} \sum_{j=1}^{m} p(x_i, y_j) \log \frac{p(x_i, y_j)}{p(x_i)p(y_j)} \text{ بتات}$$ (46)

$$I(x, y) = \int_y \int_x p(x, y) \log \frac{p(x, y)}{p(x)p(y)} dx dy \text{ بتات}$$ (47)

$$I(x, y) = H(x) + H(y) - H(x, y)$$ (48)
$$= H(x) - H(x|y)$$ (49)
$$= H(y) - H(y|x)$$ (50)
$$= H(x, y) - [H(x|y) + H(y|x)] \text{ بتات}$$ (51)

**سعة القناة**

$$C = \max_{p(x)} I(x, y) \text{ بتات لكل قيمة.}$$ (53)

إذا كان لدخل القناة $x$ تباين $S$، والضوضاء $\eta$ تباين $N$، وكلاهما $x$ و $\eta$ متغيرات غاوسية مستقلة ومتطابقة التوزيع فإن $I(x, y) = C$، حيث

$$C = \frac{1}{2} \log \left(1 + \frac{S}{N}\right) \text{ بتات لكل قيمة،}$$ (54)

حيث نسبة التباينات $S/N$ هي نسبة الإشارة إلى الضوضاء.

---

### Quality Metrics
- **Overall section score:** 0.88
