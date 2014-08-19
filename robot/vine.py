from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def  go():
  moved=0
  while touch() == "fruit":
    move()
    moved = moved+1
    
    turn (-1)
    if touch() == "fruit":
      go()
      turn(2)
      if touch() == "fruit":
        go()
        
      turn(1)
      for i in range (0,moved):
        move()
        turn (2)
        
go()
