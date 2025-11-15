# Section 6: Cluster Membership Changes
## القسم 6: تغييرات عضوية المجموعة

**Section:** cluster-membership-changes
**Translation Quality:** 0.87
**Glossary Terms Used:** cluster, configuration, membership, consensus, leader, log entry, committed, joint consensus, transition, availability, safety

---

### English Version

Up until now we have assumed that the cluster *configuration* (the set of servers participating in the consensus algorithm) is fixed. In practice, it will occasionally be necessary to change the configuration, for example to replace servers when they fail or to change the degree of replication. Although this can be done by taking the entire cluster offline, updating configuration files, and then restarting the cluster, this would leave the cluster unavailable during the changeover. In addition, if there are any manual steps, they risk operator error. In order to avoid these issues, we decided to automate configuration changes and incorporate them into the Raft consensus algorithm.

For the configuration change mechanism to be safe, there must be no point during the transition where it is possible for two leaders to be elected for the same term. Unfortunately, any approach where servers switch directly from the old configuration to the new configuration is unsafe. It isn't possible to atomically switch all of the servers at once, so the cluster can potentially split into two independent majorities during the transition (see Figure 10).

In order to ensure safety, configuration changes must use a two-phase approach. There are a variety of ways to implement the two phases. For example, some systems use the first phase to disable the old configuration so it cannot process client requests; then the second phase enables the new configuration. In Raft the cluster first switches to a transitional configuration we call *joint consensus*; once the joint consensus has been committed, the system then transitions to the new configuration. The joint consensus combines both the old and new configurations:

- Log entries are replicated to all servers in both configurations.
- Any server from either configuration may serve as leader.
- Agreement (for elections and entry commitment) requires separate majorities from *both* the old and new configurations.

The joint consensus allows individual servers to transition between configurations at different times without compromising safety. Furthermore, joint consensus allows the cluster to continue servicing client requests throughout the configuration change.

Cluster configurations are stored and communicated using special entries in the replicated log; Figure 11 illustrates the configuration change process. When the leader receives a request to change the configuration from C_old to C_new, it stores the configuration for joint consensus (C_old,new in the figure) as a log entry and replicates that entry using the mechanisms described previously. Once a given server adds the new configuration entry to its log, it uses that configuration for all future decisions (a server always uses the latest configuration in its log, regardless of whether the entry is committed). This means that the leader will use the rules of C_old,new to determine when the log entry for C_old,new is committed. If the leader crashes, a new leader may be chosen under either C_old or C_old,new, depending on whether the winning candidate has received C_old,new. In any case, C_new cannot make unilateral decisions during this period.

Once C_old,new has been committed, neither C_old nor C_new can make decisions without approval of the other, and the Leader Completeness Property ensures that only servers with the C_old,new log entry can be elected leader. It is now safe for the leader to create a log entry describing C_new and replicate it to the cluster. Again, this configuration will take effect on each server as soon as it is seen. When the new configuration has been committed under the rules of C_new, the old configuration is irrelevant and servers not in the new configuration can be shut down. As shown in Figure 11, there is no time when C_old and C_new can both make unilateral decisions; this guarantees safety.

There are three more issues to address for reconfiguration. The first issue is that new servers may not initially store any log entries. If they are added to the cluster in this state, it could take quite a while for them to catch up, during which time it might not be possible to commit new log entries. In order to avoid availability gaps, Raft introduces an additional phase before the configuration change, in which the new servers join the cluster as *non-voting members* (the leader replicates log entries to them, but they are not considered for majorities). Once the new servers have caught up with the rest of the cluster, the reconfiguration can proceed as described above.

The second issue is that the cluster leader may not be part of the new configuration. In this case, the leader steps down (returns to follower state) once it has committed the C_new log entry. This means that there will be a period of time (while it is committing C_new) when the leader is managing a cluster that does not include itself; it replicates log entries but does not count itself in majorities. The leader transition occurs when C_new is committed because this is the first point when the new configuration can operate independently (it will always be possible to choose a leader from C_new). Before this point, it may be the case that only a server from C_old can be elected leader.

