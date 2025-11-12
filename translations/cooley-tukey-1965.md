# An Algorithm for the Machine Calculation of Complex Fourier Series
## خوارزمية لحساب متسلسلات فورييه المركبة بواسطة الآلة

**Identifier:** cooley-tukey-1965
**Authors:** James W. Cooley, John W. Tukey
**Year:** 1965
**Journal:** Mathematics of Computation, Vol. 19, No. 90, pp. 297-301
**DOI:** 10.1090/S0025-5718-1965-0178586-1
**Translation Quality:** 0.95
**Glossary Terms Used:** algorithm, method, vector, matrix, sparse, factorization, operation, computation, data point, Fourier series, proportional, procedure

### English Abstract

Good's methods are applicable to certain problems in which one must multiply an N-vector by an N×N matrix which can be factored into m sparse matrices, where m is proportional to log N. This results in a procedure requiring a number of operations proportional to N log N rather than N². These methods are here applied to the calculation of complex Fourier series. They are useful in situations where the number of data points is, or can be chosen to be, a highly composite number.

### الملخص العربي

تُطبَّق طرق غود على مسائل معينة يجب فيها ضرب متجه من الرتبة N بمصفوفة بحجم N×N يمكن تحليلها إلى m مصفوفة متفرقة، حيث m يتناسب مع log N. ينتج عن هذا إجراء يتطلب عددًا من العمليات يتناسب مع N log N بدلاً من N². تُطبَّق هذه الطرق هنا على حساب متسلسلات فورييه المركبة. وهي مفيدة في الحالات التي يكون فيها عدد نقاط البيانات، أو يمكن اختياره ليكون، عددًا مركبًا بدرجة عالية.

### Back-Translation (Validation)

Good's methods are applied to certain problems in which an N-order vector must be multiplied by an N×N-sized matrix that can be factored into m sparse matrices, where m is proportional to log N. This results in a procedure that requires a number of operations proportional to N log N instead of N². These methods are applied here to the calculation of complex Fourier series. They are useful in cases where the number of data points is, or can be chosen to be, a highly composite number.

### Translation Metrics
- Iterations: 1
- Final Score: 0.95
- Quality: High

### Notes

This is the seminal 1965 paper that introduced the Fast Fourier Transform (FFT) algorithm, one of the most influential algorithms in computational mathematics and signal processing. The paper was published in Mathematics of Computation and has been cited over 12,000 times. The algorithm reduces the computational complexity of Fourier series calculation from O(N²) to O(N log N), revolutionizing digital signal processing, communications, and scientific computing.
