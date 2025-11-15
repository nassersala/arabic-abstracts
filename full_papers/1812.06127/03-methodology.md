# Section 3: Federated Optimization: Methods
## القسم 3: التحسين الاتحادي: الطرق

**Section:** methodology
**Translation Quality:** 0.88
**Glossary Terms Used:** federated learning, optimization, SGD, algorithm, epoch, distributed system, aggregation, proximal term, heterogeneous, convergence

---

### English Version

## Overview

This section introduces federated learning optimization methods, beginning with the widely-used FedAvg algorithm before presenting the proposed FedProx framework.

## 3.1 Federated Averaging (FedAvg)

The foundational approach, FedAvg, operates as follows: at each round, a subset K≪N of the total devices are selected and run SGD locally for E number of epochs, and then the resulting model updates are averaged.

**Algorithm 1: FedAvg**

The procedure involves:
- Server selects K devices randomly (each device k chosen with probability $p_k$)
- Server transmits current model $w^t$ to selected devices
- Each device $k \in S_t$ performs E epochs of SGD on local objective $F_k$ with step-size $\eta$, producing $w_k^{t+1}$
- Devices return updated models to server
- Server aggregates: $w^{t+1} = \frac{1}{K}\sum_{k \in S_t} w_k^{t+1}$

**Key Challenges with FedAvg:**

McMahan et al. demonstrated that the number of local epochs in FedAvg plays an important role in convergence. Higher local epochs reduce communication but risk local drift from the global objective when data distributions differ across devices. Additionally, in heterogeneous networks, devices unable to complete E epochs within time constraints are simply dropped, potentially inducing bias.

## 3.2 Proposed Framework: FedProx

FedProx addresses heterogeneity through two critical modifications:

**1. Tolerating Partial Work**

Rather than mandating uniform local computation, FedProx allows devices to perform variable amounts of work locally based on their available systems resources, and then aggregate the partial solutions sent from the stragglers.

This flexibility is formalized through $\gamma_k^t$-inexactness for device k at iteration t, extending Definition 1 to account for device-specific and iteration-specific accuracy levels.

**2. Proximal Term**

Instead of minimizing $F_k(\cdot)$ directly, each device approximately minimizes:

$$\min_w h_k(w; w^t) = F_k(w) + \frac{\mu}{2}\|w - w^t\|^2$$

This proximal term serves dual purposes: restricting local updates closer to the global model (addressing statistical heterogeneity) and safely incorporating variable work amounts (addressing systems heterogeneity).

**Algorithm 2: FedProx**

The procedure involves:
- Server selects K devices randomly
- Server sends current model $w^t$ to chosen devices
- Each device $k \in S_t$ computes a $\gamma_k^t$-inexact minimizer of $h_k(w; w^t)$
- Devices return updated models $w_k^{t+1}$
- Server aggregates: $w^{t+1} = \frac{1}{K}\sum_{k \in S_t} w_k^{t+1}$

**Relationship to FedAvg:**

FedAvg is a special case of FedProx with (1) $\mu=0$, (2) the local solver specifically chosen to be SGD, and (3) a constant $\gamma$ across devices and updating rounds. FedProx provides greater generality by permitting any local solver and accommodating heterogeneous work distributions.

---

### النسخة العربية

## نظرة عامة

يقدم هذا القسم طرق تحسين التعلم الاتحادي، بدءًا من خوارزمية FedAvg المستخدمة على نطاق واسع قبل تقديم إطار عمل FedProx المقترح.

## 3.1 المتوسط الاتحادي (FedAvg)

يعمل النهج الأساسي، FedAvg، على النحو التالي: في كل جولة، يتم اختيار مجموعة فرعية K≪N من إجمالي الأجهزة وتشغيل SGD محليًا لعدد E من الحقب، ثم يتم حساب متوسط تحديثات النموذج الناتجة.

**الخوارزمية 1: FedAvg**

