domain = input().strip()
domains = ""
current_domain = ""
for char in domain:
    if char == '.':
        if current_domain != "":
            if domains == "":
                domains = current_domain
            else:
                domains = current_domain + "\n" + domains
        current_domain = ""
    else:
        current_domain += char

if current_domain != "":
    if domains == "":
        domains = current_domain
    else:
        domains = current_domain + "\n" + domains
print(domains)