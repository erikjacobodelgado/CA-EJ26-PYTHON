# p006-conversor-temperatura.py
# Convertir temperatura de Celsius a Fahrenheit

print('Conversor de temperatura de °C a °F: \n')
celsius = float(input('Dame la temperatura en grados Celsius: '))
fahrenheit = (celsius * 9 / 5) + 32
print(f'La temperatura en Fahrenheit es: {fahrenheit:.2f}°F')
