
print("welcome to the leap year calculator")
year = int(input("enter a year:"))
def is_leap_year():
    global check_leap_year
    year =input("\n enter a year you want to check")
if year % 4 ==0:
    if year % 400 ==0 or year % 100 != 0:
        print( f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



while check_leap_year:

        year = int(input("enter a year to check or (type 0 to exist) :"))
if year ==0:

  print("Quit","quit")

print("Please enter a valid integer year.\n")