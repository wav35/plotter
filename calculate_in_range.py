from constants import HALF_SIZE

def calculate_in_range(states: list[list[int]], slope: float, bias: float, expo: int, numrange: range):
    """
    Calculates distinct values for given slope, bias and expo and then sets those values in state
    """
    for x in numrange:
        y = (x ** expo * slope) + bias
        
        # We only want the half value because the coordinate plane has both -x and +x
        true_x = round(HALF_SIZE + x) 
        true_y = round(int(HALF_SIZE / 2) - y)

        if true_x < 0 or true_y < 0:
            # We overflowed. This means we were limited by the x or y axis
            continue

        if true_y > len(states) -1 or true_x > len(states[true_y]) - 1:
            #  We can't plot it since it's out of bounds
            continue
        states[true_y][true_x] = 4 # 4 means the dot symbol

