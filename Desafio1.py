import math

def zetadieta(carbohidratos, proteinas, grasas):
    calorias_banana = 105
    calorias_atun = 120
    calorias_aceite = 9

    gramos_banana = 27
    gramos_atun = 30
    gramos_aceite = 1

    bananas_requeridas = math.ceil(carbohidratos / gramos_banana)
    atun_requerido = math.ceil(proteinas / gramos_atun)

    calorias_totales = (bananas_requeridas * calorias_banana) + (atun_requerido * calorias_atun) + (grasas * calorias_aceite)

    return calorias_totales

carbohidratos = 88
proteinas = 90
grasas = 50

total_calorias = zetadieta(carbohidratos, proteinas, grasas)
print("Total de calorías:", total_calorias)
