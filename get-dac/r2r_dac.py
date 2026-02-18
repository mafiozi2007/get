import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()
    def set_number(self, number):
        print(number)
        code = [int(element) for element in bin(number)[2:].zfill(8)]
        print(code)
        GPIO.output(self.gpio_bits, code)
        return
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"НАпряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            self.set_number(0)
        num = int(voltage / self.dynamic_range*255)
        self.set_number(num)
        
        return
    
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.145, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Не число")
    finally:
        dac.deinit()