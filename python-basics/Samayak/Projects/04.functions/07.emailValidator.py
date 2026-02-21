# Check if entered email address is valid or not using a function

# function to validate mail

def _validate_email(email):
    if '@' not in email or '.' not in email:
        return False
    if email.count("@") != 1:
        return False
    return True

# Function to show result
def show_result(email):
    if _validate_email(email):
        print(f"{email} is a valid email address!\n")
    else:
        print(f"{email} is not a valid email address!\n")


# Main program:
print("-----Email Validator-----")
user_email = input("Enter Your Email:\n")
show_result(user_email)
