import matplotlib.pyplot as plt
import r2r_adc
import time
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.title('ГРафик зависимости')
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(time):
    plt.figure(figsize=(10,6))
    plt.hist(time)
    plt.xlim(0,0.06)
    plt.xlabel('ПЕриод измерения, с')
    plt.ylabel('Количество измерений')
    plt.title('Гистограмма')
    plt.grid(True)
    plt.show()
r2r = r2r_adc.R2R_ADC(3.13,compare_time=0.0001)
voltage_values = []
time_values = []
time_periods = []
duration = 3.0
print('Едем')
try:
    start = time.time()
    while time.time() - start < duration:
        last_time = time.time()
        time_values.append(time.time())
        voltage_values.append(r2r.get_sart_voltage()) 
        time_periods.append(abs(last_time-time.time()))
    plot_voltage_vs_time(time_values, voltage_values, 3.3)
    plot_sampling_period_hist(time_periods)
finally:
    r2r.deinit()