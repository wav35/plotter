"""
This program plots equations in the command line.
It takes in an input of:
    - Slope
    - Bias (y-intercept) and
    - Exponential for the `x` term

It will then output a one-time plot or a visualization plot in the terminal
"""

from time import sleep
from populate_state import populate_state
from plot_state import plot_state
from calculate_in_range import calculate_in_range
from constants import SUPERSCRIPTS, HALF_SIZE

while True:
    print('Equation in the form mx + b...')
    slope = float(input('Enter slope (m):           '))
    bias = float(input('Enter bias (b):             '))
    expo = int(input('Enter exponent (default 1): ') or "1")

    print('Plotting the equation: {}x{} {}'.format(
            slope,
            SUPERSCRIPTS[expo],
            bias,
        ),
    )

    show_visualization = False
    while True:
        command = input('See (o)ne time plot, or (v)isualization plot:    ')
        if command == "o":
            show_visualization = False
            break
        elif command == "v":
            show_visualization = True
            break
        else:
            continue

    slope_min_range = slope - 1.5 # Set the range of slope
    slope_max_range = slope + 1.5
    slope_visualization_direction = 1 # 1 means increasing slope, -1 means decreasing slope
    while True:
        if show_visualization:
            # Alter the slope in a range to show how different values
            # affect the graph
            if slope < slope_min_range:
                slope_visualization_direction = 1
            elif slope > slope_max_range:
                slope_visualization_direction = -1

            slope += slope_visualization_direction * 0.02
        # Populate states
        states = populate_state()

        # Calculate values
        calculate_in_range(states, slope, bias, expo, range(-HALF_SIZE, HALF_SIZE + 1))

        # Plot state
        plot_state(states, slope, bias, expo)

        sleep(0.1)

        if not show_visualization:
            break
