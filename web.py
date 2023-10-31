
import eel



def keyboard_1():
    eel.createKey('11', 0, 0, 1, 1)
    eel.createKey('12', 1.5, 0, 1, 1)
    eel.createKey('13', 2.5, 0, 1, 1)
    eel.createKey('14', 3.5, 0, 1, 1)
    eel.createKey('15', 4.5, 0, 1, 1)
    eel.createKey('16', 5.5, 0, 1, 1)
    eel.createKey('17', 6.5, 0, 1, 1)

    eel.createKey('21', 0.5, 1.5, 1, 1)
    eel.createKey('22', 1.5, 1.5, 1, 1)
    eel.createKey('23', 2.5, 1.375, 1, 1)
    eel.createKey('24', 3.5, 1.25, 1, 1)
    eel.createKey('25', 4.5, 1.375, 1, 1)
    eel.createKey('26', 5.5, 1.5, 1, 1)
    eel.createKey('27', 6.5, 1.5, 1, 1)

    eel.createKey('31', 0, 2.5, 1.5, 1)
    eel.createKey('32', 1.5, 2.5, 1, 1)
    eel.createKey('33', 2.5, 2.375, 1, 1)
    eel.createKey('34', 3.5, 2.25, 1, 1)
    eel.createKey('35', 4.5, 2.375, 1, 1)
    eel.createKey('36', 5.5, 2.5, 1, 1)
    eel.createKey('37', 6.5, 2.5, 1, 1)



    eel.createKey('41', 0, 3.5, 1.5, 1)
    eel.createKey('42', 1.5, 3.5, 1, 1)
    eel.createKey('43', 2.5, 3.375, 1, 1)
    eel.createKey('44', 3.5, 3.25, 1, 1)
    eel.createKey('45', 4.5, 3.375, 1, 1)
    eel.createKey('46', 5.5, 3.5, 1, 1)
    eel.createKey('47', 6.5, 3.5, 1, 1)

    eel.createKey('51', 0, 4.5, 1.5, 1)
    eel.createKey('52', 1.5, 4.5, 1, 1)
    eel.createKey('53', 2.5, 4.375, 1, 1)
    eel.createKey('54', 3.5, 4.25, 1, 1)
    eel.createKey('55', 4.5, 4.375, 1, 1)
    eel.createKey('56', 5.5, 4.5, 1, 1)
    eel.createKey('57', 6.5, 4.5, 1, 1)

    eel.createKey('61', 0, 5.5, 1.5, 1)
    eel.createKey('62', 1.5, 5.5, 1, 1)
    eel.createKey('63', 2.5, 5.375, 1, 1)
    eel.createKey('64', 3.5, 5.25, 1, 1)
    eel.createKey('65', 4.5, 5.375, 1, 1, 15, 0.5)

    eel.createKey('101', 10, 0, 1, 1, 15)

    eel.keyBoard_bg_resize()


@eel.expose
def test(val):
    print(val)


def main():
    eel.init('web')
    # Open in default browser
    #eel.start('main.html', mode='default', size=(600, 400))

    eel.createKey('11', 0, 0, 1, 1)
    eel.createKey('12', 1, 0, 2, 1)
    eel.keyBoard_bg_resize()

    #keyboard_1()

    eel.justOutput('test')

    eel.start('main.html', size=(800, 600), block=False)
    
    while True:
        eel.sleep(10.0)
        eel.justOutput('test')


if __name__ == '__main__':
    main()