# En el siguiente renglon llamamos a la funcion que ejecuta el diagnostico inicial
#   from motor_decision.chequeo_inicial import checkout
    #ahora la ejecutamos dentro de main
#   INICIO = checkout()

print ("          ====================  INICIANDO CALCULADORA  ====================")
print ("          ======================= Bienvenid@ Usuari@ ======================")
TipoDeOperacion = int(input  ("""          ====== Seleccione el tipo de operación que desea realizar: 
                    1. Calculos Basicos (Suma, resta, multiplicación y división)
                    2. Calculos Trigonometricos
                    3. Calculos Avanzados
                    """))

from calculadoraB import OperacionesBasicas
from calculadoraT import OperacionesTrigonometricas
from calculadoraE import OperacionesEspeciales

if TipoDeOperacion == 1:

    OperacionesBasicas()

if TipoDeOperacion == 2:
    OperacionesTrigonometricas()

if TipoDeOperacion == 3:
    OperacionesEspeciales()

