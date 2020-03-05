import db


database = db.MyDatabase(db.SQLITE, dbname='taxi.db')

def get_auto_by_driver(driver_id):
    try:
        auto_ids =  database.get_data(query= f"SELECT auto_id FROM call WHERE driver_id = {driver_id};")
        formatted_autos = []
        for auto_id in auto_ids:
            auto = database.get_data(query=f"SELECT * FROM auto WHERE id = {auto_id[0]};")
            formatted_autos.append(f"{auto[0]['color']} {auto[0]['brand']} {auto[0]['number']}")
        return formatted_autos
    except Exception as e:
        return "Failed"

def get_drivers(fine=None, commendation=None):
    try:
        if fine:
            query = f"SELECT * FROM driver WHERE fine = 1;"
        elif commendation:
            query = f"SELECT * FROM driver  WHERE commendation = 1;"
        else:
            query = f"SELECT * FROM driver;"
        drivers = database.get_data(query=query)
        formatted_drivers = []
        for driver in drivers:   
            formatted_drivers.append(f"{driver['id']} {driver['first_name']} {driver['last_name']} - " \
                                        f"Experience {driver['experience']} years -" 
                                        f"Fine {driver['fine']} - "
                                        f"Commendation {driver['commendation']}")
        return formatted_drivers
    except Exception as e:
        return "Failed"

def get_call_by_driver(driver_id):
    try:
        calls =  database.get_data(query= f"SELECT * FROM call WHERE driver_id = {driver_id};")
        price = 0
        formatted_calls = []
        for call in calls:
            price += call['price']
            formatted_calls.append(f"Date {call['date']} - " \
                                    f"Length {call['length']} km - " \
                                    f"StreetFrom {call['call_area']} - " \
                                    f"StreetTo {call['destination_area']} - " \
                                    f"Price {call['price']}")
        return formatted_calls, price
    except Exception as e:
        return "Failed"
    


def get_by_fine():
    try:
        pass
    except Exception as e:
        return "Failed"

def get_by_commendation():
    try:
        pass
    except Exception as e:
        return "Failed"

def get_by_area():
    streets = ['Красноармейский', 'Ленина', 'Германа-Титова', 'Лихачева', 'Петра-Сухова',
			'Эмилии-Алексеевой', 'Комсомольский', 'Брестская', 'Васильковая улица',
			'Гаражная улица', 'Жемчужная улица', 'Магистральный проезд', 'Обская улица', 'Урожайная улица', 'Чапаева']
def get_by_lname():
    pass

def get_auto_by_num():
    pass


data = get_auto_by_driver(7)
for i in data:
    print(i)
