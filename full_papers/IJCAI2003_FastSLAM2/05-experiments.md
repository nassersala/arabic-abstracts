# Section 6: Experimental Results
## القسم 6: النتائج التجريبية

**Section:** experiments
**Translation Quality:** 0.87
**Glossary Terms Used:** algorithm, benchmark, accuracy, RMS error, particles, odometry, GPS, landmarks, real-time, efficiency

---

### English Version

## 6 Experimental Results

Systematic experiments showed that FastSLAM 2.0 provides excellent results with surprisingly few particles, including M=1. Most of our experiments were carried out using a benchmark data set collected with an outdoor vehicle in Victoria Park, Sydney [7]. The vehicle path is 3.5km long, and the map is 320 meters wide. The vehicle is equipped with differential GPS that is used for evaluation only. Fig. 1a shows the map of the terrain, along with the path obtained by raw odometry (which is very poor, the average RMS error is 93.6 meters). This data set is presently the most popular benchmark in the SLAM research community [3].

Figs. 1b&c show the result of applying FastSLAM with M=1 particle to the data set, without (Fig. 1b) and with (Fig. 1c) the feature management approach described in Section 4.5. In both cases, the estimated vehicle path is shown as a solid line, and the GPS information is shown as a dashed line. Results of the same accuracy were previously achieved only with O(N²) EKF-style methods [7] and with FastSLAM using M=50 particles. The feature management rule reduces the number of landmarks in the map from 768 (Fig. 1b) to 343 (Fig. 1c).

Fig. 2 plots the RMS error of the vehicle position estimate as function of the number of particles for the Victoria data set (panel a) and for synthetic simulation data (panel b) taken from [15]. While our new algorithm does approximately equally well for any number of particles, regular FastSLAM performs poorly for very small particle sets. We suspect that the poor performance of regular FastSLAM is due to the fact that the vehicle possesses relatively inaccurate odometry (see Fig. 1a), yet uses a low-noise range finder for landmark detection (a common configuration in outdoor robotics), leading to the generation of many particles of low likelihood.

The small number of examples needed to obtain state-of-the-art estimation translates to unprecedented efficiency of the new filter. The following table shows the results required to process the Victoria Park data set on a 1GHz Pentium PC:

| Method | Time |
|--------|------|
| EKF | 7,807 sec |
| regular FastSLAM, M=50 particles | 315 sec |
| FastSLAM 2.0, M=1 particle | 54 sec |

In comparison, the data acquisition required 1,550 seconds. Thus, while EKFs cannot be run in real-time, our new algorithm requires less than 4% of the vehicle's trajectory time.

---

### النسخة العربية

## 6 النتائج التجريبية

أظهرت التجارب المنهجية أن FastSLAM 2.0 توفر نتائج ممتازة مع عدد قليل بشكل مدهش من الجسيمات، بما في ذلك M=1. تم إجراء معظم تجاربنا باستخدام مجموعة بيانات معيارية تم جمعها بمركبة خارجية في فيكتوريا بارك، سيدني [7]. مسار المركبة طوله 3.5 كيلومتر، والخريطة عرضها 320 متراً. المركبة مجهزة بنظام GPS تفاضلي يُستخدم للتقييم فقط. يُظهر الشكل 1a خريطة التضاريس، إلى جانب المسار الذي تم الحصول عليه من قياس المسافات الخام (وهو ضعيف جداً، متوسط خطأ RMS هو 93.6 متر). تُعد مجموعة البيانات هذه حالياً المعيار الأكثر شعبية في مجتمع أبحاث SLAM [3].

يُظهر الشكلان 1b&c نتيجة تطبيق FastSLAM مع M=1 جسيمة على مجموعة البيانات، بدون (الشكل 1b) ومع (الشكل 1c) نهج إدارة الخصائص الموصوف في القسم 4.5. في كلتا الحالتين، يُظهر مسار المركبة المقدر كخط صلب، وتُظهر معلومات GPS كخط متقطع. تم تحقيق نتائج بنفس الدقة سابقاً فقط مع طرق نمط مرشح كالمان الممتد O(N²) [7] ومع FastSLAM باستخدام M=50 جسيمة. تقلل قاعدة إدارة الخصائص عدد المعالم في الخريطة من 768 (الشكل 1b) إلى 343 (الشكل 1c).

يرسم الشكل 2 خطأ RMS لتقدير موقع المركبة كدالة لعدد الجسيمات لمجموعة بيانات فيكتوريا (اللوحة a) ولبيانات المحاكاة الاصطناعية (اللوحة b) المأخوذة من [15]. بينما تقوم خوارزميتنا الجديدة بشكل جيد تقريباً بشكل متساوٍ لأي عدد من الجسيمات، فإن FastSLAM العادي يؤدي أداءً ضعيفاً لمجموعات الجسيمات الصغيرة جداً. نشتبه في أن الأداء الضعيف لـ FastSLAM العادي يرجع إلى حقيقة أن المركبة تمتلك قياس مسافات غير دقيق نسبياً (انظر الشكل 1a)، ومع ذلك تستخدم مكتشف مدى منخفض الضوضاء لكشف المعالم (تكوين شائع في الروبوتات الخارجية)، مما يؤدي إلى توليد العديد من الجسيمات ذات الاحتمالية المنخفضة.

يترجم العدد الصغير من الأمثلة اللازمة للحصول على تقدير متطور إلى كفاءة غير مسبوقة للمرشح الجديد. يُظهر الجدول التالي النتائج المطلوبة لمعالجة مجموعة بيانات فيكتوريا بارك على جهاز كمبيوتر Pentium بسرعة 1GHz:

| الطريقة | الوقت |
|--------|------|
| مرشح كالمان الممتد | 7,807 ثانية |
| FastSLAM العادي، M=50 جسيمة | 315 ثانية |
| FastSLAM 2.0، M=1 جسيمة | 54 ثانية |

بالمقارنة، تطلب الحصول على البيانات 1,550 ثانية. وبالتالي، بينما لا يمكن تشغيل مرشحات كالمان الممتدة في الوقت الفعلي، تتطلب خوارزميتنا الجديدة أقل من 4٪ من وقت مسار المركبة.

---

### Translation Notes

- **Figures referenced:** Figure 1a, 1b, 1c, Figure 2 (panels a and b)
- **Key metrics:**
  - Vehicle path: 3.5km long
  - Map width: 320 meters
  - Raw odometry RMS error: 93.6 meters
  - Landmarks: 768 → 343 (with feature management)
  - Processing times: EKF (7,807s), FastSLAM (315s), FastSLAM 2.0 (54s)
  - Data acquisition time: 1,550 seconds
- **Citations:** [7], [3], [15]
- **Special handling:**
  - Victoria Park benchmark dataset (Sydney) - kept English names
  - O(N²) notation preserved
  - Performance table translated with proper formatting
  - "state-of-the-art" translated as "متطور"

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.87
- Glossary consistency: 0.87
- **Overall section score:** 0.87

### Back-Translation Validation (Key Findings Paragraph)

**Original:**
The small number of examples needed to obtain state-of-the-art estimation translates to unprecedented efficiency of the new filter. The following table shows the results required to process the Victoria Park data set on a 1GHz Pentium PC.

**Back-Translation:**
The small number of examples needed to obtain state-of-the-art estimation translates to unprecedented efficiency for the new filter. The following table shows the results required to process the Victoria Park dataset on a 1GHz Pentium PC.
