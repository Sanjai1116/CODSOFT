contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact '{name}' added!")
    
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts saved!")
        else:
            print("\nAll Contacts:")
            for name, details in contacts.items():
                print(f"{name} - {details['phone']}")
    
    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            details = contacts[search_name]
            print(f"\nName: {search_name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
        else:
            print("Contact not found!")
    
    elif choice == "4":
        update_name = input("Enter name to update: ")
        if update_name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[update_name] = {"phone": phone, "email": email, "address": address}
            print(f"Contact '{update_name}' updated!")
        else:
            print("Contact not found!")
    
    elif choice == "5":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact '{delete_name}' deleted!")
        else:
            print("Contact not found!")
    
    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Try again.")