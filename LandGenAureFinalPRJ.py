#CS115 Vinci Jahniel Aure
import numpy as np 
import time
import random
import sys
import os

"""
Things that helped me: 
https://youtu.be/4GuAV1PnurU?si=hAcLoOMtfHeDkvzk
https://youtube.com/shorts/eKSFV9UuT44?si=07cT0QCplpHnE8KG
https://medium.com/@nickobrien/diamond-square-algorithm-explanation-and-c-implementation-5efa891e486f
I was going to try the tKinter version but looked challenging
"""

def colorize_altitude(val):
    if val < 20:
        return "\033[37;44m \033[0m"  #dark Blue background with empty space(Deeper water)
    elif val < 25:
        return "\033[44m~\033[0m"    #blue background with squiggly line(Water)
    elif val <= 30:
        return "\033[43m.\033[0m"    #yellow background with period(Sand)
    elif val < 45:
        return "\033[42m^\033[0m"    #green background with ^ (Grass)
    elif val < 70:
        return "\033[30;42m#\033[0m"  #dark green background, black hashtag (Forest)
    elif val < 85: 
        return "\033[37;47m*\033[0m"  #light Gray, hite asterisk (Snow)
    else:
        return "\033[31;41m \033[0m" #red, lava


def print_terrain(terrain):
    """
    display the terrain with colored symbols and clear screen before printing.
    val passed through = terrain: 2D numpy array containing altitude values (floating point values)
    """
    #prints the updates in the top left quadrant (taken from maze/labrynth)
    print("\033[33A",end="\r")
    #os.system('cls' if os.name == 'nt' else 'clear')initially used for testing
    
    #print each row with colored symbols taken from city sim
    for row in terrain:
        print("".join(colorize_altitude(val) for val in row))
    
    #time.sleep(0.001)for testing

def recuralgorithm(terrain, x1, y1, x2, y2, depth, max_depth, magnitude, offset):
    #base case if you cannot recur further(will go out of bounds) or maximum depth is reached, stop recursion
    if (x2 - x1) < 2 or (y2 - y1) < 2 or depth >= max_depth:
        return

    #find center point coordinates xm = x coords middle, ym = y coords middle
    xm = (x1 + x2) // 2
    ym = (y1 + y2) // 2
    """
    calculate current offset range based on depth where if the magnitude is 1, it looks wonky but with
    a higher number than 1, the setting up of the terrain looks better, likewise with depth, if it's too low 
    it will give it a look of only having the corners and mid points setup but the higher number you go
    the more land will be generated
    """
    
    offset_range = offset / (magnitude ** depth)

    #X-step: Calculate center point as average of four corners + random offset
    if terrain[ym, xm] == 0:  #will only set if there's no middle  point value (like actual value not the coordinates)
        corners_avg = (terrain[y1, x1] + terrain[y1, x2] + terrain[y2, x1] + terrain[y2, x2]) / 4.0
        terrain[ym, xm] = corners_avg + random.uniform(-offset_range, offset_range)
        print_terrain(terrain)

    #+-step: Calculate midpoints of edges

    #top midpoint
    #RANDOM.UNIFORM used for a floating point number where if the latter is chosen, it would get rounded up (as far as I understand)
    if terrain[y1, xm] == 0:
        terrain[y1, xm] = (terrain[y1, x1] + terrain[y1, x2] + terrain[ym, xm]) / 3.0 + random.uniform(-offset_range, offset_range)
        print_terrain(terrain)

    #bottom midpoint
    if terrain[y2, xm] == 0:
        terrain[y2, xm] = (terrain[y2, x1] + terrain[y2, x2] + terrain[ym, xm]) / 3.0 + random.uniform(-offset_range, offset_range)
        print_terrain(terrain)

    #left midpoint
    if terrain[ym, x1] == 0:
        terrain[ym, x1] = (terrain[y1, x1] + terrain[y2, x1] + terrain[ym, xm]) / 3.0 + random.uniform(-offset_range, offset_range)
        print_terrain(terrain)

    #right midpoint
    if terrain[ym, x2] == 0:
        terrain[ym, x2] = (terrain[y1, x2] + terrain[y2, x2] + terrain[ym, xm]) / 3.0 + random.uniform(-offset_range, offset_range)
        print_terrain(terrain)

    #passing through the depth so that it could check if the recursive call has recured to X amount of depth
    recuralgorithm(terrain, x1, y1, xm, ym, depth + 1, max_depth, magnitude, offset)  #top-left quadrant
    recuralgorithm(terrain, xm, y1, x2, ym, depth + 1, max_depth, magnitude, offset)  #top-right quadrant
    recuralgorithm(terrain, x1, ym, xm, y2, depth + 1, max_depth, magnitude, offset)  #bottom-left quadrant
    recuralgorithm(terrain, xm, ym, x2, y2, depth + 1, max_depth, magnitude, offset)  #bottom-right quadrant

def main():
    """
    Main function that handles command-line arguments and runs the terrain generation.
        seed: Integer for random number generation
        magnitude: Integer determining how quickly randomness decreases with depth
        depth: Integer specifying the maximum recursion depth
    """
    #Check for command-line arguments
    if len(sys.argv) < 4:
        print("to use: All must be integers like: 7 8 2")
        sys.exit(1)

    try:
        seed = int(sys.argv[1])         #Random seed set
        magnitude = int(sys.argv[2])   #How quickly random offset decreases with depth 
        max_depth = int(sys.argv[3])     #Maximum recursion depth
    except ValueError:
        print("Error: Seed and depth must be integers, and magnitude must be float.")
        sys.exit(1)

    #set random seed for reproducibility
    random.seed(seed)

    #set grid size 
    n = 5
    size = 2 ** n + 1 #33 x 33

    #initial maximum random offset (decided to follow the example in the project write up)
    initial_offset = 16.0

    #initialize terrain with zeros
    #use np.zeros to give values of to all cells as 0
    terrain = np.zeros((size, size), dtype=float)

    #set the four corners to random values
    #0 , 120 - random decision
    terrain[0, 0] = random.randint(0, 120) + random.uniform(-initial_offset, initial_offset) 
    terrain[0, size - 1] = random.randint(0, 120) + random.uniform(-initial_offset, initial_offset)
    terrain[size - 1, 0] = random.randint(0, 120) + random.uniform(-initial_offset, initial_offset)
    terrain[size - 1, size - 1] = random.randint(0, 120) + random.uniform(-initial_offset, initial_offset)

    """ 
    terrain[0,0] = top left
    terrain[0, size -1] = top right
    terrain[size -1 , 0] = bottom left
    terrain[size-1,size-1] = bottomr right
    all will be assigned a random value between 0, 120 but before it gets applied
    the random offset will be applied to it (in this case between-16, 16)
    """
    print_terrain(terrain)
    #run the X+ algorithm, passing the matrix and updating it one quadrant at a time
    recuralgorithm(terrain, 0, 0, size - 1, size - 1, 0, max_depth, magnitude, initial_offset)
    print_terrain(terrain)
    """
    #print(terrain)
    (used to check the values the matrix gets assigned, to determine what my elif statements values will be)

    """


if __name__ == "__main__":
    main()
    