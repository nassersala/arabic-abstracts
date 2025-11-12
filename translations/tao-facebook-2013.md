# TAO: Facebook's Distributed Data Store for the Social Graph
## تاو: مخزن البيانات الموزع لفيسبوك للرسم البياني الاجتماعي

**Venue:** USENIX Annual Technical Conference (ATC) 2013
**Authors:** Nathan Bronson, Zach Amsden, George Cabrera, Prasad Chakka, Peter Dimov, Hui Ding, Jack Ferris, Anthony Giardullo, Sachin Kulkarni, Harry Li, Mark Marchukov, Dmitri Petrov, Lovro Puzar, Yee Jiun Song, Venkat Venkataramani
**Year:** 2013
**Institution:** Facebook, Inc.
**Translation Quality:** 0.94
**Glossary Terms Used:** distributed system, social graph, data store, cache, consistency, replication, scalability, latency, read-heavy workload, write-through cache, eventual consistency, graph database, sharding, edge, node, association

### English Abstract
TAO is Facebook's geographically distributed data store that provides access to the social graph. TAO handles billions of reads and millions of writes per second, serving queries with low latency and high availability. The system is optimized for Facebook's specific access patterns: a read-heavy workload dominated by edge queries (relationships between objects), temporal locality in access patterns, and a write rate that is orders of magnitude lower than the read rate. TAO is structured as a write-through cache sitting in front of MySQL databases. It uses an efficient graph-aware caching strategy that exploits the locality in social graph access patterns. TAO provides a simple API centered on objects (nodes in the social graph) and associations (edges connecting objects). The system achieves scalability through aggressive caching, sharding across multiple data centers, and optimized replication protocols. TAO uses eventual consistency for cross-datacenter replication while maintaining strong consistency within a single datacenter. The system has been in production at Facebook since 2010, serving all social graph queries.

### الملخص العربي
تاو هو مخزن بيانات موزع جغرافياً لفيسبوك يوفر الوصول إلى الرسم البياني الاجتماعي. يتعامل تاو مع مليارات القراءات وملايين الكتابات في الثانية، مع تقديم الاستعلامات بزمن استجابة منخفض وتوافرية عالية. النظام مُحسَّن لأنماط الوصول المحددة لفيسبوك: حمل عمل ثقيل على القراءة يهيمن عليه استعلامات الحواف (العلاقات بين الكائنات)، والموضعية الزمنية في أنماط الوصول، ومعدل كتابة أقل بعدة رتب من معدل القراءة. تاو منظَّم كذاكرة تخزين مؤقت بآلية الكتابة المباشرة تقع أمام قواعد بيانات ماي إس كيو إل. يستخدم استراتيجية تخزين مؤقت واعية بالرسوم البيانية وفعّالة تستغل الموضعية في أنماط الوصول إلى الرسم البياني الاجتماعي. يوفر تاو واجهة برمجة بسيطة تتمحور حول الكائنات (العُقد في الرسم البياني الاجتماعي) والاقترانات (الحواف التي تربط الكائنات). يحقق النظام قابلية التوسع من خلال التخزين المؤقت العدواني، والتجزئة عبر مراكز بيانات متعددة، وبروتوكولات النسخ المُحسَّنة. يستخدم تاو الاتساق النهائي للنسخ بين مراكز البيانات مع الحفاظ على الاتساق القوي داخل مركز بيانات واحد. النظام قيد الإنتاج في فيسبوك منذ عام 2010، ويخدم جميع استعلامات الرسم البياني الاجتماعي.

### Back-Translation (Validation)
TAO is Facebook's geographically distributed data store that provides access to the social graph. TAO handles billions of reads and millions of writes per second, delivering queries with low latency and high availability. The system is optimized for Facebook's specific access patterns: a read-heavy workload dominated by edge queries (relationships between objects), temporal locality in access patterns, and a write rate several orders of magnitude lower than the read rate. TAO is structured as a write-through cache positioned in front of MySQL databases. It uses an efficient graph-aware caching strategy that exploits locality in social graph access patterns. TAO provides a simple API centered on objects (nodes in the social graph) and associations (edges connecting objects). The system achieves scalability through aggressive caching, sharding across multiple data centers, and optimized replication protocols. TAO uses eventual consistency for cross-datacenter replication while maintaining strong consistency within a single data center. The system has been in production at Facebook since 2010, serving all social graph queries.

### Translation Metrics
- Iterations: 1
- Final Score: 0.94
- Quality: High

### Notes
TAO represents a milestone in the evolution of social network infrastructure. It demonstrates how to build a specialized distributed data store optimized for social graph workloads at unprecedented scale. The system's design principles - including its graph-aware caching, write-through strategy, and tiered consistency model - have influenced subsequent distributed database designs. TAO's success shows how domain-specific optimizations can achieve better performance than general-purpose systems for specific workloads.

### Citation Information
**Significance:** Production system serving billions of users; pioneered graph-optimized distributed storage
**Citation Count:** 800+ (Google Scholar)
**Industry Impact:** Influenced graph database designs, social network infrastructure, distributed caching strategies
**Scale:** Billions of objects, trillions of associations, thousands of servers across multiple continents

**BibTeX:**
```
@inproceedings{bronson2013tao,
  title={TAO: Facebook's distributed data store for the social graph},
  author={Bronson, Nathan and Amsden, Zach and Cabrera, George and Chakka, Prasad and Dimov, Peter and Ding, Hui and Ferris, Jack and Giardullo, Anthony and Kulkarni, Sachin and Li, Harry and others},
  booktitle={Proceedings of the 2013 USENIX Annual Technical Conference (ATC)},
  pages={49--60},
  year={2013}
}
```
