from functions import analyze_func, generate_emails, generate_name, bisection_iter

list_of_domains = ["yohoo.com", "gomail.com", "happymail.com","aol.com"]

# inputs for legnth of name in email and size of email list
length_names = int(input("How many characters for the name length? "))
email_list_size = int(input("How many emails you want to generate? "))

# generates email list
email_arr = generate_emails(length_names, list_of_domains, email_list_size)

# user input for their name to creat email to be inserted into gen email list
user_name = input("Type in your name to create email:  ")
implanted_email = user_name + "@yohoo.com"

# inserts user email into list
print(f"Inserting {implanted_email} into email list...")
email_arr.append(implanted_email) # add check statement to make sure input email is valid

# sorts list of emails
sorted_email_arr = sorted(email_arr)

# print(sorted_email_arr) # uncomment to see the array

# runs bisection to find user email within gen email list
index, found = bisection_iter(implanted_email, sorted_email_arr)

# prints bisection results
print(found)

# checks to make sure the bisection worked
if index:
    print(f"Element at index {index} is {sorted_email_arr[index]}")

# analyzes functions' run times
analyze_func(generate_emails,length_names, list_of_domains, email_list_size)
analyze_func(bisection_iter,implanted_email, sorted_email_arr)