تتضمن العملية:
- يختار الخادم K من الأجهزة عشوائيًا (يتم اختيار كل جهاز k باحتمال $p_k$)
- ينقل الخادم النموذج الحالي $w^t$ إلى الأجهزة المختارة
- كل جهاز $k \in S_t$ ينفذ E من حقب SGD على الهدف المحلي $F_k$ مع حجم خطوة $\eta$، منتجًا $w_k^{t+1}$
- تعيد الأجهزة النماذج المحدثة إلى الخادم
- يقوم الخادم بالتجميع: $w^{t+1} = \frac{1}{K}\sum_{k \in S_t} w_k^{t+1}$

**التحديات الرئيسية مع FedAvg:**

أظهر McMahan et al. أن عدد الحقب المحلية في FedAvg يلعب دورًا مهمًا في التقارب. تقلل الحقب المحلية الأعلى من الاتصال ولكنها تخاطر بالانجراف المحلي عن الهدف العام عندما تختلف توزيعات البيانات عبر الأجهزة. بالإضافة إلى ذلك، في الشبكات غير المتجانسة، يتم ببساطة إسقاط الأجهزة غير القادرة على إكمال E من الحقب ضمن قيود زمنية، مما قد يؤدي إلى تحيز.

## 3.2 إطار العمل المقترح: FedProx

يعالج FedProx عدم التجانس من خلال تعديلين حاسمين:

**1. تحمل العمل الجزئي**

بدلاً من فرض حساب محلي موحد، يسمح FedProx للأجهزة بأداء كميات متغيرة من العمل محليًا بناءً على موارد الأنظمة المتاحة لها، ثم تجميع الحلول الجزئية المرسلة من الأجهزة المتأخرة.

يتم إضفاء الطابع الرسمي على هذه المرونة من خلال $\gamma_k^t$-عدم الدقة للجهاز k في التكرار t، مما يوسع التعريف 1 لحساب مستويات الدقة الخاصة بالجهاز والخاصة بالتكرار.

**2. الحد القريبي**

بدلاً من تصغير $F_k(\cdot)$ مباشرة، يصغّر كل جهاز تقريبيًا:

$$\min_w h_k(w; w^t) = F_k(w) + \frac{\mu}{2}\|w - w^t\|^2$$

يخدم هذا الحد القريبي غرضين مزدوجين: تقييد التحديثات المحلية بالقرب من النموذج العام (معالجة عدم التجانس الإحصائي) ودمج كميات العمل المتغيرة بأمان (معالجة عدم التجانس في الأنظمة).

**الخوارزمية 2: FedProx**

تتضمن العملية:
- يختار الخادم K من الأجهزة عشوائيًا
- يرسل الخادم النموذج الحالي $w^t$ إلى الأجهزة المختارة
- كل جهاز $k \in S_t$ يحسب مُصغّر $\gamma_k^t$-غير دقيق لـ $h_k(w; w^t)$
- تعيد الأجهزة النماذج المحدثة $w_k^{t+1}$
- يقوم الخادم بالتجميع: $w^{t+1} = \frac{1}{K}\sum_{k \in S_t} w_k^{t+1}$

**العلاقة مع FedAvg:**

FedAvg هي حالة خاصة من FedProx مع (1) $\mu=0$، (2) الحلال المحلي المختار على وجه التحديد ليكون SGD، و(3) $\gamma$ ثابت عبر الأجهزة وجولات التحديث. يوفر FedProx عمومية أكبر من خلال السماح بأي حلال محلي واستيعاب توزيعات العمل غير المتجانسة.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - FedAvg (المتوسط الاتحادي)
  - FedProx (إطار عمل FedProx)
  - epoch (حقبة)
  - local drift (الانجراف المحلي)
  - stragglers (الأجهزة المتأخرة)
  - proximal term (حد قريبي)
  - inexactness (عدم الدقة)
  - minimizer (مُصغّر)
- **Equations:** 1 main equation for the proximal term
- **Citations:** McMahan et al.
- **Special handling:**
  - Mathematical notation preserved in LaTeX
  - Algorithm names FedAvg and FedProx kept in English
  - Greek letters (μ, γ, η) kept as-is in formulas
  - Subscripts and superscripts maintained

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
