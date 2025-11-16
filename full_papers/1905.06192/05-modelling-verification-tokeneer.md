# Section 5: Modelling and Verification of Tokeneer
## القسم 5: نمذجة والتحقق من Tokeneer

**Section:** modelling-verification
**Translation Quality:** 0.87
**Glossary Terms Used:** formal verification (التحقق الرسمي), state machine (آلة حالات), specification (مواصفات), invariant (ثابت), Hoare logic (منطق هور)

---

### English Version

In this section we formally model the TIS in Isabelle/UTP [14], in order to provide evidence for the assurance case. In [6], the six SFRs are argued semi-formally, but here we provide a formal proof. We focus on the formalisation and verification of the user entry part of SFR1, and describe the elements necessary for this.

The TIS behaviour, formalised by Praxis in the Z notation [5], uses an elaborate state space and a collection of relational operations. The state is bipartite, consisting of (1) the digital state of the TIS and (2) the variables shared with the real world, which are monitored or controlled, respectively. The TIS monitors the time, enclave door, fingerprint reader, token reader, and several peripherals. It controls the door latch, an alarm, a display, and a screen.

The specification describes a state transition system, illustrated in Figure 6 (cf. [5, page 43]), where each transition corresponds to an operation. Several operations are ommited due to space constraints. Following enrolment, the TIS becomes quiescent (awaiting interaction). ReadUserToken triggers if the token is presented, and reads its contents. Assuming a valid token, the TIS determines whether a fingerprint is necessary, and then triggers either BioCheckRequired or BioCheckNotRequired. If required, the TIS then reads a fingerprint (ReadFingerOK), validates it (ValidateFingerOK), and finally writes an authorisation certificate to the token (WriteUserTokenOK). If the access credentials are available (waitingEntry), then a final check is performed (EntryOK), and once the user removes their token (waitingRemoveTokenSuccess), the door is unlocked (UnlockDoor).

We mechanise the TIS model by first creating hierarchical state space types, with invariants adapted from the Z specification [5]. We define the operations using Dijkstra's guarded command language [10] (GCL) rather than the Z schemas directly, as GCL is easier to reason about and provides similar expressivity. Moreover, GCL is given a denotational semantics in UTP's alphabetised relational calculus [21], and so it is possible to prove equivalence with the corresponding Z operations. We use a variant of GCL that broadly follows the following syntax:

P ::= skip | abort | P ; P | E → P | P ⊓ P | V := E | V :[P]

Here, P is a program, E is an expression or predicate, and V is a variable. The language provides the usual syntax for sequential composition, guarded commands, non-deterministic choice, and assignment. We also adopt a framing operator a :[P] which states that P can refer only to variables in the namespace a, and all other variables remain unchanged [14, 15].

We now introduce the TIS state space, on which the state machine will act.

```
IDStation ≙ [currentUserToken : TOKENTRY, currentTime : TIME,
           userTokenPresence : PRESENCE, status : STATUS,
           issuerKey : USER ⇸ KEYPART, ⋯ ]
Controlled ≙ [latch : LATCH, alarm : ALARM, ⋯ ]
Monitored ≙ [now : TIME, finger : FINGERPRINTTRY,
            userToken : TOKENTRY, ⋯ ]
RealWorld ≙ [mon : Monitored, ctrl : Controlled]
SystemState ≙ [rw : RealWorld, tis : IDStation]
```

We define five state space types that describe the TIS state, the controlled variables, monitored variables, real-world, and the entire system, respectively. The controlled variables include the physical latch, the alarm, the display, and the screen. The monitored variables correspond to time (now), the door (door), the fingerprint reader (finger), the tokens, and the peripherals. RealWorld combines the physical variables, and SystemState composes the physical world and TIS.

Variable currentUserToken represents the last token presented to the TIS, and userTokenPresence indicates whether a token is currently presented. The variable status is used to record the state the TIS is in, and can take the values indicated in the state bubbles of Figure 6. Variable issuerKey is a partial function representing the public key chain, which is needed to authorise user entry.

We now specify a selection of the operations over this state space:

```
BioCheckRequired ≙ (status = gotUserToken ∧ userTokenPresence = present
                  ∧ UserTokenOK ∧ (¬UserTokenWithOKAuthCert))
                  → status := waitingFinger; currentDisplay := insertFinger

ReadFingerOK ≙ (status = waitingFinger ∧ fingerPresence = present
               ∧ userTokenPresence = present)
               → status := gotFinger; currentDisplay := wait

UnlockDoorOK ≙ (status = waitingRemoveTokenSuccess
               ∧ userTokenPresence = absent)
               → UnlockDoor; status := quiescent;
                 currentDisplay := doorUnlocked
```

