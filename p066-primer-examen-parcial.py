## Objetivo: Programa para administrar la venta de boletos de un cine
## Nombre del Alumno: Erik Alberto Jacobo Delgado
## Matrícula: 38191485
## Materia: Computación Aplicada
## Examen: Primer Parcial

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera_edad = 0
total_academicos = 0
total_hombres = 0
total_mujeres = 0
total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos = 0.0
ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    edad = int(input('Edad del comprador: '))
    tipo_comprador = input('Tipo de boleto (E) Estudiante, (A) Adulto, (T) Tercera edad o (X) Académico: ')
    sexo = input('Sexo (H) Hombre o (M) Mujer: ')
    
    # --- 2. Validación de Edad (Clasificación B) ---
    if edad > 13:
        if tipo_comprador == 'e' or tipo_comprador == 'E':
            total_estudiantes = total_estudiantes + 1
            ingresos_estudiantes = ingresos_estudiantes + PRECIO_ESTUDIANTE
            if sexo == 'h' or sexo == 'H':
                total_hombres = total_hombres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Estudiante \nSexo: Hombre")
            elif sexo == 'm' or sexo == 'M':
                total_mujeres = total_mujeres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Estudiante \nSexo: Mujer")
                          
        elif tipo_comprador == 'a' or tipo_comprador == 'A':
            total_adultos = total_adultos + 1
            ingresos_adultos = ingresos_adultos + PRECIO_ADULTO
            if sexo == 'h' or sexo == 'H':
                total_hombres = total_hombres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Adulto \nSexo: Hombre")
            else:
                total_mujeres = total_mujeres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Adulto \nSexo: Mujer")

        elif tipo_comprador == 'T' or tipo_comprador == 't':
            total_tercera_edad = total_tercera_edad + 1
            ingresos_tercera_edad = ingresos_tercera_edad + PRECIO_TERCERA_EDAD
            if sexo == 'h' or sexo == 'H':
                total_hombres = total_hombres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Tercera edad \nSexo: Hombre")
            else:
                total_mujeres = total_mujeres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Tercera edad \nSexo: Mujer")

        else:
            total_academicos = total_academicos + 1
            ingresos_academicos = ingresos_academicos + PRECIO_ACADEMICO
            if sexo == 'h' or sexo == 'H':
                total_hombres = total_hombres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Académico \nSexo: Hombre")
            else:
                total_mujeres = total_mujeres + 1
                print(f"¡Bienvenido(a)! Venta registrada: \nEdad: {edad} \nTipo de comprador: Académico \nSexo: Mujer")

        # --- 3. Actualización de Estadísticas Generales ---
        total_asistentes = total_asistentes + 1
        suma_edades = suma_edades + edad

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        ingresos_totales = ingresos_estudiantes + ingresos_adultos + ingresos_tercera_edad + ingresos_academicos

    else:
        total_rechazados = total_rechazados + 1
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
promedio_edad = 0
if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes 


# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
print(f'Total de estudiantes: {total_estudiantes}')
print(f'Total de adultos: {total_adultos}')
print(f'Total de tercera edad: {total_tercera_edad}')
print(f'Total académicos: {total_academicos}')
print(f'\nTotal hombres: {total_hombres}')
print(f'Total mujeres: {total_mujeres}')
print(f'\nTotal de asistentes: {total_asistentes}')
print(f'Promedio de edad de asistentes: {promedio_edad}')
print(f'Personas rechazadas por edad: {total_rechazados}')
 
print("\n--- Reporte de Ingresos ---")
print(f'Ingresos por estudiantes: {ingresos_estudiantes}')
print(f'Ingresos por adultos: {ingresos_adultos}')
print(f'Ingresos por tercera edad: {ingresos_tercera_edad}')
print(f'Ingresos por académicos: {ingresos_academicos}')
print(f'\nTOTAL RECAUDADO: {ingresos_totales}')

print("\n--- Rentabilidad ---")

# --- 7. Mensaje de Rentabilidad ---
if ingresos_totales < 1500:
    print('La función generó BAJAS ganancias')
elif ingresos_totales >= 1500 and ingresos_totales <= 3500:
    print('La función generó ganancias MODERADAS')
else:
    print('La función generó BUENAS ganancias')


"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

Primero preguntaría al usuario que día de la semana es y en base a eso con una estructura if-elif-else el programa evaluaría si hace un descuento o no.
La pregunta la haría desde el inicio del programa, cuando estoy recopilando los datos como la edad, sexo y tipo de boleto.
Crearía una constante que sea descuento = PRECIO_ADULTO * 0.20.
El if lo incluiría, en este código en específico, dentro del elif de la linea 58 ya que ahí se esta trabajando con el tipo de boleto de Adulto,
y lo pondría antes del contador de ingresos_adultos para que cuente ahora con el precio con descuento.
El if sería algo asi:
if dia == 'm' or dia == 'M':
    PRECIO_ADULTO = PRECIO_ADULTO - descuento
De este modo el precio pasa de ser de 90 a 78 y el contador en lugar de sumarle 90 al acumulado le sumaria solo 78.


2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

Primero revisaria caso por caso que me este haciendo la suma de los acumulados de forma correcta,
por ejemplo en el if de la linea 48 reviaria que el contador total_estudiantes este bien redactado y funcionado correctamente
para despues pasarme al contador ingresos_estudiantes, ya que primero estaría revisando que se este acumulando de forma correcta el total de estudiantes
para despues resvisar que se este sumando de forma correcta la nueva venta con el acumulado que ya existe.
Repetiría esto para todos los contadores de tipo de boleto y acumuladores de ventas.
Y por ultimo simplemente iría a la linea 93, que es donde realizo la suma de los totales, a verificar que esten todas las variables correctas.

"""