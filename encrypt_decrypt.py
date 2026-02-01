from cryptography.fernet import Fernet
#already pip cryptography installed in cmd 
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as file:
        file.write(key)
    print("Key generated successfully!")


def load_key():
    return open("secret.key", "rb").read()


def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = fernet.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print("File encrypted successfully!")
#file name want to entered 
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = fernet.decrypt(encrypted_data)

    output_file = "decrypted_" + filename.replace(".enc", "")
    with open(output_file, "wb") as file:
        file.write(decrypted)

    print("File decrypted successfully!")
#enc file want to enter 
def main():
    print("\n1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Enter choice: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        filename = input("Enter encrypted file name: ")
        decrypt_file(filename)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