Each operation is guarded by execution conditions and consists of several assignments. BioCheckRequired requires that the current state is gotUserToken, the user token is present, and sufficient for entry (UserTokenOK), but there is no authorisation certificate (¬UserTokenWithOKAuthCert). The latter two predicates essentially require that (1) the three certificates can be verified against the public key store, and (2) additionally there is a valid authorisation certificate present. Their definitions can be found elsewhere [5]. BioCheckRequired updates the state to waitingFinger and the display with an instruction to provide a fingerprint. UnlockDoorOK requires that the current state is waitingRemoveTokenSuccess, and the token has been removed. It unlocks the door, using the elided operation UnlockDoor, returns the status to quiescent, and updates the display.

These operations act only on the TIS state space. During their execution monitored variables can also change, to reflect real-world updates. Mostly these changes are arbitrary, with the exception that time must increase monotonically. We therefore promote the operations to SystemState with the following schema.

UEC(Op) ≙ tis :[Op]; rw :[mon:now ≤ mon:now' ∧ ctrl' = ctrl]

In Z, this functionality is provided by schema UserEntryContext [5], from which we derive the name UEC. It promotes Op to act on tis, and composes this with a relation that specifies changes to the real-world variables (rw). We specify this as a UTP relational predicate. The behaviour of all monitored variables other than now is arbitrary, and all controlled variables are unchanged. Then, we promote each operation, for example TISReadTokenOK ≙ UEC(ReadTokenOK). The overall behaviour of the entry operations is given below:

```
TISUserEntryOp ≙ (TISReadUserToken ⊓ TISValidateUserToken
                ⊓ TISReadFinger ⊓ TISValidateFinger
                ⊓ TISUnlockDoor ⊓ TISCompleteFailedAccess ⊓ ⋯ )
```

In each iteration of the state machine, we non-deterministically select an enabled operation and execute it. We also update the controlled variables, which is done by composition with the following update operation.

