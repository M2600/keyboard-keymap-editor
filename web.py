
import eel
import webbrowser
import os, json
import keymapGenerator
import arduinoUploader

arduino_program_path = 'KeyboardNico/KeyboardNico/KeyboardNico.ino'

layout_dir = 'layouts/'
keymap_dir = 'keymaps/'
keycode_list_path = 'keycodeList.json'


class web_gui:
    def __init__(self):
        eel.init('web')
        
        
    ### @eel.expose付きで宣言した関数はJavaScriptから参照されるが、有効なselfは指定できないので、
    #   その関数内でselfは参照しないようにする必要がある。

    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def just_print(self, val):
        print(val)

    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def save_keymap(self, key_map, keymap_name):
        layout_name = key_map['layout']
        with open(keymap_dir + keymap_name + '.keymap', 'w') as f:
            json.dump(key_map, f, ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))
        print('save: layout: ' + layout_name + ', name: ' + keymap_name)
        return 0

    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def write(self, keymap_name, boardDict):
        keymap_file_output_path = 'KeyboardNico/KeyboardNico/keymap.h'
        keymap_generator = keymapGenerator.keymap_generator()
        uploader = arduinoUploader.arduino_uploader()

        keymap = keymap_generator.convert_keymapFile_to_keymap(keymap_dir + keymap_name + '.keymap')
        if keymap == None:
            return -1
        keymap_generator.generate_keymap_file(keymap, keymap_file_output_path)

        print('writing: ' + keymap_name + ', ' + boardDict['matching_boards'][0]['fqbn'])

        #uploader.upload(arduino_program_path, boardDict)

    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_arduino_list(self):
        print('get_arduino_list')
        uploader = arduinoUploader.arduino_uploader()
        return uploader.get_hardware_list()


    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_keycode_list(self):
        try:
            with open(keycode_list_path, 'r') as f:
                keycode_list = json.load(f)
        except FileNotFoundError as e:
            print(e)
            return 'error: keycode list file "' + keycode_list_path + '" not found.'
        print('get_keycode_list: ')
        #print(keycode_list)
        return keycode_list


    ### One argument are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_layout_list(self):
        json_list = [
            f.replace('.layout', '') for f in os.listdir(layout_dir) if f.endswith('.layout')
        ]
        print('get_layout_list: ', end='')
        print(json_list)
        return json_list
    
    ### One argument are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_layout(self, layout_name):
        print('get_layout: ' + layout_name)
        layout_path = layout_dir + layout_name + '.layout'
        try:
            with open(layout_path, 'r') as f:
                layout = json.load(f)
        except FileNotFoundError as e:
            print(e)
            return 'error: layout file "' + layout_path + '" not found.'
        return layout
    

    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_keymap_list(self):
        json_list = [
            f.replace('.keymap', '') for f in os.listdir(keymap_dir) if f.endswith('.keymap')
        ]
        print('get_keymap_list: ', end='')
        print(json_list)
        return json_list
    
    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def get_keymap(self, keymap_name):
        print('get_keymap: ' + keymap_name)
        keymap_path = keymap_dir + keymap_name + '.keymap'
        try:
            with open(keymap_path, 'r') as f:
                keymap = json.load(f)
        except FileNotFoundError as e:
            print(e)
            return 'error: keymap file "' + keymap_path + '" not found.'
        return keymap
    
    ### One argument are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def open_link_in_default_browser(self, url):
        webbrowser.open(url)


    

    def load_layout(self, layout_name):
        print('load_layout: ' + layout_name)
        eel.createKeyboard_py(layout_name)

    def start(self, html_file):
        eel.start(html_file, size=(800, 850), block=True)
        #while True:
        #    eel.sleep(1000000)

    def createKey(self, x, y, w, h, rotate=0, ranchorX=0, ranchorY=0):
        eel.createKey(x, y, w, h, rotate, ranchorX, ranchorY)

    def keyBoard_bg_resize(self):
        eel.keyBoard_bg_resize()

def main():
    pass

if __name__ == '__main__':
    main()