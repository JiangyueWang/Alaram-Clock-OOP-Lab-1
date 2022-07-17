from datetime import datetime


class AlarmClock:

    def __init__(self):
        self.current_time = datetime.now()
        self.alarm_time = ""
        self.alarm_on = True

    # print current time
    def display_current_time(self):
        print(f'current time is {self.current_time}')

    # turn on/off the alarm
    def toggle_alarm(self, alarm_on):
        if self.alarm_on == alarm_on:
            self.user_decision_set_alarm_time = input(
                "Alarm is on, would you like to set an alarm time, Eneter y/n: ").lower()
            if self.user_decision_set_alarm_time == "y":
                self.user_set_alarm_time = input(
                    "Please eneter an alarm time: ")
                self.set_alarm_time(self.user_set_alarm_time)
            else:
                print("You alarm is on but no alarm time has set yet")
        else:
            print("You have turn off the alaram")
            self.alarm_on == alarm_on

    # set the alarm time
    def set_alarm_time(self, alarm_time):
        self.alarm_time = alarm_time
        print(f'you have set the alarm time as {alarm_time}')
