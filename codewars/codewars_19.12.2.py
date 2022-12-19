def bouncing_ball(h, bounce, window):
    # your code
    b=h*bounce
    if h>0 and 0< bounce <1 and window<h:
        count=0
        while b>window:
            count+=1
            b=b*bounce
        amount = 1+ count*2
        print(amount)
    else:
        print(-1)






bouncing_ball(2, 0.5, 1)