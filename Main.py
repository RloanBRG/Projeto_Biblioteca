def menu():
    while True:
        print("")
        print("----Main Menu----")
        print(f"\non going on making a menu to exit press 0 on the keyborad")

        option = int(input("Select a option: "))

        if option == 0:
            print("bye")
            break


menu()

print("hello")
