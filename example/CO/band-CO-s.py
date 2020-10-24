import pyprocar

pyprocar.bandsplot(
procarfile="PROCAR",
mode="scatter",
atoms=[0,1], #CO
orbitals=[0],#Orbital s
fermi=0.0,
show=False, 
nbands=24, #number bands
)

