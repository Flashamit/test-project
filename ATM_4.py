# An ATM System
print("--------------------------------------------------------------------------")
print("-------------------------Wel Come to Our ATM System-----------------------")
print("--------------------------------------------------------------------------")
print("====Acount Opening Details====")

Balance = 3000 # By default Amount

print("-----Select Language-----")
print(" 1. For English\n", "2. For हिंदी")

Language = int(input("Chose any One ---"))
if Language == 1:
    pin = input("=========Enter Your 4 Digit Pin============")
    if len(pin) == 4:
        print("============Select Option============")
        print(" 1. For Statment\t", "2. For Cash Withdraw\n", "3. For Cash Deposit\t","4 For Pin Change\n") 
        print("----------Chose any One Option---------")
        a = int(input("Enter Here---"))
        if a == 1:
            print(f"Your Balance is --{Balance} Rupees.")
        elif a == 2:
            b = int(input("Enter Withdraw Amount---"))
            due = (Balance - b)
            print(f"Your Bank Balance is --{due}")    
        elif a == 3:
            c = int(input("Enter Deposite Amount---"))
            T = (Balance + c)
        elif a == 4:
            c_pin = input("Enter Your Old Pin---")
            if pin == c_pin:
                i = int(input("Enter New Pin---"))
                j = int(input("Enter Confairm Pin---")) 
                if i==j:
                    print("Pin Save Successfully")
            else:
                print("Your Pin Not Matched! Please Enter Again.")           

elif Language == 2:
    pin = input("=========अपना 4 डिजिट का पिन डाले============")
    if len(pin) == 4:
        print("============निचे दिए गये कोई एक विकल्प चुने============")
        print(" 1. खाते की जानकारी के लिए 1 दबाये\t", "2. पेसे निकलने के लिए 2 दबाये\n", "3. पेसे जमा करने के लिए 3 दबाये\t","4. पिन बदलने के लिए 4 दबाये\n") 
        print("----------कोई एक विकल्प चुने---------")
        a = int(input("यह डाले---"))
        if a == 1:
            print(f"आपके खाते का बैलेंस है---{Balance} रुपे.")
        elif a == 2:
            b = int(input("पेसे निकलने के पेसे डाले---"))
            due = (Balance - b)
            print(f"आपके खाते में बचे हुए पेसे है--{due}")    
        elif a == 3:
            c = int(input("जमा करने वाले पेसे डाले---"))
            T = (Balance + c)
            print("आपके खाते में पेसे जमा हो चुके है अब आपके खाते का बैलेंस है--{T}")
        elif a == 4:
            c_pin = input("अपना पुराने पिन डाले---")
            if pin == c_pin:
                i = int(input("नया पिन डाले---"))
                j = int(input("दुबारा पिन डाले ओर सेव करे---")) 
                if i==j:
                    print("आपका नया पिन सेव कर दिया गया है")
            else:
                print("आपका पिन मेल नही खा रहा है कृपया दुबारा डाले")

else:
    print("Please Select a Vailid Option")            
      