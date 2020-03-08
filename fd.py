import db


class FormattedData():
    database = db.MyDatabase(db.SQLITE, dbname='taxi.db')
    def get_drivers(self,lname=None, fine=None, commendation=None):
        try:
            if lname:
                query = f"SELECT * FROM driver WHERE last_name = '{lname}';"
            elif fine:
                query = f"SELECT * FROM driver WHERE fine = 1;"
            elif commendation:
                query = f"SELECT * FROM driver  WHERE commendation = 1;"
            else:
                query = f"SELECT * FROM driver;"

            drivers = self.database.get_data(query=query)
            
            formatted_drivers = []

            for driver in drivers:
                auto_ids = self.database.get_data(query=f"SELECT auto_id FROM call WHERE driver_id = {driver['id']};")
                autos = ''
                for auto_id in auto_ids:
                    autos += f"| {self.get_auto(auto_id=auto_id[0])} |"

                formatted_drivers.append(f"{driver['id']} {driver['first_name']} {driver['last_name']} - " \
                                        f"Experience {driver['experience']} years - " \
                                        f"Fine {driver['fine']} - " \
                                        f"Commendation {driver['commendation']} - " \
                                        f"{autos}")
            return formatted_drivers
        except Exception as e:
            return f"Failed {e}"

    def get_by_area(self, area):
        try:
            query = f"SELECT driver_id FROM call WHERE call_area = '{area}';"
            drivers = self.database.get_data(query=query)
            formatted_drivers = []
            for driver in drivers:
                query = f"SELECT * FROM driver WHERE id = '{driver[0]}';"
                driver = self.database.get_data(query=query)
                formatted_drivers.append(f"{driver[0]['id']} {driver[0]['first_name']} {driver[0]['last_name']} - " \
                                        f"Experience {driver[0]['experience']} years - " \
                                        f"Fine {driver[0]['fine']} - " \
                                        f"Commendation {driver[0]['commendation']} - ")
            return formatted_drivers
        except Exception as e:
            return f"Failed {e}"
        
    def get_auto(self, number=None, auto_id=None):
        try:
            query = f"SELECT * FROM auto WHERE id = {auto_id};"
            auto = self.database.get_data(query=query)
            formatted_auto = f"{auto[0]['color']} - {auto[0]['brand']} - {auto[0]['number']}"
            return formatted_auto
        except Exception as e:
            return f"Failed -> {e}"

    def get_auto_by_num(self, number):
        try:
            query = f"SELECT * FROM auto WHERE number = '{number}';"
            auto = self.database.get_data(query=query)
            formatted_auto = f"{auto[0]['color']} - {auto[0]['brand']} - {auto[0]['number']}"
            return formatted_auto
        except Exception as e:
            return f"Failed -> {e}"