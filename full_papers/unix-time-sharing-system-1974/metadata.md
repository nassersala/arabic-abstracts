# The UNIX Time-Sharing System
## نظام يونكس للمشاركة الزمنية

**Authors:** Dennis M. Ritchie, Ken Thompson
**Affiliation:** Bell Laboratories
**Year:** 1974
**Publication:** Communications of the ACM, Volume 17, Issue 7, July 1974, pp. 365-375
**DOI:** 10.1145/361011.361061
**PDF:** https://dl.acm.org/doi/10.1145/361011.361061

**Abstract Translation Quality:** 0.92 (from translations/)
**Full Paper Translation Quality:** 0.880 ✅

## Citation

```bibtex
@article{ritchie1974unix,
  title={The UNIX time-sharing system},
  author={Ritchie, Dennis M. and Thompson, Ken},
  journal={Communications of the ACM},
  volume={17},
  number={7},
  pages={365--375},
  year={1974},
  publisher={ACM}
}
```

## Historical Significance

This seminal 1974 paper introduced UNIX, one of the most influential operating systems in computing history. Written by Dennis Ritchie and Ken Thompson at Bell Labs, it describes a general-purpose, multi-user operating system for the PDP-11 series computers. UNIX established many fundamental principles still used in modern operating systems:

- Hierarchical file system with demountable volumes
- Unified treatment of files, devices, and inter-process I/O
- Asynchronous process execution
- User-selectable command language (the shell)
- Simple, elegant design philosophy

The paper's influence extends to Linux, macOS, BSD, and countless other systems. It exemplifies the "UNIX philosophy" of building simple, modular tools that work together.

## Translation Team
- Translator: Claude (Session 2025-11-15)
- Reviewer: TBD
- Started: 2025-11-15
- Completed: 2025-11-15 ✅

## Paper Structure

The paper consists of 8 main sections:
1. **Introduction** - Overview and historical context
2. **File System** - Description of the hierarchical file system
3. **Implementation of the File System** - Technical implementation details
4. **Processes and Images** - Process model and execution
5. **The Shell** - Command interpreter and user interface
6. **Implementation of the Shell** - Shell implementation details
7. **Traps** - Error and signal handling
8. **Perspective** - Conclusions and future directions
