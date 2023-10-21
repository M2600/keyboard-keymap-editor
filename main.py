

'''keyMap = [
    # left
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T, KEY_LPRN, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_LCBR, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, ____, NONE],
    [KEY_LCTL, KEY_LGUI, KEY_FN, KEY_LALT, KEY_RAIS, KEY_RSFT, KEY_DEL, ____],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_SPC, NONE],

    # leftFn
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_MUTE,
        KEY_VOLUMEDOWN, KEY_VOLUMEUP, NONE],
    [KEY_CPFL, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_CLPF, KEY_Q, KEY_W, KEY_E, KEY_ARLS, KEY_T, KEY_LPRN, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_LCBR, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, ____, NONE],
    [KEY_LCTL, KEY_LGUI, KEY_FN, KEY_LALT, KEY_RAIS, KEY_RSFT, KEY_DEL, ____],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_KLCK, NONE],

    # leftRais
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T, KEY_LPRN, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_LCBR, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, ____, NONE],
    [KEY_LCTL, KEY_LGUI, KEY_FN, KEY_LALT, KEY_RAIS, KEY_RSFT, KEY_DEL, ____],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_SPC, NONE],

    # leftLower
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_MUP, KEY_R, KEY_T, KEY_LPRN, NONE],
    [KEY_CAPS, KEY_A, KEY_MLFT, KEY_MDWN, KEY_MRIT, KEY_G, KEY_LCBR, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, ____, NONE],
    [KEY_LCTL, KEY_LGUI, KEY_FN, KEY_LALT, KEY_RAIS, KEY_MLCL, KEY_MHUP, KEY_MHDW],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_MRCL, NONE],

    # leftGame
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T, KEY_FU1, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_FU2, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, KEY_FU3, NONE],
    [KEY_LCTL, ____, KEY_FN, KEY_LALT, KEY_C, KEY_FU4, KEY_M, KEY_FU6],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_SPC, NONE],

    # leftGameFn
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_MUTE,
        KEY_VOLUMEDOWN, KEY_VOLUMEUP, NONE],
    [KEY_CPFL, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_CLPF, KEY_Q, KEY_W, KEY_E, KEY_ARLS, KEY_T, KEY_FU1, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_FU2, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, KEY_FU3, NONE],
    [KEY_LCTL, ____, KEY_FN, KEY_LALT, KEY_C, KEY_FU4, KEY_M, KEY_FU6],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_KLCK, NONE],

    # leftGameRAIS
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T, KEY_FU1, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_FU2, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, KEY_FU3, NONE],
    [KEY_LCTL, ____, KEY_FN, KEY_LALT, KEY_C, KEY_FU4, KEY_M, KEY_FU6],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_SPC, NONE],

    # leftGameLower
    [KEY_ESCP, KEY_FU1, KEY_FU2, KEY_FU3, KEY_FU4, KEY_FU5, KEY_FU6, NONE],
    [KEY_GRV, KEY_1, KEY_2, KEY_3, KEY_4, KEY_5, KEY_6, NONE],
    [KEY_TB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T, KEY_FU1, NONE],
    [KEY_CAPS, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G, KEY_FU2, NONE],
    [KEY_LSFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B, KEY_FU3, NONE],
    [KEY_LCTL, ____, KEY_FN, KEY_LALT, KEY_C, KEY_FU4, KEY_M, KEY_FU6],
    [NONE, NONE, NONE, NONE, NONE, NONE, KEY_SPC, NONE],

    # right
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, KEY_KLCK, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_RPRN, KEY_Y, KEY_U, KEY_I, KEY_O, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_RCBR, KEY_H, KEY_J, KEY_K, KEY_L, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [____, KEY_N, KEY_M, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [KEY_ENT, NONE, NONE, NONE, NONE, NONE, NONE, NONE,],

    # rightFn
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_MUTE,
        KEY_VOLUMEDOWN, KEY_VOLUMEUP, NONE, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_HOM],
    [KEY_RPRN, KEY_Y, KEY_U, KEY_INS, KEY_O, KEY_PSCR, KEY_LCBR, KEY_PGUP],
    [KEY_RCBR, KEY_H, KEY_J, KEY_K, KEY_L, KEY_SCLN, KEY_QUOT, KEY_PGDN],
    [____, KEY_N, KEY_MAIL, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_EN],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightRais
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, KEY_KLCK, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_RPRN, KEY_Y, KEY_U, KEY_UP, KEY_O, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_RCBR, KEY_H, KEY_LEFT, KEY_DOWN, KEY_RGHT, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [____, KEY_N, KEY_M, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightLower
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, NONE, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_RPRN, KEY_Y, KEY_KEYPAD_7, KEY_KEYPAD_8,
        KEY_KEYPAD_9, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_RCBR, KEY_H, KEY_KEYPAD_4, KEY_KEYPAD_5,
        KEY_KEYPAD_6, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [____, KEY_KEYPAD_0, KEY_KEYPAD_1, KEY_KEYPAD_2,
        KEY_KEYPAD_3, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightGame
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, KEY_KLCK, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_FU7, KEY_Y, KEY_U, KEY_I, KEY_O, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_FU8, KEY_H, KEY_J, KEY_K, KEY_L, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [KEY_FU9, KEY_N, KEY_M, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightGameFn
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_MUTE,
        KEY_VOLUMEDOWN, KEY_VOLUMEUP, NONE, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_HOM],
    [KEY_FU7, KEY_Y, KEY_U, KEY_INS, KEY_O, KEY_PSCR, KEY_LCBR, KEY_PGUP],
    [KEY_FU8, KEY_H, KEY_J, KEY_K, KEY_L, KEY_SCLN, KEY_QUOT, KEY_PGDN],
    [KEY_FU9, KEY_N, KEY_MAIL, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_EN],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightGameRais
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, NONE, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_FU7, KEY_Y, KEY_U, KEY_I, KEY_O, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_FU8, KEY_H, KEY_J, KEY_K, KEY_L, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [KEY_FU9, KEY_N, KEY_M, KEY_COMM, KEY_DOT, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ],

    # rightGameLower
    [KEY_FU7, KEY_FU8, KEY_FU9, KEY_FU10, KEY_FU11, KEY_FU12, NONE, KEY_CPFL],
    [KEY_BSLS, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINS, KEY_EQL, KEY_BSPC],
    [KEY_FU7, KEY_Y, KEY_KEYPAD_7, KEY_KEYPAD_8,
        KEY_KEYPAD_9, KEY_P, KEY_LBRC, KEY_RBRC],
    [KEY_FU8, KEY_H, KEY_KEYPAD_4, KEY_KEYPAD_5,
        KEY_KEYPAD_6, KEY_SCLN, KEY_QUOT, KEY_ENT],
    [KEY_FU9, KEY_KEYPAD_0, KEY_KEYPAD_1, KEY_KEYPAD_2,
        KEY_KEYPAD_3, KEY_SLSH, KEY_UP, KEY_RSFT],
    [KEY_BSPC, KEY_LSFT, KEY_LOWE, KEY_RALT, KEY_FN, KEY_LEFT, KEY_DOWN, KEY_RGHT],
    [
        KEY_ENT,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
        NONE,
    ]]'''



