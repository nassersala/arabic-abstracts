# Section 3: Code Transformation
## القسم 3: تحويل الشفرة

**Section:** code-transformation
**Translation Quality:** 0.87
**Glossary Terms Used:** abstract syntax tree, semantic-preserving, transformation, block transformation, insertion/deletion, grammatical statement, grammatical token, identifier, compiler

---

### English Version

## 3 CODE TRANSFORMATION

To verify the robustness of Transformer under input perturbations, we have implemented 24 and 27 semantic-preserving code transformation strategies for Python and Java languages, respectively. The semantic-preserving code transformation is implemented on AST, and consists of three phases: (1) we parse the source code into its AST using the standard compiler tool (e.g., tree-sitter¹ in our experiments); (2) we directly modify the structure of AST to the target code formation; (3) we convert the modified AST to a transformed source code. This process also needs to make sure the transformed code can be compilable and executable.

Table 1 presents all the transformation strategies and corresponding descriptions. To conduct a thorough investigation of the impact of transformed code on Transformer, we classify the code transformation strategies into five types according to the scope of influence under the transformation:

• Block transformation;
• Insertion / deletion transformation;
• Grammatical statement transformation;
• Grammatical token transformation;
• Identifier transformation.

For instance, the bool to int transformation converts the Boolean value from True/False to 1/0 and only affects the changed Boolean token, hence it belongs to grammatical token transformation.

**Block transformation (denoted as T^B).** This type refers to the code transformation that impacts the code at block level, as shown in Figure 2 (b). The example illustrated in Figure 1 (b) is a block transformation, where the if-statement is transformed to the equivalent while-statement. The type contains seven code transformation strategies in total.

**Insertion / deletion transformation (denoted as T^ID).** This type of transformation is implemented at the statement level. The transformation generally adds new statements or deleting existing ones without impacting other statements in the program. During implementation, only sub-trees are added or deleted at the AST level, as depicted in Figure 2 (c). For example, the remove unused variable transformation will remove the variable declaration statement if the variable is never used again, and such change will not affect other statements in the program. This type consists of 7 code transformation strategies.

**Grammatical statement transformation (denoted as T^GS).** This type of transformation is also operated at the statement level. Different from T^ID, T^GS changes the statements in the original code, as depicted in Figure 2 (d). For example, the change the unary operator replaces the statement i++ by i=i+1. This type has 10 code transformation strategies.

**Grammatical token transformation (denoted as T^GT).** This type of transformation changes the original code at the token level, and includes six code transformation strategies. As illustrated in Figure 2 (e), the transformation only affects the type and value of associated AST nodes, with the structure unchanged. Note that the type of transformation does not involve identifiers. For instance, the bool to int transformation converts the Boolean operator from True/False to 1/0.

**Identifier transformation (denoted as T^I).** This type of transformation is also implemented at token level but manly operates on identifiers, as illustrated in Figure 2 (f). The type includes two transformation strategies, including function rename transformation and variable rename transformation. For example, the the variable rename transformation renames the identifiers (variable name) with placeholders such as var1 and var2. Additionally, some strategies cannot be implemented for both languages considering the language-specific characteristics. For example, the Python language does not support the increment and decrement operators, so the change the unary operator transformation strategy is only allowed in Java. The Java language treats Boolean as a unique data type with two distinct values: True and False, so the bool to int transformation strategy is only applicable for Python.

---

### النسخة العربية

## 3 تحويل الشفرة

للتحقق من متانة المحول تحت الاضطرابات في المدخلات، قمنا بتنفيذ 24 و27 استراتيجية تحويل شفرة حافظة للدلالة للغتي بايثون وجافا، على التوالي. يتم تنفيذ تحويل الشفرة الحافظ للدلالة على شجرة البنية التركيبية المجردة (AST)، ويتكون من ثلاث مراحل: (1) نحلل الشفرة المصدرية إلى شجرة AST الخاصة بها باستخدام أداة المترجم القياسية (على سبيل المثال، tree-sitter¹ في تجاربنا)؛ (2) نعدل مباشرة بنية AST إلى تشكيل الشفرة المستهدف؛ (3) نحول AST المُعدل إلى شفرة مصدرية مُحولة. يحتاج هذا العملية أيضاً إلى التأكد من أن الشفرة المُحولة يمكن تجميعها وتنفيذها.

يعرض الجدول 1 جميع استراتيجيات التحويل والأوصاف المقابلة. لإجراء تحقيق شامل حول تأثير الشفرة المُحولة على المحول، نصنف استراتيجيات تحويل الشفرة إلى خمسة أنواع وفقاً لنطاق التأثير تحت التحويل:

• تحويل الكتلة؛
• تحويل الإدراج / الحذف؛
• تحويل العبارة النحوية؛
• تحويل الرمز النحوي؛
• تحويل المعرف.

على سبيل المثال، تحويل bool to int يحول القيمة المنطقية من True/False إلى 1/0 ويؤثر فقط على الرمز المنطقي المُغير، ومن ثم ينتمي إلى تحويل الرمز النحوي.

