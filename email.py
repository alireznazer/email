i = 0
name = input("Enter your name:")
namesave = ("ali")
result1 = name == namesave
if result1 is False :
    print("name is True")
elif result1 is True :
    print("pileass triy again")
    while result1 is True :
        result1 = input("Enter your name:") == namesave
        if result1 is True :
            print("pileass triy again")
        if result1 is False :
            print("name is True")
            break
lastname = input("Enter your last name:")
result2 = lastname == name
if lastname != name :
    print("last name is True")
elif result2 is True :
    while result2 is True :
        if result2 is True :
            print("last name is False ")
            lastname = input("Enter your last name:") == name
            if lastname is True :
                print("last name is False")
            if lastname is False :
                print("last name is True")
                break

print("Entekhab = 1 ta 100")
age = int(input("Enter your age:"))
if age<100 :
    print(True)
elif age >100 :
    print("age is False")
    while age >100 :
        print("Entekhab = 1 ta 100")
        age = int(input("Enter your age:"))
        if age>100 :
            print("False"'\n' "Pileass triy again")
        if age < 100 :
            print(True)
            break


        
no = "no"
yes = "yes"
print("entekhab = yes or no")
result3 = input("are you robat:")
result5 = (result3 == no)
result6 = (result3 == yes)
if result5 is True :
    while result5 is True:
        result7 = input("2+2=") == "4"
        if result7 is False :
            print("pileass triy again")
        if result7 is True :
            email = input("Enter your email:")
            pasword = input("Enter your pasword:")
            result4= input("Enter your pasword:") == pasword
            if result4 is True :
                    print("pasword is True")
                    print("your eamil :",email,"@gmail.com")
                    print("your pasword:",pasword)
                    print("welcom" , name,lastname.lower())
            elif result4 is False :
                while result4 is False and i<3 :
                    if result4 is False :
                        print("paswor is False" '\n' "pileass triy again")
                        result4 = input("Enter your pasword:") == pasword
                        i = i+1
                    if result4 is True :
                        print("pasword is True")
                        print("your eamil =",email,"@gmail.com")
                        print("your pasword =",pasword)
                        print("welcom" , name,lastname.lower())
                        break
            break
        
        
if result6 is True :
    print("you cant open an account")
    
elif (result5 and result6) is False :
    while(result5 or result6) is False :
        print("entekhab is False"'\n'"entekhab = yes or no")
        result3 = input("are you robat:")
        result5 = (result3 == no)
        result6 = (result3 == yes)
        if result6 is True :
            print("you cany open an account!")
                    
        if result5 is True :
            while result5 is True :
                result7 = input("2+2=") == "4"
                if result7 is False :
                    print("pileass triy again")
                if result7 is True :
                    email = input("Enter your email:")
                    pasword = input("Enter your pasword:")
                    result4= input("Enter your pasword:") == pasword
                    if result4 is True :
                        print("pasword is True")
                        print("your eamil :",email,"@gmail.com")
                        print("your pasword:",pasword)
                        print("welcom" , name,lastname.lower())
                    elif result4 is False :
                        while result4 is False and i<3:
                            if result4 is False :
                                print("pasword is False" '\n' "pileass triy again")
                                result4 = input("Enter your pasword:") == pasword
                                i = i+1
                            if result4 is True :
                                print("pasword is True")
                                print("your eamil =",emai,"@gmail.com")
                                print("your pasword =",pasword)
                                print ("welcom",name,lastname.lower())
                        break
                 
                break           
            

            















    

            
          
              
