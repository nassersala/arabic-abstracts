# Dynamo: Amazon's Highly Available Key-value Store
## ديناموا: مخزن المفتاح-القيمة عالي التوافر من أمازون

**Paper ID:** dynamo-2007
**Authors:** Giuseppe DeCandia, Deniz Hastorun, Madan Jampani, Gunavardhan Kakulapati, Avinash Lakshman, Alex Pilchin, Swaminathan Sivasubramanian, Peter Vosshall, Werner Vogels
**Year:** 2007
**Publication:** Proceedings of the 21st ACM Symposium on Operating Systems Principles (SOSP 2007)
**Categories:** Distributed Systems, Storage Systems, Key-Value Stores
**DOI:** 10.1145/1294261.1294281
**PDF:** https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf

**Abstract Translation Quality:** 0.93 (from translations/dynamo-2007.md)
**Full Paper Translation Quality:** 0.875 (Excellent - Exceeds 0.85 threshold)

## Citation

```bibtex
@inproceedings{DeCandia2007,
  author = {DeCandia, Giuseppe and Hastorun, Deniz and Jampani, Madan and Kakulapati, Gunavardhan and Lakshman, Avinash and Pilchin, Alex and Sivasubramanian, Swaminathan and Vosshall, Peter and Vogels, Werner},
  title = {Dynamo: Amazon's Highly Available Key-value Store},
  booktitle = {Proceedings of Twenty-first ACM SIGOPS Symposium on Operating Systems Principles},
  series = {SOSP '07},
  year = {2007},
  isbn = {978-1-59593-591-5},
  location = {Stevenson, Washington, USA},
  pages = {205--220},
  numpages = {16},
  url = {http://doi.acm.org/10.1145/1294261.1294281},
  doi = {10.1145/1294261.1294281},
  acmid = {1294281},
  publisher = {ACM},
  address = {New York, NY, USA},
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5) - Sessions 2025-11-14 to 2025-11-15
- Reviewer: TBD
- Started: 2025-11-14
- Completed: 2025-11-15

## Historical Significance
Dynamo, published in 2007, introduced the concept of eventual consistency for high availability and influenced the design of numerous NoSQL databases including Apache Cassandra, Riak, and Voldemort. The paper popularized techniques like consistent hashing, vector clocks, and gossip protocols for building highly available distributed systems. It demonstrated that sacrificing strong consistency for availability (following the CAP theorem) was viable for many real-world applications.

## Paper Statistics
- Pages: 16
- Sections: 8 main sections
- Figures: 8
- Tables: 2
- References: 24
