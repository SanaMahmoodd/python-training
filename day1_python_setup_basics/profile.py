import sys


def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python profile.py <name> <age> <role>")
        return

    name: str = sys.argv[1]
    age: int = int(sys.argv[2])
    role: str = sys.argv[3]

    print(f"""
====================
Name : {name}
Age  : {age}
Role : {role}
====================
""")


if __name__ == "__main__":
    main()
