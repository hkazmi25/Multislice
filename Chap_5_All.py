import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants 
from scipy.special import k0

'''
Atomic Potential from Chap 5 of Krickland for polonium atom
----------------------------------------
'''
a0= 0.529 #in Angstroms
e= 14.4   # Ang. Volts
fig,(ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=1, ncols=5)
a1,a2,a3=1.714e+000,2.141e+000,4.375e+000 # positions of PO atoms
b1,b2,b3= 9.792e+001,2.101e-001,3.669e+000
c1,c2,c3= 2.162e-002,1.97e-001,6.52e-001
d1,d2,d3= 1.984e-002,1.330e-001,7.804e-001
r= np.linspace(0,0.5,100)# in Angstroms 
sum1= 0
sum2 = 0
for (a, b) in zip([a1,a2,a3],[b1,b2,b3]):
    sum1 += (a/r)*np.exp(-2*np.pi*r*np.sqrt(b))
for (c,d) in zip([c1,c2,c3],[d1,d2,d3]):
    sum2 += (c*(d)**-3/2)*np.exp(-1*(np.pi**2)*(r**2)/d)
pot1=2*(np.pi**2)*a0*e*sum1
pot2= 2*(np.pi**5/2)*a0*e*sum2
ptot=pot1+pot2
ax2.plot(r,ptot,'-k')
ax2.set_title("Atomic Potential vs 3D radius of PO atom")
ax2.set_xlabel("radius (in Angstrom)")
ax2.set_ylabel("Atomic potential (in kilovolts)")

'''
Interaction parameter sigma
---------------------------
where 510kev= moC**2 d= speed of light in my case hehe :P 

'''

eV= np.linspace(0,1000,10) #keV

hc=15.7 # Ang. keV
h= 4.135e-18 #keV
me=9.1e-31 # kilogram
lamda = hc/(np.sqrt(eV*(2*510+eV)))
sigma=(2*np.pi*me*lamda)/(h**2)
ax1.plot(eV,sigma)
ax1.set_title("The interaction parameter \u03C3 vs electron kinetic energy")
ax1.set_ylabel("Interaction parameter, in radians/ (kV-Angstroms)")
ax1.set_xlabel("Electron Energy (in keV)")
print (sigma)
'''
Projected Atomic Potential 
--------------------------

when the atomic potential is integrated along z direction (i.e., the optic axis of the microscope)the results is called projected atomic potential
important to note that here it uses the second kind of modified bessal function k0 in "sum3 line"

'''
sum3=0
sum4=0
for (a,b) in zip([a1,a2,a3],[b1,b2,b3]):
    sum3 += a*k0(2*np.pi*r*np.sqrt(b))
for (c,d) in zip([c1,c2,c3],[d1,d2,d3]):
    sum4 += (c/d)*np.exp(-1*(np.pi**2)*(r**2)/d)
pot3= 4*(np.pi)**2*a0*e*sum3
pot4 = 2*(np.pi)**2*a0*e*sum4
pjp= pot3+pot4
ax3.plot(r,pjp, 'r')
ax3.set_title("Proj. Atomic Potential vs 2D radius of PO atom")
ax3.set_ylabel("Proj.Atomic Potential (in volts-Ang)")
ax3.set_xlabel("radius (in Angstroms)")

'''
Scattring Factors
-----------------
'''
q= np.arange(0.0,2.0,0.1)
sf1=0
sf2=0
for (a,b) in zip([a1,a2,a3],[b1,b2,b3]):
    sf1 += a/(q**2+b)
for (c,d) in zip([c1,c2,c3],[d1,d2,d3]): 
    sf2 += c*np.exp(-d*q**2)
tsf= sf1+sf2
ax4.plot(q,tsf,'green')
ax4.set_title("Scattring factor of isolated atom of PO")
ax4.set_ylabel("Scattring factor (in Ang.)")
ax4.set_xlabel("scattring angle (in 1/Ang.)")


'''
Transmission function for single Po atom
-----------------

'''
g=np.arange(0,2,0.1)
T= np.exp(1j*sigma*pjp)
ax5.plot(g,T, 'l')
ax5.set_title("Transmission function for single Po atom")
ax5.set_ylabel("Transmission fucntion (in radian)")
ax5.set_xlabel("radius(in angstrom)")

plt.show()