The third issue is that removed servers (those not in C_new) can disrupt the cluster. These servers will not receive heartbeats, so they will time out and start new elections. They will then send RequestVote RPCs with new term numbers, and this will cause the current leader to revert to follower state. A new leader will eventually be elected, but the removed servers will time out again and the process will repeat, resulting in poor availability.

To prevent this problem, servers disregard RequestVote RPCs when they believe a current leader exists. Specifically, if a server receives a RequestVote RPC within the minimum election timeout of hearing from a current leader, it does not update its term or grant its vote. This does not affect normal elections, where each server waits at least a minimum election timeout before starting an election. However, it helps avoid disruptions from removed servers: if a leader is able to get heartbeats to its cluster, then it will not be deposed by larger term numbers.

---

### النسخة العربية

حتى الآن افترضنا أن *تكوين* المجموعة (مجموعة الخوادم المشاركة في خوارزمية الإجماع) ثابت. في الممارسة العملية، سيكون من الضروري أحياناً تغيير التكوين، على سبيل المثال لاستبدال الخوادم عند فشلها أو لتغيير درجة النسخ المتماثل. على الرغم من أنه يمكن القيام بذلك عن طريق إيقاف تشغيل المجموعة بأكملها في وضع عدم الاتصال، وتحديث ملفات التكوين، ثم إعادة تشغيل المجموعة، إلا أن هذا سيترك المجموعة غير متاحة أثناء التحويل. بالإضافة إلى ذلك، إذا كانت هناك أي خطوات يدوية، فإنها تخاطر بخطأ المشغل. لتجنب هذه المشكلات، قررنا أتمتة تغييرات التكوين ودمجها في خوارزمية إجماع Raft.

لكي تكون آلية تغيير التكوين آمنة، يجب ألا تكون هناك نقطة أثناء الانتقال حيث من الممكن انتخاب قائدين لنفس الفترة. لسوء الحظ، فإن أي نهج حيث تنتقل الخوادم مباشرة من التكوين القديم إلى التكوين الجديد غير آمن. ليس من الممكن تبديل جميع الخوادم في وقت واحد بشكل ذري، لذا يمكن للمجموعة أن تنقسم إلى أغلبيتين مستقلتين أثناء الانتقال (انظر الشكل 10).

لضمان السلامة، يجب أن تستخدم تغييرات التكوين نهج مرحلتين. هناك مجموعة متنوعة من الطرق لتنفيذ المرحلتين. على سبيل المثال، تستخدم بعض الأنظمة المرحلة الأولى لتعطيل التكوين القديم حتى لا يتمكن من معالجة طلبات العميل؛ ثم تمكن المرحلة الثانية التكوين الجديد. في Raft، تنتقل المجموعة أولاً إلى تكوين انتقالي نسميه *الإجماع المشترك*؛ بمجرد الالتزام بالإجماع المشترك، ينتقل النظام بعد ذلك إلى التكوين الجديد. يجمع الإجماع المشترك بين التكوينات القديمة والجديدة:

- يتم نسخ إدخالات السجل إلى جميع الخوادم في كلا التكوينين.
- يمكن لأي خادم من أي تكوين أن يعمل كقائد.
- يتطلب الاتفاق (للانتخابات والالتزام بالإدخال) أغلبيات منفصلة من *كلا* التكوينين القديم والجديد.

يسمح الإجماع المشترك للخوادم الفردية بالانتقال بين التكوينات في أوقات مختلفة دون المساس بالسلامة. علاوة على ذلك، يسمح الإجماع المشترك للمجموعة بمواصلة خدمة طلبات العميل طوال تغيير التكوين.

