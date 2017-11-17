from simple_salesforce import Salesforce
import pymysql.cursors
import requests, sys, re, json, tqdm, time
from collections import OrderedDict
from xlswriter_Object_Orientation import *

class testing(object):
    connection = None

    def db_write(self, arg, arg2, arg3, arg4, arg5):
        #print(arg, arg2, arg3)
        try:
            with self.connection.cursor() as cursor:
                #Create a New Record
                sql = "INSERT INTO users (First_Name, Last_Name, email, Phone, Title) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sql, (arg, arg2, arg3, arg4, arg5))
                self.connection.commit()
        finally:
            return self.connection
        
    def get_sf_query(self):
       data1 = self.sf.query("SELECT Email, FirstName, LastName, Phone, Title FROM Contact")
       return data1
   
    def main(self):
        data1 = self.get_sf_query()
        #print(data1)
        records = data1['records']
        counter = 0

        for row in records:
            if row['FirstName'] is not None:
                print('Pulling Record: %s %s' % (row['FirstName'], row['LastName']))
                FirstName = row['FirstName']
                FirstName = FirstName.encode('utf8', 'ignore')
                FirstNameS = str(FirstName)
                LastName = row['LastName']
                LastName = LastName.encode('utf8', 'ignore')
                LastNameS = str(LastName)
                #name = FirstName + " " + LastName
                #name = name.encode('ascii', 'ignore')
                email = row['Email']
                emailS = str(email)
                phone = row['Phone']
                Title = row['Title']
                #TitleS = str(Title)
                #emailPrint = "Email: ".format(str) + str(email)
                #name = str(FirstName) + " ".format(str) + str(LastName)
                self.db_write(FirstNameS, LastNameS, emailS, phone, Title)
                #print(json.dumps((FirstName, LastName, emailPrint), indent=4))
                counter = counter + 1
        print("==============================")
        print("Total Contacts Pulled: %s" % (counter))
        print("==============================")
        print("")
        xls_writer()
        self.connection.close()        
        return self.d

    def __init__(self):
        print("Pulling Content... ")
        self.connection = pymysql.connect(host='localhost',
                user='HIDDEN',
                password='HIDDEN',
                db='HIDDEN',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
        self.d = {}
        self.sf = Salesforce(username='HIDDEN@gmail.com', password='HIDDEN', security_token='SF_SECURITY_TOKEN')
        self.main()


if __name__ == '__main__':
    test = testing()
