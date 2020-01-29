import time
from random import choice
from string import ascii_lowercase as letters

# def bisection_iter(n, arr):
#     start = 0
#     stop = len(arr)-1
#     while start <= stop:
#         mid = (start + stop)//2
#         if n == arr[mid]:
#             return f"{n} found at index: {mid}"
#         elif n > arr[mid]:
#             start = mid+1
#         else:
#             stop = mid-1
#     return f"{n} not found in list"

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

def generate_emails(names, list_of_domains, email_list_size):
    list_of_emails = []
    for i in range(email_list_size):
        email = names + "@" + choice(list_of_domains)
        list_of_emails.append(email)
        i += 1
    return list_of_emails

def generate_name(name_legnth):
    return "".join(choice(letters) for i in range(name_legnth))
