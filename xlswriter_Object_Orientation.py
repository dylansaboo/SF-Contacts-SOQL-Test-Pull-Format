from datetime import datetime
import xlsxwriter
import pymysql.cursors
import sys, time, progressbar, os

class xls_writer(object):
    def xls(self):
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('SF_Contacts.xlsx')
        worksheet = workbook.add_worksheet()

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': 1})

        # Adjust the column width.
        worksheet.set_column(1, 1, 20)
        worksheet.set_column(2, 2, 40)
        worksheet.set_column(0, 0, 20)

        # Write some data headers.
        worksheet.write('A1', 'First_Name', bold)
        worksheet.write('B1', 'Last_Name', bold)
        worksheet.write('C1', 'Email', bold)

        counter = 0
        print("Generating .xlsx File...")
        # Some data we want to write to the worksheet.
        try:
            with self.connection.cursor() as cursor:
                sql = 'SELECT First_Name, Last_Name, Email FROM users;'
                cursor.execute(sql)
                for row in cursor:
                    counter = counter + 1
                    #contacts.append('%s, %s, %s' % (row['First_Name'], row['Last_Name'], row['Email']))
                    worksheet.write(counter, 0, '%s' % (row['First_Name']))
                    worksheet.write(counter, 1, '%s' % (row['Last_Name']))
                    worksheet.write(counter, 2, '%s' % (row['Email']))
                self.connection.commit()
                for i in progressbar.ProgressBar()(range(80)):
                    time.sleep(0.02)
                print("File Location: %s" % (os.path.dirname(os.path.realpath("SF_Contacts.xlsx"))))
                print("")
        finally:
            self.connection.close()

        # Start from the first cell below the headers.
        row = 1
        col = 0

        workbook.close()

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',user='root',password='HIDDEN',db='HIDDEN',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        self.xls()

if __name__ == '__main__':
    test = xls_writer()
