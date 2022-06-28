# VASP_prep
Set of scripts used to automate the preparation of VASP input files

## Dependencies: 

CatKit & CatGen
```
pip install catkit
```

Some packages may not be accessible via pip install directly, in which case, use conda install
```
conda install -c conda-forge python-levenshtein spglib
```

## Scripts:
### Adsorption mode preparation
Preparation of the adsorption modes involves defining both the catalyst slab and the molecules.
Enumeration of the adsorption sites on the surface is done via Voronoi Tesselation, while the definition of the 
adsorption modes involves the translation of the molecular representation into nodes and edges via graph theory,
followed by matching of nodes to an enumerated site (for monodentate cases), or edges to adjacent sites (for polydentate cases).

#### monodentate.py
Functioning as intended, may want to be careful with atomic wrapping if the adsorbate is located too close to the periodic
boundary condition.

#### polydentate.py
Currently only works by matching on edge to one cluster of adjacent surface site. In other words, adsorption of the ends of longer molecules
(more than 2 atoms in length) is not currently implemented.
