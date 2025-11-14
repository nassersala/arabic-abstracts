# Appendix A: Word Frequency
## الملحق أ: تكرار الكلمات

**Section:** appendix
**Translation Quality:** 0.86
**Glossary Terms Used:** Map, Reduce, mapper, reducer, combiner, input files, output files, network bandwidth

---

### English Version

This section contains a program that counts the number of occurrences of each unique word in a set of input files specified on the command line.

```cpp
#include "mapreduce/mapreduce.h"

// User's map function
class WordCounter : public Mapper {
public:
    virtual void Map(const MapInput& input) {
        const string& text = input.value();
        const int n = text.size();
        for (int i = 0; i < n; ) {
            // Skip past leading whitespace
            while ((i < n) && isspace(text[i]))
                i++;
            // Find word end
            int start = i;
            while ((i < n) && !isspace(text[i]))
                i++;
            if (start < i)
                Emit(text.substr(start,i-start),"1");
        }
    }
};
REGISTER_MAPPER(WordCounter);

// User's reduce function
class Adder : public Reducer {
    virtual void Reduce(ReduceInput* input) {
        // Iterate over all entries with the
        // same key and add the values
        int64 value = 0;
        while (!input->done()) {
            value += StringToInt(input->value());
            input->NextValue();
        }
        // Emit sum for input->key()
        Emit(IntToString(value));
    }
};
REGISTER_REDUCER(Adder);

int main(int argc, char** argv) {
    ParseCommandLineFlags(argc, argv);
    MapReduceSpecification spec;
    // Store list of input files into "spec"
    for (int i = 1; i < argc; i++) {
        MapReduceInput* input = spec.add_input();
        input->set_format("text");
        input->set_filepattern(argv[i]);
        input->set_mapper_class("WordCounter");
    }
    // Specify the output files:
    // /gfs/test/freq-00000-of-00100
    // /gfs/test/freq-00001-of-00100
    // ...
    MapReduceOutput* out = spec.output();
    out->set_filebase("/gfs/test/freq");
    out->set_num_tasks(100);
    out->set_format("text");
    out->set_reducer_class("Adder");
    // Optional: do partial sums within map
    // tasks to save network bandwidth
    out->set_combiner_class("Adder");
    // Tuning parameters: use at most 2000
    // machines and 100 MB of memory per task
    spec.set_machines(2000);
    spec.set_map_megabytes(100);
    spec.set_reduce_megabytes(100);
    // Now run it
    MapReduceResult result;
    if (!MapReduce(spec, &result)) abort();
    // Done: 'result' structure contains info
    // about counters, time taken, number of
    // machines used, etc.
    return 0;
}
```

---

### النسخة العربية

يحتوي هذا القسم على برنامج يحسب عدد مرات ظهور كل كلمة فريدة في مجموعة من ملفات الإدخال المحددة في سطر الأوامر.

