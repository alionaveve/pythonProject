string_al = input(str("Enter your string: "))

def palindrome(string_al):
    string_al = string_al.lower().replace(' ', '')
    return string_al == string_al[::-1]

print(palindrome(string_al))