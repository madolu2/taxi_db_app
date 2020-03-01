from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData, ForeignKey


# Global Variables
SQLITE = 'sqlite'

# Table Names
DRIVERS = 'driver'
AUTOS = 'auto'
CALLS = 'call'

class MyDatabase:
    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None
    def __init__(self, dbtype, username='', password='', dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")
    
    def drop_tables(self):
        query = "DROP TABLE driver;"
        self.execute_query(query)
        query = "DROP TABLE call;"
        self.execute_query(query)
        query = "DROP TABLE auto;"
        self.execute_query(query)
        


    def create_db_tables(self):
        metadata = MetaData()
        driver = Table(DRIVERS, metadata,
        Column('id', Integer, primary_key=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('experience', Integer),
        Column('fine', Boolean),
        Column('commendation', Boolean))

        auto = Table(AUTOS, metadata,
        Column('id', Integer, primary_key=True),
        Column('color', String),
        Column('brand', String),
        Column('number', String))

        call = Table(CALLS, metadata,
        Column('id', Integer, primary_key=True),
        Column('date', String),
        Column('length', Integer),
        Column('call_area', String),
        Column('destination_area', String),
        Column('price', Integer),
        Column('driver_id', None, ForeignKey('driver.id')),
        Column('auto_id', None, ForeignKey('auto.id')))

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)
        
    def execute_query(self, query=''):
        if query == '' : return
        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)    

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)
    
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) # print(row[0], row[1], row[2])
                result.close()
                print("\n")

    def driver_insert(self, id, first_name, last_name, experience, fine, commendation):
        # Insert Data
        query = f"INSERT INTO {DRIVERS}(id, first_name, last_name, experience, fine, commendation) " \
                f"VALUES ({id}, '{first_name}', '{last_name}', '{experience}', {fine}, {commendation});"
        self.execute_query(query)

    def auto_insert(self, id, color, brand, number):
        # Insert Data
        query = f"INSERT INTO {AUTOS}(id, color, brand, number) " \
                f"VALUES ({id}, '{color}', '{brand}', '{number}');"
        self.execute_query(query)

    def call_insert(self, id, date, length, call_area, destination_area, price, driver_id, auto_id):
        # Insert Data
        query = f"INSERT INTO {CALLS}(id, date, length, call_area, destination_area, price, driver_id, auto_id) " \
                f"VALUES ({id}, '{date}', {length}, '{call_area}', '{destination_area}', {price}, {driver_id}, {auto_id});"
        self.execute_query(query)
    
    


