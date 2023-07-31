contact = {}
while True:
    choice = int(input("1.add new contact \n 2.search contact \n 3.display contact \n 4.end contact \n 5.delete contact \n 6.exit \n 7.enter your choice"))
if choice == 1:
   name = input("enetr the contact name")
   phone = input("enter the mobile number")
elif choice == 2:
    search_name = input("enter the contact name")
    if search_name in contact:
        print(search_name,"s contact number is",contact[search_name])
    else:
        print("name is not fount in contact book")
elif choice == 3:
    if not contact:
        print("empty contact book")
    else:
        display_contact()
