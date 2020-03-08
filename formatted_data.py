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
            query = f"SELECT * FROM call WHERE call_area = '{area}';"
            call_areas = self.database.get_data(query=query)
            query = f"SELECT * FROM call WHERE destination_area = '{area}';"
            destination_areas = self.database.get_data(query=query, debug=True)

            formatted_call_areas = []
            formatted_destination_areas = []

            for call_area in call_areas:
                formatted_call_areas.append(f"Date {call_area['date']} - " \
                                            f"Length {call_area['length']} - " \
                                            f"From {call_area['call_area']} {call_area['ca_home']} - " \
                                            f"To {call_area['destination_area']} {call_area['da_home']} - "
                                            f"Price {call_area['price']}"
                )

            for destination_area in destination_areas:
                formatted_destination_areas.append(f"Date {destination_area['date']} - " \
                                            f"Length {destination_area['length']} - " \
                                            f"From {destination_area['call_area']} {destination_area['ca_home']} - " \
                                            f"To {destination_area['destination_area']} {destination_area['da_home']} - "
                                            f"Price {destination_area['price']}"
                )
            return formatted_call_areas, formatted_destination_areas
        except Exception as e:
            return f"Failed {e}"
            
    def get_auto(self, number=None, auto_id=None):
        try:
            if number:
                query = f"SELECT * FROM auto WHERE number = '{number}';"
                auto = self.database.get_data(query=query)
                formatted_auto = f"{auto[0]['color']} - {auto[0]['brand']} - {auto[0]['number']}"
                return formatted_auto
            else:
                query = f"SELECT * FROM auto WHERE id = {auto_id};"
                auto = self.database.get_data(query=query)
                formatted_auto = f"{auto[0]['color']} - {auto[0]['brand']} - {auto[0]['number']}"
                return formatted_auto
        except Exception as e:
            return f"Failed -> {e}"
