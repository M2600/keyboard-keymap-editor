import json
import web


#keyList = { 'key_name': ['label', 'key_code', 'description'], ... }
keyList = {
    'profileKeys': ['FN', 'RAISE', 'LOWER'],
    'keyList':{
        'NONE': ['', 'NONE', ''],
        '____': ['', '____', ''], # 空白キー
        'FN': ['FN', 'KEY_FN',''],
        'CHANGE_PROFILE': ['CHPRFL', 'KEY_CPFL', 'Change profile.'], # Change Profile
        'CHANGE_COLOR': ['CHCPRFL', 'KEY_CLPF', 'Change LED color.'],  # Change LED Color
        'RAISE': ['RAISE', 'KEY_RAIS', 'Keyboard\'s profile change to \"RAISE\" while holding this key.'],
        'LOWER': ['LOWER', 'KEY_LOWE', 'Keyboard\'s profile change to \"LOWER\" while holding this key.'],

        'MAIL': ['MAIL', 'KEY_MAIL', ''],
        'FOR': ['FOR', 'KEY_FOR', ''],
        'IF': ['IF', 'KEY_IF', ''],

        'MUTE_SOUND': ['MUTE', 'KEY_MUTE', ''],
        'VOLUME_UP': ['VOLUP', 'KEY_VOLUMEUP', ''],
        'VOLUME_DOWN': ['VOLDOWN', 'KEY_VOLUMEDOWN', ''],

        'MOUSE_UP': ['MUP', 'KEY_MUP', 'Mouse move up.'], # Mouse move up
        'MOUSE_DOWN': ['MDOWN', 'KEY_MDWN', 'Mouse move down.'], # Mouse move down
        'MOUSE_LEFT': ['MLEFT','KEY_MLFT', 'Mouse move left.'], # Mouse move left
        'MOUSE_RIGHT': ['MRIGHT', 'KEY_MRIT', 'Mouse move right.'], # Mouse move right
        'MOUSE_LEFT_CLICK': ['MLCLk', 'KEY_MLCL', 'Mouse left click.'], # Mouse left click
        'MOUSE_RIGHT_CLICK': ['MRCLK', 'KEY_MRCL', 'Mouse right click.'], # Mouse right click
        'MOUSE_WHEEL_UP': ['MWUP', 'KEY_MHUP', 'Mouse wheel up.'], # Mouse wheel up
        'MOUSE_WHEEL_DOWN': ['MWDOWN', 'KEY_MHDW', 'Mouse wheel down.'], # Mouse wheel down

        'DUAL_CONNECT_MODE': ['DUAL', 'KEY_KLCK', 'Mode to ensure that signals are only sent from either the left or right Arudino'], # 左右どちらかのArudinoからしか信号が送信されないようにするためのモード

        'ALL_RELEASE': ['ARELEASE', 'KEY_ARLS', 'Release all key. For development.'], # 全てのキーをリリースする

        'ENTER': ['ENTER', 'KEY_ENT', ''], # Enter
        'ESCAPE': ['ESC', 'KEY_ESCP', ''], # Escape
        'BACKSPACE': ['BACK', 'KEY_BSPC', ''], # Backspace
        'DELETE': ['DEL', 'KEY_DEL', ''], # Delete
        'TAB': ['TAB', 'KEY_TB', ''], # Tab
        'CAPS_LOCK': ['CAPS', 'KEY_CAPS', ''], # Caps Lock
        'LEFT_CONTROL': ['LCTRL', 'KEY_LCTL', ''], # Left Control
        'LEFT_SHIFT': ['LSHIFT', 'KEY_LSFT', ''], # Left Shift
        'LEFT_ALT': ['LALT', 'KEY_LALT', ''], # Left Alt
        'LEFT_GUI': ['LGUI', 'KEY_LGUI', ''], # Left GUI
        'RIGHT_CONTROL': ['RCTRL', 'KEY_RCTL', ''], # Right Control
        'RIGHT_SHIFT': ['RSHIFT', 'KEY_RSFT', ''], # Right Shift
        'RIGHT_ALT': ['RALT', 'KEY_RALT', ''], # Right Alt
        'RIGHT_GUI': ['RGUI', 'KEY_RGUI', ''], # Right GUI

        'PRINT_SCREEN': ['PSCR', 'KEY_PSCR', ''], # Print Screen
        'SCROLL_LOCK': ['SCRLK', 'KEY_SLCK', ''], # Scroll Lock
        'PAUSE': ['PAUSE', 'KEY_PAUS', ''], # Pause
        'INSERT': ['INS', 'KEY_INS', ''], # Insert

        'PAGE_UP': ['PGUP', 'KEY_PGUP', ''], # Page Up
        'PAGE_DOWN': ['PGDOWN', 'KEY_PGDN', ''], # Page Down
        'HOME': ['HOME', 'KEY_HOM', ''], # Home
        'END': ['END', 'KEY_EN', ''], # End
        'ARROW_UP': ['UP', 'KEY_UP', ''], # Arrow Up
        'ARROW_DOWN': ['DOWN', 'KEY_DOWN', ''], # Arrow Down
        'ARROW_LEFT': ['LEFT', 'KEY_LEFT', ''], # Arrow Left
        'ARROW_RIGHT': ['RIGHT', 'KEY_RIGHT', ''], # Arrow Right

        '0': ['0', 'KEY_0', ''], # 0
        '1': ['1', 'KEY_1', ''], # 1
        '2': ['2', 'KEY_2', ''], # 2
        '3': ['3', 'KEY_3', ''], # 3
        '4': ['4', 'KEY_4', ''], # 4
        '5': ['5', 'KEY_5', ''], # 5
        '6': ['6', 'KEY_6', ''], # 6
        '7': ['7', 'KEY_7', ''], # 7
        '8': ['8', 'KEY_8', ''], # 8
        '9': ['9', 'KEY_9', ''], # 9

        '!': ['!', 'KEY_EXLM', ''], # !
        '@': ['@', 'KEY_AT', ''], # @
        '#': ['#', 'KEY_HASH', ''], # #
        '$': ['$', 'KEY_DLR', ''], # $
        '%': ['%', 'KEY_PERC', ''], # %
        '^': ['^', 'KEY_CIRC', ''], # ^
        '&': ['&', 'KEY_AMPR', ''], # &
        '*': ['*', 'KEY_ASTR', ''], # *
        '(': ['(', 'KEY_LPRN', ''], # (
        ')': [')', 'KEY_RPRN', ''], # )

        '-': ['-', 'KEY_MINS', ''], # -
        '=': ['=', 'KEY_EQL', ''], # =
        'SPACE': ['SPACE', 'KEY_SPC', ''], # Space
        '[': ['[', 'KEY_LBRC', ''], # [
        ']': [']', 'KEY_RBRC', ''], # ]
        '{': ['{', 'KEY_LCBR', ''], # {
        '}': ['}', 'KEY_RCBR', ''], # }
        '\\': ['\\', 'KEY_BSLS', ''], # \
        ';': [';', 'KEY_SCLN', ''], # ;
        '\'': ['\'', 'KEY_QUOT', ''], # '
        '`': ['`', 'KEY_GRV', ''], # `
        ',': [',', 'KEY_COMM', ''], # ,
        '.': ['.', 'KEY_DOT', ''], # .
        '/': ['/', 'KEY_SLSH', ''], # /

        'A': ['A', 'KEY_A', ''], # A
        'B': ['B', 'KEY_B', ''], # B
        'C': ['C', 'KEY_C', ''], # C
        'D': ['D', 'KEY_D', ''], # D
        'E': ['E', 'KEY_E', ''], # E
        'F': ['F', 'KEY_F', ''], # F
        'G': ['G', 'KEY_G', ''], # G
        'H': ['H', 'KEY_H', ''], # H
        'I': ['I', 'KEY_I', ''], # I
        'J': ['J', 'KEY_J', ''], # J
        'K': ['K', 'KEY_K', ''], # K
        'L': ['L', 'KEY_L', ''], # L
        'M': ['M', 'KEY_M', ''], # M
        'N': ['N', 'KEY_N', ''], # N
        'O': ['O', 'KEY_O', ''], # O
        'P': ['P', 'KEY_P', ''], # P
        'Q': ['Q', 'KEY_Q', ''], # Q
        'R': ['R', 'KEY_R', ''], # R
        'S': ['S', 'KEY_S', ''], # S
        'T': ['T', 'KEY_T', ''], # T
        'U': ['U', 'KEY_U', ''], # U
        'V': ['V', 'KEY_V', ''], # V
        'W': ['W', 'KEY_W', ''], # W
        'X': ['X', 'KEY_X', ''], # X
        'Y': ['Y', 'KEY_Y', ''], # Y
        'Z': ['Z', 'KEY_Z', ''], # Z

        'F1': ['F1', 'KEY_FU1', ''], # F1
        'F2': ['F2', 'KEY_FU2', ''], # F2
        'F3': ['F3', 'KEY_FU3', ''], # F3
        'F4': ['F4', 'KEY_FU4', ''], # F4
        'F5': ['F5', 'KEY_FU5', ''], # F5
        'F6': ['F6', 'KEY_FU6', ''], # F6
        'F7': ['F7', 'KEY_FU7', ''], # F7
        'F8': ['F8', 'KEY_FU8', ''], # F8
        'F9': ['F9', 'KEY_FU9', ''], # F9
        'F10': ['F10', 'KEY_FU10', ''], # F10
        'F11': ['F11', 'KEY_FU11', ''], # F11
        'F12': ['F12', 'KEY_FU12', ''], # F12
        'F13': ['F13', 'KEY_FU13', ''], # F13
        'F14': ['F14', 'KEY_FU14', ''], # F14
        'F15': ['F15', 'KEY_FU15', ''], # F15
        'F16': ['F16', 'KEY_FU16', ''], # F16
        'F17': ['F17', 'KEY_FU17', ''], # F17
        'F18': ['F18', 'KEY_FU18', ''], # F18
        'F19': ['F19', 'KEY_FU19', ''], # F19
        'F20': ['F20', 'KEY_FU20', ''], # F20
        'F21': ['F21', 'KEY_FU21', ''], # F21
        'F22': ['F22', 'KEY_FU22', ''], # F22
        'F23': ['F23', 'KEY_FU23', ''], # F23
        'F24': ['F24', 'KEY_FU24', ''], # F24

        'KEYPAD_0': ['KP0', 'KEY_KEYPAD_0', ''], # Keypad 0
        'KEYPAD_1': ['KP1', 'KEY_KEYPAD_1', ''], # Keypad 1
        'KEYPAD_2': ['KP2', 'KEY_KEYPAD_2', ''], # Keypad 2
        'KEYPAD_3': ['KP3', 'KEY_KEYPAD_3', ''], # Keypad 3
        'KEYPAD_4': ['KP4', 'KEY_KEYPAD_4', ''], # Keypad 4
        'KEYPAD_5': ['KP5', 'KEY_KEYPAD_5', ''], # Keypad 5
        'KEYPAD_6': ['KP6', 'KEY_KEYPAD_6', ''], # Keypad 6
        'KEYPAD_7': ['KP7', 'KEY_KEYPAD_7', ''], # Keypad 7
        'KEYPAD_8': ['KP8', 'KEY_KEYPAD_8', ''], # Keypad 8
        'KEYPAD_9': ['KP9', 'KEY_KEYPAD_9', ''], # Keypad 9

        'KEYPAD_DECIMAL': ['KP.', 'KEY_KEYPAD_DECIMAL', ''], # Keypad .
        'KEYPAD_ENTER': ['KPENT', 'KEY_KEYPAD_ENTER', ''], # Keypad Enter
        'KEYPAD_PLUS': ['KP+', 'KEY_KEYPAD_PLUS', ''], # Keypad +
        'KEYPAD_MINUS': ['KP-', 'KEY_KEYPAD_MINUS', ''], # Keypad -
        'KEYPAD_MULTIPLY': ['KP*', 'KEY_KEYPAD_MULTIPLY', ''], # Keypad *
        'KEYPAD_DIVIDE': ['KP/', 'KEY_KEYPAD_DIVIDE', ''], # Keypad /
        'KEYPAD_NUM_LOCK': ['KPNUM', 'KEY_KEYPAD_NUMLOCK', ''] # Keypad Num Lock
    }
}


