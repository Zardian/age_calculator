from datetime import date

name=input("Enter Your Name:\n")
age=input("Enter Your Birth date (dd/mm/yyyy):\n")

u_d,u_m,u_y=age.split("/")
u_y=int(u_y)
u_m=int(u_m)
u_d=int(u_d)

today=str(date.today())
#print("today is",today)

p_y,p_m,p_d=today.split("-")
p_y=int(p_y)
p_m=int(p_m)
p_d=int(p_d)

def is_leap():
    if (year % 4)==0:

        if (year % 100)==0:

            if (year % 400)==0:
                return True

            else:
                return False

        else:
             return True

    else:
        return False

    return True

year=p_y-u_y
month=p_m-u_m
day=p_d-u_d

if u_m>12:
        print("Hey",name,"\nThere are only 12 months in a year")

elif u_y>p_y:
    print("Can't predict future")

else:        
    if u_m>p_m :
        month+=12
        year=year-1

    elif u_m<p_m:
        month-=1

    elif u_m==p_m and u_d>p_d:
        year-=1
        month = 11

    elif u_d>p_d:
        if u_m =='01' or u_m =='03' or u_m =='05' or u_m =='07' or u_m =='08' or u_m =='10' or u_m =='12': 
            day+=31

        elif u_m =='04' or u_m =='06' or u_m =='09' or u_m =='11':  
            day+=30

        elif u_m =='02':
            if is_leap(p_y)==True:
                day+=29

            else:
                day+=28

    print("Hey",name,"\nYou are",year,"years ", month,"months and",day,"days old")
