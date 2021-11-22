import csv
import json
 
 
# a function to import the data from csv - jason)
# takes two argument
def convert_json(csvFile, jsonFile):
 
    data = {}
 
    with open(csvFile, 'r') as csvf:
        csvReader = csv.DictReader(csvf)
 
        for i, row in enumerate (csvReader):
           
            details = {

                
                "first_name": row["First Name"],
                "second_name": row["Last Name"],
                "age": row["Age (Years)"],
                "sex": row["Sex"],
                "retired": bool(row["Retired"]),
                "marital_status": row["Marital Status"],
                "dependents": row["Dependants"],
                "salary": row["Yearly Salary (£)"],
                "pension": row["Yearly Pension (£)"],
                "company": row["Employer Company"],
                "commute_distance": row["Distance Commuted to Work (miles)"],
                "Address": {
                    "street": row["Address Street"],
                    "city": row["Address City"],
                    "postcode": row["Address Postcode"],
                },
                "Credit Card": {
                    "start_date": row["Credit Card Start Date"],
                    "end_date": row["Credit Card Expiry Date"],
                    "number": row["Credit Card Number"],
                    "ccv": row["Credit Card CVV"],
                    "iban": row["Bank IBAN"]
                },
                "Vehicle": {
                    "make": row["Vehicle Make"],
                    "model": row["Vehicle Model"],
                    "year": row["Vehicle Year"],
                    "category": row["Vehicle Type"]

                }

            }

            data.setdefault(i, details)
    
        
    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
 
csvFile = r'acw_user_data (1).csv'
jsonFile = r'Company_Db.json'
 
convert_json(csvFile,jsonFile)

#  Finding the errors/empty values in the dict

with open("Company_Db.json",'r') as error_file:
    search = json.load(error_file)


def find_errors(error):
    error = ""
    
    dependent_list = []

    if error in search.values():
        dependent_list.append(error)
        num_errors = len(dependent_list)

        print(" {} Problematic contents found".format(num_errors))

find_errors(" ")
