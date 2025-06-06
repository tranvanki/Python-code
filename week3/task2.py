import matplotlib.pyplot as plt
import numpy as np

def line_chart(months, racoon_temp, leer_temp):
    plt.figure(figsize=(10, 6))
    plt.plot(months, racoon_temp, marker='o', label='Racoon City')
    plt.plot(months, leer_temp, marker='s', label='Leer City')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Comparison Between Cities')
    plt.grid(True)
    plt.legend()
    plt.show()

def bar_chart(months, racoon_temp, leer_temp):
    plt.figure(figsize=(10, 6))
    x = np.arange(len(months))
    width = 0.35
    
    plt.bar(x - width/2, racoon_temp, width, label='Racoon City')
    plt.bar(x + width/2, leer_temp, width, label='Leer City')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Comparison Between Cities')
    plt.xticks(x, months)
    plt.legend()
    plt.show()

def box_plot(racoon_temp, leer_temp):
    plt.figure(figsize=(8, 6))
    data = [racoon_temp, leer_temp]
    plt.boxplot(data, labels=['Racoon City', 'Leer City'])
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Distribution')
    plt.grid(True)
    plt.show()

def main():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    racoon_temp = [15, 20, 25, 30, 35]  # Racoon City temperatures
    leer_temp = [10, 15, 20, 25, 30]    # Leer City temperatures
    
    line_chart(months, racoon_temp, leer_temp)
    bar_chart(months, racoon_temp, leer_temp)
    box_plot(racoon_temp, leer_temp)

if __name__ == "__main__":
    main()