```cpp
#include "mapreduce/mapreduce.h"

// دالة Map الخاصة بالمستخدم
// User's map function
class WordCounter : public Mapper {
public:
    virtual void Map(const MapInput& input) {
        const string& text = input.value();
        const int n = text.size();
        for (int i = 0; i < n; ) {
            // تخطي المسافات البيضاء في البداية
            // Skip past leading whitespace
            while ((i < n) && isspace(text[i]))
                i++;
            // إيجاد نهاية الكلمة
            // Find word end
            int start = i;
            while ((i < n) && !isspace(text[i]))
                i++;
            if (start < i)
                Emit(text.substr(start,i-start),"1");
        }
    }
};
REGISTER_MAPPER(WordCounter);

// دالة Reduce الخاصة بالمستخدم
// User's reduce function
class Adder : public Reducer {
    virtual void Reduce(ReduceInput* input) {
        // التكرار على جميع الإدخالات ذات المفتاح نفسه وجمع القيم
        // Iterate over all entries with the
        // same key and add the values
        int64 value = 0;
        while (!input->done()) {
            value += StringToInt(input->value());
            input->NextValue();
        }
        // إصدار المجموع للمفتاح input->key()
        // Emit sum for input->key()
        Emit(IntToString(value));
    }
};
REGISTER_REDUCER(Adder);

int main(int argc, char** argv) {
    ParseCommandLineFlags(argc, argv);
    MapReduceSpecification spec;
    // تخزين قائمة ملفات الإدخال في "spec"
    // Store list of input files into "spec"
    for (int i = 1; i < argc; i++) {
        MapReduceInput* input = spec.add_input();
        input->set_format("text");
        input->set_filepattern(argv[i]);
        input->set_mapper_class("WordCounter");
    }
    // تحديد ملفات الإخراج:
    // Specify the output files:
    // /gfs/test/freq-00000-of-00100
    // /gfs/test/freq-00001-of-00100
    // ...
    MapReduceOutput* out = spec.output();
    out->set_filebase("/gfs/test/freq");
    out->set_num_tasks(100);
    out->set_format("text");
    out->set_reducer_class("Adder");
    // اختياري: القيام بمجاميع جزئية ضمن مهام map
    // لتوفير النطاق الترددي للشبكة
    // Optional: do partial sums within map
    // tasks to save network bandwidth
    out->set_combiner_class("Adder");
    // معاملات الضبط: استخدام 2000 جهاز كحد أقصى
    // و 100 ميغابايت من الذاكرة لكل مهمة
    // Tuning parameters: use at most 2000
    // machines and 100 MB of memory per task
    spec.set_machines(2000);
    spec.set_map_megabytes(100);
    spec.set_reduce_megabytes(100);
    // الآن قم بتشغيله
    // Now run it
    MapReduceResult result;
    if (!MapReduce(spec, &result)) abort();
    // تم: بنية 'result' تحتوي على معلومات
    // حول العدادات، والوقت المستغرق، وعدد الأجهزة المستخدمة، إلخ.
    // Done: 'result' structure contains info
    // about counters, time taken, number of
    // machines used, etc.
    return 0;
}
```

---

### الوصف

يوضح هذا الملحق مثالاً عملياً كاملاً لبرنامج بلغة C++ يستخدم مكتبة MapReduce لحساب تكرار الكلمات. البرنامج يتكون من ثلاثة أجزاء رئيسية:

1. **صنف WordCounter (عداد الكلمات)**: يرث من Mapper ويقوم بتحليل النص إلى كلمات منفصلة. لكل كلمة يتم العثور عليها، يصدر زوجاً من (الكلمة، "1").

2. **صنف Adder (المُجمِّع)**: يرث من Reducer ويقوم بجمع جميع القيم "1" لكل كلمة فريدة، مُنتجاً العدد الإجمالي لظهور كل كلمة.

3. **الدالة main**: تقوم بإعداد مواصفات MapReduce، بما في ذلك:
   - ملفات الإدخال من سطر الأوامر
   - ملفات الإخراج في نظام GFS
   - استخدام Adder كدالة combiner لتقليل استخدام الشبكة
   - معاملات الضبط (2000 جهاز، 100 ميغابايت ذاكرة لكل مهمة)

هذا المثال يوضح بساطة واجهة برمجة MapReduce: يحتاج المبرمج فقط لتعريف دالتي Map وReduce، بينما يتعامل إطار العمل مع كل التعقيدات المتعلقة بالتوزيع، والتوازي، وتحمل الأخطاء، وموازنة الحمل.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** WordCounter, Adder, MapReduceSpecification, combiner function (practical usage)
- **Equations:** None
- **Citations:** None
- **Special handling:**
  - C++ code preserved in English with Arabic comments added alongside
  - Code comments translated and placed above original English comments
  - Additional Arabic description provided to explain the program structure

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.86
- Readability: 0.85
- Glossary consistency: 0.86
- **Overall section score:** 0.86
