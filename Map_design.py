import numpy as np

# Select map parameters
# Size of map
map = 10
total_map_blocks = map ** 2
# Start of the map
start = np.array([500, 500])  
# Size of the walls
wall = 100

upper_map_walls = np.zeros((map,4))
left_map_walls = np.zeros((total_map_blocks,4))
right_map_walls = np.zeros((total_map_blocks,4))
bottom_map_walls = np.zeros((total_map_blocks,4))


i = 0 
j = 0 
ij = 0


# Creates the map -> Don't know how it is possible to read te map. Now it is 
# all in a x * 4 matrix (point 1 to point 2). 
while i < total_map_blocks:

    start = np.array([start[0]+wall * j,start[1]])
    if i < map: 
        upper_map_walls[i,0:4] =    [start[0],start[1],start[0] + wall,start[1]]    
        
    left_map_walls[i,0:4] =         [start[0],start[1],start[0],start[1] + wall]
    right_map_walls[i,0:4] =        [start[0] + wall,start[1],start[0] + wall,start[1] + wall]
    bottom_map_walls[i,0:4] =       [start[0],start[1] + wall, start[0] + wall,start[1] + wall]

    
    i = i + 1 
    j = 1
    ij = ij + 1
    if ij == map:
            ij = ij - map
            start = np.array([start[0] - (map - 1) * wall,start[1] + wall])
            j = j - 1
                


            
            
            