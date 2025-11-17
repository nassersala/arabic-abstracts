# Projective Dynamics: Fusing Constraint Projections for Fast Simulation
## الديناميكيات الإسقاطية: دمج إسقاطات القيود للمحاكاة السريعة

**Paper ID:** bouaziz-2014
**Authors:** Sofien Bouaziz, Sebastian Martin, Tiantian Liu, Ladislav Kavan, Mark Pauly
**Year:** 2014
**Publication:** ACM Transactions on Graphics (TOG), Volume 33, Issue 4, Article 154
**Conference:** SIGGRAPH 2014
**Categories:** Computer Graphics, Physics Simulation, Numerical Methods
**DOI:** 10.1145/2601097.2601116
**PDF:** https://www.cs.utah.edu/~ladislav/bouaziz14projective/bouaziz14projective.pdf
**ACM DL:** https://dl.acm.org/doi/10.1145/2601097.2601116

**Abstract Translation Quality:** 0.91 (from translations/bouaziz-2014.md)
**Full Paper Translation Quality:** TBD

## Citation

```bibtex
@article{Bouaziz:2014:PD,
  author = {Bouaziz, Sofien and Martin, Sebastian and Liu, Tiantian and Kavan, Ladislav and Pauly, Mark},
  title = {Projective Dynamics: Fusing Constraint Projections for Fast Simulation},
  journal = {ACM Transactions on Graphics},
  volume = {33},
  number = {4},
  year = {2014},
  pages = {154:1--154:11},
  articleno = {154},
  doi = {10.1145/2601097.2601116},
  publisher = {ACM},
  address = {New York, NY, USA}
}
```

## Paper Significance

This paper presents a groundbreaking method for physics simulation that bridges the gap between implicit time integration methods (Finite Element Method) and explicit position-based dynamics. The approach has been highly influential in computer graphics and physical simulation, providing a fast, robust solver for various deformable objects including solids, cloths, and shells.

**Key Contributions:**
- Novel implicit time integration method using alternating optimization
- Unification of FEM and Position Based Dynamics approaches
- Efficient constraint projection framework
- Real-time performance for various simulation types

**Citation Count:** 800+ citations (highly influential paper in graphics/simulation)

## Translation Team
- Translator: Claude (Sonnet 4.5)
- Session ID: 2025-11-17
- Started: 2025-11-17
- Completed: TBD

## Domain-Specific Notes

This is an important physics simulation paper requiring careful handling of:
- Mathematical notation (matrices, vectors, energy functions)
- Physics terminology (dynamics, constraints, forces, energy potentials)
- Numerical methods terminology (implicit/explicit integration, solvers)
- Computer graphics terminology (mesh, deformation, rendering)
