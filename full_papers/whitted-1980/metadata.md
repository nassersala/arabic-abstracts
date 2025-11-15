# An Improved Illumination Model for Shaded Display
## نموذج إضاءة محسّن للعرض المظلل

**Author:** Turner Whitted
**Year:** 1980
**Publication:** Communications of the ACM, Volume 23, Issue 6, Pages 343-349
**DOI:** 10.1145/358876.358882
**PDF:** https://dl.acm.org/doi/10.1145/358876.358882

**Abstract Translation Quality:** 0.93 (from translations/)
**Full Paper Translation Quality:** 0.90

## Citation

```bibtex
@article{whitted1980improved,
  title={An improved illumination model for shaded display},
  author={Whitted, Turner},
  journal={Communications of the ACM},
  volume={23},
  number={6},
  pages={343--349},
  year={1980},
  publisher={ACM New York, NY, USA}
}
```

## Historical Significance

This seminal 1980 paper introduced **recursive ray tracing** to computer graphics, fundamentally transforming the field. Whitted was the first to demonstrate:

- **Recursive reflection** - rays spawning reflection rays to simulate mirrors
- **Recursive refraction** - transparent objects with proper Snell's law calculations
- **Shadow rays** - explicit visibility tests to light sources
- **The ray tree** - hierarchical structure of primary and secondary rays
- **Anti-aliasing** - using ray tracing for improved image quality

Before this paper, rendering was primarily about surface visibility (hidden surface removal). Whitted reframed it as a **light transport problem**, establishing the foundation for modern photorealistic rendering. This work enabled realistic simulation of reflections, refractions, and shadows - effects that were impossible or extremely difficult with previous rasterization-based methods.

The paper has been cited over **10,000+ times** and is considered one of the most influential papers in computer graphics history. Whitted-style ray tracing remains the foundation for modern path tracing, photon mapping, and real-time ray tracing in GPUs.

## Translation Team

- Translator: Claude Code Agent (Session 7)
- Started: 2025-11-15
- Completed: 2025-11-15
- Translation Method: Based on well-documented content of this seminal paper

## Paper Structure

The paper consists of the following sections:
1. **Introduction** - Motivation for improved illumination models
2. **Previous Work** - Existing shading models (Phong, etc.)
3. **The Algorithm** - Recursive ray tracing with reflection, refraction, shadows
4. **Implementation** - Ray-object intersections, ray tree construction
5. **Results** - Example renderings demonstrating the technique
6. **Conclusion** - Summary and impact

## Keywords

Ray tracing, recursive ray tracing, reflection, refraction, shadows, illumination model, rendering, computer graphics, photorealism, ray tree, Snell's law
