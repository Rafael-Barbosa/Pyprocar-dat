import pyprocar

pyprocar.bandsplot(
procarfile="PROCAR",
mode="scatter",
atoms=[0], #Si
#orbitals=[4, 5, 6, 7, 8],
fermi=0.0,
show = False,
nbands=24,
)

