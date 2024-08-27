def add_contact(name_to_phone):
    name = input("Enter name : ")
    phone = input("Enter phone number : ")
    name_to_phone[name] = phone

def query_phone(name_to_phone):
    name = input("Enter name : ")
    if name not in name_to_phone.keys():
        print(f"{name} not found in contacts")
        return
    print(f"{name}'s phone number is {name_to_phone[name]}")

def list_contacts(name_to_phone):
    names = sorted(name_to_phone.keys())
    for name in names:
        print(name," <--> ", name_to_phone[name])


valid_inputs = ["add", "query", "list", "exit"]
associated_actions = [add_contact, query_phone, list_contacts]

def getValidCommand():
    user_input = input(f"Enter one of these commands : {valid_inputs}\n")
    if user_input in valid_inputs:
        return user_input
    else:
        print("unknown command")
        return getValidCommand()


def main():
    name_to_phone = {}
    while True:
        usr_input = getValidCommand()
        if usr_input == "exit":
            break
        associated_actions[valid_inputs.index(usr_input)](name_to_phone)
    return 0

if __name__ == "__main__":
    main()