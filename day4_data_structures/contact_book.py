# contact_book.py

contacts = {}


def show_menu():
    print("\n📒 Contact Book")
    print("1. Add contact")
    print("2. Search by name")
    print("3. Search by phone")
    print("4. List contacts")
    print("5. Delete contact")
    print("6. Exit")


def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Name is required.")
        return

    if name in contacts:
        choice = input("Contact exists. Overwrite? (y/n): ").lower()
        if choice != "y":
            return

    phone = input("Enter phone: ").strip()
    if not phone:
        print("Phone is required.")
        return

    email = input("Enter email (optional): ").strip()

    tags_input = input("Enter tags separated by commas (optional): ").strip()
    if tags_input:
        tags = set(tag.strip() for tag in tags_input.split(","))
    else:
        tags = set()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": tags
    }

    print("Contact added successfully.")


def search_by_name():
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)

    if not contact:
        print("Contact not found.")
        return

    print_contact(name, contact)


def search_by_phone():
    phone = input("Enter phone to search: ").strip()

    for name, data in contacts.items():
        if data.get("phone") == phone:
            print_contact(name, data)
            return

    print("No contact found with this phone number.")


def list_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for name in sorted(contacts):
        print_contact(name, contacts[name])


def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def print_contact(name, data):
    print("\n---------------------")
    print(f"Name : {name}")
    print(f"Phone: {data.get('phone')}")
    print(f"Email: {data.get('email') or 'N/A'}")

    tags = data.get("tags")
    if tags:
        print("Tags :", ", ".join(tags))
    else:
        print("Tags : None")
    print("---------------------")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_by_name()
        elif choice == "3":
            search_by_phone()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
