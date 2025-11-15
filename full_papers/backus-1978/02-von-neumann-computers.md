# Section 2: Von Neumann Computers
## القسم 2: حواسيب فون نيومان

**Section:** von-neumann-computers
**Translation Quality:** 0.86
**Glossary Terms Used:** von Neumann computer, architecture, CPU, memory, bottleneck, data structure

---

### English Version

A von Neumann computer consists of three parts: a memory, a processing unit (CPU), and a connecting tube that can transmit a single word between the memory and the CPU. This tube is the von Neumann bottleneck. The task of a program is to change the contents of the memory in some desirable way.

The von Neumann computer has the following characteristics:

1. **Centralized sequential control**: Programs execute one instruction at a time in sequence
2. **Shared memory**: Both program and data reside in the same memory
3. **Word-at-a-time operation**: The CPU operates on individual words fetched from memory
4. **Von Neumann bottleneck**: The narrow channel between CPU and memory limits throughput

The von Neumann bottleneck is a fundamental limitation: no matter how fast we make the CPU, we are limited by the rate at which we can move data between the CPU and memory through the connecting tube. This architectural constraint has profound implications for programming language design.

In a von Neumann computer, a program consists of:
- A sequence of instructions stored in memory
- Each instruction operates on words in memory
- The program counter determines which instruction executes next
- Execution proceeds by repeatedly fetching, decoding, and executing instructions

This architecture leads to the word-at-a-time style of programming, where programs are expressed as sequences of operations on individual memory locations. The fundamental mode of operation is:

```
1. Fetch an instruction from memory
2. Fetch operands from memory
3. Perform operation in CPU
4. Store result back to memory
5. Increment program counter
6. Repeat
```

This cycle enforces a sequential, imperative programming style that is deeply embedded in the structure of conventional programming languages.

---

### النسخة العربية

يتكون حاسوب فون نيومان من ثلاثة أجزاء: ذاكرة، ووحدة معالجة (CPU)، وأنبوب اتصال يمكنه نقل كلمة واحدة بين الذاكرة ووحدة المعالجة المركزية. هذا الأنبوب هو عنق الزجاجة في نمط فون نيومان. مهمة البرنامج هي تغيير محتويات الذاكرة بطريقة مرغوبة.

يتميز حاسوب فون نيومان بالخصائص التالية:

1. **التحكم التسلسلي المركزي**: تُنفذ البرامج تعليمة واحدة في كل مرة بشكل تسلسلي
2. **ذاكرة مشتركة**: يقيم كل من البرنامج والبيانات في نفس الذاكرة
3. **عملية كلمة بكلمة**: تعمل وحدة المعالجة المركزية على كلمات فردية مُجلَبة من الذاكرة
4. **عنق زجاجة فون نيومان**: القناة الضيقة بين وحدة المعالجة المركزية والذاكرة تحد من الإنتاجية

عنق زجاجة فون نيومان هو قيد أساسي: بغض النظر عن مدى سرعة وحدة المعالجة المركزية، نحن محدودون بمعدل نقل البيانات بين وحدة المعالجة المركزية والذاكرة عبر أنبوب الاتصال. لهذا القيد المعماري آثار عميقة على تصميم لغات البرمجة.

في حاسوب فون نيومان، يتكون البرنامج من:
- سلسلة من التعليمات المخزنة في الذاكرة
- كل تعليمة تعمل على كلمات في الذاكرة
- عداد البرنامج يحدد التعليمة التي تُنفذ تالياً
- يستمر التنفيذ من خلال جلب وفك تشفير وتنفيذ التعليمات بشكل متكرر

تؤدي هذه المعمارية إلى أسلوب البرمجة كلمة بكلمة، حيث تُعبَّر البرامج كسلاسل من العمليات على مواقع ذاكرة فردية. نمط العملية الأساسي هو:

```
1. جلب تعليمة من الذاكرة
2. جلب المعاملات من الذاكرة
3. تنفيذ العملية في وحدة المعالجة المركزية
4. تخزين النتيجة مرة أخرى في الذاكرة
5. زيادة عداد البرنامج
6. التكرار
```

تفرض هذه الدورة أسلوب برمجة تسلسلي وأمري متجذر بعمق في بنية لغات البرمجة التقليدية.

---

### Translation Notes

- **Key terms introduced:**
  - von Neumann bottleneck (عنق زجاجة فون نيومان)
  - connecting tube (أنبوب اتصال)
  - program counter (عداد البرنامج)
  - word-at-a-time (كلمة بكلمة)
  - sequential control (التحكم التسلسلي)
  - shared memory (ذاكرة مشتركة)

- **Equations:** None
- **Citations:** None
- **Special handling:** Pseudo-code for fetch-execute cycle

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86
