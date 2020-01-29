import time
from random import choice
from string import ascii_lowercase as letters

def bisection_iter(email, arr):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop)//2
        if email == arr[mid]:
            return mid, f"{email} found at index {mid}"
        elif email > arr[mid]:
            start = mid+1
        else:
            stop = mid-1
    return None, f"{email} not found in list"

def analyze_func(func_name, *args):
    tic = time.time()
    func_name(*args)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

################# email generation functions below ##########################

def generate_emails(length_names, list_of_domains, email_list_size):
    list_of_emails = []
    for i in range(email_list_size):
        email = generate_name(length_names) + "@" + get_domain_name(list_of_domains)
        list_of_emails.append(email) # can make shorter by inserting email assignment into append parenthesis
    return list_of_emails            # did not do that to keep process clear

def get_domain_name(list_of_domains):
    return choice(list_of_domains)

def generate_name(name_length):
    return "".join(choice(letters) for i in range(name_length))
