# Initial thickness of the paper in millimeters
initial_thickness = 0.08

# Number of folds
folds = 43

# Thickness after 43 folds (2^folds times the initial thickness)
final_thickness = initial_thickness * (2 ** folds)

# Print the result in millimeters
print(f"The thickness of the paper after {folds} folds is {final_thickness} millimeters.")
# Initial thickness of the paper in mill
# Initial thickness of the paper in millimeters
initial_thickness = 0.08  # 0.08 mm

# Number of folds
folds = 43

# Calculate the thickness using exponentiation
final_thickness = initial_thickness * (2 ** folds)

# Display the result
print(f"The thickness of the paper after {folds} folds is {final_thickness} millimeters.")
# Initial thickness of the paper in millimeters
initial_thickness = 0.08  # 0.08 mm

# Number of folds
folds = 43

# Start with the initial thickness
final_thickness = initial_thickness

# Use a for loop to double the thickness for each fold
for _ in range(folds):
    final_thickness *= 2  # Double the thickness

# Display the result
print(f"The thickness of the paper after {folds} folds is {final_thickness} millimeters.")
import time

# Initial thickness of the paper in millimeters
initial_thickness = 0.08  # 0.08 mm
folds = 43

# Method 1: Using a for loop
start_time_loop = time.time()  # Record start time
final_thickness_loop = initial_thickness
for _ in range(folds):
    final_thickness_loop *= 2  # Double the thickness
end_time_loop = time.time()  # Record end time

# Method 2: Using the arithmetic exponentiation operator
start_time_exponentiation = time.time()  # Record start time
final_thickness_exponentiation = initial_thickness * (2 ** folds)
end_time_exponentiation = time.time()  # Record end time

# Calculate elapsed times
time_loop = end_time_loop - start_time_loop
time_exponentiation = end_time_exponentiation - start_time_exponentiation

# Print the results
print(f"Thickness using the for loop: {final_thickness_loop} mm")
print(f"Thickness using the exponentiation operator: {final_thickness_exponentiation} mm")
print(f"Time taken using the for loop: {time_loop:.10f} seconds")
print(f"Time taken using the exponentiation operator: {time_exponentiation:.10f} seconds")
def confirm_values():
    # Create an empty list
    values_list = []
    
    # Add 44 values to the list (can be any values, here we'll use numbers from 1 to 44)
    for i in range(1, 45):  # Range is from 1 to 44, inclusive
        values_list.append(i)
    
    # Check if the list has exactly 44 values
    if len(values_list) == 44:
        print(f"Success: The list contains {len(values_list)} values.")
    else:
        print(f"Error: The list contains {len(values_list)} values, not 44.")

# Call the function to test
confirm_values()
import matplotlib.pyplot as plt

def confirm_values_and_plot():
    # Create an empty list
    values_list = []
    
    # Add 44 values to the list (here we use numbers from 1 to 44)
    for i in range(1, 45):  # Range is from 1 to 44
        values_list.append(i)
    
    # Check if the list has exactly 44 values
    if len(values_list) == 44:
        print(f"Success: The list contains {len(values_list)} values.")
    else:
        print(f"Error: The list contains {len(values_list)} values, not 44.")
    
    # Plot the values using Matplotlib
    plt.plot(values_list, marker='o', linestyle='-', color='b')  # Line plot with markers
    plt.title("Plot of 44 Values")  # Title of the graph
    plt.xlabel("Index")  # X-axis label
    plt.ylabel("Value")  # Y-axis label
    plt.grid(True)  # Enable grid
    plt.show()  # Display the plot

# Call the function to test and plot
confirm_values_and_plot()
import matplotlib.pyplot as plt

def plot_thickness_log_scale():
    # Calculate the thickness values
    initial_thickness = 0.1  # in millimeters
    thickness_list = [initial_thickness * (2 ** i) for i in range(44)]

    plt.figure(figsize=(10, 6))
    plt.plot(range(44), thickness_list, marker='o', linestyle='-', color='b', label='Thickness')
    plt.yscale('log')  # Logarithmic scale for better readability
    plt.title("Paper Thickness Growth (Logarithmic Scale)")
    plt.xlabel("Number of Folds")
    plt.ylabel("Thickness (mm)")
    plt.grid(True, which="both", linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

plot_thickness_log_scale()
def plot_thickness_bar_chart():
    # Calculate the thickness values
    initial_thickness = 0.1  # in millimeters
    thickness_list = [initial_thickness * (2 ** i) for i in range(44)]

    plt.figure(figsize=(12, 6))
    plt.bar(range(44), thickness_list, color='skyblue', edgecolor='black')
    plt.title("Paper Thickness Growth (Bar Chart)")
    plt.xlabel("Number of Folds")
    plt.ylabel("Thickness (mm)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate each bar with the thickness value
    for i, thickness in enumerate(thickness_list):
        plt.text(i, thickness + 1e6, f"{thickness:.1e}", ha='center', va='bottom', fontsize=8, rotation=90)

    plt.show()

plot_thickness_bar_chart()
def plot_thickness_scatter():
    # Calculate the thickness values
    initial_thickness = 0.1  # in millimeters
    thickness_list = [initial_thickness * (2 ** i) for i in range(44)]

    plt.figure(figsize=(10, 6))
    plt.scatter(range(43), thickness_list[:-1], color='purple', s=100, alpha=0.6, label='Intermediate Values')
    plt.scatter(43, thickness_list[-1], color='red', s=150, label='Final Thickness')  # Highlight the final point
    plt.title("Paper Thickness Growth (Scatter Plot)")
    plt.xlabel("Number of Folds")
    plt.ylabel("Thickness (mm)")
    plt.grid(True)
    plt.legend()
    plt.show()

plot_thickness_scatter()

