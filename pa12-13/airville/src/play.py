# Kevin Nash (kjn33)
# EECS 293
# Assignment 12

from gamestate import GSM

if __name__ == "__main__":
    
    gsm = GSM()    
    
    gsm.setup()
    
    # Simulate the game
    while True:
        gsm.tick()
