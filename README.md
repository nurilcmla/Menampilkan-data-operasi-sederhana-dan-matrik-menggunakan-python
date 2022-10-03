# Menampilkan-data-operasi-sederhana-dan-matrik-menggunakan-python
#cara menampilkan hasil

m = 10
print(m)
print("hasil m+m = ", m+m)
print("hasil m x m = ", m*m)

print('------------')
kar_1 = 'kenapa harus dia'
kar_2 = 'karena orang lain bukan dia'
print(kar_1+' '+kar_2)
print(kar_1[0:10])
karakter = 'kenapa harus dia karena orang lain bukan dia'
print(karakter.split())

from math import *
#operasi perhitungan sederhana
a = 10
b = -4.5
c = 5.0
d = 5/2

print(a+b)
print("bentuk bilangan integer = ", int(b))
print("bentuk bilangan float = ", float(a))
print("perkalian c x d = ", c*d)

print("------------------")
print("contoh soal = tentukan kecepatan v (W(usaha) = 20; s(waktu)=-10 t(waktu)=2)")
W = 20
s = -10
t = 2
#v = s/t
kecepatan = s/t
print(kecepatan," m/s")

print("------------")
print("soal 1 = tentukan energi dalam J dari m = 9,31x10^-31; c = 3x10^8")
m = 9.31*10**-31
c = 3*10**8
#energi : E = m x c^2
E = m* c**2
print (E)

print("-------------")
print("soal 2 = tentukan periode dalam s (l = 0.5 m ; g = 9.8 m/s^2")
l = 0.5
g = 9.8
#periode = 2 x pi x sqrt (l/g)
periode = 2* pi*sqrt (l/g)
print (periode)

from numpy import *
#menampilkan matrik
M = [[0 ,1 ,1 ,0] , [2,3,2,1]]
print(M)

a = zeros ((3,3),int)
print(a)
print (" ")

a[0] = [1,4,2]
a[1,1] = 9
a[2,0:2] = [9,4]
print (a)

from numpy import array
print(' ')
A = array([[2,3,4],\
     [2,3,4]])
print (A)

import matplotlib.pyplot as plt
from numpy import arange,sin,cos

x = arange(0.0,6.0,0.1)
plt.plot(x, sin(x), 'o-',x,cos(x),'s-')
plt.title('grafik sinusoidal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('sinus','cosinus'),loc = 0)
plt.grid(True)
plt.show()
