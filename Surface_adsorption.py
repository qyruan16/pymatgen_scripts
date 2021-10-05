from pymatgen.core.structure import Structure, Lattice, Molecule
from pymatgen.core.surface import generate_all_slabs
from matplotlib import pyplot as plt
from pymatgen.analysis.adsorption import AdsorbateSiteFinder, plot_slab


fcc_ni = Structure.from_spacegroup("Fm-3m", Lattice.cubic(3.5), ["Ni", "Ni"], [[0, 0, 0], [0.5, 0.5, 0.5]])
slabs = generate_all_slabs(fcc_ni, max_index=1, min_slab_size=8.0, min_vacuum_size=15.0)
ni_111 = [slab for slab in slabs if slab.miller_index==(1,1,1)][0]

asf_ni_111 = AdsorbateSiteFinder(ni_111)
ads_sites = asf_ni_111.find_adsorption_sites()
# print(ads_sites)
assert len(ads_sites) == 4


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plot_slab(ni_111, ax, adsorption_sites=True)
plt.savefig('Ni-111.png', format='png')


# Adding H adsorbate

fig = plt.figure()
ax = fig.add_subplot(111)
adsorbate = Molecule("H", [[0, 0, 0]])
ads_structs = asf_ni_111.generate_adsorption_structures(adsorbate, repeat=[1, 1, 1])
plot_slab(ads_structs[0], ax, adsorption_sites=False, decay=0.09)
plt.savefig('Ni-111-H.png', format='png')


# Other adsorbates
#OH = Molecule("OH", [[0, 0, 0], [-0.793, 0.384, 0.422]])
#O = Molecule("O", [[0, 0, 0]])
#OOH = Molecule("OOH", [[0, 0, 0], [-1.067, -0.403, 0.796], [-0.696, -0.272, 1.706]])
