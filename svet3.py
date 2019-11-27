import numpy as np#импортируем библиотеки 
import matplotlib.pyplot as plt
G=6.672*10**(-11)
R=69.6*10**6
c=299792458
M=2*10**30
alpha=(4*G*M)/(R*c**2)
def iskr_okolo_sun(R=69.6*(10**6), t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R*np.sin(t)#Задаем переменную х
    y=R*np.cos(t)#Задаем переменную y
    plt.plot(x,y, color='k')#Создание луча
    plt.plot([R,R], [-5*R,5*R], color='b')
    plt.plot([R,R*(1-5*np.tan(alpha))], [0,5*R], color='g')
    plt.axis('equal')
    plt.show()
iskr_okolo_sun(R=69.6*(10**6), t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции


print (alpha)
R=98789*10**7
c=299792458
M=3.384*10**31
alpha=(4*G*M)/(R*c**2)
def iskr_okolo_psa(R=98789*10**7, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R*np.sin(t)#Задаем переменную х
    y=R*np.cos(t)#Задаем переменную y
    plt.plot(x,y, color='k')#Создание луча
    plt.plot([R,R], [-5*R,5*R], color='y')
    plt.plot([R,R*(1-5*np.tan(alpha))], [0,5*R], color='r')
    plt.axis('equal')
    plt.show()
iskr_okolo_psa(R=98789*10**7, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции


print (alpha)
R=2*10**4
c=299792458
M=2.464*10**31
alpha=(4*G*M)/(R*c**2)
def iskr_okolo_neytronnoy_star(R=2*10**4, t=np.arange(-2*np.pi,2*np.pi,0.1)):#Функция созданиия искревленного луча
    x=R*np.sin(t)#Задаем переменную х
    y=R*np.cos(t)#Задаем переменную y
    plt.plot(x,y, color='k')#Создание луча
    plt.plot([R,R], [-5*R,5*R], color='c')
    plt.plot([R,R*(1-5*np.tan(alpha))], [0,5*R], color='m')
    plt.axis('equal')
    plt.show()
iskr_okolo_neytronnoy_star(R=2*10**4, t=np.arange(-2*np.pi,2*np.pi,0.1))#Вызов функции



