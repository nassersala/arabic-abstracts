# Abstract: Generative Adversarial Networks
## الملخص: الشبكات التنافسية التوليدية

**Section:** Abstract
**Translation Quality:** 0.90
**Glossary Terms Used:** framework, training, model, probability distribution, generative, adversarial, discriminative, backpropagation

---

### English Abstract

We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

---

### الملخص العربي

تقدم هذه الورقة إطار عمل لتدريب النماذج التوليدية من خلال عملية تنافسية خصامية مع مكونين يتم تدريبهما في وقت واحد: "نموذج توليدي G يلتقط توزيع البيانات، ونموذج تمييزي D يقدر احتمال أن تكون العينة قادمة من بيانات التدريب بدلاً من G." يستخدم النهج صياغة لعبة minimax ويدعم التدريب عبر الانتشار العكسي دون الحاجة إلى سلاسل ماركوف.

---

### Back-Translation (Validation)

This paper introduces a framework for training generative models through an adversarial competitive process with two simultaneously trained components: "a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample comes from training data rather than G." The approach uses a minimax game formulation and supports training via backpropagation without requiring Markov chains.

---

### Translation Metrics

- Iterations: 1
- Final Score: 0.90
- Quality: High
- Source: Copied from /home/user/arabic-abstracts/translations/1406.2661.md

---

**Note:** This abstract was previously translated and is included here for completeness of the full paper translation.
