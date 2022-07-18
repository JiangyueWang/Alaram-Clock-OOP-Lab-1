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
        if alarm_on == True:
            if self.alarm_time == "":
                self.user_decision_set_alarm_time = input(
                    "Alarm is on, would you like to set an alarm time, Eneter y/n: ").lower()
                alarm_time = input("Enter it now: ")
                self.set_alarm_time(alarm_time)
            else:
                print("You alarm is on but no alarm time has set yet")
        else:
            print("You have turn off the alaram")
            self.alarm_on == alarm_on
            self.alarm_time = ""

    # set the alarm time
    def set_alarm_time(self, alarm_time):
        if self.alarm_on == True:
            self.alarm_time = alarm_time
            print(f'you have set the alarm time as {alarm_time}')
        else:
            print("you need to turn on the alarm")
