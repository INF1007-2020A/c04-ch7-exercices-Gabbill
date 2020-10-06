#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
from sys.path(1,"C:\Users\gabri\PycharmProjects\c04-ch6-exercices-Gabbill")
from exercice2 import frequence

#a)

# TODO: Définissez vos fonction ici
def volume_elypsoide(a=2,b=3,c=1,p=4):
    volume=(4/3)*math.pi*a*b*c
    mass = p * volume
    return volume, mass

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(volume_elypsoide())
    pass
