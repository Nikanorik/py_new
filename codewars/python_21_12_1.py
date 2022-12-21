def get_grade(s1, s2, s3):
    # Code here
    mid=(s1+s2+s3)/3
    if 0<=mid<60:
        return 'F'
    elif 60<=mid<70:
        return 'D'
    elif 70<=mid<80:
        return 'C'
    elif 80<=mid<90:
        return 'B'
    else:
        return 'A'




get_grade(100, 85, 96)
