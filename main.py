


#from arduinoUploader import arduino_uploader
#from keymapGenerator import keymap_generator
import web
import json

def main():
    #keymap_generator と arduino_uploader のサンプル

    #generater = keymap_generator(keymapTemplate_dir='keymap_template')
    #generater.generate_keymap_file(testKeyMap, 'KeyboardNico/KeyboardNico/keymap.h')

    #uploader = arduino_uploader()
    #board_index = uploader.hardware_selecter()
    #uploader.upload('KeyboardNico/KeyboardNico/KeyboardNico.ino', board_index)
    

    gui = web.web_gui()
    gui.start('main.html')



if __name__ == '__main__':
    main()
