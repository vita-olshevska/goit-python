from datetime import datetime, date, timedelta
from collections import defaultdict

user_list = [
    {"name": "Bill",
     "birthday": datetime(year=1993, month=10, day=2)},
    {"name": "Jill",
     "birthday": datetime(year=1993, month=8, day=22)},
    {"name": "Kim",
     "birthday": datetime(year=1993, month=8, day=21)},
    {"name": "Jan",
     "birthday": datetime(year=1993, month=8, day=25)},
    {"name": "Nick",
     "birthday": datetime(year=1993, month=8, day=23)}
]


def next_monday_date():
    current_date = date.today()
    next_monday = current_date + timedelta(days=-current_date.weekday(), weeks=1)
    # print(next_monday)
    return next_monday


def congratulate(users):
    result = defaultdict(list)
    saturday_date = next_monday_date() - timedelta(days=2)
    next_friday_date = saturday_date + timedelta(days=-1, weeks=1)
    # print(saturday_date, next_friday_date)
    for user in users:
        user_date = date(year=datetime.now().year, month=user["birthday"].month, day=user["birthday"].day)
        if saturday_date <= user_date <= next_friday_date:
            if user_date.weekday() >= 5:
                result["Monday"].append(user["name"])
            else:
                result[user_date.strftime('%A')].append(user["name"])

    for key, val in result.items():
        print(f"{key}: {', '.join(val)}")


congratulate(user_list)
