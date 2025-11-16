# Section 4: Function Selection
## القسم 4: اختيار الدالة

**Section:** Function Selection
**Translation Quality:** 0.88
**Glossary Terms Used:** algorithm (خوارزمية), hardware (عتاد), specification (مواصفة), intellectual property (الملكية الفكرية)

---

### English Version

The examples in this study have been taken from the control software of a sensor that ESG has developed as a central component of a pilot assistance system for a military helicopter. The sensor control software has been developed in accordance with DO-178B, level D and was accepted by the German military certification authority WTD 61/ML in 2014.

Monitoring the environmental conditions, especially the temperature, is important to the correct operation of the sensor. Therefore, two temperature sensors (NTC1 and NTC2 in figure 1) are installed within the equipment for redundant temperature measurements.

The temperature monitoring function is part of the sensor's control program that is running on the processor shown in figure 1. It calculates the mean temperature of both readings, as long as they do not differ more than a certain amount (declared as positive integer TEMP_FAIL). It accepts MAX_TEMP_ERR_CNT consecutive differences larger than TEMP_FAIL before returning the error EC_TEMP.

Figure 2 shows the temperature monitoring call hierarchy: the function cbit_check_temperature is executed every 500ms. This function calls acq_measure_temp that returns the temperature readings of the two temperature sensors. To do so, the latter function calls adc_read to obtain the voltage levels from the Analog-Digital converters (ADCs, see Fig. 1) connected to the temperature sensors.

If the temperature reading is outside operational limits, this fact is reported as a working condition in a module state variable that is set by the function cbit_set_working_cond.

This set of functions has been selected for the following reasons:

• The functions are rather simple but already required some of the major concepts of ACSL for their formalization.

• The selected functions have been taken from a real project, it is real code and real specifications with all the flaws that typically occur in a time constrained industrial project.

• The functions cover a standard problem (monitoring a certain value obtained from an analogue-to-digital (AD) converter) so it does not reveal intellectual property. They are well suited for public discussion.

• The example could well be isolated: the source files contain only the selected C functions without failing compilation and analysis.

• The whole set of functions encompasses purely algorithmic as well as hardware related functions.

---

### النسخة العربية

تم أخذ الأمثلة في هذه الدراسة من برمجيات التحكم في مستشعر طورته ESG كمكون مركزي في نظام مساعدة الطيار لطائرة هليكوبتر عسكرية. تم تطوير برمجيات التحكم في المستشعر وفقاً لـ DO-178B، المستوى D وتم قبولها من قبل سلطة الاعتماد العسكرية الألمانية WTD 61/ML في عام 2014.

تُعد مراقبة الظروف البيئية، وخاصة درجة الحرارة، مهمة للتشغيل الصحيح للمستشعر. لذلك، يتم تثبيت مستشعرين لدرجة الحرارة (NTC1 و NTC2 في الشكل 1) داخل المعدات لقياسات درجة الحرارة الاحتياطية.

تُعد دالة مراقبة درجة الحرارة جزءاً من برنامج التحكم في المستشعر الذي يعمل على المعالج الموضح في الشكل 1. تحسب متوسط درجة الحرارة من كلتا القراءتين، طالما أنهما لا تختلفان بأكثر من مقدار معين (مُعرَّف كعدد صحيح موجب TEMP_FAIL). تقبل MAX_TEMP_ERR_CNT اختلافاً متتالياً أكبر من TEMP_FAIL قبل إرجاع الخطأ EC_TEMP.

يوضح الشكل 2 التسلسل الهرمي لاستدعاء مراقبة درجة الحرارة: يتم تنفيذ الدالة cbit_check_temperature كل 500 ميلي ثانية. تستدعي هذه الدالة acq_measure_temp التي تُرجع قراءات درجة الحرارة من مستشعري درجة الحرارة. للقيام بذلك، تستدعي الدالة الأخيرة adc_read للحصول على مستويات الجهد من محولات التناظري إلى الرقمي (ADCs، انظر الشكل 1) المتصلة بمستشعرات درجة الحرارة.

إذا كانت قراءة درجة الحرارة خارج الحدود التشغيلية، يتم الإبلاغ عن هذه الحقيقة كحالة تشغيل في متغير حالة الوحدة الذي يتم تعيينه بواسطة الدالة cbit_set_working_cond.

تم اختيار هذه المجموعة من الدوال للأسباب التالية:

• الدوال بسيطة نسبياً ولكنها تطلبت بالفعل بعض المفاهيم الرئيسية لـ ACSL لصياغتها رسمياً.

• تم أخذ الدوال المختارة من مشروع حقيقي، إنها شفرة حقيقية ومواصفات حقيقية مع جميع العيوب التي تحدث عادة في مشروع صناعي محدود الوقت.

• تغطي الدوال مشكلة قياسية (مراقبة قيمة معينة تم الحصول عليها من محول التناظري إلى الرقمي) لذا فهي لا تكشف عن الملكية الفكرية. إنها مناسبة تماماً للمناقشة العامة.

• يمكن عزل المثال بشكل جيد: تحتوي الملفات المصدرية على دوال C المختارة فقط دون فشل في الترجمة والتحليل.

• تشمل المجموعة الكاملة من الدوال دوالاً خوارزمية بحتة بالإضافة إلى دوال متعلقة بالعتاد.

---

### Translation Notes

- **Figures referenced:** Figure 1 (Temperature Monitoring Hardware), Figure 2 (Temperature Monitoring Call Hierarchy)
- **Key Terms:**
  - Control software: برمجيات التحكم
  - Sensor: مستشعر
  - Pilot assistance system: نظام مساعدة الطيار
  - Certification authority: سلطة الاعتماد
  - Environmental conditions: الظروف البيئية
  - Redundant: احتياطية
  - Mean temperature: متوسط درجة الحرارة
  - Consecutive differences: اختلاف متتالي
  - Call hierarchy: التسلسل الهرمي لاستدعاء
  - Voltage levels: مستويات الجهد
  - Analog-Digital converter (ADC): محول التناظري إلى الرقمي
  - Working condition: حالة تشغيل
  - Module state variable: متغير حالة الوحدة
  - Time constrained: محدود الوقت
  - Compilation: الترجمة

- **Code/Function names (kept in English):**
  - NTC1, NTC2
  - TEMP_FAIL
  - MAX_TEMP_ERR_CNT
  - EC_TEMP
  - cbit_check_temperature
  - acq_measure_temp
  - adc_read
  - cbit_set_working_cond

- **Citations:** None

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
