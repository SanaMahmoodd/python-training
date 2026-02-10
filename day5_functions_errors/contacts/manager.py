from contacts.utils import safe_load_json, safe_write_json, strong_password, WeakPasswordError

DEFAULT_COUNTRY = "PS"

class ContactBook:
    def __init__(self, storage_path: str = "contacts.json"):
        self.storage_path = storage_path
        self.contacts = safe_load_json(self.storage_path, default=[])

    def save(self):
        safe_write_json(self.storage_path, self.contacts)

    def list_contacts(self):
        return self.contacts

    def add_contact(self, name: str, phone: str, country: str = DEFAULT_COUNTRY):
        # Example of default args + keyword args usage
        contact = {"name": name, "phone": phone, "country": country}
        self.contacts.append(contact)
        self.save()
        return contact

    def find_index_by_phone(self, phone: str):
        for i, c in enumerate(self.contacts):
            if c["phone"] == phone:
                return i
        return None

    def update_contact(self, phone: str, *, name=None, country=None):
        # keyword-only args after *
        idx = self.find_index_by_phone(phone)
        if idx is None:
            raise ValueError("Contact not found")

        if name is not None:
            self.contacts[idx]["name"] = name
        if country is not None:
            self.contacts[idx]["country"] = country

        self.save()
        return self.contacts[idx]

    def delete_contact(self, phone: str):
        idx = self.find_index_by_phone(phone)
        if idx is None:
            raise ValueError("Contact not found")
        deleted = self.contacts.pop(idx)
        self.save()
        return deleted

    def create_account_for_contact(self, phone: str, password: str):
        """
        Just to practice exceptions + business logic
        """
        idx = self.find_index_by_phone(phone)
        if idx is None:
            raise ValueError("Contact not found")

        strong_password(password)  # may raise WeakPasswordError
        # In a real app we'd hash and store. Here we just mark "has_account".
        self.contacts[idx]["has_account"] = True
        self.save()
        return True
