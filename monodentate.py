'''
Python script that creates an atomic slab, enumerates the unique adsorption sites via graph theory,
then creates the adsorption mode for a particular adsorption edge.

This script is intended for only monodentate adsorption modes.
'''

from catkit.build import molecule
from catkit.gen.surface import SlabGenerator
from catkit.gen.adsorption import Builder
from ase.build import bulk

# Set the bulk property of the surface, lattice type, lattice constant, etc.
atoms = bulk('Cu', 'fcc', a=3.57, cubic=True)

# If necessary, particular atoms in the phase can be replaced to simulate alloys.
#bulk[3].symbol = 'Pd'

# From the defined bulk phase, create a general slab definition
gen = SlabGenerator(
    atoms,
    miller_index=(1, 1, 1), # Surface termination
    layers=6,               # Thickness of slab in Angstroms
    vacuum=10)              # Thickness of vacuum layer

# From the general slab, extract a defined slab; Number of repetitions can be set via the size tag
slab = gen.get_slab(size=(3,3))

# If necessary (especially for alloys), the unique termination attribute gives the fractional
# coordinate shifts which will result in the unique termination.
#terminations = gen.get_unique_terminations()

# Define adsorbate molecule via chemical symbol as string input. the argument in the square
# brackets defines which graph representation is selected, i.e. whether the H is bonded to
# the C or the O, etc. To browse through the variations, you can print out the full
# molecule representation array.
adsorbate = molecule('HCOOH')[0]
# test = molecule('HCOO')
# print(test)

# Manually set adsorption tags using the array input.
# Length of array must match number of atoms in the adsorbate molecule.
# For this monodentate adsorption case, the atom that is directly bonded to the surface
# needs to have the adsorbate tag set to -1, with the rest of the non-bonding atoms set to 0.
adsorbate.set_tags([0, -1, 0, 0, 0])

# Creation of the adsorption slab with enumerated adsorption sites.
builder = Builder(slab)
# If necessary, printing the builder object will show information on what kind of slab it is,
# number of unique adsorption sites, the site-connectivity for each site, and number of
# unique adsorption edges.
print(builder)

# Finally, creation of the adsorption mode. Selection of which adsorption site to use
# is controlled by the index tag, following the unique sites defined by the Builder module.
ads_slab = builder.add_adsorbate(adsorbate, index=0)

# Call-in 3D visualization of the adsorption mode.
ads_slab.edit()
