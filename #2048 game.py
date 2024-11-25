#2048 game
import random
grid = [
    0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000, 0000,
]

playing = True
def four_by_four_grid():
        print(grid[0:4])
        print(grid[4:8])
        print(grid[8:12])
        print(grid[12:16])
    
def numb_posiction():
    grid[random.choice(range(0,16))] = 2 
    global x
    x = grid.index(2)
    index = int(x)
    print(index)
    return index

     

def player_input(x):
    
        
    while playing:
        
        input_ = str(input("Chose your move: ")).lower()
        if input_ != "a" and input_ != "w" and input_ != "d" and input_ != "s":
            print("invalid code")
            continue
        if input_ == "a":
            index = grid[x-16]
            
            
           
        if input_ == "w":
            pass
        if input_ == "s":
            pass
        if input_ == "d":
            pass
            
            
        


def main():
    four_by_four_grid()
    print("Game starts")
    numb_posiction()
    four_by_four_grid()
    player_input(numb_posiction)
    

    
    
    

if __name__ == "__main__":
    main()
    