from genetic import genetic
from nonGenetic import NGA

def start():

    choice = input("Enter 1 for non-genetic or 2 for genetic: ")
    choice = int(choice)
    if choice == 1:
        NGA()
    elif choice == 2:
        genetic()
    else:
        print("Invalid choice.")
    # genetic()

start()