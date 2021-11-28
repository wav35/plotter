def plot_state(state: list[list[int]], slope: float, bias: float, expo: int):
    """
    Plots the given state using print statements
    """
    for y_i, ys in enumerate(state):
        for xs in ys:
            char = ""
            if xs == 0:
                char = " "
            elif xs == 1:
                char = "│"
            elif xs == 2:
                char = "─"
            elif xs == 3:
                char = "┼"
            elif xs == 4:
                char = "•"

            print(char, end="")
        if y_i == 0:
            print('Slope: %.2f' % slope, end="")
        elif y_i == 1:
            print('Bias: %.2f' % bias, end="")
        elif y_i == 2:
            print(f'Expo: {expo}', end="")
        print("")

