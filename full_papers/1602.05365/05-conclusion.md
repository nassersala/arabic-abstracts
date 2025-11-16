# Section 5: Conclusions
## القسم 5: الخلاصة

**Section:** conclusion
**Translation Quality:** 0.87
**Glossary Terms Used:** transactional memory, composable, atomicity, isolation, opacity, nesting, runtime

---

### English Version

In this paper we have presented OTM, a programming model supporting interactions between composable memory transactions. This model separates isolated transactions from non-isolated ones, still guaranteeing atomicity; the latter can interact by accessing to shared variables. Consistency is ensured by transparently merging interacting transactions at runtime. We have showed the versatility and simplicity of OTM by implementing some examples which are incompatible with isolation, and we have given a formal semantics for OTM, which allowed us to prove that this model satisfies the opacity criterion.

There are two main directions for future work each posing its own challenges. First, like STM, this model supports nesting (via `orElse`); however, this feature is currently limited to isolated (sub)transactions. Supporting nesting of open transaction requires additional care in the handling of side-effects: is merging transactions at different level of nesting feasible and meaningful or are we breaking the intuition behind the programming model? Secondly, an implementation is due in order to validate experimentally the model. A possible approach is to implement OTM completely in Haskell on top of STM. This solution does not need any specific support from the Haskell RunTime (HRT) but cannot benefit of the performance gains offered by a deeper integration, thus hindering any fair comparison with existing TM models, like STM. On the other hand, integrating OTM with the HRT and the Glasgow Haskell Compiler, akin STM, would be more efficient but also more complex and invasive.

We have presented OTM within Haskell (especially to leverage its type system), but this model is general and can be applied to other languages. A possible future work is to port this model to an imperative object oriented language, such as Java or C++; however, like other TM implementations, we expect that this extension will require some changes in the compiler and/or the runtime.

This work builds on the ideas in [mpt:coord15] where we described an abstract calculus with shared memory and open transactions. In loc. cit. we showed how this model is expressive enough to represent TCCS^m [ksh:fossacs2014], a variant of the Calculus of Communicating Systems with transactional synchronization. Being based on CCS, communication in TCCS^m is synchronous; however, nowadays asynchronous models play an important role (see e.g. actors, event-driven programming, etc.). It may be interesting to generalize the discussion so as to consider also this case, e.g. by defining an actor-based calculus with open transactions. Such a calculus can be quite useful also for modelling speculative reasoning for cooperating systems [ma2010:speculative, mmp:dais14, mmp:eceast2014, mpm:gcm14w, mp:memo14]. A local version of actor-based open transactions can be implemented in OTM using lock-free data structures (e.g., message queues) in shared transactional memory.

**Acknowledgements**

We thank Nicola Gigante and Valentino Picotti for their valuable feedback about the OTM programming model.

---

### النسخة العربية

في هذا البحث قدمنا ذاكرة المعاملات المفتوحة (OTM)، وهو نموذج برمجة يدعم التفاعلات بين معاملات الذاكرة القابلة للتركيب. يفصل هذا النموذج المعاملات المعزولة عن المعاملات غير المعزولة، مع الاستمرار في ضمان الذرية؛ يمكن للأخيرة التفاعل عن طريق الوصول إلى المتغيرات المشتركة. يتم ضمان الاتساق من خلال دمج المعاملات المتفاعلة بشفافية في وقت التشغيل. أظهرنا تنوع وبساطة OTM من خلال تنفيذ بعض الأمثلة غير المتوافقة مع العزل، وقدمنا دلالات رسمية لـ OTM، مما سمح لنا بإثبات أن هذا النموذج يحقق معيار العتامة.

