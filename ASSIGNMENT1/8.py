def validatepassword(pas):
    errors = []
    spchar = "!@#$%"

    if len(pas) < 8:
        errors.append("Password must contain at least 8 characters.")
    if not any(x.isupper() for x in pas):
        errors.append("Password must contain at least 1 uppercase letter.")
    if not any(x.islower() for x in pas):
        errors.append("Password must contain at least 1 lowercase letter.")
    if not any(x.isdigit() for x in pas):
        errors.append("Password must contain at least 1 digit.")
    if not any(x in spchar for x in pas):
        errors.append("Password must contain at least 1 special character (!@#$%).")
    if any(x.isspace() for x in pas):
        errors.append("Password must not contain spaces.")

    if len(errors) == 0:
        return True, []
    else:
        return False, errors


# Main program
pas = input("Enter the password: ")
val, errors = validatepassword(pas)

if val:
    print(f"'{pas}' is a valid password ")
else:
    print(f"'{pas}' is NOT a valid password ")
    print("Errors:")
    for e in errors:
        print("-", e)
