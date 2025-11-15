# Section 2: Framework
## القسم 2: الإطار العام

**Section:** framework
**Translation Quality:** 0.87
**Glossary Terms Used:** neural network, activation, dataset, architecture, autoencoder, regularization, weight decay

---

### English Version

**Notation** We denote by $x \in \mathbb{R}^m$
an input image, and $\phi(x)$ activation values of some layer. We first examine properties
of the image of $\phi(x)$, and then we search for its blind spots.

We perform a number of experiments on a few different networks and three datasets:
\begin{itemize}
	\item For the MNIST dataset, we used the following architectures~\cite{lecun1998mnist}
	\begin{itemize}
		\item A simple fully connected network with one or more hidden layers and a Softmax classifier. We refer to this network as ``FC''.
		\item A classifier trained on top of an autoencoder. We refer to this network as ``AE''.
	\end{itemize}
	\item The ImageNet dataset~\cite{deng2009imagenet}.
	\begin{itemize}
		\item Krizhevsky et. al architecture \cite{krizhevsky2012imagenet}. We refer to it as ``AlexNet''.
	\end{itemize}
	\item $\sim 10$M image samples from Youtube (see~\cite{le2011building})
	\begin{itemize}
		\item Unsupervised trained network with $\sim$ 1 billion learnable parameters. We refer to it as ``QuocNet''.
	\end{itemize}
\end{itemize}

For the MNIST experiments, we use regularization with a weight decay of $\lambda$. Moreover, in some experiments we
split the MNIST training dataset into two disjoint datasets $P_1$, and $P_2$, each with 30000 training cases.

---

### النسخة العربية

**الترميز** نرمز بـ $x \in \mathbb{R}^m$ إلى صورة إدخال، و $\phi(x)$ إلى قيم تنشيط طبقة معينة. نفحص أولاً خصائص صورة $\phi(x)$، ثم نبحث عن نقاطها العمياء.

نُجري عدداً من التجارب على عدد قليل من الشبكات المختلفة وثلاث مجموعات بيانات:
\begin{itemize}
	\item لمجموعة بيانات MNIST، استخدمنا المعماريات التالية~\cite{lecun1998mnist}
	\begin{itemize}
		\item شبكة متصلة بالكامل بسيطة بطبقة أو أكثر من الطبقات المخفية ومصنف Softmax. نشير إلى هذه الشبكة باسم ``FC''.
		\item مصنف مُدرَّب على قمة مشفر تلقائي. نشير إلى هذه الشبكة باسم ``AE''.
	\end{itemize}
	\item مجموعة بيانات ImageNet~\cite{deng2009imagenet}.
	\begin{itemize}
		\item معمارية Krizhevsky وآخرون \cite{krizhevsky2012imagenet}. نشير إليها باسم ``AlexNet''.
	\end{itemize}
	\item $\sim 10$ مليون عينة صورة من Youtube (انظر~\cite{le2011building})
	\begin{itemize}
		\item شبكة مدربة بدون إشراف مع $\sim$ مليار معامل قابل للتعلم. نشير إليها باسم ``QuocNet''.
	\end{itemize}
\end{itemize}

لتجارب MNIST، نستخدم التنظيم مع تسوس الوزن بقيمة $\lambda$. علاوة على ذلك، في بعض التجارب نقسم مجموعة بيانات تدريب MNIST إلى مجموعتي بيانات منفصلتين $P_1$ و $P_2$، كل منهما بـ 30000 حالة تدريب.

---

### Translation Notes

- **Figures referenced:** None
- **Key terms introduced:**
  - activation values (قيم تنشيط)
  - blind spots (نقاط عمياء)
  - fully connected network (شبكة متصلة بالكامل)
  - autoencoder (مشفر تلقائي)
  - weight decay (تسوس الوزن)
  - learnable parameters (معاملات قابلة للتعلم)
  - disjoint datasets (مجموعات بيانات منفصلة)
- **Equations:** Mathematical notation for $x \in \mathbb{R}^m$ and $\phi(x)$
- **Citations:** 4 references (MNIST, ImageNet, AlexNet, QuocNet)
- **Special handling:**
  - Preserved LaTeX itemize/enumerate structure
  - Kept network names in English (FC, AE, AlexNet, QuocNet) as they are proper names
  - Maintained mathematical notation for datasets ($P_1$, $P_2$) and parameters ($\lambda$)

### Quality Metrics

- Semantic equivalence: 0.88
- Technical accuracy: 0.89
- Readability: 0.85
- Glossary consistency: 0.87
- **Overall section score:** 0.87
