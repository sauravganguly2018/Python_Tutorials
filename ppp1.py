# python practice problem 1(easy, 10 points)
# your age in 2090
#
# take age or year of birth as an input from the user and tell them when they turn 100years old.(points)
# Don't use any type of module like datetime or dateutils (5 points). They can then optionally provide a year and
# your program must tell their age in that particular year.(3 points)
#
# you should be handling all sorts of errors like (2 points):
# 1. you are nor yet born
# 2. you seem to be the oldest person alive
# 3. you can also handle any other error if possible!

def age_or_year(age_or_year):
    if age_or_year<=150:
        age=age_or_year
        if age>=0 and age<110:
            y_to_hundred=2021-age+100
            print(f"You become 100 years of age in year {y_to_hundred}")
        elif age<=150:
            y_to_hundred = 2021 - age + 100
            print(f"You seems to be the oldest person alive")
    elif age_or_year<=2021 and age_or_year>=1900:
        y_to_hundred=age_or_year+100
        print(f"You become 100 years of age in year {y_to_hundred}")
    else:
        print("you are not yet born")

    year=int(input("Enter a year in which you want to find your age : "))
    if age_or_year<150:
        age=age_or_year
        y_now=year-2021+age
        print(f"you are {y_now} years of age in {year}")
    elif age_or_year<=2021:
        y_now=year-age_or_year
        print(f"you are {y_now} years of age in {year}")
    else:
        y_now=year-age_or_year
        print(f"you are not yet born but when you will born you will become {y_now} years of age in {year}")

if __name__ == '__main__':
    choice='y'
    while(choice=='y' or choice=='Y'):
        try:
            a_o_y = int(input("Enter your age or year in which you born : "))
            if(a_o_y<0 or a_o_y>150 and a_o_y<1900):
                print("Something wrong with your age or year of birth !\nTry Again !")
                continue
            else:
                age_or_year(a_o_y)
                choice='n'
        except Exception as e:
            print(f"Invalid Input ! because {e}\nTry again !")
            continue
