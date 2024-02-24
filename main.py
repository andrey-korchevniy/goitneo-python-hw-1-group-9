BLUE = '\033[94m'
ENDC = '\033[0m'

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts, is_consent=False):
    try:
        name, phone = args
    except ValueError:
        return "Yhe command is bad. Please try again."
    
    if name in contacts and not is_consent:
        return f"Here is a contact with name {name} yet. To overwrite? Type yes/no: "
    
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Yhe command is bad. Failed to find all the mandatory data."
    
    if name not in contacts:
        return f"There isn't a contacts with name {name}"
    
    contacts[name] = phone
    return 'Contact changed'


def contact_phone(args, contacts):
    try:
        name = args[0]
    except:
        return "The command is bad. Failed to find all the mandatory data."
    
    if name not in contacts:
        return f"There isn't a contacts with name {name}"
    
    return contacts[name]
    

def all_contacts(contacts):
    if not contacts:
        return "No contacts to display."

    max_name_length = max(len(contact) for contact in contacts.keys())
    contact_list = ''
    
    for contact, phone in contacts.items():
        contact_list += f"{BLUE}{contact:<{max_name_length}}{ENDC}: {phone}\n"
    return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            response = add_contact(args, contacts)
            if 'overwrite' in response:
                option = input(response)
                command = parse_input(option)[0]
                print(command)
                if command == 'yes':
                    print(add_contact(args, contacts, True))
                else:
                    print('Saving the contact was cancelled')
            else:
                print(response)
                    
        elif command == 'change':
            print(change_contact(args, contacts))
            
        elif command == 'phone':
            print(contact_phone(args, contacts))
            
        elif command == 'all':
            print(all_contacts(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()