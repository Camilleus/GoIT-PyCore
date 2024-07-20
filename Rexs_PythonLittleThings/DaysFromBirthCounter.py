import datetime
import math


def days_from_date():
    while True:
        def count_leap_years(year):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 1
            else:
                return 0

        BD = input("What is your Birthdate? (yyyy/mm/dd)")
        date_obj = datetime.datetime.strptime(BD, '%Y/%m/%d')

        def time_since(date_obj):
            now = datetime.datetime.now()
            delta = now - date_obj

            years = (math.floor(now.year - date_obj.year))
            leap_years = sum(count_leap_years(year)
                             for year in range(date_obj.year, now.year))
            total_days = delta.days + leap_years

            months = now.month - date_obj.month
            days = delta.days - years * 365 - leap_years
            if months < 0:
                months += 12
                years -= 1
            if days < 0 or days > 31:
                days = days = delta.days - years * 365 - leap_years
                if days > 31:
                    days = delta.days - years * 365 - leap_years - months*30
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            return years, months, days, hours, minutes, seconds

        years, months, days, hours, minutes, seconds = time_since(date_obj)
        formatted_date_obj = date_obj.strftime("%d %B, %Y, %H:%M:%S")
        print(f"From {formatted_date_obj} passed: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
        answer = input("Do you want to try once again? ")
        if answer.lower() in ["no", "non", "n"]:
            break

        def get_days_from_today(date):
            now = datetime.now().date()
            parts = date.split('-')
            the_date = datetime(int(parts[0]), int(
                parts[1]), int(parts[2])).date()
            return (now - the_date).days


if __name__ == "__main__":
    days_from_date()

"""
#ITS FIRST VERSION OF IT    
def time_since(BD):
    delta = datetime.now() - date_obj
    return delta

time_elapsed = time_since(BD)
print(f"From {BD} passed: {time_elapsed.days} days.")
print(f"From {BD} passed: {time_elapsed.days/30} months.")
print(f"From {BD} passed: {time_elapsed.days/365} years.")
"""
