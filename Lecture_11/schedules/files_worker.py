import csv
import json
from mimesis import Address, Generic, Finance, Person
from transliterate import translit


def json_writer(flight_db: dict, directory: str) -> None:
    try:
        with open(directory, "w") as fh:
            json.dump(flight_db, fh, indent=4, sort_keys=True)
        print('Success!')
    except Exception as error:
        print(f'Something went wrong: {error}')


def reader_csvdb():
    flight_dict = {}
    try:
        with open("schedules/schedule.csv", newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                flight_dict.update({row.get('Number'): row})
        return flight_dict
    except Exception as error:
        print(f'Something went wrong: {error}')


field_names = ['Number', 'Company', 'Full Name', 'Departure Point', 'Departure Time',
               'Destination Point', 'Arrival Time', 'Price']

with open("schedules/schedule.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, lineterminator='\n', fieldnames=field_names)
    writer.writeheader()


address_ua, address_en, generic, finance, person = Address('UK'), Address('EN'), \
                                                   Generic('UA'), Finance('EN'), Person('UK')


for i in range(100):
    company = finance.company()
    passenger_name = translit(person.full_name(), language_code='uk', reversed=True)
    departure_point = translit(address_ua.city(), language_code='uk', reversed=True)
    departure_time = str(generic.datetime.time())[0:5]
    destination_point = address_en.city()
    arrival_time = str(generic.datetime.time())[0:5]
    price = finance.price(minimum=30, maximum=10000)
    with open("schedules/schedule.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, lineterminator='\n', fieldnames=field_names)
        writer.writerow({'Number': i+1, 'Company': company, 'Full Name': passenger_name,
                         'Departure Point': departure_point, 'Departure Time': departure_time,
                         'Destination Point': destination_point,
                         'Arrival Time': arrival_time, 'Price': price})

flight_database = reader_csvdb()
print(flight_database)

json_writer(flight_database, "schedules/schedule.json")