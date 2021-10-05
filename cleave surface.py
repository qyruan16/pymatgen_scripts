# Cleave LiFePO4-(001)

from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.adsorption import plot_slab
from pymatgen.core.surface import SlabGenerator
from matplotlib import pyplot as plt
from pymatgen.io.vasp.inputs import Poscar

mpr = MPRester()
LiPO4 = mpr.get_materials_ids("LiPO4")

struct = mpr.get_structure_by_material_id(LiPO4[0])
slab = SlabGenerator(struct, (0, 0, 1), 10, 15, center_slab=True)


for n, slabs in enumerate(slab.get_slabs(bonds = {('P', 'O'): 3})):
    # slabs.make_supercell([[1, 0, 0],
    #                       [0, 1, 0],
    #                       [0, 0, 1]])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plot_slab(slabs, ax, adsorption_sites=True)
    plt.savefig(str(n) + '-LiFePO4-001.png', format='png')
    open('POSCAR-LiPO4-' + str(n), 'w').write(str(Poscar(slabs)))

# More complicated supercell
# slabs.make_supercell([[1,1,0],
#                       [2,1,0],
#                       [0,0,1]])