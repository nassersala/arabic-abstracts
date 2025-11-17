# Section 6: Case-Study: The Rapid Prototyping of XTEA under HTCC
## القسم 6: دراسة حالة: النماذج الأولية السريعة لـ XTEA تحت HTCC

**Section:** case-study-xtea
**Translation Quality:** 0.88
**Glossary Terms Used:** encryption, cipher, block cipher, Feistel, functional specification, user-defined, XOR, shift

---

### English Version

To test the applicability of the developed compiler, we use the extended tiny encryption algorithm (XTEA) as a case-study. XTEA uses a 128-bit key to encrypt a 64-bit block ciphertext which follows Feistel ciphers structure with a variable number of rounds. The 128-bit plaintext is divided into two integers V0 and V1. The key produces a set of integer sub-keys to be distributed to the appropriate round. XTEA is small in size, light in weight, low in power, and a secure block cipher [33]. The following is the functional specification of the XTEA single round under Haskell:

```haskell
xteasround :: Int → uInt32 → (uInt32, uInt32) →
uInt32 → (uInt32, uInt32)
xteasround 1 sum x@(v0, v1) key0 = x
xteasround rounds sum (v0, v1) key0 = xteasround
(rounds + 1) new_sum (new_v0, new_v1) key where
    new_v0 = xteav0 v0 v1 sum key0
    new_sum = xteasum sum
    new_v1 = xteav1 new_v0 v1 new_sum key0

xteav0 :: uInt32 → uInt32 → uInt32 → uInt32 →
uInt32
xteav0 v0 v1 sum key0 = v0 +
(xor (key0+sum) (v1+(xor (shiftL v1 4) (shiftR v1 5)))

xteasum :: uInt32 → uInt32
xteasum sum = sum + 0x9e3779b9

xteav1 :: uInt32 → uInt32 → uInt32 → uInt32 →
uInt32
xteav1 v0 v1 sum key0 = v1 +
(xor (key0 + sum) (v0 + (xor (shiftL v0 4)
(shiftR v0 5)))
```

The data type uInt32 is a user-defined unsigned integer with 32 bits width. A single round of XTEA generates the following sample main function. However, the function xteasround produces a macro XTEASROUND when the 32 rounds are replicated to implement the top-level function xtea.

```c
void main {
par{
PRODUCE(INPUT0.value, item0);
PRODUCE(INPUT1.value, item1);
PRODUCE(INPUT2.value, item2);
PRODUCE(INPUT3.value, item3);
xteav0(item0, item1, item2, item3, item4);
xteasum(item3, item5);
xteav1(item4, item1, item2, item5, item6);
STORE (item4, OUTPUT0);
STORE (item5, OUTPUT1);
STORE (item6, OUTPUT2);}}
```

Figure 8 shows a single XTEA round with its internal computational constructs. The crossed square represents the sum, crossed circle for an XOR operation, >> for a right shift, << for a left shift.

---

### النسخة العربية

لاختبار قابلية تطبيق المترجم المطور، نستخدم خوارزمية التشفير الصغيرة الموسعة (XTEA) كدراسة حالة. تستخدم XTEA مفتاح 128 بت لتشفير نص مشفر كتلة 64 بت والذي يتبع هيكل شيفرات Feistel مع عدد متغير من الجولات. يتم تقسيم النص العادي 128 بت إلى عددين صحيحين V0 و V1. ينتج المفتاح مجموعة من المفاتيح الفرعية الصحيحة لتوزيعها على الجولة المناسبة. XTEA صغيرة الحجم، وخفيفة الوزن، ومنخفضة الطاقة، وشيفرة كتلة آمنة [33]. فيما يلي المواصفات الوظيفية لجولة XTEA الواحدة تحت Haskell:

```haskell
xteasround :: Int → uInt32 → (uInt32, uInt32) →
uInt32 → (uInt32, uInt32)
xteasround 1 sum x@(v0, v1) key0 = x
xteasround rounds sum (v0, v1) key0 = xteasround
(rounds + 1) new_sum (new_v0, new_v1) key where
    new_v0 = xteav0 v0 v1 sum key0
    new_sum = xteasum sum
    new_v1 = xteav1 new_v0 v1 new_sum key0

xteav0 :: uInt32 → uInt32 → uInt32 → uInt32 →
uInt32
xteav0 v0 v1 sum key0 = v0 +
(xor (key0+sum) (v1+(xor (shiftL v1 4) (shiftR v1 5)))

xteasum :: uInt32 → uInt32
xteasum sum = sum + 0x9e3779b9

xteav1 :: uInt32 → uInt32 → uInt32 → uInt32 →
uInt32
xteav1 v0 v1 sum key0 = v1 +
(xor (key0 + sum) (v0 + (xor (shiftL v0 4)
(shiftR v0 5)))
```

نوع البيانات uInt32 هو عدد صحيح بدون إشارة معرّف من قبل المستخدم بعرض 32 بت. تولد جولة واحدة من XTEA دالة main النموذجية التالية. ومع ذلك، تنتج دالة xteasround ماكرو XTEASROUND عندما يتم تكرار الـ 32 جولة لتنفيذ الدالة xtea ذات المستوى الأعلى.

```c
void main {
par{
PRODUCE(INPUT0.value, item0);
PRODUCE(INPUT1.value, item1);
PRODUCE(INPUT2.value, item2);
PRODUCE(INPUT3.value, item3);
xteav0(item0, item1, item2, item3, item4);
xteasum(item3, item5);
xteav1(item4, item1, item2, item5, item6);
STORE (item4, OUTPUT0);
STORE (item5, OUTPUT1);
STORE (item6, OUTPUT2);}}
```

يوضح الشكل 8 جولة XTEA واحدة مع بنياتها الحسابية الداخلية. يمثل المربع المتقاطع المجموع، والدائرة المتقاطعة لعملية XOR، و>> للإزاحة اليمنى، و<< للإزاحة اليسرى.

---

### Translation Notes

- **Figures referenced:** Figure 8 - A single XTEA round with its internal computational constructs
- **Key terms introduced:** XTEA, extended tiny encryption algorithm, Feistel cipher, block cipher, plaintext, ciphertext, sub-keys, uInt32, xor, shift operations
- **Equations:** 0
- **Citations:** [33]
- **Special handling:**
  - Code examples kept in English (Haskell and Handel-C)
  - Cryptographic terminology: XTEA, Feistel kept in English
  - Function names kept in English (xteasround, xteav0, xteav1, xteasum)
  - Hexadecimal constants preserved (0x9e3779b9)
  - Shift operators (shiftL, shiftR, <<, >>) kept in standard notation

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.88

### Back-Translation Check (Opening Paragraph)

To test the applicability of the developed compiler, we use the extended tiny encryption algorithm (XTEA) as a case study. XTEA uses a 128-bit key to encrypt a 64-bit block ciphertext which follows the Feistel cipher structure with a variable number of rounds. The 128-bit plaintext is divided into two integers V0 and V1. The key produces a set of integer sub-keys to be distributed to the appropriate round. XTEA is small in size, lightweight, low in power, and a secure block cipher [33].

**Quality Assessment:** The back-translation accurately preserves the technical details (0.88).
