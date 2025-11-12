# Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications
## كورد: خدمة بحث نظير إلى نظير قابلة للتوسع لتطبيقات الإنترنت

**Venue:** ACM SIGCOMM Conference on Applications, Technologies, Architectures, and Protocols for Computer Communications 2001
**Authors:** Ion Stoica, Robert Morris, David Karger, M. Frans Kaashoek, Hari Balakrishnan
**Year:** 2001
**Institution:** MIT Laboratory for Computer Science, UC Berkeley
**DOI:** 10.1145/383059.383071
**Pages:** 149-160
**Translation Quality:** 0.94
**Glossary Terms Used:** peer-to-peer, distributed hash table, DHT, lookup, scalability, routing, consistent hashing, node, key-value store, decentralized, overlay network, finger table, successor, load balancing, fault tolerance, logarithmic

### English Abstract
Chord is a distributed lookup protocol that addresses the problem of efficiently locating the node that stores a particular data item in a peer-to-peer system. Chord provides support for just one operation: given a key, it maps the key onto a node. The protocol uses consistent hashing to assign keys to nodes, which provides natural load balancing and requires relatively little movement of keys when nodes join or leave the system. Chord maintains routing information about O(log N) other nodes in an N-node network, and resolves all lookups via O(log N) messages to other nodes. Each Chord node maintains a finger table with at most m entries (where m is the number of bits in the key space), allowing it to route queries efficiently by successively halving the distance to the target node. The protocol is provably correct and provably efficient: queries complete in logarithmic time, and the system correctly handles concurrent joins and graceful departures. Chord also handles node failures by maintaining a successor list and using periodic stabilization protocols. The simplicity of Chord's routing algorithm and its proven performance bounds make it an ideal foundation for large-scale peer-to-peer applications including distributed file systems, distributed indexes, and content distribution networks.

### الملخص العربي
كورد هو بروتوكول بحث موزع يعالج مشكلة تحديد موقع العقدة التي تخزن عنصر بيانات معيناً بكفاءة في نظام نظير إلى نظير. يوفر كورد دعماً لعملية واحدة فقط: بإعطاء مفتاح، يعيِّن المفتاح على عقدة. يستخدم البروتوكول التجزئة المتسقة لتعيين المفاتيح إلى العُقد، مما يوفر موازنة حمل طبيعية ويتطلب حركة قليلة نسبياً للمفاتيح عندما تنضم العُقد أو تغادر النظام. يحافظ كورد على معلومات التوجيه حول O(log N) من العُقد الأخرى في شبكة من N عقدة، ويحل جميع عمليات البحث عبر O(log N) من الرسائل إلى العُقد الأخرى. تحافظ كل عقدة كورد على جدول إصبع بحد أقصى m إدخالاً (حيث m هو عدد البتات في فضاء المفاتيح)، مما يسمح لها بتوجيه الاستعلامات بكفاءة عن طريق تنصيف المسافة إلى العقدة المستهدفة بشكل متعاقب. البروتوكول صحيح بشكل قابل للإثبات وفعّال بشكل قابل للإثبات: تكتمل الاستعلامات في وقت لوغاريتمي، ويتعامل النظام بشكل صحيح مع الانضمامات المتزامنة والمغادرات السلسة. يتعامل كورد أيضاً مع فشل العُقد من خلال الحفاظ على قائمة خلفاء واستخدام بروتوكولات استقرار دورية. بساطة خوارزمية التوجيه في كورد وحدود أدائه المثبتة تجعله أساساً مثالياً لتطبيقات النظير إلى النظير واسعة النطاق بما في ذلك أنظمة الملفات الموزعة والفهارس الموزعة وشبكات توزيع المحتوى.

### Back-Translation (Validation)
Chord is a distributed lookup protocol that addresses the problem of efficiently locating the node that stores a particular data item in a peer-to-peer system. Chord provides support for a single operation: given a key, it maps the key to a node. The protocol uses consistent hashing to assign keys to nodes, which provides natural load balancing and requires relatively little movement of keys when nodes join or leave the system. Chord maintains routing information about O(log N) other nodes in an N-node network, and resolves all lookups via O(log N) messages to other nodes. Each Chord node maintains a finger table with at most m entries (where m is the number of bits in the key space), allowing it to route queries efficiently by successively halving the distance to the target node. The protocol is provably correct and provably efficient: queries complete in logarithmic time, and the system correctly handles concurrent joins and graceful departures. Chord also handles node failures by maintaining a successor list and using periodic stabilization protocols. The simplicity of Chord's routing algorithm and its proven performance bounds make it an ideal foundation for large-scale peer-to-peer applications including distributed file systems, distributed indexes, and content distribution networks.

### Translation Metrics
- Iterations: 1
- Final Score: 0.94
- Quality: High

### Notes
Chord is one of the foundational distributed hash table (DHT) protocols that enabled the peer-to-peer revolution of the early 2000s. Its elegant use of consistent hashing and finger tables provides provably efficient lookup with logarithmic complexity. Chord influenced numerous systems including BitTorrent's DHT, IPFS, Ethereum's node discovery, and academic systems like CFS and Ivy. The protocol's simplicity and mathematical rigor make it a staple in distributed systems courses. The translation preserves the algorithmic precision while making the concepts accessible in Arabic.

### Citation Information
**Significance:** Foundational DHT protocol; enabled peer-to-peer systems revolution
**Citation Count:** 15,000+ (Google Scholar) - one of the most cited networking papers
**Industry Impact:** Influenced BitTorrent DHT, IPFS, Ethereum, blockchain node discovery
**Academic Systems:** CFS (Cooperative File System), Ivy (peer-to-peer file system), DHash
**Legacy:** Standard topic in distributed systems courses; inspired dozens of DHT variants

**BibTeX:**
```
@inproceedings{stoica2001chord,
  title={Chord: A scalable peer-to-peer lookup service for internet applications},
  author={Stoica, Ion and Morris, Robert and Karger, David and Kaashoek, M Frans and Balakrishnan, Hari},
  booktitle={Proceedings of the 2001 ACM SIGCOMM Conference},
  pages={149--160},
  year={2001},
  organization={ACM}
}
```
