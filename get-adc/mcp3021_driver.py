import smbus
import time
class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.adress = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.adress, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"ПРинятые данные: {data}, Старший байт: {upper_data_byte:x}, МЛадший байт: {lower_data_byte:x}, Число: {number}")
        return number
    def get_voltage(self):
        return self.get_number() / 1024 * self.dynamic_range
        
if __name__ == "__main__":
    try:
        mcp = MCP3021(5.18)
       # while True:
        while True:
            volt = mcp.get_voltage()
            print(volt)
            time.sleep(1)
          # print(adc.get_sc_voltage())
    finally:
        mcp.deinit()