import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02}:{secs:02}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds




try:
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)
except ValueError:
    print("Please enter a valid number of seconds.")



try:
    total_seconds = int(input("Enter time in seconds: "))
    h, m, s = convert_seconds(total_seconds)
    print(f"{total_seconds} seconds is equal to {h} hour(s), {m} minute(s), and {s} second(s).")
except ValueError:
    print("Please enter a valid number of seconds.")
