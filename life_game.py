import numpy as np
import sys, argparse
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N,N)

def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                    [255, 0, 255],
                    [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
# grid = np.zeros(N*N).reshape(N, N)
# addGlider(1, 1, grid)

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum using toroidal boundary conditions
            # x and y wrap around so that the simulation
            
            total = int((grid[i, (j-1)%N]+grid[i, (j+1)%N]+
                        grid[(i-1)%N, j]+grid[(i+1)%N, j]+
                        grid[(i-1)%N, (j-1)%N]+grid[(i-1)%N, (j+1)%N]+
                        grid[(i+1)%N, (j-1)%N]+ grid[(i+1)%N, (j+1)%N])/255)
            
            if grid[i, j] == ON:
                if(total<2) or (total>3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
            
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# command line argumentss are in sys.argv[1], sys.argv[2], ...
# sys.argv[0] is the script name and can be ignored
def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    args = parser.parse_args()#args=['--grid-size', '50', '--glider']
    N = 100
    if args.N and int(args.N)>8:
        N = int(args.N)

    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
    
    grid = np.array([])
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    
    else:
        grid = randomGrid(N)
        
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N,),
                                frames=10,
                                interval=updateInterval,
                                save_count=50)
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    
    plt.show()

if __name__ == '__main__':
    main()
