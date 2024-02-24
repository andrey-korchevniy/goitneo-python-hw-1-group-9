from datetime import date, timedelta

users = [
    {"name": "Bill1 Gates", "birthday": date(1955, 2, 24)},
    {"name": "Bill2 Gates", "birthday": date(1979, 2, 25)},
    {"name": "Bill3 Gates", "birthday": date(1996, 2, 25)},
    {"name": "Bill4 Gates", "birthday": date(1982, 2, 28)},
    {"name": "Bill5 Gates", "birthday": date(1999, 3, 2)},
    {"name": "Bill6 Gates", "birthday": date(1994, 12, 11)},
    {"name": "Bill7 Gates", "birthday": date(1982, 10, 15)},
    {"name": "Bill8 Gates", "birthday": date(1993, 5, 3)},
]

WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DELTA_MAP = {'Monday': 5, 'Sunday': 6}
BLUE = '\033[94m'
ENDC = '\033[0m'


def get_birthdays_per_week(users):
    
    if not users or len(users) == 0:
        return([])
    
    this_week_birthdays = {}
    current_date = date.today()
    current_week_day = current_date.strftime("%A")
    delta = DELTA_MAP.get(current_week_day, 7)
    
    time_delta = timedelta(days = delta)
    
    for user in users:
        birthday = user["birthday"]
        birthday_this_year = birthday.replace(year=current_date.year)
        
        if (birthday_this_year - current_date) > time_delta:
            continue
        
        birtday_week_day = birthday_this_year.strftime('%A')
        
        if (birtday_week_day == 'Saturday' or birtday_week_day == "Sunday"): 
            birtday_week_day = 'Monday'
        
        if birtday_week_day in this_week_birthdays:
            this_week_birthdays[birtday_week_day].append(user["name"])
        else:
            this_week_birthdays[birtday_week_day] = [user["name"]]
        
    sorted_birthdays = {day: this_week_birthdays[day] for day in WEEK_DAYS if day in this_week_birthdays}
    
    for day, values in sorted_birthdays.items():
        print(f"{BLUE}{day:<9}{ENDC}: {', '.join(values)}")


if __name__ == '__main__':
    get_birthdays_per_week(users)