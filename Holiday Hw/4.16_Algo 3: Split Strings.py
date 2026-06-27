

###########################################################
# Scenario 6: Processing Customer Data from a CRM System

# You are working on a Customer Relationship Management (CRM) system 
# that stores customer records as a single raw string.

# Each record contains:
# - Customer Name followed by a semicolon (;).
# - Phone Number (8-digit number) immediately after the semicolon.
# - Records are separated by a comma (,).

# Your task is to:
# - Part 1: Extract individual customer records from the raw string 
#           and store them in a list.

# expected output
# ["Alice Johnson;98653263", "Catherine Lee;89653215", "Johnson Lam;95321453",
#     "Brandon Tan;81234567", "Emily Wong;92345678", "Hafiz Zaid;85678912",
#     "Isabelle Ng;96541234", "Ken Lim;97865432", "Noraini Ahmad;88776655",
#     "Samuel Chan;90123456"]


# - Part 2: Convert the list in part 1 into a dictionary, where:
# -   Customer names are the keys.
# -   Phone numbers are stored as integer values.

# expected output
# {"Alice Johnson": 98653263, "Catherine Lee": 89653215, "Johnson Lam": 95321453,
#     "Brandon Tan": 81234567, "Emily Wong": 92345678, "Hafiz Zaid": 85678912,
#     "Isabelle Ng": 96541234, "Ken Lim": 97865432, "Noraini Ahmad": 88776655,
#     "Samuel Chan": 90123456 }

customers = "Alice Johnson;98653263,Catherine Lee;89653215,Johnson Lam;95321453,Brandon Tan;81234567,Emily Wong;92345678,Hafiz Zaid;85678912,Isabelle Ng;96541234,Ken Lim;97865432,Noraini Ahmad;88776655,Samuel Chan;90123456"
# write your code for part 1 here
records = []
index = customers.find(",")
while index != -1:
    records.append(customers[:index])
    customers = customers[index+1:]
    index = customers.find(",")
records.append(customers)
print(records)
# write your code for part 2 here
customer_dict = {}
for i in records:
    index = i.find(";")
    customer_dict[i[:index]] = i[index+1:]
print(customer_dict)