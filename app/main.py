from rns import Identity, Destination, Reticulum
from app.crypto_utils import encrypt_message, decrypt_message

def main():
    # Initialize Reticulum
    Reticulum()
    
    print("Reticulum network initialized!")
    
    # Example usage
    message = "Hello, Reticulum!"
    encrypted = encrypt_message(message)
    decrypted = decrypt_message(encrypted)
    
    print(f"Original: {message}")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
