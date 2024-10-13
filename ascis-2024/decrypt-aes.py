from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
import base64
def decode_and_reverse(encoded_string):
    # Step 1: Reverse the string
    reversed_string = encoded_string[::-1]
    
    # Step 2: Replace '-' with 'C' and '_' with 'E'
    replaced_string = reversed_string.replace('-', 'C').replace('_', 'E')
    
    # Step 3: Add padding if necessary
    padding_needed = len(replaced_string) % 4
    if padding_needed:
        replaced_string += '=' * (4 - padding_needed)
    print("orign: " + replaced_string)
    return base64.b64decode(replaced_string).decode('utf-8')
def aes_cbc_decrypt(encrypted_data, key1):
    try:
        # Create SHA256 hash of the key
        sha256 = SHA256.new()
        sha256.update(key1.encode('utf-8'))
        key = sha256.digest()
        
        # Decode the base64-encoded data
        encrypted_data = base64.b64decode(encrypted_data)
        
        # Extract the IV and the ciphertext
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        # Debugging: Print IV and Ciphertext
        print("IV:", iv.hex())
        print("Ciphertext:", ciphertext.hex())
        
        # Create AES cipher object with the key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt the ciphertext
        decrypted_data = cipher.decrypt(ciphertext)

        # Debugging: Print decrypted data before unpadding
        print("Decrypted data before unpadding:", decrypted_data.hex())
        
        # Remove PKCS7 padding
        decrypted_data = unpad(decrypted_data, AES.block_size)
        
        # Convert bytes to string and return the result
        return decrypted_data.decode('utf-8')
    
    except (ValueError, KeyError) as e:
        print(f"Decryption failed: {e}")
        return None

# Example usage
encrypted_base64 = input("Try: ")
key = "YaMfem0zr4jdiZsDUxv1TH69"
# Decrypt the data
decrypted_text = aes_cbc_decrypt(encrypted_base64, key)

if decrypted_text:
    print("Decrypted data:", decrypted_text)