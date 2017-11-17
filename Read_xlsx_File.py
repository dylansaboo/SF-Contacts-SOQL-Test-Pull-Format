import sys, pyexcel, os

records = pyexcel.iget_records(file_name='SF_Contacts.xlsx')
for record in records:
    print("Name: %s %s" % (record['First_Name'], record['Last_Name']))
    print("      Email: %s" % (record['Email']))
    print("      Phone: %s" % (record['Phone']))
    print("      Title: %s" % (record['Title']))
    print("      ")
    print("")