TISUpdate ≙ rw :[mon:now ≤ mon:now']; rw:ctrl:latch := tis:currentLatch;
            rw:ctrl:display := tis:currentDisplay

We also formalise the TIS state invariants necessary to prove SFR1:

```
Inv₁ ≙ status ∈ {gotFinger, waitingFinger, waitingUpdateToken,
                waitingEntry, waitingUpdateTokenSuccess}
      ⇒ (UserTokenWithOKAuthCert ∨ UserTokenOK)

Inv₂ ≙ status ∈ {waitingEntry, waitingUpdateTokenSuccess}
      ⇒ (UserTokenWithOKAuthCert ∨ FingerOK)

TIS-inv ≙ Inv₁ ∧ Inv₂ ∧ ⋯
```

Inv₁ states that whenever the TIS is in a state beyond gotUserToken, then either a valid authorisation certificate is present, or else the user token is valid. Inv₂ states that whenever in state waitingEntry or waitingUpdateTokenSuccess, then either an authorisation certificate or a valid finger print is present. We elide the additional invariants that deal with the alarm and audit data [5].

Next, we show that each operation preserves TIS-inv using Hoare logic.

**Theorem 5.1.** {TIS-inv} TISUserEntryOp {TIS-inv}

**Proof.** Automatic, by application of Isabelle/UTP proof tactic hoare-auto.

This theorem shows that the state machine never violates the invariants, and we can assume they hold to satisfy any requirements. We use this to formalise and prove SFR1, which requires that we determine all states under which the latch will be unlocked. We can determine these states by application of the weakest precondition calculus [10]. Specifically, we characterise the weakest precondition under which execution of TISUserEntryOp followed by TISUpdate leads to a state satisfying rw:ctrl:latch = unlocked. We formalise this in the theorem below.

**Theorem 5.2 (FSFR1 is satisfied).**

(TIS-inv ∧ tis:currentLatch = locked
∧ (TISEntryOp ; TISUpdate) wp (rw:ctrl:latch = unlocked))
⇒ ((UserTokenOK ∧ FingerOK) ∨ UserTokenWithOKAuthCert)

**Proof.** Automatic, by application of weakest precondition and relational calculi.

We calculate the weakest precondition, and conjoin this with TIS-Inv, which always holds, and the predicate tis:currentLatch = locked to capture behaviours when the latch was initially locked. We show that this composite precondition implies that either a valid user token and fingerprint were present, or else a valid authorisation certificate. We have therefore now verified a formalisation of SFR1. In the next section we place this in the context of an assurance argument.

---

### النسخة العربية

في هذا القسم نقوم بنمذجة TIS رسمياً في Isabelle/UTP [14]، من أجل تقديم أدلة لحالة الضمان. في [6]، يتم الجدال حول SFRs الستة بشكل شبه رسمي، لكننا هنا نقدم إثباتاً رسمياً. نركز على الإضفاء الرسمي والتحقق من جزء دخول المستخدم من SFR1، ونصف العناصر اللازمة لذلك.

سلوك TIS، المضفى عليه طابع رسمي بواسطة Praxis في تدوين Z [5]، يستخدم فضاء حالة متقن ومجموعة من العمليات العلائقية. الحالة ثنائية الأجزاء، وتتكون من (1) الحالة الرقمية لـ TIS و(2) المتغيرات المشتركة مع العالم الحقيقي، والتي يتم مراقبتها أو التحكم فيها، على التوالي. يراقب TIS الوقت، وباب الحاوية، وقارئ بصمات الأصابع، وقارئ الرموز المميزة، والعديد من الملحقات. يتحكم في مزلاج الباب، والإنذار، والشاشة، والشاشة.

تصف المواصفات نظام انتقال الحالة، الموضح في الشكل 6 (قارن [5، صفحة 43])، حيث يتوافق كل انتقال مع عملية. يتم حذف العديد من العمليات بسبب قيود المساحة. بعد التسجيل، يصبح TIS خاملاً (في انتظار التفاعل). يتم تشغيل ReadUserToken إذا تم تقديم الرمز المميز، ويقرأ محتوياته. بافتراض رمز مميز صالح، يحدد TIS ما إذا كانت بصمة الإصبع ضرورية، ثم يُشغل إما BioCheckRequired أو BioCheckNotRequired. إذا كان مطلوباً، فإن TIS يقرأ بصمة الإصبع (ReadFingerOK)، ويتحقق من صحتها (ValidateFingerOK)، وأخيراً يكتب شهادة ترخيص إلى الرمز المميز (WriteUserTokenOK). إذا كانت بيانات اعتماد الوصول متاحة (waitingEntry)، فيتم إجراء فحص نهائي (EntryOK)، وبمجرد أن يزيل المستخدم رمزه المميز (waitingRemoveTokenSuccess)، يتم فتح قفل الباب (UnlockDoor).

نقوم بأتمتة نموذج TIS من خلال إنشاء أنواع فضاء حالة هرمية أولاً، مع ثوابت مُكيفة من مواصفات Z [5]. نحدد العمليات باستخدام لغة الأوامر المحروسة لديكسترا [10] (GCL) بدلاً من مخططات Z مباشرة، حيث أن GCL أسهل في الاستدلال عليها وتوفر تعبيرية مماثلة. علاوة على ذلك، يتم إعطاء GCL دلالات تدليلية في حساب علائقي أبجدي لـ UTP [21]، وبالتالي من الممكن إثبات التكافؤ مع عمليات Z المقابلة. نستخدم متغيراً من GCL الذي يتبع على نطاق واسع البنية التركيبية التالية:

P ::= skip | abort | P ; P | E → P | P ⊓ P | V := E | V :[P]

هنا، P هو برنامج، و E هو تعبير أو محمول، و V هو متغير. توفر اللغة البنية التركيبية المعتادة للتركيب المتسلسل، والأوامر المحروسة، والاختيار غير الحتمي، والإسناد. نتبنى أيضاً مشغل تأطير a :[P] الذي ينص على أن P يمكن أن يشير فقط إلى متغيرات في مساحة الاسم a، وتظل جميع المتغيرات الأخرى دون تغيير [14، 15].

نقدم الآن فضاء حالة TIS، الذي ستعمل عليه آلة الحالات.

```
IDStation ≙ [currentUserToken : TOKENTRY, currentTime : TIME,
           userTokenPresence : PRESENCE, status : STATUS,
           issuerKey : USER ⇸ KEYPART, ⋯ ]
Controlled ≙ [latch : LATCH, alarm : ALARM, ⋯ ]
Monitored ≙ [now : TIME, finger : FINGERPRINTTRY,
            userToken : TOKENTRY, ⋯ ]
RealWorld ≙ [mon : Monitored, ctrl : Controlled]
SystemState ≙ [rw : RealWorld, tis : IDStation]
```

نحدد خمسة أنواع فضاء حالة تصف حالة TIS، والمتغيرات المتحكم فيها، والمتغيرات المراقبة، والعالم الحقيقي، والنظام بأكمله، على التوالي. تشمل المتغيرات المتحكم فيها المزلاج المادي، والإنذار، والشاشة، والشاشة. تتوافق المتغيرات المراقبة مع الوقت (now)، والباب (door)، وقارئ بصمات الأصابع (finger)، والرموز المميزة، والملحقات. يجمع RealWorld المتغيرات المادية، ويؤلف SystemState العالم المادي و TIS.

يمثل المتغير currentUserToken الرمز المميز الأخير المقدم إلى TIS، ويشير userTokenPresence إلى ما إذا كان الرمز المميز مقدماً حالياً. يُستخدم المتغير status لتسجيل الحالة التي يكون فيها TIS، ويمكن أن يأخذ القيم المشار إليها في فقاعات الحالة في الشكل 6. المتغير issuerKey هو دالة جزئية تمثل سلسلة المفاتيح العامة، المطلوبة لتفويض دخول المستخدم.

نحدد الآن مجموعة مختارة من العمليات على فضاء الحالة هذا:

```
BioCheckRequired ≙ (status = gotUserToken ∧ userTokenPresence = present
                  ∧ UserTokenOK ∧ (¬UserTokenWithOKAuthCert))
                  → status := waitingFinger; currentDisplay := insertFinger

ReadFingerOK ≙ (status = waitingFinger ∧ fingerPresence = present
               ∧ userTokenPresence = present)
               → status := gotFinger; currentDisplay := wait

UnlockDoorOK ≙ (status = waitingRemoveTokenSuccess
               ∧ userTokenPresence = absent)
               → UnlockDoor; status := quiescent;
                 currentDisplay := doorUnlocked
```

كل عملية محروسة بشروط تنفيذ وتتكون من عدة إسنادات. تتطلب BioCheckRequired أن تكون الحالة الحالية gotUserToken، والرمز المميز للمستخدم موجوداً، وكافياً للدخول (UserTokenOK)، ولكن لا توجد شهادة ترخيص (¬UserTokenWithOKAuthCert). المحمولان الأخيران يتطلبان بشكل أساسي أن (1) يمكن التحقق من الشهادات الثلاث مقابل مخزن المفاتيح العامة، و(2) بالإضافة إلى ذلك توجد شهادة ترخيص صالحة. يمكن العثور على تعريفاتها في مكان آخر [5]. تحدّث BioCheckRequired الحالة إلى waitingFinger والشاشة بتعليمات لتقديم بصمة الإصبع. تتطلب UnlockDoorOK أن تكون الحالة الحالية waitingRemoveTokenSuccess، وأن يكون الرمز المميز قد تمت إزالته. يفتح قفل الباب، باستخدام العملية المحذوفة UnlockDoor، ويعيد الحالة إلى quiescent، ويحدّث الشاشة.

تعمل هذه العمليات فقط على فضاء حالة TIS. أثناء تنفيذها، يمكن أن تتغير المتغيرات المراقبة أيضاً، لتعكس تحديثات العالم الحقيقي. معظم هذه التغييرات تعسفية، باستثناء أن الوقت يجب أن يزداد بشكل رتيب. لذلك نروج للعمليات إلى SystemState بالمخطط التالي.

UEC(Op) ≙ tis :[Op]; rw :[mon:now ≤ mon:now' ∧ ctrl' = ctrl]

في Z، يتم توفير هذه الوظيفة بواسطة المخطط UserEntryContext [5]، الذي نشتق منه الاسم UEC. يروج Op للعمل على tis، ويؤلف هذا مع علاقة تحدد التغييرات على متغيرات العالم الحقيقي (rw). نحدد هذا كمحمول علائقي UTP. سلوك جميع المتغيرات المراقبة بخلاف now تعسفي، وجميع المتغيرات المتحكم فيها لا تتغير. ثم، نروج لكل عملية، على سبيل المثال TISReadTokenOK ≙ UEC(ReadTokenOK). يُعطى السلوك الكلي لعمليات الدخول أدناه:

```
TISUserEntryOp ≙ (TISReadUserToken ⊓ TISValidateUserToken
                ⊓ TISReadFinger ⊓ TISValidateFinger
                ⊓ TISUnlockDoor ⊓ TISCompleteFailedAccess ⊓ ⋯ )
```

في كل تكرار لآلة الحالات، نختار بشكل غير حتمي عملية ممكنة وننفذها. نحدّث أيضاً المتغيرات المتحكم فيها، والتي تتم من خلال التركيب مع عملية التحديث التالية.

TISUpdate ≙ rw :[mon:now ≤ mon:now']; rw:ctrl:latch := tis:currentLatch;
            rw:ctrl:display := tis:currentDisplay

نضفي أيضاً طابعاً رسمياً على ثوابت حالة TIS اللازمة لإثبات SFR1:

```
Inv₁ ≙ status ∈ {gotFinger, waitingFinger, waitingUpdateToken,
                waitingEntry, waitingUpdateTokenSuccess}
      ⇒ (UserTokenWithOKAuthCert ∨ UserTokenOK)

Inv₂ ≙ status ∈ {waitingEntry, waitingUpdateTokenSuccess}
      ⇒ (UserTokenWithOKAuthCert ∨ FingerOK)

TIS-inv ≙ Inv₁ ∧ Inv₂ ∧ ⋯
```

ينص Inv₁ على أنه كلما كان TIS في حالة بعد gotUserToken، فإما توجد شهادة ترخيص صالحة، أو أن الرمز المميز للمستخدم صالح. ينص Inv₂ على أنه كلما كان في حالة waitingEntry أو waitingUpdateTokenSuccess، فإما توجد شهادة ترخيص أو بصمة إصبع صالحة. نحذف الثوابت الإضافية التي تتعامل مع الإنذار وبيانات التدقيق [5].

بعد ذلك، نُظهر أن كل عملية تحافظ على TIS-inv باستخدام منطق هور.

**النظرية 5.1.** {TIS-inv} TISUserEntryOp {TIS-inv}

**الإثبات.** آلي، من خلال تطبيق تكتيك الإثبات Isabelle/UTP hoare-auto.

توضح هذه النظرية أن آلة الحالات لا تنتهك أبداً الثوابت، ويمكننا افتراض أنها تحمل لتلبية أي متطلبات. نستخدم هذا لإضفاء طابع رسمي وإثبات SFR1، الذي يتطلب منا تحديد جميع الحالات التي سيتم فيها فتح قفل المزلاج. يمكننا تحديد هذه الحالات من خلال تطبيق حساب أضعف شرط مسبق [10]. على وجه التحديد، نميز أضعف شرط مسبق يتم فيه تنفيذ TISUserEntryOp متبوعاً بـ TISUpdate يؤدي إلى حالة تلبي rw:ctrl:latch = unlocked. نضفي طابعاً رسمياً على هذا في النظرية أدناه.

**النظرية 5.2 (FSFR1 راضٍ).**

(TIS-inv ∧ tis:currentLatch = locked
∧ (TISEntryOp ; TISUpdate) wp (rw:ctrl:latch = unlocked))
⇒ ((UserTokenOK ∧ FingerOK) ∨ UserTokenWithOKAuthCert)

**الإثبات.** آلي، من خلال تطبيق حساب أضعف شرط مسبق وحسابات علائقية.

نحسب أضعف شرط مسبق، ونربط هذا مع TIS-Inv، الذي يحمل دائماً، والمحمول tis:currentLatch = locked لالتقاط السلوكيات عندما كان المزلاج مقفلاً في البداية. نُظهر أن هذا الشرط المسبق المركب يعني أن إما رمز مستخدم مميز صالح وبصمة إصبع كانا موجودين، أو شهادة ترخيص صالحة. لقد تحققنا الآن من إضفاء طابع رسمي على SFR1. في القسم التالي نضع هذا في سياق حجة ضمان.

---

### Translation Notes

- **Figures referenced:** Figure 6 (TIS Main States)
- **Key terms introduced:**
  - State transition system (نظام انتقال الحالة)
  - Guarded command language - GCL (لغة الأوامر المحروسة)
  - Denotational semantics (دلالات تدليلية)
  - Alphabetised relational calculus (حساب علائقي أبجدي)
  - Framing operator (مشغل تأطير)
  - Partial function (دالة جزئية)
  - Hoare logic (منطق هور)
  - Weakest precondition (أضعف شرط مسبق)
  - Non-deterministic choice (اختيار غير حتمي)
  - Invariant (ثابت)
- **Equations:** Multiple formal specifications in Z notation and GCL
- **Citations:** [5,6,10,14,15,21]
- **Special handling:**
  - Mathematical notation preserved in English
  - Z notation syntax preserved
  - GCL syntax preserved
  - State names (quiescent, gotUserToken, etc.) kept in English
  - Operation names (BioCheckRequired, ReadFingerOK, etc.) kept in English
  - Variable names kept in English
  - Subscripts and mathematical symbols preserved

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.87
- Readability: 0.86
- Glossary consistency: 0.87
- **Overall section score:** 0.87
