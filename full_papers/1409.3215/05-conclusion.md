# Section 5: Conclusion
## القسم 5: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** LSTM, sequence learning, SMT, short term dependencies, long sentences, RNN, optimization, sequence to sequence

---

### English Version

In this work, we showed that a large deep LSTM, that has a limited vocabulary and that makes almost no assumption about problem structure can outperform a standard SMT-based system whose vocabulary is unlimited on a large-scale MT task. The success of our simple LSTM-based approach on MT suggests that it should do well on many other sequence learning problems, provided they have enough training data.

We were surprised by the extent of the improvement obtained by reversing the words in the source sentences. We conclude that it is important to find a problem encoding that has the greatest number of short term dependencies, as they make the learning problem much simpler. In particular, while we were unable to train a standard RNN on the non-reversed translation problem (shown in fig. 1), we believe that a standard RNN should be easily trainable when the source sentences are reversed (although we did not verify it experimentally).

We were also surprised by the ability of the LSTM to correctly translate very long sentences. We were initially convinced that the LSTM would fail on long sentences due to its limited memory, and other researchers reported poor performance on long sentences with a model similar to ours [5, 2, 26]. And yet, LSTMs trained on the reversed dataset had little difficulty translating long sentences.

Most importantly, we demonstrated that a simple, straightforward and a relatively unoptimized approach can outperform an SMT system, so further work will likely lead to even greater translation accuracies. These results suggest that our approach will likely do well on other challenging sequence to sequence problems.

---

### النسخة العربية

في هذا العمل، أظهرنا أن LSTM عميقة كبيرة، لديها مفردات محدودة وتضع افتراضات قليلة جداً حول بنية المشكلة يمكن أن تتفوق على نظام قياسي قائم على SMT الذي مفرداته غير محدودة في مهمة ترجمة آلية واسعة النطاق. نجاح نهجنا البسيط القائم على LSTM في الترجمة الآلية يشير إلى أنه يجب أن يؤدي بشكل جيد في العديد من مشاكل تعلم التسلسل الأخرى، بشرط أن يكون لديهم بيانات تدريب كافية.

فوجئنا بمدى التحسين الذي تم الحصول عليه من خلال عكس الكلمات في الجمل المصدر. نستنتج أنه من المهم إيجاد ترميز للمشكلة يحتوي على أكبر عدد من التبعيات قصيرة المدى، حيث إنها تجعل مشكلة التعلم أبسط بكثير. على وجه الخصوص، بينما لم نتمكن من تدريب RNN قياسية على مشكلة الترجمة غير المعكوسة (الموضحة في الشكل 1)، نعتقد أن RNN قياسية يجب أن تكون قابلة للتدريب بسهولة عندما يتم عكس الجمل المصدر (على الرغم من أننا لم نتحقق من ذلك تجريبياً).

فوجئنا أيضاً بقدرة LSTM على ترجمة الجمل الطويلة جداً بشكل صحيح. كنا مقتنعين في البداية أن LSTM ستفشل في الجمل الطويلة بسبب ذاكرتها المحدودة، وأبلغ باحثون آخرون عن أداء ضعيف على الجمل الطويلة باستخدام نموذج مشابه لنموذجنا [5، 2، 26]. ومع ذلك، فإن شبكات LSTM المدربة على مجموعة البيانات المعكوسة واجهت صعوبة قليلة في ترجمة الجمل الطويلة.

الأهم من ذلك، أظهرنا أن نهجاً بسيطاً ومباشراً وغير محسّن نسبياً يمكن أن يتفوق على نظام SMT، لذلك من المحتمل أن يؤدي العمل الإضافي إلى دقة ترجمة أكبر. تشير هذه النتائج إلى أن نهجنا من المحتمل أن يؤدي بشكل جيد في مشاكل التسلسل إلى التسلسل الصعبة الأخرى.

---

### Translation Notes

- **Figures referenced:** Figure 1
- **Key terms introduced:** None (summary of contributions)
- **Equations:** 0
- **Citations:** [5, 2, 26]
- **Special handling:** Summary and future directions

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.89
- **Overall section score:** 0.88
