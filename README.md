# 3D Solid Modeling – Final Project

This repository contains the complete implementation of the 3D Modeling and Visualization project, including:

- Parametric cube
- Parametric torus
- Curved pipe defined by a Bézier or Hermite curve
- Polygon mesh generation (triangular meshes)
- Scene composition without intersections
- Geometric transformations (scaling, rotation, translation)
- Camera coordinate system construction
- Perspective projection
- Rasterization at multiple resolutions

---
### Folder Overview

- **src/models** – Contains the geometric primitives (cube, torus, curved pipe).  
  Each function returns vertices and faces for the corresponding solid.

- **src/utils** – Utility functions used throughout the project:
  - Transformation matrices  
  - Camera coordinate system  
  - Perspective projection  
  - Rasterization  

- **notebooks** – Experimentation area with Jupyter Notebooks for debugging, quick visualizations, and generating images for the report.

- **report** – Final report.

- **tests** – Unit tests to validate geometric generation, projections, and transforms.

---


Install all dependencies:

```bash
pip install -r requirements.txt