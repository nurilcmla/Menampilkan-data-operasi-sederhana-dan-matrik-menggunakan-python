import numpy as np

#Gunakan oerasi perhitungan fisika matematika untuk menghitung jarak fokus lensa (f)ndalam cm pada persamaan pembuat lensa 1/f = (n-1)[1/R1+1/R2] dengan indek  n bias medium
n = 1.50
R1 = 20 
R2 = 18 
F = (n-1)*(1/R1+1/R2)
f = 1/F

print(f)
