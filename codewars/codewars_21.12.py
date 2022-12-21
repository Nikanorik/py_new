def quarter_of(month):
    # your code here
    month_list=[1,2,3,4,5,6,7,8,9,10,11,12]
    if month in month_list[1:4]:
        return 1
    elif month in month_list[4:7]:
        return 2
    elif month in month_list[7:10]:
        return 3
    else:
        return 4



quarter_of(2)