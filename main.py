def add_contact(nameToPhone):
    name = input("Enter name : ")
    phone = input("Enter phone number : ")
    nameToPhone[name] = phone

def query_phone(nameToPhone):
    name = input("Enter name : ")
    if name not in nameToPhone.keys():
        print(f"{name} not found in contacts")
        return
    print(f"{name}'s phone number is {nameToPhone[name]}")

def list_contacts(nameToPhone):
    names = sorted(nameToPhone.keys())
    for name in names:
        print(name," <--> ",nameToPhone[name])


validInputs = ["add","query","list","exit"]
assiociatedActions = [add_contact,query_phone,list_contacts]

def getValidCommand():
    userInput = input(f"Enter one of these commands : {validInputs}\n")
    if userInput in validInputs:
        return userInput
    else:
        print("unknown command")
        return getValidCommand()


def main():
    nameToPhone = {}
    while True:
        usrInput = getValidCommand()
        if usrInput == "exit":
            break
        assiociatedActions[validInputs.index(usrInput)](nameToPhone)
    return 0

if __name__ == "__main__":
    main()