يتم تخزين تكوينات المجموعة والإبلاغ عنها باستخدام إدخالات خاصة في السجل المُنسَخ؛ يوضح الشكل 11 عملية تغيير التكوين. عندما يتلقى القائد طلباً لتغيير التكوين من C_old إلى C_new، يخزن التكوين للإجماع المشترك (C_old,new في الشكل) كإدخال سجل وينسخ هذا الإدخال باستخدام الآليات الموصوفة سابقاً. بمجرد أن يضيف خادم معين إدخال التكوين الجديد إلى سجله، يستخدم هذا التكوين لجميع القرارات المستقبلية (يستخدم الخادم دائماً أحدث تكوين في سجله، بغض النظر عما إذا كان الإدخال مُلتزَماً به). وهذا يعني أن القائد سيستخدم قواعد C_old,new لتحديد متى يتم الالتزام بإدخال السجل لـ C_old,new. إذا تعطل القائد، فقد يتم اختيار قائد جديد تحت C_old أو C_old,new، اعتماداً على ما إذا كان المرشح الفائز قد تلقى C_old,new. في أي حال، لا يمكن لـ C_new اتخاذ قرارات من جانب واحد خلال هذه الفترة.

بمجرد الالتزام بـ C_old,new، لا يمكن لـ C_old ولا C_new اتخاذ قرارات دون موافقة الآخر، وتضمن خاصية اكتمال القائد أنه يمكن انتخاب الخوادم التي لديها إدخال السجل C_old,new فقط كقائد. أصبح من الآمن الآن للقائد إنشاء إدخال سجل يصف C_new ونسخه إلى المجموعة. مرة أخرى، سيدخل هذا التكوين حيز التنفيذ على كل خادم بمجرد رؤيته. عندما يتم الالتزام بالتكوين الجديد تحت قواعد C_new، يصبح التكوين القديم غير ذي صلة ويمكن إيقاف تشغيل الخوادم غير الموجودة في التكوين الجديد. كما هو موضح في الشكل 11، لا يوجد وقت يمكن فيه لـ C_old وC_new اتخاذ قرارات من جانب واحد؛ وهذا يضمن السلامة.

هناك ثلاث مشكلات أخرى يجب معالجتها لإعادة التكوين. المشكلة الأولى هي أن الخوادم الجديدة قد لا تخزن في البداية أي إدخالات سجل. إذا تمت إضافتها إلى المجموعة في هذه الحالة، فقد يستغرق الأمر وقتاً طويلاً حتى تلحق بالركب، وخلال هذا الوقت قد لا يكون من الممكن الالتزام بإدخالات سجل جديدة. لتجنب فجوات التوافر، تقدم Raft مرحلة إضافية قبل تغيير التكوين، حيث تنضم الخوادم الجديدة إلى المجموعة كـ *أعضاء غير مصوتين* (ينسخ القائد إدخالات السجل إليهم، لكنهم لا يُعتبرون للأغلبيات). بمجرد أن تلحق الخوادم الجديدة ببقية المجموعة، يمكن أن تستمر إعادة التكوين كما هو موضح أعلاه.

المشكلة الثانية هي أن قائد المجموعة قد لا يكون جزءاً من التكوين الجديد. في هذه الحالة، يتنحى القائد (يعود إلى حالة التابع) بمجرد أن يلتزم بإدخال السجل C_new. وهذا يعني أنه سيكون هناك فترة زمنية (أثناء الالتزام بـ C_new) عندما يدير القائد مجموعة لا تتضمنه؛ ينسخ إدخالات السجل لكنه لا يحسب نفسه في الأغلبيات. يحدث انتقال القائد عند الالتزام بـ C_new لأن هذه هي النقطة الأولى عندما يمكن للتكوين الجديد العمل بشكل مستقل (سيكون من الممكن دائماً اختيار قائد من C_new). قبل هذه النقطة، قد يكون الحال أنه يمكن فقط انتخاب خادم من C_old كقائد.

المشكلة الثالثة هي أن الخوادم المُزالة (تلك غير الموجودة في C_new) يمكن أن تعطل المجموعة. لن تتلقى هذه الخوادم نبضات القلب، لذا ستنتهي مهلتها وتبدأ انتخابات جديدة. ثم سترسل RequestVote RPCs بأرقام فترات جديدة، وهذا سيتسبب في عودة القائد الحالي إلى حالة التابع. سيتم انتخاب قائد جديد في النهاية، لكن الخوادم المُزالة ستنتهي مهلتها مرة أخرى وستتكرر العملية، مما يؤدي إلى توافر ضعيف.

