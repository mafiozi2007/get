import RPi.GPIO as GPIO
import numpy as np
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time =0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21
        self.cur_voltage = 0.0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial =0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio,0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        signal = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, signal)
        return signal
    def sequential_counting_adc(self): 
            for value in range(256):
                signal = self.number_to_dac(value)
                voltage = value / 256 * self.dynamic_range
                self.cur_voltage = voltage
              #  print(value,voltage)
                comparatorvalue = GPIO.input(self.comp_gpio)
                if comparatorvalue == 1:
                    
                    break
                time.sleep(self.compare_time)
            return self.get_sc_voltage()
           # print(value)
    def get_sc_voltage(self):
        return self.cur_voltage
    def successive_approximation_adc(self):
        value = 0
        for i in range(7,-1,-1):
            test_value = value | (1 << i)
        
            self.number_to_dac(test_value)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                value = test_value
        return value
    def get_sart_voltage(self):
        code = self.successive_approximation_adc()
        return (code / 256)*self.dynamic_range

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.13)
       # while True:
        while True:
            u = adc.get_sart_voltage()
            print(u)
            
          # print(adc.get_sc_voltage())
    finally:
        adc.deinit()