# Section 0: Abstract
## القسم 0: الملخص

**Section:** abstract
**Translation Quality:** 0.93
**Glossary Terms Used:** dynamic optimization, binary translation, just-in-time compilation, runtime optimization, hot path, trace, interpreter, native code, profiling, adaptive optimization, instruction cache, code cache, fragment, superblock

---

### English Version

We describe the design and implementation of Dynamo, a software dynamic optimization system that is capable of transparently improving the performance of a native instruction stream as it executes on the processor. The input native instruction stream to Dynamo can be dynamically generated (by a JIT for example), or it can come from the execution of a statically compiled native binary. This paper evaluates the Dynamo system in the latter, more challenging situation, in order to emphasize the limits, rather than the potential, of the system. Our experiments demonstrate that even statically optimized native binaries can be accelerated by Dynamo, and often by a significant degree. For example, the average performance of –O optimized SpecInt95 benchmark binaries created by the HP product C compiler is improved to a level comparable to their –O4 optimized version running without Dynamo. Dynamo achieves this by focusing its efforts on optimization opportunities that tend to manifest only at runtime, and hence opportunities that might be difficult for a static compiler to exploit. Dynamo's operation is transparent in the sense that it does not depend on any user annotations or binary instrumentation, and does not require multiple runs, or any special compiler, operating system or hardware support. The Dynamo prototype presented here is a realistic implementation running on an HP PA-8000 workstation under the HPUX 10.20 operating system.

---

### النسخة العربية

نصف تصميم وتطبيق دينامو، وهو نظام برمجي للتحسين الديناميكي قادر على تحسين أداء تسلسل التعليمات الأصلية بشكل شفاف أثناء تنفيذها على المعالج. يمكن أن يكون تسلسل التعليمات الأصلية المدخل إلى دينامو مُولَّداً ديناميكياً (بواسطة مترجم JIT على سبيل المثال)، أو يمكن أن يأتي من تنفيذ ملف ثنائي أصلي مُترجَم بشكل ساكن. تقيّم هذه الورقة نظام دينامو في الحالة الأخيرة الأكثر تحدياً، وذلك للتأكيد على حدود النظام بدلاً من إمكاناته. تُظهر تجاربنا أن الملفات الثنائية الأصلية المُحسَّنة بشكل ساكن يمكن تسريعها بواسطة دينامو، وغالباً بدرجة كبيرة. على سبيل المثال، يُحسَّن متوسط أداء ملفات SpecInt95 المعيارية المُحسَّنة بـ -O والمنشأة بواسطة مترجم HP C إلى مستوى مماثل لنسختها المُحسَّنة بـ -O4 التي تعمل بدون دينامو. يحقق دينامو ذلك من خلال تركيز جهوده على فرص التحسين التي تميل إلى الظهور فقط في وقت التشغيل، وبالتالي الفرص التي قد يصعب على المترجم الساكن استغلالها. يعمل دينامو بشكل شفاف بمعنى أنه لا يعتمد على أي تعليقات توضيحية من المستخدم أو أدوات قياس ثنائية، ولا يتطلب عمليات تشغيل متعددة، أو أي دعم خاص من المترجم أو نظام التشغيل أو العتاد. النموذج الأولي لدينامو المقدم هنا هو تطبيق واقعي يعمل على محطة عمل HP PA-8000 تحت نظام التشغيل HPUX 10.20.

---

### Translation Notes

- **Figures referenced:** Figure 1 (how Dynamo works)
- **Key terms introduced:** transparent dynamic optimization, native instruction stream, hot traces, fragment cache, JIT, runtime optimization
- **Technical terms:** PA-8000, HPUX, SpecInt95
- **Benchmarks:** -O vs -O4 optimization levels
- **Special handling:** Preserved technical terms like JIT, PA-8000, HPUX

### Quality Metrics

- Semantic equivalence: 0.94
- Technical accuracy: 0.93
- Readability: 0.92
- Glossary consistency: 0.93
- **Overall section score:** 0.93

(Copied from translations/dynamo-2000.md with quality score 0.93)
