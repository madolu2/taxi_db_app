import db


class UI():

    database = db.MyDatabase(db.SQLITE, dbname='taxi.db')

    def get_drivers(self,lname=None, fine=None, commendation=None):
        try:
            if lname:
                query = f"SELECT * FROM driver WHERE last_name = {lname};"
            elif fine:
                query = f"SELECT * FROM driver WHERE fine = 1;"
            elif commendation:
                query = f"SELECT * FROM driver  WHERE commendation = 1;"
            else:
                query = f"SELECT * FROM driver;"
            drivers = self.database.get_data(query=query)
            formatted_drivers = []
            for driver in drivers:   
                formatted_drivers.append(f"{driver['id']} {driver['first_name']} {driver['last_name']} - " \
                                            f"Experience {driver['experience']} years -" 
                                            f"Fine {driver['fine']} - "
                                            f"Commendation {driver['commendation']}")
            return formatted_drivers
        except Exception as e:
            return f"Failed {e}"
    def get_by_area(self, area):
        try:
            query = f"SELECT * FROM call WHERE call_area = {area};"
            call_area = self.database.get_data(query=query)
            query = f"SELECT * FROM call WHERE destination_area = {area};"
            destination_area = self.database.get_data(query=query)
        except Exception as e:
            return f"Failed {e}"



        # try:
        #     pass
        # except Exception as e:
        #     return f"Failed {e}"