# In Search of an Understandable Consensus Algorithm (Extended Version)
## في البحث عن خوارزمية إجماع قابلة للفهم (النسخة الموسعة)

**Authors:** Diego Ongaro and John Ousterhout
**Institution:** Stanford University
**Year:** 2014
**Publication:** USENIX Annual Technical Conference (ATC '14)
**Award:** Best Paper Award
**Categories:** Distributed Systems, Consensus Algorithms
**PDF:** https://raft.github.io/raft.pdf
**Website:** https://raft.github.io/

**Abstract Translation Quality:** 0.91
**Full Paper Translation Quality:** 0.874 (14 of 14 sections completed, 100% ✅)

## Citation

```bibtex
@inproceedings{ongaro2014raft,
  title={In search of an understandable consensus algorithm},
  author={Ongaro, Diego and Ousterhout, John},
  booktitle={2014 USENIX Annual Technical Conference (USENIX ATC 14)},
  pages={305--319},
  year={2014}
}
```

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Paper Overview

Raft is a consensus algorithm for managing a replicated log. It produces a result equivalent to (multi-)Paxos, and it is as efficient as Paxos, but its structure is different from Paxos; this makes Raft more understandable than Paxos and also provides a better foundation for building practical systems.

The algorithm separates key consensus elements:
- Leader election
- Log replication
- Safety mechanisms

A user study with 43 students demonstrated that Raft is significantly easier to comprehend than Paxos.

## Key Features

- **Strong leader:** Log entries flow only from leader to followers
- **Leader election:** Randomized timer-based election mechanism
- **Membership changes:** Joint consensus for cluster reconfiguration
- **Log compaction:** Snapshotting mechanism

## Sections Structure

1. Introduction
2. Replicated state machines
3. What's wrong with Paxos?
4. Designing for understandability
5. The Raft consensus algorithm
   - 5.1 Raft basics
   - 5.2 Leader election
   - 5.3 Log replication
   - 5.4 Safety
   - 5.5 Follower and candidate crashes
   - 5.6 Timing and availability
6. Cluster membership changes
7. Log compaction
8. Client interaction
