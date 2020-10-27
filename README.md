# Pyprocar-dat

O Pyprocar-dat é uma extensão do pyprocar, para exportar as bandas projetadas em .dat.

Verifique as dependências:

--> Pandas (pip3 install pandas --user)


### Primeiro passo:

Instale o [pyprocar](https://romerogroup.github.io/pyprocar/).

Utilize o pip (para python3)

```sh
$ pip3 install pyprocar --user
```
A seguir:

```sh
$ python3 path-barbosa-pyprocar.py
```
Já está instalado o path.

# Exemplos

```sh
$ cd example/CO
$ python3 band-CO-s.py
```
depois de executado, irá criar um proj.dat, ou seja CO orbital s (terceiro coluna são os valores relativos ao orbital).
Para mais informações de como acessar outros orbitais:
https://romerogroup.github.io/pyprocar/bands.html

```sh
$ cd example/SiS
```
Caso seus PROCAR's estejam em arquivos diferentes, você poderá utilizar o concate.py, ele automaticamente irá ler "#of k-points"
e atualizar o seu valor.

### No entanto se em seus cálculos você estiver utilizando o funcional híbrido, deverá utilizar:

```sh
$ ./cut-for-hse06.sh
```
Depois utilize:

```sh
$ python3 concate.py
```
Ele irá atualizar automaticamente os valores k-points, **no entanto você deverá arrumar**.
Em nosso caso coloque o valor "# of k-points:   **90**         # of bands:  24         # of ions:   2"
em vez de 138.

### Lembrando que isso é apenas para o HSE06.:point_up:

```sh
$ python3 proj-Si.py
```

Projetando assim o átomo Si.:runner:


ESPERO TER AJUDADO!! :bowtie:







