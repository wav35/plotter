from constants import SIZE, HALF_SIZE

def populate_state() -> list[list[int]]:
    """
    Populates thee initial state, ie. sets the initial lines
    """
    x_size = SIZE + 1
    y_size = HALF_SIZE

    x_mid = int(x_size / 2)
    y_mid = int(y_size / 2)

    state_list = []
    for y in range(y_size):
        state_list.append([])
        for x in range(x_size):
            elem = 0 # 0 means 'blank space'
            if y == y_mid and x == x_mid:
                elem = 3 # 3 means '+' symbol
            elif (x % 4 == 0 and y == y_mid) or ((y - 1) % 2 == 0 and x == x_mid):
                elem = 3 # 3 means '+' symbol
            elif y == y_mid:
                elem = 2 # 2 means horizontal line
            elif x == x_mid:
                elem = 1 # 1 means vertical line
            state_list[y].append(elem)
    return state_list

