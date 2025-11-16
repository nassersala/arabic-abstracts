# Section 3: Security Properties
## القسم 3: خصائص الأمان

**Section:** security definitions
**Translation Quality:** 0.88
**Glossary Terms Used:** RFID (RFID), privacy (خصوصية), reader (قارئ), tag (وسم), protocol (بروتوكول), authentication (مصادقة), unlinkability (عدم الربط), adversary (خصم), session (جلسة)

---

### English Version (Summary)

**Section III: SECURITY PROPERTIES**

Radio Frequency IDentification (RFID) systems allow to wirelessly identify objects. These systems are composed of readers and tags. Readers are radio-transmitters connected through a secure channel to a single server hosting a database with all the tracked objects information. Tags are wireless transponders attached to physical objects that have a limited memory and computational capacity. For simplicity we assume there is only one reader, representing the database server and all physical radio-transmitters.

**Example 1 (KCL Protocol):** A simple version of the protocol KCL:
```
R : nR ←$
TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ nT, nT ⊕ H(nR, kA)⟩
```
The key kA is a shared secret between tag TA and reader R. The protocol ensures both authentication and unlinkability.

**A. Privacy of RFID protocols**

We use the notion of Privacy for RFID protocols defined in [18] (Juels and Weis). This is a game-based definition where the adversary is a probabilistic polynomial time Turing machine interacting with a reader R and a finite set of tags {T₁, ..., Tₙ} through fixed communication interfaces:

**Tag Ti interface:**
- SETKEY: Corrupts the tag by returning its old key ki and id Idi, allows adversary to send new key k'i and new id Id'i
- TAGINIT: Initialize a tag with session identifier sid'
- TAGMSG: Tag receives challenge ci and returns response ri

**Reader R interface:**
- READERINIT: Returns fresh session identifier sid with first challenge c₀
- READERMSG: Reader receives session identifier sid and response ri, updates session

**Privacy Game:**
1. First phase: Adversary interacts with R and {T₁, ..., Tₙ}, can corrupt up to n-2 tags
2. Adversary chooses two uncorrupted tags Ti₀ and Ti₁
3. One tag chosen uniformly at random (bit b sampled), made accessible as oracle
4. Second phase: Adversary interacts with R, tags {T₁, ..., Tₙ}\{Ti₀, Ti₁}, and Tib
5. Adversary outputs bit b'
6. Adversary wins if b = b'

A protocol satisfies m-Privacy if any adversary A using at most m calls to interfaces has winning probability bounded by 1/2 + fA(η), where fA is negligible in security parameter.

**B. Bounded Session Privacy**

We formalize the privacy game using terms and substitutions representing protocol state:
- Γn: set of possible actions {SETKEYi, TAGINITi, TAGMSGi, READERINIT, READERMSG | 1 ≤ i ≤ n}
- Substitution σ saves internal memory state of reader and tags
- For each action α, term t^σ_α(φ) represents answer and θ^σ_α(φ) represents memory update

**Folding technique:** Given subset of actions S, construct term t^σ_S(φ) gathering all possible interleavings using conditional expressions and attacker function symbol to ∈ G.

**Definition 3 (m-Bounded Session Privacy):** Protocol satisfies m-Bounded Session Privacy if for every p, q with p+q=m and for every computational model:
M_c ⊨ (t^σi(φi))i≤m, gguess(φm+1) ∼ (t^σ̃i(φ̃i))i≤m, gguess(φ̃m+1)

where sequences represent protocol execution with tag Tn-1 vs tag Tn.

**Theorem 1:** A protocol satisfies m-Bounded Session Privacy iff it satisfies m-Privacy.

**C. Fixed Trace Privacy**

**Definition 4 (m-Fixed Trace Privacy):** For fixed sequence of actions (αi)1≤i≤m:
M_c ⊨ (t^σi_αi(φi))i≤m, gguess(φm+1) ∼ (t^σ̃i_αi(φ̃i))i≤m, gguess(φ̃m+1)

**Proposition 4:** m-Fixed Trace Privacy is equivalent to m-Bounded Session Privacy.

This splits the big equivalence into exponentially many smaller formulas for specific action sequences.

---

### النسخة العربية (ملخص)

**القسم III: خصائص الأمان**

تسمح أنظمة التعريف بترددات الراديو (RFID) بتحديد الأجسام لاسلكياً. تتكون هذه الأنظمة من قارئات ووسوم. القارئات هي أجهزة إرسال راديو متصلة عبر قناة آمنة بخادم واحد يستضيف قاعدة بيانات بجميع معلومات الأجسام المتعقبة. الوسوم هي أجهزة استجابة لاسلكية ملحقة بأجسام مادية لها ذاكرة محدودة وقدرة حسابية محدودة. للبساطة نفترض وجود قارئ واحد فقط، يمثل خادم قاعدة البيانات وجميع أجهزة إرسال الراديو المادية.

**مثال 1 (بروتوكول KCL):** نسخة بسيطة من بروتوكول KCL:
```
R : nR ←$
TA : nT ←$
1 : R → TA : nR
2 : TA → R : ⟨A ⊕ nT, nT ⊕ H(nR, kA)⟩
```
المفتاح kA هو سر مشترك بين الوسم TA والقارئ R. يضمن البروتوكول كلاً من المصادقة وعدم الربط.

