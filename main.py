import eel
import fd

try:
    eel.init('web')
    fdata = fd.FormattedData()

    @eel.expose
    def get_drivers(lname=None):
        if lname:
            return fdata.get_drivers(lname=lname)
        else:
            return fdata.get_drivers()

    @eel.expose
    def get_by_fine():
        return fdata.get_drivers(fine=True)

    @eel.expose
    def get_by_commendation():
        return fdata.get_drivers(commendation=True)

    @eel.expose
    def get_by_area(area):
        return fdata.get_by_area(area)

    @eel.expose
    def get_auto_by_num(number=None):
        return fdata.get_auto_by_num(number)

    eel.start('index.html', size=(800,800), port=0)

except Exception as e:
    print(e)
