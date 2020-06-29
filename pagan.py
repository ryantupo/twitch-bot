








    
#boardT  = ['_0_','_1_','_2_',
#           '_3_','_4_','_5_',
#            _6_','_7_','_8_'



# 012 , 345, 678 - landscape wins
# 036 , 147 , 258 - portrait wins
# 048 ,642 - diagonal wins

def win_clause(boardT):
#---------------------------------------------------------------------------    
    #landscape wins
    
    #top wins
    if((boardT[0] == "X") and (boardT[1] == "X") and (boardT[2] == "X")):
        print("X won")
        state = True
        return state
        
    elif((boardT[0] == "O") and (boardT[1] == "O") and (boardT[2] == "O")):
        print("O won")
        state = True
        return state
        

    #middle wins
    elif((boardT[3] == "X") and (boardT[4] == "X") and (boardT[5] == "X")):
        print("X won")
        state = True
        return state
        
    elif((boardT[3] == "O") and (boardT[4] == "O") and (boardT[5] == "O")):
        print("O won")
        state = True
        return state
        

    #bottom wins
    elif((boardT[6] == "X") and (boardT[7] == "X") and (boardT[8] == "X")):
        print("X won")
        state = True
        return state
        
    elif((boardT[6] == "O") and (boardT[7] == "O") and (boardT[8] == "O")):
        print("O won")
        state = True
        return state
        
#---------------------------------------------------------------------------
    #portrait wins
        
    #left wins
    elif((boardT[3] == "X") and (boardT[4] == "X") and (boardT[5] == "X")):
        print("X won")
        state = True
        return state
        
    elif((boardT[3] == "O") and (boardT[4] == "O") and (boardT[5] == "O")):
        print("O won")
        state = True
        return state
       

    
    #middle wins
    elif((boardT[1] == "X") and (boardT[4] == "X") and (boardT[7] == "X")):
        print("X won")
        state = True
        return state
  
    elif((boardT[1] == "O") and (boardT[4] == "O") and (boardT[7] == "O")):
        print("O won")
        state = True
        return state
      
    
    #right wins
    elif((boardT[2] == "X") and (boardT[5] == "X") and (boardT[8] == "X")):
        print("X won")
        state = True
        return state
    
    elif((boardT[2] == "O") and (boardT[5] == "O") and (boardT[8] == "O")):
        print("O won")
        state = True
        return state
    

#---------------------------------------------------------------------------
    #diagonal wins
    
    #left top bottom down
    elif((boardT[0] == "X") and (boardT[4] == "X") and (boardT[8] == "X")):
        print("X won")
        state = True
        return state
    
    elif((boardT[0] == "O") and (boardT[4] == "O") and (boardT[8] == "O")):
        print("O won")
        state = True
        return state



    #bottom left top right
    elif((boardT[6] == "X") and (boardT[4] == "X") and (boardT[2] == "X")):
        print("X won")
        state = True
        return state
    
    elif((boardT[6] == "O") and (boardT[4] == "O") and (boardT[2] == "O")):
        print("O won")
        state = True
        return state
  

#--------------------------------------------------------------------------
    else:
        print("no one won")
        print((boardT[0] == "X") , " " , (boardT[1] == "X") , " " , (boardT[2] == "X"))
        return False



    
    







# 3 lists




boardT  = ['_','_','_',
            '_','_','_',
            '_','_','_']
            

#boardT  = ['_0_','_1_','_2_',
#           '_3_','_4_','_5_',
#            _6_','_7_','_8_'

def board_print():
    
    print("|"+boardT[0]+"|"+boardT[1]+"|"+boardT[2]+"|")
    print("|"+boardT[3]+"|"+boardT[4]+"|"+boardT[5]+"|")
    print("|"+boardT[6]+"|"+boardT[7]+"|"+boardT[8]+"|")



win =(False)
def choose_X(x_entry):
    while(win == False):
        board_print()
        
        while True:
            try:
                x_entry = int(input("which space you want? (first)" ))
                if((x_entry >= 0) and (x_entry<= 8) and (boardT[x_entry] !="X") and (boardT[x_entry] !="O")):
                    boardT[x_entry]=("X")
                    win_clause(boardT)
                    break
                elif(boardT[x_entry] == "X" or boardT[x_entry] == "O"):
                    print("space already held try again")
                    x_entry = int(input("which space you want?(second)" ))
                    continue
            except:
                print("invalid entry try again")
               
                continue

    
                
              
    
    board_print()

    while True:
        try:
            O_entry = int(input("which space you want? (first)" ))
            if((O_entry >= 0) and (O_entry<= 8) and (boardT[O_entry] !="X") and (boardT[O_entry] !="O")):
                boardT[O_entry]=("O")
                win_clause(boardT)
                break
            elif(boardT[O_entry] == "X" or boardT[O_entry] == "O"):
                print("space already held try again")
                O_entry = int(input("which space you want?(second)" ))
                continue

        except:
            print("invalid entry try again")
           
            continue

    board_print()
    print()
    print()
