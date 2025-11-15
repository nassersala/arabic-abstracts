# Section 9: Noise Reduces Channel Capacity
## القسم 9: الضوضاء تقلل من سعة القناة

**Section:** noise-effects
**Translation Quality:** 0.87
**Glossary Terms Used:** channel capacity, noise, entropy, conditional entropy, equiprobable

---

### English Version

Here, we examine how noise effectively reduces the maximum information that a channel can communicate. If the number of equiprobable (signal) input states is $m_x$ then the input entropy is

$$H(x) = \log m_x \text{ bits.}$$ (11)

For example, suppose there are $m_x = 3$ equiprobable input states, say, $x_1 = 100$ and $x_2 = 200$ and $x_3 = 300$, so the input entropy is $H(x) = \log 3 = 1.58$ bits. And if there are $m_\eta = 2$ equiprobable values for the channel noise, say, $\eta_1 = 10$ and $\eta_2 = 20$, then the noise entropy is $H(\eta) = \log 2 = 1.00$ bit.

Now, if the input is $x_1 = 100$ then the output can be one of two equiprobable states, $y_1 = 100 + 10 = 110$ or $y_2 = 100 + 20 = 120$. And if the input is $x_2 = 200$ then the output can be either $y_3 = 210$ or $y_4 = 220$. Finally, if the input is $x_3 = 300$ then the output can be either $y_5 = 310$ or $y_6 = 320$. Thus, given three equiprobable input states and two equiprobable noise values, there are $m_y = 6(= 3 \times 2)$ equiprobable output states. So the output entropy is $H(y) = \log 6 = 2.58$ bits. However, some of this entropy is due to noise, so not all of the output entropy comprises information about the input.

In general, the total number $m_y$ of equiprobable output states is $m_y = m_x \times m_\eta$, from which it follows that the output entropy is

$$H(y) = \log m_x + \log m_\eta$$ (12)
$$= H(x) + H(\eta) \text{ bits.}$$ (13)

Because we want to explore channel capacity in terms of channel noise, we will pretend to reverse the direction of data along the channel. Accordingly, before we 'receive' an input value, we know that the output can be one of 6 values, so our uncertainty about the input value is summarised by its entropy $H(y) = 2.58$ bits.

**Conditional Entropy.** Our average uncertainty about the output value given an input value is the conditional entropy $H(y|x)$. The vertical bar denotes 'given that', so $H(y|x)$ is, 'the residual uncertainty (entropy) of $y$ given that we know the value of $x$'.

After we have received an input value, our uncertainty about the output value is reduced from $H(y) = 2.58$ bits to

$$H(y|x) = H(\eta) = \log 2 = 1\text{bit.}$$ (14)

Because $H(y|x)$ is the entropy of the channel noise $\eta$, we can write it as $H(\eta)$. Equation 14 is true for every input, and it is therefore true for the average input. Thus, for each input, we gain an average of

$$H(y) - H(\eta) = 2.58 - 1 \text{ bits,}$$ (15)

about the output, which is the mutual information between $x$ and $y$.

---

### النسخة العربية

هنا، نفحص كيف تقلل الضوضاء فعلياً من الحد الأقصى للمعلومات التي يمكن للقناة نقلها. إذا كان عدد حالات الدخل (الإشارة) متساوية الاحتمال هو $m_x$ فإن إنتروبيا الدخل هي

$$H(x) = \log m_x \text{ بتات.}$$ (11)

على سبيل المثال، لنفترض أن هناك $m_x = 3$ حالات دخل متساوية الاحتمال، قل، $x_1 = 100$ و $x_2 = 200$ و $x_3 = 300$، لذلك إنتروبيا الدخل هي $H(x) = \log 3 = 1.58$ بتة. وإذا كان هناك $m_\eta = 2$ قيمتان متساويتا الاحتمال لضوضاء القناة، قل، $\eta_1 = 10$ و $\eta_2 = 20$، فإن إنتروبيا الضوضاء هي $H(\eta) = \log 2 = 1.00$ بتة.

الآن، إذا كان الدخل هو $x_1 = 100$ فيمكن أن يكون الخرج واحدة من حالتين متساويتي الاحتمال، $y_1 = 100 + 10 = 110$ أو $y_2 = 100 + 20 = 120$. وإذا كان الدخل هو $x_2 = 200$ فيمكن أن يكون الخرج إما $y_3 = 210$ أو $y_4 = 220$. أخيراً، إذا كان الدخل هو $x_3 = 300$ فيمكن أن يكون الخرج إما $y_5 = 310$ أو $y_6 = 320$. وبالتالي، نظراً لثلاث حالات دخل متساوية الاحتمال وقيمتي ضوضاء متساويتي الاحتمال، هناك $m_y = 6(= 3 \times 2)$ حالة خرج متساوية الاحتمال. لذلك إنتروبيا الخرج هي $H(y) = \log 6 = 2.58$ بتة. ومع ذلك، بعض هذه الإنتروبيا ناتج عن الضوضاء، لذلك ليست كل إنتروبيا الخرج تتألف من معلومات حول الدخل.

بشكل عام، العدد الإجمالي $m_y$ من حالات الخرج متساوية الاحتمال هو $m_y = m_x \times m_\eta$، ومن ذلك يتبع أن إنتروبيا الخرج هي

$$H(y) = \log m_x + \log m_\eta$$ (12)
$$= H(x) + H(\eta) \text{ بتات.}$$ (13)

نظراً لأننا نريد استكشاف سعة القناة من حيث ضوضاء القناة، سنتظاهر بعكس اتجاه البيانات على طول القناة. وفقاً لذلك، قبل أن "نتلقى" قيمة دخل، نعلم أن الخرج يمكن أن يكون واحدة من 6 قيم، لذلك يتم تلخيص عدم يقيننا حول قيمة الدخل بإنتروبيته $H(y) = 2.58$ بتة.

**الإنتروبيا الشرطية.** متوسط عدم يقيننا حول قيمة الخرج بالنظر إلى قيمة دخل هو الإنتروبيا الشرطية $H(y|x)$. يشير الشريط العمودي إلى "بالنظر إلى أن"، لذلك $H(y|x)$ هو، "عدم اليقين المتبقي (الإنتروبيا) لـ $y$ بالنظر إلى أننا نعرف قيمة $x$".

بعد أن تلقينا قيمة دخل، ينخفض عدم يقيننا حول قيمة الخرج من $H(y) = 2.58$ بتة إلى

$$H(y|x) = H(\eta) = \log 2 = 1\text{ بتة.}$$ (14)

نظراً لأن $H(y|x)$ هي إنتروبيا ضوضاء القناة $\eta$، يمكننا كتابتها كـ $H(\eta)$. المعادلة 14 صحيحة لكل دخل، وبالتالي فهي صحيحة لمتوسط الدخل. وبالتالي، لكل دخل، نكتسب متوسط

$$H(y) - H(\eta) = 2.58 - 1 \text{ بتات،}$$ (15)

حول الخرج، وهي المعلومات المشتركة بين $x$ و $y$.

---

### Quality Metrics
- **Overall section score:** 0.87
