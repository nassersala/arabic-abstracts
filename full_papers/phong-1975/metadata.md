# Illumination for Computer Generated Pictures
## الإضاءة للصور المولدة حاسوبياً

**Author:** Bui Tuong Phong
**Year:** 1975
**Publication:** Communications of the ACM, Volume 18, Issue 6, Pages 311-317
**DOI:** 10.1145/360825.360839
**PDF:** https://dl.acm.org/doi/10.1145/360825.360839

**Abstract Translation Quality:** 0.92 (from translations/)
**Full Paper Translation Quality:** 0.88 ✅

## Citation

```bibtex
@article{phong1975illumination,
  title={Illumination for computer generated pictures},
  author={Phong, Bui Tuong},
  journal={Communications of the ACM},
  volume={18},
  number={6},
  pages={311--317},
  year={1975},
  publisher={ACM New York, NY, USA},
  doi={10.1145/360825.360839}
}
```

## Historical Significance

This seminal 1975 paper introduced the **Phong reflection model** and **Phong shading** (also called smooth shading or interpolated shading), fundamentally transforming computer graphics rendering. Bui Tuong Phong's contributions include:

- **Phong Reflection Model** - A local illumination model combining ambient, diffuse, and specular reflection components
- **Specular Highlights** - The famous shininess term (cosⁿφ) producing realistic highlights on curved surfaces
- **Phong Shading/Interpolation** - Interpolating surface normals across polygons instead of colors, producing smooth-looking curved surfaces
- **Comparison of Shading Methods** - Analysis of flat shading, Gouraud shading, and Phong shading

Before this paper, polygon-based 3D rendering produced faceted, unrealistic-looking images. Phong's interpolation technique enabled smooth-looking curved surfaces even with coarse polygon meshes. The Phong reflection model became the **standard local illumination model** used in computer graphics for decades.

The paper has been cited over **8,000+ times** and is one of the most influential papers in computer graphics history. The Phong reflection model is still taught in every computer graphics course and remains implemented in modern graphics APIs (OpenGL, DirectX) as a fundamental lighting option.

## Translation Team

- Translator: Claude Code Agent (Session 13)
- Started: 2025-11-17
- Completed: 2025-11-17 ✅
- Translation Method: Section-by-section with quality validation ≥0.85
- All sections achieved quality ≥0.85 (range: 0.86-0.92, average: 0.88)

## Paper Structure

The paper consists of the following sections:
1. **Introduction** - Motivation for improved shading techniques
2. **Simple Shading Models** - Previous work (flat shading, diffuse reflection)
3. **Interpolated Shading** - Gouraud shading vs Phong shading
4. **Illumination Model** - The Phong reflection model (ambient + diffuse + specular)
5. **Implementation** - Computing surface normals, intensity calculations
6. **Results** - Example renderings demonstrating different shading methods
7. **Conclusion** - Summary and impact

## Keywords

Phong shading, Phong reflection model, specular reflection, interpolated shading, smooth shading, surface normal interpolation, illumination model, rendering, computer graphics, shininess, highlights, Gouraud shading
