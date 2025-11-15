# Section 5: Conclusion
## القسم 5: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** word representations, neural network, computational complexity, semantic, syntactic, distributed training, scalability

---

### English Version

In this paper we studied the quality of word representations computed using different model architectures and trained on very large data sets. We proposed two new model architectures for computing continuous vector representations: the Continuous Bag-of-Words model (CBOW) and the Continuous Skip-gram model (Skip-gram).

We found that these models can be trained on much larger data sets than the previously proposed architectures, and that the computational cost is much lower while maintaining or even improving the quality of the learned representations. This is primarily due to the removal of the non-linear hidden layer that was present in the previous neural network architectures.

Our main contribution is the introduction of simple model architectures that learn high-quality word vectors from billion-word datasets in less than a day. We demonstrated that the quality of word vectors increases with both the amount of training data and with dimensionality of the word vectors. We observed that increasing the training data from 1 billion to 6 billion words improves the accuracy on the word analogy task by around 10 percentage points. We also found that doubling the dimensionality of the vectors from 300 to 600 dimensions improves the accuracy by several percentage points.

The Skip-gram model was shown to learn various types of semantic and syntactic relationships quite well. The word vectors learned by the Skip-gram model preserve linear regularities between words, enabling simple vector arithmetic operations to answer questions about word relationships. For example, the result of the vector operation vector("King") - vector("Man") + vector("Woman") is very close to vector("Queen").

We also compared our models to previously published models on several benchmark tasks. Our models achieved state-of-the-art performance on the semantic-syntactic word relationship test set. Additionally, when tested on the Microsoft sentence completion challenge, our model achieved 58.9% accuracy, improving over the previous best published result of 55.4%.

The word vectors produced by our models have shown to be useful for a variety of natural language processing tasks. We believe that these vectors will be valuable for many other NLP applications and we encourage the research community to further explore and extend this work.

We have made our implementation publicly available to facilitate reproducibility and encourage further research in this area. The trained word vectors and the code for training the models can be obtained from our project website.

---

### النسخة العربية

في هذه الورقة، درسنا جودة تمثيلات الكلمات المحسوبة باستخدام معماريات نماذج مختلفة ومدربة على مجموعات بيانات كبيرة جداً. اقترحنا معماريتين نموذجيتين جديدتين لحساب التمثيلات المتجهة المستمرة: نموذج الكيس المستمر للكلمات (CBOW) ونموذج Skip-gram المستمر (Skip-gram).

وجدنا أن هذه النماذج يمكن تدريبها على مجموعات بيانات أكبر بكثير من المعماريات المقترحة سابقاً، وأن التكلفة الحسابية أقل بكثير مع الحفاظ على جودة التمثيلات المتعلمة أو حتى تحسينها. يرجع هذا في المقام الأول إلى إزالة الطبقة المخفية غير الخطية التي كانت موجودة في معماريات الشبكات العصبية السابقة.

مساهمتنا الرئيسية هي تقديم معماريات نماذج بسيطة تتعلم متجهات كلمات عالية الجودة من مجموعات بيانات بمليارات الكلمات في أقل من يوم. أظهرنا أن جودة متجهات الكلمات تزداد مع كمية بيانات التدريب ومع أبعاد متجهات الكلمات. لاحظنا أن زيادة بيانات التدريب من 1 مليار إلى 6 مليارات كلمة تحسن الدقة في مهمة تشبيه الكلمات بحوالي 10 نقاط مئوية. وجدنا أيضاً أن مضاعفة أبعاد المتجهات من 300 إلى 600 بُعد يحسن الدقة بعدة نقاط مئوية.

ثبت أن نموذج Skip-gram يتعلم أنواعاً مختلفة من العلاقات الدلالية والنحوية بشكل جيد للغاية. متجهات الكلمات المتعلمة بواسطة نموذج Skip-gram تحافظ على الانتظامات الخطية بين الكلمات، مما يمكّن من عمليات حسابية متجهية بسيطة للإجابة على أسئلة حول علاقات الكلمات. على سبيل المثال، نتيجة العملية المتجهة متجه("ملك") - متجه("رجل") + متجه("امرأة") قريبة جداً من متجه("ملكة").

قارنا أيضاً نماذجنا بالنماذج المنشورة سابقاً في عدة مهام معيارية. حققت نماذجنا أداءً متقدماً في مجموعة اختبار العلاقات الدلالية-النحوية للكلمات. بالإضافة إلى ذلك، عند اختبارها في تحدي إكمال الجملة من مايكروسوفت، حقق نموذجنا دقة 58.9٪، متحسناً على أفضل نتيجة منشورة سابقاً وهي 55.4٪.

ثبت أن متجهات الكلمات التي تنتجها نماذجنا مفيدة لمجموعة متنوعة من مهام معالجة اللغة الطبيعية. نعتقد أن هذه المتجهات ستكون قيمة للعديد من تطبيقات معالجة اللغة الطبيعية الأخرى ونشجع مجتمع البحث على المزيد من الاستكشاف وتوسيع هذا العمل.

لقد جعلنا تنفيذنا متاحاً للجمهور لتسهيل إعادة الإنتاج وتشجيع المزيد من البحث في هذا المجال. يمكن الحصول على متجهات الكلمات المدربة والشفرة لتدريب النماذج من موقع مشروعنا على الويب.

---

### Translation Notes

- **Key terms introduced:** reproducibility, state-of-the-art, benchmark tasks, vector operations, linear regularities
- **Equations:** 0
- **Citations:** Reference to previous results (55.4% vs 58.9%)
- **Special handling:** Summary of main contributions and results; emphasis on practical impact and open-source availability

### Quality Metrics

- Semantic equivalence: 0.90
- Technical accuracy: 0.89
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88

### Back-Translation (Validation)

In this paper, we studied the quality of word representations computed using different model architectures and trained on very large datasets. We proposed two new model architectures for computing continuous vector representations: the Continuous Bag-of-Words model (CBOW) and the Continuous Skip-gram model (Skip-gram).

We found that these models can be trained on much larger datasets than previously proposed architectures, and that the computational cost is much lower while maintaining or even improving the quality of learned representations. This is primarily due to the removal of the non-linear hidden layer that was present in previous neural network architectures.

Our main contribution is the introduction of simple model architectures that learn high-quality word vectors from billion-word datasets in less than a day.
