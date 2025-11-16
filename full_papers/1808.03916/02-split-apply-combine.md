# Section 2: A Simple Data Science Task - Split, Apply, Combine
## القسم 2: مهمة علم بيانات بسيطة - التقسيم، التطبيق، الدمج

**Section:** methodology/examples
**Translation Quality:** 0.86
**Glossary Terms Used:** علم البيانات, بنية البيانات, دالة, متوسط, مصفوفة بيانات

---

### English Version

## 2. A simple data science task: split, apply, combine

Here is a simple data analysis task that is perhaps emblematic of our house sharing, carpooling times. Suppose I am a data scientist working at a ride sharing company and here are the user ratings data for the last ten trips taken by a particular driver:

```
userid  381  1291  3992  193942  9493  381  3992  381  3992  193942
rating   5     4     4       4     5     5     5     3     5       4
```

Suppose also that I am interested in working out the average rating given by each unique user. A seasoned R user might immediately recognize this task as a "split-apply-combine" problem, which could be solved using the dplyr package as follows (Wickham, 2011):

```r
1  library(dplyr);
2  userid = c(381, 1291, 3992, 193942, 9493, 381,
3             3992, 381, 3992, 193942)
4  rating = c(5, 4, 4, 4, 5, 5, 5, 3, 5, 4)
5  mycar = data.frame(rating, userid)
6  summarize(group_by(mycar, userid), avgrating=mean(rating))
```

Output:
```
# A tibble: 5 x 2
  userid avgrating
   <dbl>     <dbl>
1    381  4.333333
2   1291  4.000000
3   3992  4.666667
4   9493  5.000000
5 193942  4.000000
```

The key computation is expressed by the `summarize` function, a higher-order function which combines the data in the `mycar` data frame after being split by (grouped by) `userid` and had the function `mean` applied to each group. This function is provided by dplyr and is perfectly well-suited to the split-apply-combine task. Now let's look at how the same idiom can be expressed in other programming languages.

---

### النسخة العربية

## 2. مهمة علم بيانات بسيطة: التقسيم، التطبيق، الدمج

إليك مهمة تحليل بيانات بسيطة ربما تكون رمزية لأوقات مشاركة المنزل ومشاركة السيارات. لنفترض أنني عالم بيانات أعمل في شركة مشاركة الرحلات وهنا بيانات تقييمات المستخدمين للرحلات العشر الأخيرة التي قام بها سائق معين:

```
userid  381  1291  3992  193942  9493  381  3992  381  3992  193942
rating   5     4     4       4     5     5     5     3     5       4
```

لنفترض أيضاً أنني مهتم بحساب متوسط التقييم الذي قدمه كل مستخدم فريد. قد يتعرف مستخدم R المتمرس على الفور على هذه المهمة كمشكلة "التقسيم-التطبيق-الدمج"، والتي يمكن حلها باستخدام حزمة dplyr على النحو التالي (Wickham, 2011):

```r
1  library(dplyr);
2  userid = c(381, 1291, 3992, 193942, 9493, 381,
3             3992, 381, 3992, 193942)
4  rating = c(5, 4, 4, 4, 5, 5, 5, 3, 5, 4)
5  mycar = data.frame(rating, userid)
6  summarize(group_by(mycar, userid), avgrating=mean(rating))
```

النتيجة:
```
# A tibble: 5 x 2
  userid avgrating
   <dbl>     <dbl>
1    381  4.333333
2   1291  4.000000
3   3992  4.666667
4   9493  5.000000
5 193942  4.000000
```

يتم التعبير عن الحساب الرئيسي بواسطة دالة `summarize`، وهي دالة من الرتبة الأعلى تدمج البيانات في إطار البيانات `mycar` بعد تقسيمها (تجميعها) بواسطة `userid` وتطبيق دالة `mean` على كل مجموعة. يتم توفير هذه الدالة بواسطة dplyr وهي مناسبة تماماً لمهمة التقسيم-التطبيق-الدمج. الآن دعونا ننظر إلى كيفية التعبير عن نفس التعبير الاصطلاحي في لغات برمجة أخرى.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - data science (علم البيانات)
  - split-apply-combine (التقسيم-التطبيق-الدمج)
  - data frame (إطار البيانات)
  - higher-order function (دالة من الرتبة الأعلى)
  - average/mean (متوسط)
- **Equations:** None
- **Citations:** Wickham, 2011
- **Special handling:**
  - R code kept in original English format (standard practice for code)
  - Function names (summarize, group_by, mean) kept in English
  - Package names (dplyr) kept in English
  - Variable names (userid, rating, mycar, avgrating) kept in English as they appear in code
  - Table/data output preserved exactly as shown

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.85
- Glossary consistency: 0.85
- **Overall section score:** 0.86

### Back-Translation Check (Key Paragraph)

Original: "The key computation is expressed by the summarize function, a higher-order function which combines the data in the mycar data frame after being split by (grouped by) userid and had the function mean applied to each group."

Back-translation: "The main computation is expressed by the summarize function, which is a higher-order function that combines the data in the mycar data frame after dividing it (grouping it) by userid and applying the mean function to each group."

✓ Semantically equivalent with minor acceptable variations
