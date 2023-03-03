def main():
    age = int(input("What is your age: "))
    print('Your legal status is:' + legalStatus(age))

def legalStatus(age):
    if age >= 35:
        return 'President'
    elif age >= 30:
        return 'Senator'
    elif age >= 21:
        return 'Alcohol'
    elif age >= 18:
        return 'Adult'
    else: return 'Minor'

main()




"""

In the United States, one is assumed to be an adult, when the
age of 18 is reached. However, 21 years are required to
purchase alcohol. 30 years to serve as a Senator, and 35 to
serve as president.
Write the function legal_status(age) which returns one of
the strings 'minor', 'adult', 'alcohol', 'senator', or
'president', depending on the parameter age.
Add the function main() which asks the user for his/her age
and prints out his legal status. The main function should take
care of the input/output while the pure computations should be
left to legal_status. The legal_status on the other hand
should not do any input/output.
This is an example dialog with the program:
>>> main()
What is your age: 20
Your legal status is: adult

"""