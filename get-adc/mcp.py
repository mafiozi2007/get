import mcp3021_driver as MCP
import matplotlib.pyplot as plt
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
mcp = MCP.MCP3021(5.18)
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
        voltage_values.append(mcp.get_voltage()) 
        time_periods.append(abs(last_time-time.time()))
    plot_voltage_vs_time(time_values, voltage_values, 3.3)
    plot_sampling_period_hist(time_periods)
finally:
    mcp.deinit()