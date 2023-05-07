while True:
    month_year = input()
    month = int(month_year.split('-')[0])
    year = int(month_year.split('-')[1])

    month_str = ""
    match month:
        case 1:
            month_str = 'January'
        case 2:
            month_str = 'February'
        case 3:
            month_str = 'March'
        case 4:
            month_str = 'April'
        case 5:
            month_str = 'May'
        case 6:
            month_str = 'June'
        case 7:
            month_str = 'July'
        case 8:
            month_str = 'August'
        case 9:
            month_str = 'September'
        case 10:
            month_str = 'October'
        case 11:
            month_str = 'November'
        case 12:
            month_str = 'December'
        case _:
            continue
    break

print("    " + month_str + " " + str(year))
print(" Mo Tu We Th Fr Sa Su")

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days_in_month[1] = 29

if month < 3 :
    m = month + 12
    year = year - 1
else:
    m = month

K = year % 100
J = year // 100

for i in range(1, days_in_month[month - 1] + 1):
    q = i

    h = (q + (13*(m+1)) // 5 + K + K // 4 + J // 4 - 2*J) % 7

    h = (h + 5) % 7

    if i == 1:
        print("   " * h, end = "")

    if(i < 10):
        print(" " + str(i), end = " ")
    else:
        print(str(i), end = " ")
    
    if h == 6:
        print()