import sys, pyexcel, os

records = pyexcel.iget_records(file_name='SF_Contacts.xlsx')
for record in records:
    print("%s, %s, %s" % (record['First_Name'], record['Last_Name'], record['Email']))


