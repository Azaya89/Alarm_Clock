import sys
import re
from tkinter import *
from datetime import datetime
import time
import winsound


def main():
    """Main function that runs the script."""
    clock.mainloop()


def set_alarm(alarm_time):
    """Sets the alarm time and prints a result when it matches the current time."""
    # Print current time:
    print(f"Current time is: {current_time()}")
    # Print the set alarm time:
    print(f"Alarm will go off by: {alarm_time}")
    # Create a while loop that runs until the alarm time matches the current time.
    while True:
        # Delay the start of the loop for half a second.
        time.sleep(0.5)
        if alarm_time == current_time():
            print("It's time to wake up!")
            winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
            break
        else:
            pass


def current_time():
    """Gets the current time from the datetime module."""
    local_time = datetime.now()
    string_time = local_time.strftime("%H:%M:%S")
    # Return the local time in string format
    return string_time


def alarm_time():
    """Validates the user input."""
    # Convert user input to ALL CAPS
    alarm = f"{hr.get()}:{mins.get()} {per.get()}"
    t = alarm.upper()
    # Match the user input if it's in the time format, HH:MM AM|PM
    matches = re.search(r"^([0-9]|[0-1][0-2])\:([0-9]|[0-5][0-9]) (AM|PM)$", t)
    if matches:
        # Minutes is integers between 0 and 59
        minutes = int(matches.group(2))
        # Check if set period is AM and convert Hour to 24 hour format
        if matches.group(3) == "AM":
            if int(matches.group(1)) < 12:
                hour = int(matches.group(1))
            elif int(matches.group(1)) == 12:
                hour = int(matches.group(1)) - 12
        # Check if set period is PM and convert hour to 24 hour format
        elif matches.group(3) == "PM":
            if int(matches.group(1)) < 12:
                hour = int(matches.group(1)) + 12
            elif int(matches.group(1)) == 12:
                hour = int(matches.group(1))
        # Convert time to double integer string format
        time = f"{hour:02}:{minutes:02}:{0:02}"
    else:
        sys.exit("Invalid time format.")

    set_alarm(time)


clock = Tk()

clock.title("Azaya Alarm Clock")
clock.geometry("400x200")
time_format = Label(
    clock, text="Enter time in 12 hour format.", fg="blue", font=("Arial", 14, "bold")
).place(x=60, y=120)
addTime = Label(clock, text="Hr  Min   AM|PM", font=60).place(x=120)
setAlarm = Label(
    clock, text="Alarm time:", fg="blue", font=("Arial", 12, "bold")
).place(x=0, y=30)

# The Variables we require to set the alarm(initialization):
hr = StringVar()
mins = StringVar()
per = StringVar()
# Time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hr, border=4, width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=mins, border=4, width=15).place(x=150, y=30)
day = Entry(clock, textvariable=per, border=4, width=15).place(x=200, y=30)

# Take the time input by user:
submit = Button(
    clock,
    text="Set Alarm",
    font=("Arial", 12, "bold"),
    fg="green",
    width=10,
    justify="center",
    command=alarm_time,
).place(x=110, y=70)


# Call the main function to run the script
if __name__ == "__main__":
    main()
