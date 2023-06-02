import random

# Constants
desired_alignment = 0  # Desired alignment (in some unit)
sensor_noise = 0.1  # Noise level in the sensor measurement
actuator_noise = 0.05  # Noise level in the actuator movement

def measure_alignment():
    # Simulate sensor measurement with noise
    true_alignment = desired_alignment + random.uniform(-sensor_noise, sensor_noise)
    return true_alignment

def adjust_position(current_alignment):
    # Simulate actuator movement with noise
    control_signal = desired_alignment - current_alignment
    adjusted_position = current_alignment + control_signal + random.uniform(-actuator_noise, actuator_noise)
    return adjusted_position

# Main simulation loop
num_iterations = 10
current_alignment = 0  # Initial alignment
for iteration in range(num_iterations):
    # Measure alignment
    measured_alignment = measure_alignment()

    # Adjust position using control algorithm
    current_alignment = adjust_position(measured_alignment)

    # Print results
    print(f"Iteration {iteration+1}: Measured Alignment = {measured_alignment:.3f}, Adjusted Alignment = {current_alignment:.3f}")
#
# # working
# # This simulation code demonstrates a simplified control system for aligning the capacitor plates. Here's how it works:
# # The measure_alignment() function simulates the sensor measurement by adding random noise to the desired alignment.
# # The adjust_position() function simulates the actuator movement based on the control signal calculated as the diff
# # between the desired alignment and the current alignment.
# # The main simulation loop iterates a specified number of times, where in each iteration, the alignment is measured, and
# # the position is adjusted using the control algorithm.
# # The results of each iteration, including the measured alignment and the adjusted alignment, are printed to the console
# # Note that this is a basic simulation code and does not include advanced control algorithms or real-time interactions
# # with physical hardware. It serves as a starting point for understanding the concept of the control system and can be
# # extended and customized based on your specific requirements and control algorithm implementation.
#
# # Code with grpahics
#
import random
import matplotlib.pyplot as plt

# Constants
desired_alignment = 0  # Desired alignment (in some unit)
sensor_noise = 0.1  # Noise level in the sensor measurement
actuator_noise = 0.05  # Noise level in the actuator movement

def measure_alignment():
    # Simulate sensor measurement with noise
    true_alignment = desired_alignment + random.uniform(-sensor_noise, sensor_noise)
    return true_alignment

def adjust_position(current_alignment):
    # Simulate actuator movement with noise
    control_signal = desired_alignment - current_alignment
    adjusted_position = current_alignment + control_signal + random.uniform(-actuator_noise, actuator_noise)
    return adjusted_position

# Initialize variables
num_iterations = 100
current_alignment = 0  # Initial alignment
iterations = []
measured_alignments = []
adjusted_alignments = []

# Main simulation loop
for iteration in range(num_iterations):
    # Measure alignment
    measured_alignment = measure_alignment()

    # Adjust position using control algorithm
    current_alignment = adjust_position(measured_alignment)

    # Store iteration results
    iterations.append(iteration + 1)
    measured_alignments.append(measured_alignment)
    adjusted_alignments.append(current_alignment)

# Plot results
plt.plot(iterations, measured_alignments, label='Measured Alignment')
plt.plot(iterations, adjusted_alignments, label='Adjusted Alignment')
plt.axhline(y=desired_alignment, color='r', linestyle='--', label='Desired Alignment')
plt.xlabel('Iteration')
plt.ylabel('Alignment')
plt.title('Alignment of Capacitor Plates')
plt.legend()
plt.grid(True)
plt.show()

# code for 3d graphical simulation

import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
desired_alignment = 0  # Desired alignment (in some unit)
sensor_noise = 0.1  # Noise level in the sensor measurement
actuator_noise = 0.05  # Noise level in the actuator movement

def measure_alignment():
    # Simulate sensor measurement with noise
    true_alignment = desired_alignment + random.uniform(-sensor_noise, sensor_noise)
    return true_alignment

def adjust_position(current_alignment):
    # Simulate actuator movement with noise
    control_signal = desired_alignment - current_alignment
    adjusted_position = current_alignment + control_signal + random.uniform(-actuator_noise, actuator_noise)
    return adjusted_position

# Initialize variables
num_iterations = 100
current_alignment = 0  # Initial alignment
measured_alignments = [0]
adjusted_alignments = [0]

# Start the simulation loop
for _ in range(num_iterations):
    # Measure alignment
    measured_alignment = measure_alignment()

    # Adjust position using control algorithm
    current_alignment = adjust_position(measured_alignment)

    # Update plot data
    measured_alignments.append(measured_alignment)
    adjusted_alignments.append(current_alignment)

# Generate 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create time array
t = np.arange(num_iterations + 1)

# Plot measured alignment
ax.plot(t, measured_alignments, t, 'blue')

# Plot adjusted alignment
ax.plot(t, adjusted_alignments, t, 'green')

# Plot desired alignment
ax.plot(t, [desired_alignment] * (num_iterations + 1), t, 'red')

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Alignment')
ax.set_zlabel('Iteration')
ax.set_title('Alignment of Capacitor Plates')

# Show the plot
plt.show()