"""keyboard_layout = [
    #left
    [[0, 0, 1, 1],  [1.5, 0, 1, 1], [2.5, 0, 1, 1], [3.5, 0, 1, 1],  KEY_FU4,  KEY_FU5,  KEY_FU6,  NONE     ],
    [KEY_GRV,  KEY_1,    KEY_2,    KEY_3,    KEY_4,    KEY_5,    KEY_6,    NONE     ],
    [KEY_TB,   KEY_Q,    KEY_W,    KEY_E,    KEY_R,    KEY_T,    KEY_LPRN, NONE     ],
    [KEY_CAPS, KEY_A,    KEY_S,    KEY_D,    KEY_F,    KEY_G,    KEY_LCBR, NONE     ],
    [KEY_LSFT, KEY_Z,    KEY_X,    KEY_C,    KEY_V,    KEY_B,    ____,     NONE     ],
    [KEY_LCTL, KEY_LGUI, KEY_FN,   KEY_LALT, KEY_RAIS, KEY_RSFT, KEY_DEL,  ____     ],
    [NONE,     NONE,     NONE,     NONE,     NONE,     NONE,     KEY_SPC,  NONE     ]
]"""




def main():
    keycode_list_path = 'keycodeList.json'
    with open(keycode_list_path, 'w') as f:
        json.dump(keyList, f, indent=4, sort_keys=False)
    
    


if __name__ == '__main__':
    main()