# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like
# 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# [
#   "January",
#  "February",
#   "March",
#   "April",
#   "May",
#   "June",
#   "July",
#   "August",
#   "September",
#   "October",
#   "November",
#   "December"
# ]
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    date = input("Date: ").strip().title()

    try:
        if date[0].isdigit():
            mm, dd, yyyy = date.split("/")
            if 1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
                print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                break
        else:
            mm, dd, yyyy = date.split(" ")
            mm = months.index(mm) + 1
            q = len(dd) - 1
            dd = dd[0:q]
            if 1 <= int(mm) <= 12 and 1 <= int(dd) <= 31:
                print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                break
    except:
        print("")
        pass
