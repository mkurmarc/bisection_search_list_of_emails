from functions import analyze_func, generate_emails, generate_name

generate_name(15)

list_of_domains = ["yahoo.com", "gmail.com", "hotmail.com","aol.com"]
email_list_size = int(input("How many emails you want to generate?"))

print(generate_emails(generate_name(15), list_of_domains, email_list_size))
