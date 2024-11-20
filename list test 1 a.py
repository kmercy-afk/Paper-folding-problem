import matplotlib.pyplot as plt

# Constants
initial_thickness = 0.08 / 1000  # Thickness of a paper in meters (0.08 mm)
num_folds = 43

# List to store thickness after each fold
thickness_values = [initial_thickness]

# Calculate thickness values for each fold
for fold in range(1, num_folds + 1):
    new_thickness = thickness_values[-1] * 2
    thickness_values.append(new_thickness)

# Print the final thickness
final_thickness = thickness_values[-1]
print(f"Final thickness after {num_folds} folds: {final_thickness:.2e} meters")

# Plotting the process values
plt.figure(figsize=(10, 6))
plt.plot(range(num_folds + 1), thickness_values, marker='o')
plt.title("Thickness of Paper after Each Fold")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness (meters)")
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt

# Function to calculate thickness values
def calculate_thickness(initial_thickness, num_folds):
    thickness_values = [initial_thickness]
    for _ in range(num_folds):
        thickness_values.append(thickness_values[-1] * 2)
    return thickness_values

# Function to check the length of the list
def check_length(thickness_list):
    return len(thickness_list)

# Constants
initial_thickness = 0.08 / 1000  # Initial thickness in meters (0.08 mm)
num_folds = 43

# Calculate thickness values
thickness_values = calculate_thickness(initial_thickness, num_folds)

# Verify the length of the list
list_length = check_length(thickness_values)
print(f"Number of values stored in the list: {list_length}")

# Ensure the length is 44
if list_length == 44:
    print("The list correctly contains 44 values.")
else:
    print("Error: The list does not contain 44 values.")

# Print the final thickness
final_thickness = thickness_values[-1]
print(f"Final thickness after {num_folds} folds: {final_thickness:.2e} meters")

# Plot the thickness values
plt.figure(figsize=(10, 6))
plt.plot(range(list_length), thickness_values, marker='o')
plt.title("Thickness of Paper after Each Fold")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness (meters)")
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt

# Function to calculate thickness values
def calculate_thickness(initial_thickness, num_folds):
    thickness_values = [initial_thickness]
    for _ in range(num_folds):
        thickness_values.append(thickness_values[-1] * 2)
    return thickness_values

# Constants
initial_thickness = 0.08 / 1000  # Initial thickness in meters (0.08 mm)
num_folds = 43

# Calculate thickness values
thickness_values = calculate_thickness(initial_thickness, num_folds)
folds = range(len(thickness_values))

# Customized Graph 1: Green line, thicker line
plt.figure(figsize=(10, 6))
plt.plot(folds, thickness_values, color='green', linewidth=2.5, marker='o')
plt.title("Thickness of Paper after Each Fold (Green, Thick Line)", fontsize=16)
plt.xlabel("Number of Folds", fontsize=14)
plt.ylabel("Thickness (meters)", fontsize=14)
plt.grid(True)
plt.show()

# Customized Graph 2: Purple, dotted line
plt.figure(figsize=(10, 6))
plt.plot(folds, thickness_values, color='purple', linestyle='dotted', linewidth=2, marker='o')
plt.title("Thickness of Paper after Each Fold (Purple, Dotted Line)", fontsize=16)
plt.xlabel("Number of Folds", fontsize=14)
plt.ylabel("Thickness (meters)", fontsize=14)
plt.grid(True)
plt.show()

# Customized Graph 3: Orange line with larger font size for axis labels
plt.figure(figsize=(10, 6))
plt.plot(folds, thickness_values, color='orange', linewidth=2, marker='o')
plt.title("Thickness of Paper after Each Fold (Orange, Large Font)", fontsize=18)
plt.xlabel("Number of Folds", fontsize=16)
plt.ylabel("Thickness (meters)", fontsize=16)
plt.grid(True)
plt.show()
