print("Welcome to Amit ATM System")
print("Select the Option \n\n")
print("1. Deposit \t","2. Cash Withdrow \n")

print("3. Show your Pin \t","4. User Details \n\n")

global a

a = 3000# By Defual Amount
data = int(input())
pin = 1997
if data == 1:
    p_1 = int(input("Enter your pin.- "))
    if p_1 == 1997:
        a_1 = int(input("Enter the amount you Dipsite.- "))
        a_2 = a + a_1
        print(f"Your Diposite Amount is {a_1}")
        print(f"Your current Balance is {a_2}")
        print("Thanyou for using ATM machine\n")
        if data == 2:
            p_2 = int(input("Enter your pin.- "))
            if p_2 == 1997:
                b = int(input("Enter Amount.- "))
                b_1 = a - b
                print(f"Your Cash Amount is {b}")
                print(f"Your current Balance is {b_1}")
                print("Thanyou for using ATM machine\n")
elif data == 3:
    print(f"your pin is {pin}")
elif data == 4:
    print("Your Name is Amit\n","your acount Balance is {a}\n","Your ATM pin is {pin}")
                    
else :
    print("Pin is Worngh try Again")  

          

