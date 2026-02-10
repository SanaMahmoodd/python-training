from contacts.manager import ContactBook
from contacts.utils import WeakPasswordError

def menu():
    print("\n=== Contact Book ===")
    print("1) List")
    print("2) Add")
    print("3) Update")
    print("4) Delete")
    print("5) Create Account (password validation)")
    print("0) Exit")

def main():
    book = ContactBook("contacts.json")

    while True:
        menu()
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                contacts = book.list_contacts()
                if not contacts:
                    print("No contacts yet.")
                else:
                    for c in contacts:
                        print(f'- {c["name"]} | {c["phone"]} | {c.get("country","")}')

            elif choice == "2":
                name = input("Name: ").strip()
                phone = input("Phone: ").strip()
                country = input("Country (Enter for PS): ").strip() or "PS"
                book.add_contact(name, phone, country=country)  # keyword arg
                print("Added ✅")

            elif choice == "3":
                phone = input("Phone to update: ").strip()
                new_name = input("New name (Enter to skip): ").strip() or None
                new_country = input("New country (Enter to skip): ").strip() or None
                updated = book.update_contact(phone, name=new_name, country=new_country)
                print("Updated ✅", updated)

            elif choice == "4":
                phone = input("Phone to delete: ").strip()
                deleted = book.delete_contact(phone)
                print("Deleted ✅", deleted)

            elif choice == "5":
                phone = input("Phone: ").strip()
                password = input("Password: ").strip()
                book.create_account_for_contact(phone, password)
                print("Account created ✅")

            elif choice == "0":
                print("Bye 👋")
                break
            else:
                print("Invalid choice.")

        except WeakPasswordError as e:
            print("Password error:", e)
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)
        finally:
            # runs always
            pass

if __name__ == "__main__":
    main()
