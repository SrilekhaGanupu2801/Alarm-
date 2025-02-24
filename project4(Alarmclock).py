import time
import winsound  # For Windows users
# import os  # Uncomment this line if you're using macOS or Linux

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end="\r")  # Overwrite the line
        if current_time == alarm_time:
            print("\nTime to wake up!")
            # For Windows
            winsound.Beep(1000, 10000)  # Beep for 10 seconds
            # For macOS/Linux, you can use:
            # os.system('say "Time to wake up!"')
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock!")
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    try:
        time.strptime(alarm_time, "%H:%M:%S")  # Validate time format
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")

if __name__ == "__main__":
    main()