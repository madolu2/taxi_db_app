import db
import driver_generator
import random as r


dgen = driver_generator.DriverGenerator()
database = db.MyDatabase(db.SQLITE, dbname='taxi.db')


database.create_db_tables()
call_ids = []
driver_id  = 1
auto_id = 1

for i in range(400):
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
                        call['destination_area'],
                        call['price'],
                        driver_id,
                        auto_id)

    driver_id  += 1
    auto_id += 1


database.print_all_data(table='driver')
        
