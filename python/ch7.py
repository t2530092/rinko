index_number = input("Which practice do you want to select?")
if index_number == "7.1":
    #p7.1
    car_name = input("what kind of car do you want to rent?")
    print(f"Let me see if i can finnd you a {car_name}.")

elif index_number == "7.2":
    #p7.2
    count = input("how many people will come for dinner?")
    int_count = int(count)
    if int_count <= 8:
            print("I will deal with it.")
    else:
            print("We don't have any more tables.")

elif index_number == "7.3":
        str_number = input("input a number")
        int_number = int(str_number)
        if int_number % 10 == 0:
            print("〇")
        else:
            print("X")
else:
      print(f"{index_number} is not a correct index")



