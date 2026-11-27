# # ATM SIMULATOR

#User_Details = [name, passwd, balance]
User_Details = []
name = input("Enter Your Name : ")
User_Details.append(name)
passwd = int(input("Enter Your Pin : "))
User_Details.append(passwd)
User_Details.append(sum(ord(ASCII) for ASCII in name))

menu = ["1) check Balance", "2) Deposite Money", "3) Transfer Money", "4) Exit"]
print("Hello ", User_Details[0])

while True:
    print(menu)
    user_input_2 = int(input("Choose one Option : "))

    match user_input_2:
        case 1:
            Attempt = 0   #number of Attempts
            Prompt = ["Enter Pin : ", "Incorrect Pin Enter Pin : ", "Incorrect Pin Final Attempt Enter Pin : "]

            while Attempt < 3:  #using while loop finalizing number of attempts
                user_input = int(input(Prompt[Attempt]))  #Taking user input as integer
                if user_input == User_Details[1]:
                    print(User_Details[2])
                break
            Attempt += 1
        case 2:
            print("Currently This Option is Unavailable")
        case 3:
            UPI_IDs = ["okhdfcbank", "okicici", "oksbi", "okaxis", "ybl", "ibl", "axl", "ptaxis", "ptyes", "ptsbi", "pthdfc", "upi", "apl", "yapl", "rapl", "axisb", "yescred", "yescurie", "waicici", "icici", "kotak", "kotak811", "barodampay", "airtel", "jupiteraxis", "fifederal", "naviaxis", "tapicici", "fkaxis", "sliceaxis", "slicepay", "slc", "fam", "yesfam", "inhdfc", "abfspay", "freecharge", "ikwik", "jio", "sbi", "pnb", "cnrb", "boi"]
            UPI_ID = input("Enter UPI ID : ").strip().lower()
            parts = UPI_ID.split("@", 1)
            if len(parts) == 2 and parts[0].isdigit() and 1 <= len(parts[0]) <= 10:
                if parts[1] in UPI_IDs:

                    if UPI_ID == True:
                        Transaction_Amount = float(input("Enter Amount : "))
                        if Transaction_Amount > User_Details[2]:
                            print("Transaction Failed Enter Valid Amount")
                        else:
                            User_Details[2] = User_Details[2] - Transaction_Amount
                            print("Transaction Successful")
                            print("Your currnt balance is : ", User_Details[2])
                    else:
                        print("Enter Valid UPI ID")
        case 4:
            print("Thank You Visit Again")
            break
        case _:
            print("invalid Option")
        