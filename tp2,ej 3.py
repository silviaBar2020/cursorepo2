"""TP 2 Ejercicio 3: Ingresar la longitud del radio de un círculo. Calcular e imprimir:
· La superficie del círculo (Sup = p * r²)
· El perímetro de la circunferencia (Per = p * d)
· La superficie de la esfera (Sup = 4 * p * r²)
· El volumen de la esfera (Vol = 4/3 * p * r³)"""

#programa radio de un circulo
r=int(input("Ingresar la longitud del radio de un circulo:"))
pi=3.14
sup=pi*(r**2)
per=pi*(r*2)
supes=4*pi*(r**2)
vol=4/3*pi*(r**3)
print("La superficie del circulo es",sup)
print("El perimetro del circulo es",per)
print("La superficie de la esfera es",supes)
print("El volumen de la esfera es",vol)



# otra forma de hacerlo
r=int(input("Ingrese el redio del circulo: "))
sup_cir=3.14*r**2
per_circunf=3.14*(r*2)
sup_esf=4*3.14*r**2
vol_esf=4/3*3.14*r**3
print("Superficie del circulo es ",sup_cir,"\nPerimetro de la circunferencia es ",
      per_circunf,"\nSuperficie de la esfera es ",sup_esf,"\nVolumen de la esfera es ",vol_esf)