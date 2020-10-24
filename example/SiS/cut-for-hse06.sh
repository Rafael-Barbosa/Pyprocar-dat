#!/bin/bash

#Informe o corte no k-point

for KPRO in PROCAR1 PROCAR2 PROCAR3 ; 
do
  NUMa=$(grep -n "k-point   17 :" $KPRO | cut -d ':' -f 1)
  NUMa1=$(bc <<< $NUMa-1)
  sed -i "4,$NUMa1 d" $KPRO
done