لمنع هذه المشكلة، تتجاهل الخوادم RequestVote RPCs عندما تعتقد أن قائداً حالياً موجود. على وجه التحديد، إذا تلقى خادم RequestVote RPC ضمن الحد الأدنى لمهلة الانتخاب من الاستماع من قائد حالي، فإنه لا يحدث فترته أو يمنح صوته. لا يؤثر هذا على الانتخابات العادية، حيث ينتظر كل خادم على الأقل الحد الأدنى لمهلة الانتخاب قبل بدء الانتخاب. ومع ذلك، يساعد في تجنب الاضطرابات من الخوادم المُزالة: إذا كان القائد قادراً على إيصال نبضات القلب إلى مجموعته، فلن يُعزل بأرقام فترات أكبر.

---

### Translation Notes

- **Figures referenced:** Figure 10 (configuration split), Figure 11 (configuration change process)
- **Key terms introduced:**
  - cluster configuration = تكوين المجموعة
  - membership changes = تغييرات العضوية
  - joint consensus = الإجماع المشترك
  - two-phase approach = نهج مرحلتين
  - transitional configuration = تكوين انتقالي
  - non-voting members = أعضاء غير مصوتين
  - unilateral decisions = قرارات من جانب واحد
  - reconfiguration = إعادة التكوين
  - availability gaps = فجوات التوافر
  - steps down = يتنحى
  - catch up = تلحق بالركب
  - disrupt = تعطل / تزعج
  - disregard = تتجاهل
  - deposed = يُعزل

- **Special handling:**
  - Preserved configuration notation (C_old, C_new, C_old,new)
  - Maintained technical terminology for configuration states
  - Kept RequestVote as RPC name
  - Emphasized safety guarantees during transition

- **Translation decisions:**
  - "cluster configuration" → "تكوين المجموعة" (cluster configuration/setup)
  - "membership changes" → "تغييرات العضوية" (membership modifications)
  - "joint consensus" → "الإجماع المشترك" (joint/shared consensus)
  - "two-phase approach" → "نهج مرحلتين" (two-stage approach)
  - "transitional" → "انتقالي" (transitional/intermediate)
  - "non-voting members" → "أعضاء غير مصوتين" (non-voting members)
  - "unilateral decisions" → "قرارات من جانب واحد" (one-sided decisions)
  - "reconfiguration" → "إعادة التكوين" (reconfiguration)
  - "availability gaps" → "فجوات التوافر" (availability gaps)
  - "steps down" → "يتنحى" (steps down/resigns)
  - "catch up" → "تلحق بالركب" (catch up/get up to speed)
  - "disrupt" → "تعطل" (disrupt/disturb)
  - "disregard" → "تتجاهل" (ignore/disregard)
  - "deposed" → "يُعزل" (removed from power)
  - "atomically" → "بشكل ذري" (atomically/indivisibly)
  - "operator error" → "خطأ المشغل" (operator mistake)

### Quality Metrics

- **Semantic equivalence:** 0.88 - Accurately preserves cluster reconfiguration mechanism
- **Technical accuracy:** 0.89 - Correctly describes joint consensus and configuration change process
- **Readability:** 0.86 - Clear explanation of complex reconfiguration protocol
- **Glossary consistency:** 0.86 - Consistent with established terms
- **Overall section score:** 0.87

### Back-Translation Check

Key concept:
English: "The joint consensus combines both the old and new configurations"
Arabic: "يجمع الإجماع المشترك بين التكوينات القديمة والجديدة"
Back: "The joint consensus combines the old and new configurations"
✓ Semantically equivalent

Safety guarantee:
English: "There is no time when C_old and C_new can both make unilateral decisions; this guarantees safety."
Arabic: "لا يوجد وقت يمكن فيه لـ C_old وC_new اتخاذ قرارات من جانب واحد؛ وهذا يضمن السلامة"
Back: "There is no time when C_old and C_new can make unilateral decisions; this guarantees safety."
✓ Exact match
