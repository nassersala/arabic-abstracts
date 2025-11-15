# Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications
## كورد: خدمة بحث نظير إلى نظير قابلة للتوسع لتطبيقات الإنترنت

**arXiv ID:** chord-2001
**Authors:** Ion Stoica, Robert Morris, David Karger, M. Frans Kaashoek, Hari Balakrishnan
**Year:** 2001
**Publication:** ACM SIGCOMM Conference on Applications, Technologies, Architectures, and Protocols for Computer Communications 2001
**Institution:** MIT Laboratory for Computer Science, UC Berkeley
**Categories:** Distributed Systems, Networking, Peer-to-Peer
**DOI:** 10.1145/383059.383071
**Pages:** 149-160
**PDF:** https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf

**Abstract Translation Quality:** 0.94 (from translations/)
**Full Paper Translation Quality:** 0.89

## Citation

```bibtex
@inproceedings{stoica2001chord,
  title={Chord: A scalable peer-to-peer lookup service for internet applications},
  author={Stoica, Ion and Morris, Robert and Karger, David and Kaashoek, M Frans and Balakrishnan, Hari},
  booktitle={Proceedings of the 2001 ACM SIGCOMM Conference},
  pages={149--160},
  year={2001},
  organization={ACM}
}
```

## Translation Team
- Translator: Claude Code Session 2025-11-15
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15

## Significance
Chord is one of the foundational distributed hash table (DHT) protocols that enabled the peer-to-peer revolution of the early 2000s. With over 15,000 citations, it's one of the most influential networking papers. The protocol's elegant use of consistent hashing and finger tables provides provably efficient lookup with O(log N) complexity. Chord influenced numerous systems including BitTorrent's DHT, IPFS, Ethereum's node discovery, and academic systems like CFS and Ivy.
