import mcp4725_driver as mcp4
import signal_generator as sg
import time


amplitude = 3.2
signal_frequency = 50
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        mcp = mcp4.MCP4725(5.0)

        start = time.time()

        while True:
            current = time.time() - start
            mcp.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, current)*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        mcp.deinit()