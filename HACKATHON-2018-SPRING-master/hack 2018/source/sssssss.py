       print(i)
# Asking input from the user to enter number to get contact
num = int(input("Enter number to get contact: "))
# Iterating over contact_list
for j in contact_list:
# If condition for checking whether the entered number is in dictinary or not
  if num in j.values():
# Prnting the contact if condition is true
        print(j)
# Asking user to enter the name
nme = input("Enter name to get contact and edit number: ")
# Iterating over the contact_list
for k in contact_list:
# If the entered name in dictionary
    if nme in k.values():
# Prnting the contact
        print(k)
# Asking user if he want to edit the number
        newnumber = int(input("Enter number to edit: "))
# Editing the number for the particular user
        k["number"] = newnumber
# Printing the contact number
        print(k)