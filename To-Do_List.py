with open("list.txt", "a") as f:
    pass


def main_menu():
    print("To-Do List | Main menu\n\n" \
    "a) Add Item\n" \
    "b) View Items\n" \
    "c) Remove Item")


def add_item():
    add_item_input = input("Enter item to add to To-Do list: ")
    with open("list.txt", "a") as f:
        f.write("# " + add_item_input + "\n")

def view_item():
    with open("list.txt") as f:
        print(f"{f.read()}")

def remove_item():
    while True:
        print("\nRemove Options:")
        print("a) Delete a specific item")
        print("b) Clear entire list")
        print("c) Return to main menu")

        choice = input("Choose either option a, b or c: ")

        if choice == "a":
            item_to_remove = input("Enter exact item name to remove: ")

            with open("list.txt", "r") as f:
                items = f.readlines()

            found = False
            with open("list.txt", "w") as f:
                for item in items:
                    if item.strip() != f"# {item_to_remove}":
                        f.write(item)
                    else:
                        found = True
            
            if found:
                print(f"Item '{item_to_remove}' removed from list.")
            else:
                print(f"Item '{item_to_remove}' not found.")
                retry = input("Try again (y/n): ")
                if retry.lower() == "y":
                    continue
                else:
                    break
            
        elif choice == "b":
            open("list.txt", "w").close()
            print("List Cleared")
            break

        elif choice == "c":
            break
            
        else:
            print("Invalid input")


main_menu()

user_input = input("Choose either a, b, or c quit: ")


while user_input != "quit":
    if user_input == "a" or user_input == "b" or user_input == "c":
        if user_input == "a":
            add_item()
        elif user_input == "b":
            print("\nItems in List")
            view_item()
        elif user_input == "c":
            print("\n")
            remove_item()

        user_input = input("\nChoose either a, b, c or quit: ")
            
    else:
        print("Invalid Input!\n")
        main_menu()
        user_input = input("\nChoose either a, b, c or quit: ")   