# Python program to display calendar of given month of the year

# import module
import calendar
import datetime
import test

yy = 2019
mm = 8

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
# print(calendar.month(yy, mm))

datesOfMonth = calendar.Calendar().monthdatescalendar(yy, mm)
for datesrow in datesOfMonth:
    for dates in datesrow:
        # format_str = '%Y-%m-%d'  # The format
        # datetime_obj = datetime.datetime.strptime(dates, format_str)
        # print(datetime_obj)
        if dates.month == mm:
            DateString = str(dates.day) + "/" + str(dates.month) + "/" + str(dates.year)
            # print("%s/%s/%s" % (dates.day,dates.month, dates.year))
            print(DateString)
            test.timesheet_Fill(DateString)
    # print("\n")
