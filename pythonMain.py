import random

grid = [    
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# this generates a random grid position
def random_placement_of_2_or_4_number_each_move():
    global grid
    x_cords = random.randint(0, 3)
    y_cords = random.randint(0, 3)
    # now that we have the position lets make sure we dont spawn the new number in a occupied position
    if grid[x_cords][y_cords] != 0:
        random_placement_of_2_or_4_number_each_move()
    else:
        grid[x_cords][y_cords] = 2

def defeat_checker():
    global grid
    grid_copy = [row[:] for row in grid]  
    for row in grid_copy:
        if 0 in row:
            return False 
    
    # Check for adjacent cells with the same value
    for i in range(3):
        for j in range(3):
            if grid_copy[i][j] == grid_copy[i+1][j] or grid_copy[i][j] == grid_copy[i][j+1]:
                return False  
    
    # Check the last row and column
    for i in range(3):
        if grid_copy[3][i] == grid_copy[3][i+1]:
            return False  
        if grid_copy[i][3] == grid_copy[i+1][3]:
            return False 
            
    return True

def move(direction):
    global grid
    old = [row[:] for row in grid]
    cells_that_already_added = []

    # lets add and move the numbers up!
    if direction == "w":
        while True: 
            for i in range(4):
                if grid[1][i] != 0:
                    if grid[0][i] == 0:
                        grid[0][i] = grid[1][i]
                        grid[1][i] = 0
                    elif grid[1][i] == grid[0][i]:
                        grid[0][i] = grid[0][i] + grid[0][i]
                        grid[1][i] = 0
                        cells_that_already_added.append((0, i))

                if grid[2][i] != 0:
                    if grid[1][i] == 0:
                        grid[1][i] = grid[2][i]
                        grid[2][i] = 0
                        if grid[0][i] == 0:
                            grid[0][i] = grid[1][i]
                            grid[1][i] = 0
                        elif grid[1][i] == grid[0][i]:
                            if (0, i) not in cells_that_already_added:
                                grid[0][i] = grid[0][i] + grid[0][i]
                                grid[1][i] = 0
                                cells_that_already_added.append((0, i))
                    elif grid[2][i] == grid[1][i]:
                        grid[1][i] = grid[1][i] + grid[1][i]
                        grid[2][i] = 0
                
                if grid[3][i] != 0:
                    if grid[2][i] == 0:
                        grid[2][i] = grid[3][i]
                        grid[3][i] = 0
                        if grid[1][i] == 0:
                            grid[1][i] = grid[2][i]
                            grid[2][i] = 0
                            if grid[0][i] == 0:
                                grid[0][i] = grid[1][i]
                                grid[1][i] = 0
                            elif grid[0][i] == grid[1][i]:
                                if (0, i) not in cells_that_already_added:
                                    grid[0][i] = grid[0][i] + grid[0][i]
                                    grid[1][i] = 0   
                        elif grid[1][i] == grid[2][i]:
                            if (1, i) not in cells_that_already_added:
                                grid[1][i] = grid[1][i] + grid[1][i]
                                grid[2][i] = 0  
                    elif grid[3][i] == grid[2][i]:
                        grid[2][i] = grid[2][i] + grid[2][i]
                        grid[3][i] = 0
                        
            # if grid changed add a new number on the board
            if grid != old:
                random_placement_of_2_or_4_number_each_move()
            else:
                print("\nthis move didnt change anything")
            # display the board
            for row in grid:
                print(*row)
            break
    if direction == "s":
        while True:
            # lets add and move the numbers down
            for i in range(3, -1, -1):
                if grid[2][i] != 0:
                    if grid[3][i] == 0:
                        grid[3][i] = grid[2][i]
                        grid[2][i] = 0
                    elif grid[3][i] == grid[2][i] and (3, i) not in cells_that_already_added:
                        grid[3][i] = grid[3][i] + grid[3][i]
                        grid[2][i] = 0
                        cells_that_already_added.append((3, i))

                if grid[1][i] != 0:
                    if grid[2][i] == 0:
                        grid[2][i] = grid[1][i]
                        grid[1][i] = 0
                        if grid[3][i] == 0:
                            grid[3][i] = grid[2][i]
                            grid[2][i] = 0
                        elif grid[3][i] == grid[2][i] and (3, i) not in cells_that_already_added:
                            grid[3][i] = grid[3][i] + grid[3][i]
                            grid[2][i] = 0
                            cells_that_already_added.append((3, i))
                    elif grid[2][i] == grid[1][i] and (2, i) not in cells_that_already_added:
                        grid[2][i] = grid[2][i] + grid[2][i]
                        grid[1][i] = 0
                        cells_that_already_added.append((2, i))

                if grid[0][i] != 0:
                    if grid[1][i] == 0:
                        grid[1][i] = grid[0][i]
                        grid[0][i] = 0
                        if grid[2][i] == 0:
                            grid[2][i] = grid[1][i]
                            grid[1][i] = 0
                            if grid[3][i] == 0:
                                grid[3][i] = grid[2][i]
                                grid[2][i] = 0
                            elif grid[3][i] == grid[2][i] and (3, i) not in cells_that_already_added:
                                grid[3][i] = grid[3][i] + grid[3][i]
                                grid[2][i] = 0
                                cells_that_already_added.append((3, i))
                        elif grid[2][i] == grid[1][i] and (2, i) not in cells_that_already_added:
                            grid[2][i] = grid[2][i] + grid[2][i]
                            grid[1][i] = 0
                            cells_that_already_added.append((2, i))
                    elif grid[1][i] == grid[0][i] and (1, i) not in cells_that_already_added:
                        grid[1][i] = grid[1][i] + grid[1][i]
                        grid[0][i] = 0
                        cells_that_already_added.append((1, i))

            # if grid changed add a new number on the board
            if grid != old:
                random_placement_of_2_or_4_number_each_move()
            else:
                print("\nthis move didn't change anything")
            
            # display the board
            for row in grid:
                print(*row)
            break

    if direction == "d":
        while True:
            # lets add and move the numbers to the right
            for i in range(3, -1, -1):
                if grid[i][2] != 0:
                    if grid[i][3] == 0:
                        grid[i][3] = grid[i][2]
                        grid[i][2] = 0
                    elif grid[i][3] == grid[i][2] and (i, 3) not in cells_that_already_added:
                        grid[i][3] = grid[i][3] + grid[i][3]
                        grid[i][2] = 0
                        cells_that_already_added.append((i, 3))

                if grid[i][1] != 0:
                    if grid[i][2] == 0:
                        grid[i][2] = grid[i][1]
                        grid[i][1] = 0
                        if grid[i][3] == 0:
                            grid[i][3] = grid[i][2]
                            grid[i][2] = 0
                        elif grid[i][3] == grid[i][2] and (i, 3) not in cells_that_already_added:
                            grid[i][3] = grid[i][3] + grid[i][3]
                            grid[i][2] = 0
                            cells_that_already_added.append((i, 3))
                    elif grid[i][2] == grid[i][1] and (i, 2) not in cells_that_already_added:
                        grid[i][2] = grid[i][2] + grid[i][2]
                        grid[i][1] = 0
                        cells_that_already_added.append((i, 2))

                if grid[i][0] != 0:
                    if grid[i][1] == 0:
                        grid[i][1] = grid[i][0]
                        grid[i][0] = 0
                        if grid[i][2] == 0:
                            grid[i][2] = grid[i][1]
                            grid[i][1] = 0
                            if grid[i][3] == 0:
                                grid[i][3] = grid[i][2]
                                grid[i][2] = 0
                            elif grid[i][3] == grid[i][2] and (i, 3) not in cells_that_already_added:
                                grid[i][3] = grid[i][3] + grid[i][3]
                                grid[i][2] = 0
                                cells_that_already_added.append((i, 3))
                        elif grid[i][2] == grid[i][1] and (i, 2) not in cells_that_already_added:
                            grid[i][2] = grid[i][2] + grid[i][2]
                            grid[i][1] = 0
                            cells_that_already_added.append((i, 2))
                    elif grid[i][1] == grid[i][0] and (i, 1) not in cells_that_already_added:
                        grid[i][1] = grid[i][1] + grid[i][1]
                        grid[i][0] = 0
                        cells_that_already_added.append((i, 1))

            # if grid changed add a new number on the board
            if grid != old:
                random_placement_of_2_or_4_number_each_move()
            else:
                print("\nthis move didn't change anything")
            
            # display the board
            for row in grid:
                print(*row)
            break

    if direction == "a":
        while True:
            # lets add and move the numbers to the left
            for i in range(4):
                if grid[i][1] != 0:
                    if grid[i][0] == 0:
                        grid[i][0] = grid[i][1]
                        grid[i][1] = 0
                    elif grid[i][0] == grid[i][1] and (i, 0) not in cells_that_already_added:
                        grid[i][0] = grid[i][0] + grid[i][0]
                        grid[i][1] = 0
                        cells_that_already_added.append((i, 0))

                if grid[i][2] != 0:
                    if grid[i][1] == 0:
                        grid[i][1] = grid[i][2]
                        grid[i][2] = 0
                        if grid[i][0] == 0:
                            grid[i][0] = grid[i][1]
                            grid[i][1] = 0
                        elif grid[i][0] == grid[i][1] and (i, 0) not in cells_that_already_added:
                            grid[i][0] = grid[i][0] + grid[i][0]
                            grid[i][1] = 0
                            cells_that_already_added.append((i, 0))
                    elif grid[i][1] == grid[i][2] and (i, 1) not in cells_that_already_added:
                        grid[i][1] = grid[i][1] + grid[i][1]
                        grid[i][2] = 0
                        cells_that_already_added.append((i, 1))

                if grid[i][3] != 0:
                    if grid[i][2] == 0:
                        grid[i][2] = grid[i][3]
                        grid[i][3] = 0
                        if grid[i][1] == 0:
                            grid[i][1] = grid[i][2]
                            grid[i][2] = 0
                            if grid[i][0] == 0:
                                grid[i][0] = grid[i][1]
                                grid[i][1] = 0
                            elif grid[i][0] == grid[i][1] and (i, 0) not in cells_that_already_added:
                                grid[i][0] = grid[i][0] + grid[i][0]
                                grid[i][1] = 0
                                cells_that_already_added.append((i, 0))
                        elif grid[i][1] == grid[i][2] and (i, 1) not in cells_that_already_added:
                            grid[i][1] = grid[i][1] + grid[i][1]
                            grid[i][2] = 0
                            cells_that_already_added.append((i, 1))
                    elif grid[i][2] == grid[i][3] and (i, 2) not in cells_that_already_added:
                        grid[i][2] = grid[i][2] + grid[i][2]
                        grid[i][3] = 0
                        cells_that_already_added.append((i, 2))

            # if grid changed add a new number on the board
            if grid != old:
                random_placement_of_2_or_4_number_each_move()
            else:
                print("\nthis move didn't change anything")
            
            # display the board
            for row in grid:
                print(*row)
            break
                    
def move_in_what_direction():
    while True:
        try:
            user_response = str(input("(W = up)(A = Left)(S = down)(D = right): ")).lower()
        except:
            print("please only type (W, A, S or D)")
            continue
        if len(user_response) != 1:
            print("please only type (W, A, S or D)")
            continue
        if user_response not in ["w", "a", "s", "d"]:
            print("please only type (W, A, S or D)")
        return user_response

def play_game():
    global grid
    random_placement_of_2_or_4_number_each_move()
    for row in grid:
        print(*row)
    while True:
        direction = move_in_what_direction()
        move(direction)
        if defeat_checker():
            print("YOU LOST, GAME OVER!!!!!!!!!!")
            user_response = input("do you want to play again?: ").lower()
            if user_response in ["y", "yes", "yup", "jes", "yup", "yep", "yessir", "fien"]:
                grid = [    
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]
                main()
            else:
                break

def main():
    play_game()

if __name__ == "__main__":
    main()