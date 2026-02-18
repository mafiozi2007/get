import RPi.GPIO as GPIO
pins = [22, 27, 17, 26, 25, 21, 20, 16]
pins = list(reversed(pins))
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(pins, GPIO.OUT)

dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"НАпряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    
    return int(voltage / dynamic_range*255)



def number_to_dac(number):
    code = [int(element) for element in bin(number)[2:].zfill(8)]
    GPIO.output((pins), code )
    return 

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число")
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()