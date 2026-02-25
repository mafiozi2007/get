import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 1000, 3.290, True)

        start = time.time()

        while True:
            current = time.time() - start
            dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, current)*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()