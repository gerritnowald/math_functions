import numpy as np

V = np.arange(60,220,30)

Tdrink = 40  
Tboil  = 100
Ttab   = 22.5

for Vdrink in V:

    A = np.array([[Tboil,Ttab],[1,1]])
    b = [Tdrink*Vdrink, Vdrink]

    Vboil, Vtab = np.linalg.solve(A, b)

    print(f'{Vdrink} ml = {int(Vboil)} ml kochendes Wasser + {int(Vtab)} ml Leitungswasser')
