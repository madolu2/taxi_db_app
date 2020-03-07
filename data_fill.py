import db
import driver_generator
import random as r


dgen = driver_generator.DriverGenerator()
#Put ur DMS and DBname here ->
database = db.MyDatabase(db.SQLITE, dbname='taxi.db')
#Delete and create tables
database.drop_tables()
database.create_db_tables()

number_of_drivers = 5
call_ids = []
driver_id  = 1
auto_id = 1

for i in range(number_of_drivers):
    driver = dgen.generate_driver()
    auto = dgen.generate_auto()
    call = dgen.generate_call()

    while(True):
        call_id = r.randint(0,1000)
        if call_id not in call_ids:
            call_ids.append(call_id)
            break

    database.driver_insert(driver_id,
                            driver['name'],
                            driver['lname'],
                            driver['experience'],
                            driver['fine'],
                            driver['commendation'])

    database.auto_insert(auto_id,
                          auto['color'],
                          auto['brand'],
                          auto['number'])

    database.call_insert(call_ids[i],
                        call['date'],
                        call['length'],
                        call['call_area'],
                        call['ca_home'],
                        call['destination_area'],
                        call['da_home'],
                        call['price'],
                        r.randint(1,number_of_drivers),
                        r.randint(1,number_of_drivers))

    driver_id  += 1
    auto_id += 1

        
