import datetime
import os

def set_alarm(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}")
    while True:
        current_time = datetime.datetime.now()
        if(current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute):
            print("WAKE UP!")
            os.system(f"start {sound_file}")
            break

def main():
    alarm_hour = int(input("Enter the hour for the alarm: "))
    alarm_minute = int(input("Enter the minute for the alarm: "))
    alarm_time = datetime.datetime.now()
    alarm_time = alarm_time.replace(hour=alarm_hour, minute=alarm_minute, second=0)
    sound_file = "alarm_sound.mp3"      # replace with your sound file
    set_alarm(alarm_time, sound_file)   
    if__name__=="__main__"
main()