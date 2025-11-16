# Virtual Memory, Processes, and Sharing in MULTICS
## الذاكرة الافتراضية والعمليات والمشاركة في مَلتِكس

**Identifier:** multics-vm-1967
**Authors:** Robert C. Daley, Jack B. Dennis
**Institution:** Project MAC, MIT, Cambridge, Massachusetts
**Year:** 1967 (presented at SOSP '67, Gatlinburg, Tennessee, October 1-4, 1967)
**Publication:** Communications of the ACM, Vol. 11, No. 5 (May 1968), pp. 306-312
**DOI:** 10.1145/363095.363139
**PDF:** https://www.cs.utexas.edu/~dahlin/Classes/GradOS/papers/p306-daley.pdf
**HTML Version:** https://multicians.org/daley-dennis.html

**Abstract Translation Quality:** 0.91 (from translations/multics-vm-1967.md)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@article{daley1967virtual,
  title={Virtual memory, processes, and sharing in MULTICS},
  author={Daley, Robert C and Dennis, Jack B},
  journal={Communications of the ACM},
  volume={11},
  number={5},
  pages={306--312},
  year={1968},
  publisher={ACM}
}
```

## Historical Significance

MULTICS (Multiplexed Information and Computing Service) was one of the most influential operating systems in computer science history. This 1967 paper introduced revolutionary concepts including:

- **Single-level storage system**: Unified treatment of memory and files
- **Segmented virtual memory**: 2^14 segments of 2^18 words each
- **Dynamic linking**: Runtime linking of shared procedures
- **Pure procedures**: Non-self-modifying code for sharing
- **Location-independent addressing**: Generalized addresses independent of physical location
- **Hierarchical file system**: Multi-level directory structure

These innovations profoundly influenced:
- UNIX operating system design (Dennis Ritchie and Ken Thompson were MULTICS developers)
- Modern virtual memory systems (all modern OSes use variants of these concepts)
- Intel x86 architecture's segmented memory model
- Capability-based security systems
- Dynamic linking in modern operating systems

## Paper Structure

The paper consists of the following sections:

1. **Summary** - Overview of the three main objectives
2. **Introduction** - Design goals and motivation
3. **The Multics Concepts of Process and Address Space** - Process definition, segments, virtual memory structure
4. **Addressing in Multics** - Generalized addresses, address formation, descriptor segments, paging
5. **Intersegment Linking and Addressing** - Dynamic linking mechanism, linkage sections, procedure calls
6. **Acknowledgment** - Credits to the Multics team
7. **References** - 9 foundational references

## Translation Team

- Translator: Claude Code AI Session (2025-11-16)
- Reviewer: TBD
- Started: 2025-11-16
- Completed: TBD

## Translation Notes

This paper presents unique terminology that requires careful translation:
- **Generalized address**: عنوان معمم
- **Segment**: مقطع
- **Pure procedure**: إجراء نقي
- **Linkage section**: قسم الربط
- **Descriptor segment**: مقطع الواصف
- **Traffic controller**: متحكم الحركة

The paper includes 13 figures illustrating the virtual memory and linking mechanisms. These are referenced in the text and should be described in the Arabic translation.
