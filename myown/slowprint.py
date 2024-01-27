from time import sleep
from random import randrange

# Prints chars to the console continuously in pseudo-natural intervals
def print_slow(text, pause1 = 10, pause2 = 25, special_pause = 30, special_pause2 = 55):
    for char in text:
        sleep(randrange(pause1, pause2)/100)
        
        print(char, end="", flush=True)
        
        if char in (',', '.', '<', '>', '?', '!', ':', ';',
        '[', ']', '-', '_', '=', '+', '@', '#', '$', '%', '^',
        '&', '*', '(', ')', '/'):
            sleep(randrange(special_pause, special_pause2)/100)

if __name__ == "__main__":
    while 1:    
        with open("newhitchhikers.txt", "r") as f:
            one = int(input("First: "))
            two = int(input("Second: "))
            third = int(input("Third: "))
            fourth = int(input("Fourth: "))

            while 1:    
                print_slow(f.readline(), one, two, third, fourth)
        
    # input = input("Input: ")
    # for i in range(50):
    #     print("\n")
    # print_slow(input)
