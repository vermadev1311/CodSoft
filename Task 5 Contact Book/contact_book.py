import json
import os

CONTACT_FILE = "contacts.json"

# Load existing contacts
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []

# Save updated contact list
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Add new contact
def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']} | {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   Address: {contact['address']}")

# Search by name or phone
def search_contact(contacts):
    keyword = input("Search by name or phone: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print(f"\n✅ Found: {contact['name']} | {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            found = True
    if not found:
        print("❌ No matching contact found.")

# Update contact
def update_contact(contacts):
    search_name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("Leave blank if no change.")
            contact["phone"] = input(f"Phone [{contact['phone']}]: ") or contact["phone"]
            contact["email"] = input(f"Email [{contact['email']}]: ") or contact["email"]
            contact["address"] = input(f"Address [{contact['address']}]: ") or contact["address"]
            save_contacts(contacts)
            print("✅ Contact updated.")
            return
    print("❌ Contact not found.")

# Delete contact
def delete_contact(contacts):
    search_name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == search_name:
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").lower()
            if confirm == "yes":
                contacts.pop(i)
                save_contacts(contacts)
                print("🗑️ Contact deleted.")
            else:
                print("❌ Deletion cancelled.")
            return
    print("❌ Contact not found.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\n====== CONTACT BOOK MENU ======")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
