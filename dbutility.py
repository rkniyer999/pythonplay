import csv
import pyodbc

# ---------------------------------------------------------------------------------------------------------
# Method used to create connection to DB
# ---------------------------------------------------------------------------------------------------------
def getConnection(server,database,username,password,driver):
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn

# ---------------------------------------------------------------------------------------------------------
# Method used to execute a query
# ---------------------------------------------------------------------------------------------------------
def executeSelectSQL(cnxn,SQLCommand):
    try:
        cursor = cnxn.cursor()
        
        # Handle the cursor.close() with a 'with' statement.
        with cursor as cursor:
            # Execute the query.
            cursor.execute( SQLCommand )       
            # Use list( cursor ) to get a Python list.
            results = cursor.fetchall()
        cnxn.close()
        return results
    except Exception as e:
        print(e)

# ---------------------------------------------------------------------------------------------------------
# Method used to insert data in a table
# ---------------------------------------------------------------------------------------------------------

def executeInsertSQL(cnxn,SQLCommand,valueList):
    try:
        cursor = cnxn.cursor()
        cursor.execute(SQLCommand,valueList)   
        cnxn.commit()
        cursor.close()
        cnxn.close()
    except Exception as e:
        print(e)


# ---------------------------------------------------------------------------------------------------------
# Method used to read a CSV file 
# ---------------------------------------------------------------------------------------------------------
def readCSVAndPopulateDB(csvFile):
    try:
        with open(csvFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                cnnx = getConnection("xxxxx","xxxx","xxx","xxx","{SQL Server}")
                executeInsertSQL(cnnx,"insert into [dbo].[employee1] (empid,empname) VALUES (?,?)",row)
                line_count += 1
    except Exception as e:
        print(e)





# Main method.
if __name__ == '__main__':
    readCSVAndPopulateDB("emp.csv")

        
    #writeCSV("emp1.csv")
        
    #results = executeSelectSQL(cnnx,"SELECT * FROM SalesLT.ProductCategory")
    #i = 0
    #while results:
    #    print (str(results[i]))
    #    i= i + 1
    


    # Inserting in table
    #valueslst = [5]
    #executeInsertSQL(cnnx,"insert into [dbo].[employee] (empid) VALUES (?)",row)

