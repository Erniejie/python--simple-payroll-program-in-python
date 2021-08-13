#simple payroll program in python
#Computer Tutor Program,Friday 13th,August 2021

def main():

    hrs = float(input("Enter Total Worked Hours:"))
    while hrs < 6 or hrs > 120:
        print("Error - Invalid Entry")
        hrs = float(input("Re-Enter Hours Wroked:"))

    rate = float(input("Enter Hourly Rate [£/h]:"))
    while rate <6 or rate >80:
        print("Error- Pay Rate is between £6 and £80")
        rate = float(input("Re-Enter Hourly Rate [£/h]:"))

    if hrs <= 40:
        print("==========Payroll Information==========")
        print("Pay Rate ,[£/hr]:",format(rate,"8.2f"))
        print("Regular Hours:        ",format(hrs,"2.0f"))
        print("Overtime Hours:        0")
        print("Regular Pay,[£]:",format(hrs*rate,"8.2f"))
        print("Overtime Pay,[£]:    ")
        print("Total Pay,[£]:",format(hrs*rate,"8.2f"))


    else:
        hours = hrs - 40
        pay = hours*(rate*1.5)
        regularpay = 40*rate
        print(" --------Payroll Information--------------")
        print("Pay Rate,[£/hr]:",format(rate,"8.2f"))
        print("Regular Hours:       ",format(hrs,"2.0f"))
        print("Overtime Hours:      ",format(hours,"2.0f"))
        print("Regular Pay,[£]:",format(hrs*rate,"8.2f"))
        print("Overtime Pay,[£]:",format(pay,"8.2f"))
        print("Total Pay,[£]:",format(regularpay + pay,"8.2f"))


main()
        
        
