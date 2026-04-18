# Contact Book App

# 1. Load contacts from JSON file
# 2. Save contacts to JSON file
# 3. Add a new contact
# 4. View all contacts
# 5. Search for a contact
# 6. Update a contact
# 7. Delete a contact
# 8. Main menu

import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_password():
    password = input("Set a password for your contact book: ")
    hashed = hash_password(password)
    with open('password.json', 'w') as f:
        json.dump({"password": hashed}, f)
    print("Password set successfully!!")

def check_password():
    try:
        with open('password.json', 'r') as f:
            stored = json.load(f)
        password = input("Enter password: ")
        if hash_password(password) == stored["password"]:
            return True
        else:
            print("Wrong password!!")
            return False
    except FileNotFoundError:
        set_password()
        return True

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save contacts to JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ")
    existing = [contact for contact in contacts if contact['name'].lower() == name.lower()]
    
    if len(existing) > 0:
        print("Contact already exists!!")
    else:
        phone = input("Enter phone: ")
        if len(phone) == 10 and phone.isdigit():
            email = input("Enter email: ")
            new_contact = {"name": name, "phone": phone, "email": email}
            contacts.append(new_contact)
            save_contacts(contacts)
            print("Contact added successfully!!")
        else:
            print("Invalid phone number!! Must be 10 digits!!")

def view_contacts():
    contacts = load_contacts()
    contacts = sorted(contacts, key=lambda x: x['name'])
    if len(contacts) == 0:
        print("No contacts found!!")
    else:
        print(f"Total number of contacts: {len(contacts)}")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    contacts = load_contacts()
    search = input("Enter name or phone to search: ")
    found_contacts = [contact for contact in contacts if 
                      contact['name'].lower() == search.lower() 
                      or contact['phone'] == search]
    if len(found_contacts) == 0:
        print("Contact not found!!")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    save_contacts(contacts)
    print("Contact deleted successfully!!")

def update_contact():
    contacts = load_contacts()
    name = input("Enter name of contact to update: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details:")
            phone = input("Enter phone: ")
            if len(phone) == 10 and phone.isdigit():
                contact['phone'] = phone
                contact['email'] = input("Enter email: ")
                found = True
            else:
                print("Invalid phone number!!")
            break
    if not found:
        print("Contact not found!!")
    else:
        save_contacts(contacts)
        print("Contact updated successfully!!")
        
def main():
    
    while True:
        print("\n📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice!!")

main()