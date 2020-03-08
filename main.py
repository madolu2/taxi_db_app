import eel


try:
    eel.init('web')

    @eel.expose
    def some_func():
        return "some string"

    eel.start('index.html', size=(800,800))

except Exception as e:
    print(e)
