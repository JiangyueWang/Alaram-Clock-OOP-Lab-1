from alarm_clock import AlarmClock

alarm_clock_one = AlarmClock()

# display current time of alarm via instance variable and method
print(f'current time is {alarm_clock_one.current_time}')
alarm_clock_one.display_current_time()

# change alarm time
alarm_clock_one.set_alarm_time("14pm")

# turn off the alarm
alarm_clock_one.toggle_alarm(False)

# turn on the alarm and set alarm time
alarm_clock_one.toggle_alarm(True)
