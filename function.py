#def luas_segi4(p,l):
    #luas_segi4 = p * l
    #print(luas_segi4)


#p_input = int(input("Panjang: "))
#l_input = int(input("Lebar: "))

#luas_segi4(p_input, l_input)
print("YOUR SALARY\n–––––––––––––––––––––––")
name = input("Enter your name: ")
def gaji(work_hour, salary_hour):
    if work_hour <= 40:
        gaji = work_hour * salary_hour
    else:
        gaji = work_hour * salary_hour + 500
    print(f"–––––––––––––––––––––––\nHey {name}, this is your salary: {gaji}")

work_hour_input = int(input("Enter your working hour: "))
salary_hour_input = int(input("Enter your rate per hour: "))
gaji(work_hour_input, salary_hour_input)

print("Have a nice day!")
