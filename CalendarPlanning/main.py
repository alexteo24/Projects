def computeTimeBetween(firstTime, secondTime):
    """
    Calculates the time in minutes between 2 clock times having the format h:min
    :param firstTime: string, first time for comparison
    :param secondTime: string, second time for comparison
    :return: time in minutes between the 2 given times, or 0 if result would come out as negative
    """
    first_hour = int(firstTime.split(":")[0])
    first_minutes = int(firstTime.split(":")[1])
    second_hour = int(secondTime.split(":")[0])
    second_minutes = int(secondTime.split(":")[1])
    if first_hour < second_hour:
        return (second_hour - first_hour) * 60 + second_minutes - first_minutes
    elif first_hour == second_hour:
        if first_minutes < second_minutes:
            return second_minutes - first_minutes
    return 0


def compareTwoTimes(firstTime, secondTime):
    first_hour = int(firstTime.split(":")[0])
    first_minutes = int(firstTime.split(":")[1])
    second_hour = int(secondTime.split(":")[0])
    second_minutes = int(secondTime.split(":")[1])
    if first_hour < second_hour:
        return True
    if first_hour == second_hour:
        if first_minutes <= second_minutes:
            return True
    return False


if __name__ == "__main__":
    pass
    #  input
    #  booked_calendar1: [['9:00','10:30'], ['12:00','13:00'], ['16:00','18:'00']]
    #  range_limits_calendar1: ['9:00','20:00']
    #  booked_calendar2:  [['10:00','11:30'], ['12:30','14:30'], ['14:30','15:00'], ['16:00','17:00']]
    #  range_limits_calendar2: ['10:00', '18:30']
    #  Meeting Time minutes: 30

    #  Sample output: [['11:30','12:00'], ['15:00', '16:00'], ['18:00':'18:30']
    booked_calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    range_limits_calendar1 = ['9:00', '20:00']
    booked_calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    range_limits_calendar2 = ['10:00', '18:30']
    meeting_time = 30

    #  Merging the two calendars
    booked_calendar_together = booked_calendar1
    booked_calendar_together.extend(booked_calendar2)

    #  Sorting the merged calendar based on starting hour first and then on ending hour
    booked_calendar_together.sort(key=lambda x: (
        int(x[0].split(":")[0]), int(x[0].split(":")[1]), int(x[1].split(":")[0]), int(x[1].split(":")[1])))

    #  Merging the two range limits together
    range_limits_together = range_limits_calendar1
    range_limits_together.extend(range_limits_calendar2)

    #  Sorting the range limits based on hour first and then minutes
    range_limits_together.sort(key=lambda x: (int(x.split(":")[0]), int(x.split(":")[1])))

    #  Keeping only the middle ones, since that will be the range for everyone involved
    range_limits_together = range_limits_together[1:-1]

    available_time = []
    for i in range(0, len(booked_calendar_together) - 1):
        end_time_first_booked_event = booked_calendar_together[i][1]
        start_time_second_booked_event = booked_calendar_together[i + 1][0]
        if computeTimeBetween(end_time_first_booked_event, start_time_second_booked_event) >= meeting_time:
            #  check if there is enough time for the meeting
            if compareTwoTimes(range_limits_together[0], end_time_first_booked_event) and compareTwoTimes(
                    end_time_first_booked_event, range_limits_together[1]):
                #  if the meeting takes place during both people's schedule
                available_time.append([end_time_first_booked_event, start_time_second_booked_event])

    #  Also checking after the last event there is still time left for the meeting for both of them
    end_time_first_booked_event = booked_calendar_together[-1][1]
    end_of_day = range_limits_together[1]

    if computeTimeBetween(end_time_first_booked_event, end_of_day) >= meeting_time:
        #  check if there is enough time for the meeting
        available_time.append([end_time_first_booked_event, end_of_day])
    print(available_time)
