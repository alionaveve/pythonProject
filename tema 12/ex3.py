def is_valid_email(string):
    a = ' ' in string
    r = 0
    if not a:
        b = "@" in string
        if b:
            c = "@." in string
            if c:
                r = False
            else:
                r = True
        else:
            r = False
    else:
        r = False
    return r
a = input("Enter your email :")
print(is_valid_email(a))
