from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter
from matplotlib import *

# with MPRester() as mpr:
#     structure = mpr.get_structure_by_material_id("mp-23")
#     dos = mpr.get_dos_by_material_id("mp-23")
#     bandstructure = mpr.get_bandstructure_by_material_id("mp-23")
#     data = mpr.get_data("Al2O3")
#     energies = mpr.get_data("Al2O3", "energy")


# Entries are containers for calculated information, which is used in many analyses

with MPRester() as mpr:
    mp_entries = mpr.get_entries_in_chemsys(["Li", "Fe", "O"])
    
len(mp_entries)

phase_diagram = PhaseDiagram(mp_entries)
#plotter = PDPlotter(phase_diagram, show_unstable=10, markersize=20, backend="matplotlib")
plotter = PDPlotter(phase_diagram, backend="matplotlib")
plotter.get_plot(label_unstable=False).show()