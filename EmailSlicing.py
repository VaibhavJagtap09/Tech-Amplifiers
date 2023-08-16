email = input("Enter Your Email: ")
username = email[0:email.index('@')]
RawDomain = email[email.index('@'):]    # consider string only after '@'
domain = RawDomain[RawDomain.index('@')+1:RawDomain.index('.')]     # This will consider '.' only from string after '@'
print("Username is: ", username + "  domain is: ", domain)