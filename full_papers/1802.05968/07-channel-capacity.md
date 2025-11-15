# Section 7: Channel Capacity
## القسم 7: سعة القناة

**Section:** channel-capacity
**Translation Quality:** 0.88
**Glossary Terms Used:** channel capacity, additive channel, noise, entropy, mutual information

---

### English Version

A very important (and convenient) channel is the additive channel. As encoded values pass through an additive channel, noise $\eta$ (eta) is added, so that the channel output is a noisy version $y$ of the channel input $x$

$$y = x + \eta.$$ (9)

The channel capacity $C$ is the maximum amount of information that a channel can provide at its output about the input.

The rate at which information is transmitted through the channel depends on the entropies of three variables: 1) the entropy $H(x)$ of the input, 2) the entropy $H(y)$ of the output, 3) the entropy $H(\eta)$ of the noise in the channel. If the output entropy is high then this provides a large potential for information transmission, and the extent to which this potential is realised depends on the input entropy and the level of noise. If the noise is low then the output entropy can be close to the channel capacity. However, channel capacity gets progressively smaller as the noise increases. Capacity is usually expressed in bits per usage (i.e. bits per output), or bits per second (bits/s).

---

### النسخة العربية

قناة مهمة جداً (ومريحة) هي القناة الجمعية. عندما تمر القيم المشفرة عبر قناة جمعية، يُضاف ضوضاء $\eta$ (إيتا)، بحيث يكون خرج القناة نسخة مشوشة $y$ من دخل القناة $x$

$$y = x + \eta.$$ (9)

سعة القناة $C$ هي الحد الأقصى لكمية المعلومات التي يمكن للقناة توفيرها في خرجها حول الدخل.

يعتمد معدل نقل المعلومات عبر القناة على إنتروبيات ثلاثة متغيرات: 1) إنتروبيا $H(x)$ للدخل، 2) إنتروبيا $H(y)$ للخرج، 3) إنتروبيا $H(\eta)$ للضوضاء في القناة. إذا كانت إنتروبيا الخرج عالية فإن هذا يوفر إمكانية كبيرة لنقل المعلومات، ويعتمد مدى تحقق هذه الإمكانية على إنتروبيا الدخل ومستوى الضوضاء. إذا كانت الضوضاء منخفضة فيمكن أن تكون إنتروبيا الخرج قريبة من سعة القناة. ومع ذلك، تصبح سعة القناة أصغر تدريجياً مع زيادة الضوضاء. تُعبر السعة عادة بالبتات لكل استخدام (أي بتات لكل خرج)، أو بتات في الثانية (بتات/ث).

---

### Quality Metrics
- **Overall section score:** 0.88
