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

## Hard-coded Changes to CatGen
In some subscripts/modules in CatKit, some object attributes are called with a single leading underscore, i.e. indicating a weak internal use property. For some reason, this causes errors when the modules are being called from external scripts, and thus have been modified.

In particular, in the module for translating the atomic representation into graph representation, via a script called *gratoms.py* under CatKit, any instance where the cell dimensions attribute of the atoms object is called via *._cell*, they need to be modified to call it without the leading underscore, as in *.cell*. See the example below

From:

```python
atoms = self.__class__(cell=self._cell, pbc=self._pbc, info=self.info,
                        celldisp=self._celldisp)
```
Note the section when the cell attribute is called in
```python
cell=self._cell
```

Modified to:
```python
atoms = self.__class__(cell=self.cell, pbc=self._pbc, info=self.info,
                        celldisp=self._celldisp)
```
As of now, applying these changes to the cell attribute is enough to allow the codes to run.

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
