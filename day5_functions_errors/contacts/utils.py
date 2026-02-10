import json

class WeakPasswordError(Exception):
    pass


def strong_password(password: str) -> bool:
    if len(password) < 8:
        raise WeakPasswordError("Too short (min 8 chars)")
    if not any(c.isupper() for c in password):
        raise WeakPasswordError("Missing uppercase letter")
    if not any(c.isdigit() for c in password):
        raise WeakPasswordError("Missing number")
    if not any(c in "!@#$%^&*" for c in password):
        raise WeakPasswordError("Missing special char (!@#$%^&*)")
    return True


def safe_load_json(path: str, default):
    """
    Load JSON safely.
    Handles:
    - FileNotFoundError
    - Empty file
    - Corrupted JSON
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content == "":
                return default
            return json.loads(content)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        return default


def safe_write_json(path: str, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
