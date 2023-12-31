
import json

class keymap_generator:

    def __init__(self, keymapTemplate_dir  = 'keymap_template', key_list_path = 'keycodeList.json'):
        with open(key_list_path, 'r') as f:
            self.keycodeList = json.load(f)
        self.keymapTemplata_dir = keymapTemplate_dir
        self.keymapRow = 7 * 16  # 7 rows each 16 profiles
        self.keymapCol = 8       # 8 columns
        # Read keymap template
        with open(self.keymapTemplata_dir, 'r') as f:
            self.keymapTemplate = f.read()


    def convert_keymapFile_to_keymap(self, keymapFile_path):
        keymap = []
        with open(keymapFile_path, 'r') as f:
            keymapData = json.load(f)
        mappingRule = keymapData['mappingRule']
        for rule in mappingRule:
            self.ret = keymapData
            for i in rule:
                self.ret = self.ret[i]
            keymap.append(self.ret)
        print('Keymap', end='')
        print(keymap)
        #json.dump(keymap, open('test_out.json', 'w'), ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))

        # replace keymap with keycode
        for i, row in enumerate(keymap):
            for j, col in enumerate(row):
                if isinstance(col, str):
                    try:
                        keymap[i][j] = self.keycodeList['keyList'][col][1]

                    except KeyError:
                        print('Keycode not found: ' + col + ' at ' + str(i) + ', ' + str(j))
                        return -1
        print('Keymap_keycode', end='')
        print(keymap)
        return keymap


    def generate_keymap_file(self, keymap, output_dir):
        self.keymapFile_dir = output_dir
        # Check keymap size
        if len(keymap) != self.keymapRow:
            print('keymap row size error')
            return 'keymap row size error'
        else:
            for col in keymap:
                if len(col) != self.keymapCol:
                    print('keymap column size error')
                    return 'keymap column size error'
                else:
                    for key in col:
                        if isinstance(key, list):
                            print(
                                'Keymap dimension is too high. It must be 2D array.')
                            return 'Keymap dimension is too high. It must be 2D array.'
        # Generate keymap file
        keymap_text = self.keymapTemplate + \
            self.generate_cpp_array_from_python_array(
                'const byte keyMap', keymap)
        with open(self.keymapFile_dir, 'w') as f:
            f.write(keymap_text)
        print(self.keymapFile_dir + ' generated.')
        return 0

    def generate_cpp_array_from_python_array(self, arrayName, keymap):
        self.cpp_array = ''
        self.array_size = ''
        self.get_array_size(keymap)
        self.cpp_array += arrayName + self.array_size + ' = \n'
        self.convert_array(keymap)
        # Remove last comma if last element.
        self.cpp_array = self.cpp_array[:-2] + ';\n'
        return self.cpp_array

    def get_array_size(self, array):
        if isinstance(array, list):
            self.array_size += '[' + str(len(array)) + ']'
            self.get_array_size(array[0])
        else:
            return self.array_size

    def convert_array(self, array):
        self.cpp_array += '{'
        for e in array:
            if isinstance(e, list):
                self.convert_array(e)
            else:
                self.cpp_array += str(e) + ', '
        # Remove last comma if last element.
        self.cpp_array = self.cpp_array[:-2]
        self.cpp_array += '},\n'
