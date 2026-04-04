import time

def wait_game():
    print(
        """
        ##################################################################

        Welcome to the Waiting Game!
        
        The goal is to press Enter exactly 4 seconds after the first Enter.
        
        ##################################################################
        """
    )
    print("Press Enter to start the game.")
    input()
    start_time = time.time()
    print("Press Enter again after 4 seconds.")
    input()
    end_time = time.time()
    elapsed_time = end_time - start_time

    target_time = 4.0
    difference = elapsed_time - target_time

    if difference == 0:
        print("Perfect!")
    elif difference < 0:
        print(f"You were {abs(difference):.2f} seconds too early.")
    else:
        print(f"You were {difference:.2f} seconds too late.")

if __name__ == "__main__":
    wait_game()