import pyduinocli 
import os



class keymap_generator:

    def __init__(self):
        self.keymapTemplata_dir = 'keymap_template'
        self.keymapRow = 7 * 16  # 7 rows each 16 profiles
        self.keymapCol = 8       # 8 columns    
        # Read keymap template
        with open(self.keymapTemplata_dir, 'r') as f:
            self.keymapTemplate = f.read()

    
    def generate_keymap_file(self, keymap):
        # Check keymap size
        if len(keymap) != self.keymapRow:
            print('keymap row size error')
            return
        else:
            for row in keymap:
                if isinstance(row, list) or len(row) != self.keymapCol:
                    print('keymap column size error')
                    return
        # Generate keymap file
        keymap_text = self.keymapTemplate + self.generate_cpp_array_from_python_array('const byte keyMap', keymap)
        with open('keymap.h', 'w') as f:
            f.write(keymap_text)

    def generate_cpp_array_from_python_array(self, arrayName, keymap):
        self.cpp_array = ''
        self.array_size = ''
        self.get_array_size(keymap)
        self.cpp_array += arrayName + self.array_size + ' = \n'
        self.convert_array(keymap)
        self.cpp_array = self.cpp_array[:-2] + ';\n'  # Remove last comma if last element.
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
        self.cpp_array = self.cpp_array[:-2] # Remove last comma if last element.
        self.cpp_array += '},\n'


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def main():
    generater = keymap_generator()
    generater.generate_keymap_file(arr)

    if os.name == 'nt':
        arduinoCli_path = 'arduino-cli/arduino-cli.exe'
    elif os.name == 'posix':
        arduinoCli_path = 'arduino-cli'
    arduino = pyduinocli.Arduino(arduinoCli_path)
    bords = arduino.board.list()
    print(bords)

if __name__ == '__main__':
    main()
