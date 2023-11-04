
import eel
import os, json



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
        layout_name = key_map['keymap']
        with open(keymap_dir + keymap_name + '.keymap', 'w') as f:
            json.dump(key_map, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        print('save ' + layout_name + ', ' + keymap_name)
    ### Two arguments are required when calling from Javascript. ###
    ### However, the first argument is not referenced, so set it to whatever you like. ###
    @eel.expose
    def write(self, layout_name, keymap_name):
        print('write: ' + layout_name + ', ' + keymap_name)



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
        print('get_keycode_list: ', end='')
        print(keycode_list)
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


    def load_layout(self, layout_name):
        print('load_layout: ' + layout_name)
        eel.createKeyboard_py(layout_name)

    def start(self, html_file):
        eel.start(html_file, size=(800, 600), block=False)
        while True:
            eel.sleep(1)

    def createKey(self, x, y, w, h, rotate=0, ranchorX=0, ranchorY=0):
        eel.createKey(x, y, w, h, rotate, ranchorX, ranchorY)

    def keyBoard_bg_resize(self):
        eel.keyBoard_bg_resize()

def main():
    pass

if __name__ == '__main__':
    main()