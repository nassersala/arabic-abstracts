# Kafka: a Distributed Messaging System for Log Processing
## كافكا: نظام رسائل موزع لمعالجة السجلات

**Paper ID:** kafka-2011
**Authors:** Jay Kreps (LinkedIn Corp.), Neha Narkhede (LinkedIn Corp.), Jun Rao (LinkedIn Corp.)
**Year:** 2011
**Publication:** NetDB'11, Jun. 12, 2011, Athens, Greece
**Categories:** Distributed Systems, Messaging Systems, Log Processing
**DOI:** 10.1145/1989323.1989328
**PDF:** https://notes.stephenholiday.com/Kafka.pdf

**Abstract Translation Quality:** 0.90
**Full Paper Translation Quality:** 0.88

## Citation

```bibtex
@inproceedings{kreps2011kafka,
  title={Kafka: a distributed messaging system for log processing},
  author={Kreps, Jay and Narkhede, Neha and Rao, Jun},
  booktitle={Proceedings of the NetDB},
  volume={11},
  pages={1--7},
  year={2011}
}
```

## Paper Overview

This paper introduces Kafka, a distributed messaging system developed at LinkedIn for collecting and delivering high volumes of log data with low latency. The system is designed to handle both offline and online message consumption, making it suitable for real-time analytics and batch processing. The paper demonstrates superior performance compared to Apache ActiveMQ and RabbitMQ.

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Key Contributions
1. Novel distributed messaging system combining benefits of log aggregators and messaging systems
2. Pull-based consumption model allowing consumers to control their own pace
3. Efficient storage using sequential I/O and offset-based addressing
4. Stateless broker design with consumer-managed offsets
5. Production deployment handling hundreds of GB of data daily at LinkedIn
