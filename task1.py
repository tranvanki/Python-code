import numpy as np

def city_climate():
    # Define the average temperatures for each city
    first_city = np.array([15, 20, 25, 30, 35])
    second_city = np.array([10, 15, 20, 25, 30])
    month_name = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    
    print("Average Temperatures for Each City:")
    print("-" * 45)
    print("{:<6} {:<20} {:<20}".format("Month", "Racoon (°C)", "Leer (°C)"))
    print("-" * 45)
    
    for i in range(len(month_name)):
        print("{:<6} {:<20} {:<20}".format(
            month_name[i], 
            str(first_city[i]), 
            str(second_city[i])
        ))

def main():
    city_climate()

if __name__ == "__main__":
    main()