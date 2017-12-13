'''
Created on 12/12/2017

@author: 

XXX: https://www.hackerrank.com/challenges/counter-game/problem
'''

import logging

from math import log,floor
from sys import stdin


nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

def reducir(n):
    tiros=1
    while(n>1):
        pot_2_f=log(n,2)
        pot_2_exacta=pot_2_f.is_integer()
        if(pot_2_exacta):
            n>>=1
#            print("n x redu {}".format(n))
        else:
            pot_2=floor(pot_2_f)
            n&=~(1<<pot_2)
#            print("n redu {}".format(n))
        tiros+=1
#    print("tiros {}".format(tiros))
    if tiros&1:
        return "Richard"
    else:
        return "Louise"

if __name__=="__main__":
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    num_casos=int(stdin.readline().strip())
    for _ in range(num_casos):
        caca=int(stdin.readline().strip())
        mierda=reducir(caca)
        print("{}".format(mierda))
