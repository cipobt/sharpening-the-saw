import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02}:{secs:02}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

try:
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)
except ValueError:
    print("Please enter a valid number of seconds.")