**أ. خصوصية بروتوكولات RFID**

نستخدم مفهوم الخصوصية لبروتوكولات RFID المُعرَّف في [18] (Juels و Weis). هذا تعريف قائم على اللعبة حيث الخصم هو آلة تورينج احتمالية متعددة الحدود في الزمن تتفاعل مع قارئ R ومجموعة منتهية من الوسوم {T₁, ..., Tₙ} من خلال واجهات اتصال ثابتة:

**واجهة الوسم Ti:**
- SETKEY: يفسد الوسم بإرجاع مفتاحه القديم ki ومعرفه Idi، يسمح للخصم بإرسال مفتاح جديد k'i ومعرف جديد Id'i
- TAGINIT: تهيئة وسم بمعرف جلسة sid'
- TAGMSG: يتلقى الوسم تحدياً ci ويرجع استجابة ri

**واجهة القارئ R:**
- READERINIT: يرجع معرف جلسة جديد sid مع التحدي الأول c₀
- READERMSG: يتلقى القارئ معرف جلسة sid واستجابة ri، يحدث الجلسة

**لعبة الخصوصية:**
1. المرحلة الأولى: يتفاعل الخصم مع R و {T₁, ..., Tₙ}، يمكنه إفساد ما يصل إلى n-2 وسم
2. يختار الخصم وسمين غير مُفسدين Ti₀ و Ti₁
3. يُختار وسم واحد عشوائياً بشكل موحد (يُسحب بت b)، يُجعل متاحاً كأوراكل
4. المرحلة الثانية: يتفاعل الخصم مع R، والوسوم {T₁, ..., Tₙ}\{Ti₀, Ti₁}، و Tib
5. يُخرج الخصم بتاً b'
6. يفوز الخصم إذا b = b'

يحقق البروتوكول m-Privacy إذا كان لأي خصم A يستخدم على الأكثر m استدعاء للواجهات احتمال فوز محدود بـ 1/2 + fA(η)، حيث fA ضئيلة في معامل الأمان.

**ب. خصوصية الجلسة المحدودة**

نصوغ رسمياً لعبة الخصوصية باستخدام حدود وتعويضات تمثل حالة البروتوكول:
- Γn: مجموعة الإجراءات الممكنة {SETKEYi, TAGINITi, TAGMSGi, READERINIT, READERMSG | 1 ≤ i ≤ n}
- التعويض σ يحفظ حالة الذاكرة الداخلية للقارئ والوسوم
- لكل إجراء α، الحد t^σ_α(φ) يمثل الإجابة و θ^σ_α(φ) يمثل تحديث الذاكرة

**تقنية الطي:** بالنظر إلى مجموعة فرعية من الإجراءات S، نبني حداً t^σ_S(φ) يجمع جميع التشابكات الممكنة باستخدام تعبيرات شرطية ورمز دالة المهاجم to ∈ G.

**التعريف 3 (خصوصية الجلسة المحدودة m):** يحقق البروتوكول خصوصية الجلسة المحدودة m إذا لكل p, q مع p+q=m ولكل نموذج حسابي:
M_c ⊨ (t^σi(φi))i≤m, gguess(φm+1) ∼ (t^σ̃i(φ̃i))i≤m, gguess(φ̃m+1)

حيث التسلسلات تمثل تنفيذ البروتوكول مع الوسم Tn-1 مقابل الوسم Tn.

**المبرهنة 1:** يحقق البروتوكول خصوصية الجلسة المحدودة m إذا وفقط إذا حقق m-Privacy.

**ج. خصوصية التتبع الثابت**

**التعريف 4 (خصوصية التتبع الثابت m):** لتسلسل ثابت من الإجراءات (αi)1≤i≤m:
M_c ⊨ (t^σi_αi(φi))i≤m, gguess(φm+1) ∼ (t^σ̃i_αi(φ̃i))i≤m, gguess(φ̃m+1)

**القضية 4:** خصوصية التتبع الثابت m مكافئة لخصوصية الجلسة المحدودة m.

هذا يقسم التكافؤ الكبير إلى عدد أسي من الصيغ الأصغر لتسلسلات إجراءات محددة.

---

### Translation Notes

- **Figures referenced:** Figure 3 (Privacy game diagram)
- **Key terms introduced:**
  - RFID system (نظام RFID)
  - Reader (قارئ)
  - Tag (وسم)
  - Transponder (جهاز استجابة)
  - Corruption (إفساد)
  - Session identifier (معرف جلسة)
  - Challenge-response (تحدي-استجابة)
  - Privacy game (لعبة الخصوصية)
  - Oracle (أوراكل)
  - Folding (طي)
  - Trace equivalence (تكافؤ التتبع)
- **Equations:** Multiple formal expressions
- **Citations:** [18], [13], [4]
- **Special handling:**
  - Protocol notation preserved
  - Game-based security definition
  - Formal definitions with quantifiers

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.88
- Readability: 0.87
- Glossary consistency: 0.88
- **Overall section score:** 0.88