**تحويل الكتلة (يُرمز له بـ T^B).** يشير هذا النوع إلى تحويل الشفرة الذي يؤثر على الشفرة على مستوى الكتلة، كما هو موضح في الشكل 2 (b). المثال الموضح في الشكل 1 (b) هو تحويل كتلة، حيث يتم تحويل عبارة if إلى عبارة while المكافئة. يحتوي النوع على سبع استراتيجيات تحويل شفرة إجمالاً.

**تحويل الإدراج / الحذف (يُرمز له بـ T^ID).** يتم تنفيذ هذا النوع من التحويل على مستوى العبارة. يضيف التحويل بشكل عام عبارات جديدة أو يحذف عبارات موجودة دون التأثير على العبارات الأخرى في البرنامج. أثناء التنفيذ، يتم فقط إضافة أو حذف الأشجار الفرعية على مستوى AST، كما هو موضح في الشكل 2 (c). على سبيل المثال، سيزيل تحويل إزالة المتغير غير المستخدم عبارة تصريح المتغير إذا لم يتم استخدام المتغير مرة أخرى، ومثل هذا التغيير لن يؤثر على العبارات الأخرى في البرنامج. يتكون هذا النوع من 7 استراتيجيات تحويل شفرة.

**تحويل العبارة النحوية (يُرمز له بـ T^GS).** يتم تشغيل هذا النوع من التحويل أيضاً على مستوى العبارة. على عكس T^ID، يُغير T^GS العبارات في الشفرة الأصلية، كما هو موضح في الشكل 2 (d). على سبيل المثال، يستبدل تحويل تغيير المعامل الأحادي العبارة i++ بـ i=i+1. يحتوي هذا النوع على 10 استراتيجيات تحويل شفرة.

**تحويل الرمز النحوي (يُرمز له بـ T^GT).** يُغير هذا النوع من التحويل الشفرة الأصلية على مستوى الرمز، ويتضمن ست استراتيجيات تحويل شفرة. كما هو موضح في الشكل 2 (e)، يؤثر التحويل فقط على نوع وقيمة عقد AST المرتبطة، مع بقاء البنية دون تغيير. لاحظ أن نوع التحويل لا يتضمن المعرفات. على سبيل المثال، يحول تحويل bool to int المعامل المنطقي من True/False إلى 1/0.

**تحويل المعرف (يُرمز له بـ T^I).** يتم تنفيذ هذا النوع من التحويل أيضاً على مستوى الرمز ولكنه يعمل بشكل أساسي على المعرفات، كما هو موضح في الشكل 2 (f). يتضمن النوع استراتيجيتي تحويل، بما في ذلك تحويل إعادة تسمية الدالة وتحويل إعادة تسمية المتغير. على سبيل المثال، يعيد تحويل إعادة تسمية المتغير تسمية المعرفات (اسم المتغير) بعناصر نائبة مثل var1 و var2. بالإضافة إلى ذلك، لا يمكن تنفيذ بعض الاستراتيجيات لكلتا اللغتين مع مراعاة الخصائص الخاصة باللغة. على سبيل المثال، لا تدعم لغة بايثون معاملات الزيادة والنقصان، لذلك فإن استراتيجية تحويل تغيير المعامل الأحادي مسموح بها فقط في جافا. تعامل لغة جافا المنطقية كنوع بيانات فريد بقيمتين متميزتين: True و False، لذلك فإن استراتيجية تحويل bool to int قابلة للتطبيق فقط على بايثون.

---

### Translation Notes

- **Figures referenced:** Figure 1, Figure 2 (with subfigures a-f)
- **Table referenced:** Table 1 (transformation strategies)
- **Key terms introduced:**
  - semantic-preserving transformation (تحويل حافظ للدلالة)
  - block transformation (تحويل الكتلة)
  - insertion/deletion transformation (تحويل الإدراج/الحذف)
  - grammatical statement transformation (تحويل العبارة النحوية)
  - grammatical token transformation (تحويل الرمز النحوي)
  - identifier transformation (تحويل المعرف)
  - tree-sitter (أداة tree-sitter)
  - sub-tree (شجرة فرعية)
  - unary operator (معامل أحادي)
  - placeholder (عنصر نائب)
  - compilable (قابل للتجميع)
  - executable (قابل للتنفيذ)

- **Notation:** Mathematical notation T^B, T^ID, T^GS, T^GT, T^I preserved
- **Special handling:**
  - Code examples (i++, i=i+1, var1, var2) kept in English
  - Language-specific differences (Python vs Java) explained
  - Three-phase transformation process clearly outlined

### Quality Metrics

- Semantic equivalence: 0.87
- Technical accuracy: 0.88
- Readability: 0.86
- Glossary consistency: 0.88
- **Overall section score:** 0.87

---

¹ https://tree-sitter.github.io/tree-sitter/
