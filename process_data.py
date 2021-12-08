import csv
import json
from datetime import date, datetime
from pathlib import Path

CUSTOMERS_CSV = 'data/acw_user_data (1).csv'


def write_to_processed(csvfile: str|Path = CUSTOMERS_CSV) -> list[dict]:
    """
    Read in and parse acw_users_data and output data formatted for a json file.

    Args:
        csvfile (str|Path, optional): File path to the acw_user_data.csv file.

    Returns:
        list[dict]: Containing acw_user_data formatted in json format.
    """
    customer_data = []

    # Read and parse customer_csv data.
    with open(csvfile, encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        to_bool = lambda x: True if x == 'True' else False
        for i, row in enumerate(csv_reader, start=1):
            get_month = lambda x: int(row[x].split('/')[0])
            get_year = lambda x: int(row[x].split('/')[1])
            customer_details = {
                'name': {
                    'first': row['First Name'],
                    'last': row['Last Name']
                },
                'age': make_int(row['Age (Years)'], 'age', i),
                'sex': row['Sex'],
                'marital_status': row['Marital Status'],
                'dependants': make_int(row['Dependants'], 'dependents', i),
                'address': {
                    'street': row['Address Street'],
                    'city': row['Address City'],
                    'postcode': row['Address Postcode']
                },
                'credit_card': {
                    'start_date': {
                        'month': get_month('Credit Card Start Date'),
                        'year': get_year('Credit Card Start Date')
                        },
                    'end_date': {
                        'month': get_month('Credit Card Expiry Date'),
                        'year': get_year('Credit Card Expiry Date')
                        },
                    'number': row['Credit Card Number'],
                    'cvv': row['Credit Card CVV'],
                    'iban': row['Bank IBAN']
                },
                'employment': {
                    'retired': to_bool(row['Retired']),
                    'yearly_pension': make_int(
                        row['Yearly Pension (£)'], 'yearly_pension', i),
                    'employer': row['Employer Company'],
                    'yearly_salary': make_int(
                        row['Yearly Salary (£)'], 'yearly_salary', i),
                    'commute_distance': float(row[
                        'Distance Commuted to Work (miles)'])
                },
                'vehicle':{
                    'type': [item.strip() for item in row['Vehicle Type'].split(',')],
                    'year': make_int(row['Vehicle Year'], 'vehicle_year', i),
                    'make': row['Vehicle Make'],
                    'model': row['Vehicle Model']
                }
            }
            customer_data.append(customer_details)
    return customer_data


if __name__ == "__main__":
    corrected_data = dict()

    def make_int(data: str, column_header: str, row_num: int) -> int:
        key = column_header
        try:
            converted_data = int(data)
        except ValueError as e:
            columns_corrected = corrected_data.setdefault(key, [row_num])
            if columns_corrected != [row_num]:
                columns_corrected.append(row_num)
            if data == '' or data == 'N/A':
                converted_data = 0
            else:
                print(e)
        finally:
            return converted_data


    # Writes data from acw_user_data to processed.json file.
    with open('output/processed.json', mode='w', encoding='utf-8') as f:
        f.write(json.dumps(write_to_processed(CUSTOMERS_CSV), indent=2))

    for key, values in corrected_data.items():
        print(f'Problematic rows for {key}: {values}')
