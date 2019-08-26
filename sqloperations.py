import pyodbc
import contextlib

server = 'lombardsvr.database.windows.net'
database = 'icicilombarddb'
username = 'admin123'
password = 'Mythili@99999'
driver= '{SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
#row = cursor.fetchone()
#while row:
#    print (str(row[0]) + " " + str(row[1]))
#    row = cursor.fetchone()






def bulk_insert(table_name, file_path):
    string = "BULK INSERT {} FROM '{}' WITH (FORMAT = 'CSV');"
    with contextlib.closing(pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)) as conn:
        with contextlib.closing(conn.cursor()) as cursor:
            print(string.format(table_name, file_path))
            cursor.execute(string.format(table_name, file_path))
        conn.commit()
        conn.close()


# Main method.
if __name__ == '__main__':
    #run_sample()
    #listFilesInFolder()
    bulk_insert("employee","C:\WorkArea\Code\Pythoncode\Azureblob\storage-blobs-python-quickstart\employee_file2.csv")




# ---------------------------------------------------------------------------------------------------------
# Method used to write a CSV file
# ---------------------------------------------------------------------------------------------------------
def writeCSV(csvFile):
    try:
        with open(csvFile, mode='w') as csv_file:
            fieldnames = ['emp_name', 'dept', 'birth_month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
            writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    except Exception as e:
        print(e)