# Section 7: Conclusion and Future Work
## القسم 7: الخلاصة والعمل المستقبلي

**Section:** conclusion
**Translation Quality:** 0.88
**Glossary Terms Used:** reinforcement learning, off-policy, offline RL, demonstrations, suboptimal expert, waypoint tracking, exploration, reward function

---

### English Version

We have presented an approach for learning from suboptimal experts for complex dexterous robotic manipulation. We demonstrated that our algorithm, Relative Entropy Q-Learning (REQ), is effective in many different learning scenarios – including off-policy and offline RL as well as RL from demonstration (RLfD). In addition, our proposed approach for Reinforcement Learning from Suboptimal Experts (RLfSE), significantly outperforms competitive baselines. In particular, REQfSE leverages intertwining exploration to solve highly complex tasks that are otherwise intractable. To achieve this, we proposed using waypoint tracking controllers as the suboptimal experts. We argue that this approach can provide an intuitive and simple interface for humans to specify the desired behaviors for the task without requiring human demonstrations or engineering shaped reward functions.

**Acknowledgments**

We would like to thank Abbas Abdolmaleki, Akhil Raju, Antoine Laurens, Charles Game, Celine Smith, Christopher Schuster, Claudio Fantacci, Dave Barker, David Khosid, Emre Karagozler, Federico Casarini, Francesco Romano, Giulia Vezzani, Jon Scholz, Jose Enrique Chen, Michael Neunert, Murilo Martins, Nathan Batchelor, Nicole Hurley, Nimrod Gileadi, Nylda Adelise, Oleg Sushkov, Stefano Saliceti, Thomas Lampe, Thomas Rothörl, Tom Erez, Tuomas Haarnoja and Yuval Tassa for fruitful discussion and support.

---

### النسخة العربية

قدمنا نهجاً للتعلم من الخبراء غير المثاليين للتلاعب الروبوتي البارع المعقد. أظهرنا أن خوارزميتنا، التعلم-Q بالإنتروبيا النسبية (REQ)، فعالة في العديد من سيناريوهات التعلم المختلفة – بما في ذلك التعلم المعزز خارج السياسة وغير المتصل بالإنترنت بالإضافة إلى التعلم المعزز من العروض التوضيحية (RLfD). بالإضافة إلى ذلك، يتفوق نهجنا المقترح للتعلم المعزز من الخبراء غير المثاليين (RLfSE) بشكل كبير على خطوط الأساس التنافسية. على وجه الخصوص، تستفيد REQfSE من الاستكشاف المتشابك لحل المهام المعقدة للغاية التي لا يمكن التعامل معها بطريقة أخرى. لتحقيق ذلك، اقترحنا استخدام متحكمات تتبع نقاط المسار كخبراء غير مثاليين. نجادل بأن هذا النهج يمكن أن يوفر واجهة بديهية وبسيطة للبشر لتحديد السلوكيات المرغوبة للمهمة دون الحاجة إلى عروض توضيحية بشرية أو هندسة دوال مكافأة مشكلة.

**شكر وتقدير**

نود أن نشكر Abbas Abdolmaleki، Akhil Raju، Antoine Laurens، Charles Game، Celine Smith، Christopher Schuster، Claudio Fantacci، Dave Barker، David Khosid، Emre Karagozler، Federico Casarini، Francesco Romano، Giulia Vezzani، Jon Scholz، Jose Enrique Chen، Michael Neunert، Murilo Martins، Nathan Batchelor، Nicole Hurley، Nimrod Gileadi، Nylda Adelise، Oleg Sushkov، Stefano Saliceti، Thomas Lampe، Thomas Rothörl، Tom Erez، Tuomas Haarnoja و Yuval Tassa على المناقشات المثمرة والدعم.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:** None (summary section)
- **Equations:** 0
- **Citations:** 0
- **Special handling:** Acknowledgments section included; names kept in original English

### Quality Metrics

- Semantic equivalence: 0.89
- Technical accuracy: 0.90
- Readability: 0.87
- Glossary consistency: 0.86
- **Overall section score:** 0.88