هناك اتجاهان رئيسيان للعمل المستقبلي يطرح كل منهما تحدياته الخاصة. أولاً، مثل STM، يدعم هذا النموذج التداخل (عبر `orElse`)؛ ومع ذلك، هذه الميزة محدودة حالياً بالمعاملات (الفرعية) المعزولة. يتطلب دعم تداخل المعاملات المفتوحة عناية إضافية في التعامل مع التأثيرات الجانبية: هل دمج المعاملات على مستويات مختلفة من التداخل ممكن ومفيد أم أننا نكسر الحدس وراء نموذج البرمجة؟ ثانياً، يجب تنفيذ التطبيق من أجل التحقق تجريبياً من النموذج. نهج محتمل هو تنفيذ OTM بالكامل في Haskell فوق STM. لا يحتاج هذا الحل إلى أي دعم محدد من بيئة تشغيل Haskell (HRT) ولكنه لا يمكن أن يستفيد من مكاسب الأداء التي يوفرها التكامل الأعمق، وبالتالي يعيق أي مقارنة عادلة مع نماذج TM الموجودة، مثل STM. من ناحية أخرى، سيكون دمج OTM مع HRT ومترجم Glasgow Haskell، على غرار STM، أكثر كفاءة ولكنه أيضاً أكثر تعقيداً وتدخلاً.

قدمنا OTM ضمن Haskell (خاصة للاستفادة من نظام الأنواع الخاص بها)، ولكن هذا النموذج عام ويمكن تطبيقه على لغات أخرى. عمل مستقبلي محتمل هو نقل هذا النموذج إلى لغة موجهة للكائنات إلزامية، مثل Java أو C++؛ ومع ذلك، مثل تنفيذات TM الأخرى، نتوقع أن هذا التوسيع سيتطلب بعض التغييرات في المترجم و/أو بيئة التشغيل.

يبني هذا العمل على الأفكار في [mpt:coord15] حيث وصفنا حسابات مجردة مع الذاكرة المشتركة والمعاملات المفتوحة. في المرجع المذكور أظهرنا كيف أن هذا النموذج تعبيري بما يكفي لتمثيل TCCS^m [ksh:fossacs2014]، وهو متغير من حساب الأنظمة المتواصلة مع المزامنة المعاملاتية. كونها مبنية على CCS، فإن الاتصال في TCCS^m متزامن؛ ومع ذلك، تلعب النماذج غير المتزامنة في الوقت الحاضر دوراً مهماً (انظر على سبيل المثال الممثلين، والبرمجة المدفوعة بالأحداث، وما إلى ذلك). قد يكون من المثير للاهتمام تعميم المناقشة للنظر أيضاً في هذه الحالة، على سبيل المثال من خلال تعريف حسابات قائمة على الممثلين مع المعاملات المفتوحة. يمكن أن تكون مثل هذه الحسابات مفيدة جداً أيضاً لنمذجة الاستدلال التخميني للأنظمة المتعاونة [ma2010:speculative, mmp:dais14, mmp:eceast2014, mpm:gcm14w, mp:memo14]. يمكن تنفيذ نسخة محلية من المعاملات المفتوحة القائمة على الممثلين في OTM باستخدام هياكل البيانات الخالية من القفل (على سبيل المثال، طوابير الرسائل) في ذاكرة المعاملات المشتركة.

**الشكر والتقدير**

نشكر Nicola Gigante و Valentino Picotti على ملاحظاتهما القيمة حول نموذج البرمجة OTM.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - Nesting → التداخل
  - Haskell RunTime (HRT) → بيئة تشغيل Haskell
  - Glasgow Haskell Compiler → مترجم Glasgow Haskell
  - Imperative object oriented language → لغة موجهة للكائنات إلزامية
  - Calculus of Communicating Systems (CCS) → حساب الأنظمة المتواصلة
  - Transactional synchronization → المزامنة المعاملاتية
  - Actor-based calculus → حسابات قائمة على الممثلين
  - Event-driven programming → البرمجة المدفوعة بالأحداث
  - Speculative reasoning → الاستدلال التخميني
  - Lock-free data structures → هياكل البيانات الخالية من القفل

- **Equations:** None

- **Citations:**
  - [mpt:coord15]
  - [ksh:fossacs2014]
  - [ma2010:speculative, mmp:dais14, mmp:eceast2014, mpm:gcm14w, mp:memo14]

- **Special handling:**
  - Preserved mathematical notation (TCCS^m)
  - Acknowledgements section included
  - Future work directions clearly outlined

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
