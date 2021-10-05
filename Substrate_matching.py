from pymatgen.core.structure import Structure
from pymatgen.ext.matproj import MPRester
from pymatgen.core.surface import SlabGenerator
from pymatgen.analysis.adsorption import plot_slab
from matplotlib import pyplot as plt
from pymatgen.analysis.interfaces.substrate_analyzer import SubstrateAnalyzer

mpr = MPRester()
mp_id = mpr.get_materials_ids("LiFePO4")
LiFePO4 = mpr.get_structure_by_material_id('mp-19017')
# LiFePO4.add_oxidation_state_by_element({"Fe": 2, "Li": 1, "P": 5, "O": -2})

slabgen = SlabGenerator(LiFePO4, (0, 0, 1), 10, 15, center_slab=True)

slabs = slabgen.get_slabs()

LiFePO4_001 = slabs[0]

for n, slab in enumerate(slabs):
     print(n, "Polar:" ,slab.is_polar(), "Symmetric: ", slab.is_symmetric())

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plot_slab(LiFePO4_001, ax, adsorption_sites = False)

# There will be a bug when display slabs with a site is assigned with an oxidation state.
# Chaning line 716 in analysis\adsorption.py into   color = color_dict[sites[n].element.symbol]  may fix it.
# It seems that this modification doesn't work, so just cancel the oxidation settings above during plotting

ax.set_title ("LiFePO4 (0 0 1) Surface")
ax.set_xticks([])
ax.set_yticks([])
plt.show()

# Epitaxial Matching
silicon = Structure.from_file("Si.cif")
slabgen = SlabGenerator(silicon, (1,1,1), 10, 10)
slabs = slabgen.get_slabs()
print("Number of slabs:", len(slabs))

sub_analyzer = SubstrateAnalyzer()
sub_analyzer.calculate(film=LiFePO4,substrate=silicon)

matches = list(sub_analyzer.calculate(film=LiFePO4,substrate=silicon))
