import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=False):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?/" if use_special_chars else ''
    
    # Combine character sets based on preferences
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    
    # Check if at least one character set is selected
    if not all_chars:
        print("Please select at least one character set.")
        return None

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

# Function to get user preferences for password generation
def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    return length, use_lowercase, use_uppercase, use_digits, use_special_chars

if __name__ == "__main__":
    print("Random Password Generator")
    length, use_lowercase, use_uppercase, use_digits, use_special_chars = get_user_preferences()
    
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    
    if password:
        print("Generated Password:", password)