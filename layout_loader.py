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


separate_layout = [
    #left
    [[0, 0, 1, 1],     [1.5, 0, 1, 1],   [2.5, 0, 1, 1],     [3.5, 0, 1, 1],    [4.5, 0, 1, 1],                    [5.5, 0, 1, 1],                     [6.5, 0, 1, 1],                   []                               ],
    [[0.5, 1.5, 1, 1], [1.5, 1.5, 1, 1], [2.5, 1.375, 1, 1], [3.5, 1.25, 1, 1], [4.5, 1.375, 1, 1],                [5.5, 1.5, 1, 1],                   [6.5, 1.5, 1, 1],                 []                               ],
    [[0, 2.5, 1.5, 1], [1.5, 2.5, 1, 1], [2.5, 2.375, 1, 1], [3.5, 2.25, 1, 1], [4.5, 2.375, 1, 1],                [5.5, 2.5, 1, 1],                   [6.5, 2.5, 1, 1],                 []                               ],
    [[0, 3.5, 1.5, 1], [1.5, 3.5, 1, 1], [2.5, 3.375, 1, 1], [3.5, 3.25, 1, 1], [4.5, 3.375, 1, 1],                [5.5, 3.5, 1, 1],                   [6.5, 3.5, 1, 1],                 []                               ],
    [[0, 4.5, 1.5, 1], [1.5, 4.5, 1, 1], [2.5, 4.375, 1, 1], [3.5, 4.25, 1, 1], [4.5, 4.375, 1, 1],                [5.5, 4.5, 1, 1],                   [6.5, 4.5, 1, 1],                 []                               ],
    [[0, 5.5, 1.5, 1], [1.5, 5.5, 1, 1], [2.5, 5.375, 1, 1], [3.5, 5.25, 1, 1], [4.75, 5.63, 1, 1, 15, 5.75, 5.5], [6.25, 5.75, 1, 1.5, 30, 6.5, 5.5], [7.25, 5.25, 1, 1, 30, 6.5, 5.5], [8.25, 5.25, 1, 1, 30, 6.5, 5.5] ],
    [[],               [],               [],                 [],                [],                                [],                                 [7.25, 6.25, 2, 1, 30, 6.5, 5.5], []                               ],

    #right
    [[12, 0, 1, 1],                      [13, 0, 1, 1],                        [14, 0, 1, 1],                      [15, 0, 1, 1],     [16, 0, 1, 1],       [17, 0, 1, 1],       [18.5, 0, 1, 1],     [19.5, 0, 1, 1]    ],
    [[12, 1.5, 1, 1],                    [13, 1.5, 1, 1],                      [14, 1.375, 1, 1],                  [15, 1.25, 1, 1],  [16, 1.375, 1, 1],   [17, 1.5, 1, 1],     [18, 1.75, 1, 1],    [19, 1.75, 1.5, 1] ],
    [[12, 2.5, 1, 1],                    [13, 2.5, 1, 1],                      [14, 2.375, 1, 1],                  [15, 2.25, 1, 1],  [16, 2.375, 1, 1],   [17, 2.5, 1, 1],     [18, 2.75, 1, 1],    [19, 2.75, 1.5, 1] ],
    [[12, 3.5, 1, 1],                    [13, 3.5, 1, 1],                      [14, 3.375, 1, 1],                  [15, 3.25, 1, 1],  [16, 3.375, 1, 1],   [17, 3.5, 1, 1],     [18, 3.75, 1, 1],    [19, 3.75, 1.5, 1] ],
    [[12, 4.5, 1, 1],                    [13, 4.5, 1, 1],                      [14, 4.375, 1, 1],                  [15, 4.25, 1, 1],  [16, 4.375, 1, 1],   [17, 4.5, 1, 1],     [18, 4.75, 1, 1],    [19, 4.75, 1.5, 1] ],
    [[10.25, 5.25, 2, 1, -30, 13, 5.5],  [12.25, 5.75, 1, 1.5, -30, 13, 5.5],  [13.75, 5.88, 1, 1, -15, 13, 5.5],  [15, 5.25, 1, 1],  [16, 5.375, 1, 1],   [17, 5.75, 1, 1],    [18, 5.75, 1, 1],    [19, 5.75, 1, 1]   ],
    [[10.25, 6.25, 2, 1, -30, 13, 5.5],  [],                                   [],                                 [],                [],                  [],                  [],                  [],                ]
]


separate_keymap = {
        'name': 'separate',
        'description': 'separate keyboard.',
        'layout': 'separate',
        'mappingRule': [
            ['keymap', 'default', 'default', 0],
            ['keymap', 'default', 'default', 1],
            ['keymap', 'default', 'default', 2],
            ['keymap', 'default', 'default', 3],
            ['keymap', 'default', 'default', 4],
            ['keymap', 'default', 'default', 5],
            ['keymap', 'default', 'default', 6],
            ['keymap', 'default', 'fn', 0],
            ['keymap', 'default', 'fn', 1],
            ['keymap', 'default', 'fn', 2],
            ['keymap', 'default', 'fn', 3],
            ['keymap', 'default', 'fn', 4],
            ['keymap', 'default', 'fn', 5],
            ['keymap', 'default', 'fn', 6],
            ['keymap', 'default', 'raise', 0],
            ['keymap', 'default', 'raise', 1],
            ['keymap', 'default', 'raise', 2],
            ['keymap', 'default', 'raise', 3],
            ['keymap', 'default', 'raise', 4],
            ['keymap', 'default', 'raise', 5],
            ['keymap', 'default', 'raise', 6],
            ['keymap', 'default', 'lower', 0],
            ['keymap', 'default', 'lower', 1],
            ['keymap', 'default', 'lower', 2],
            ['keymap', 'default', 'lower', 3],
            ['keymap', 'default', 'lower', 4],
            ['keymap', 'default', 'lower', 5],
            ['keymap', 'default', 'lower', 6],
            ['keymap', 'game', 'default', 0],
            ['keymap', 'game', 'default', 1],
            ['keymap', 'game', 'default', 2],
            ['keymap', 'game', 'default', 3],
            ['keymap', 'game', 'default', 4],
            ['keymap', 'game', 'default', 5],
            ['keymap', 'game', 'default', 6],
            ['keymap', 'game', 'fn', 0],
            ['keymap', 'game', 'fn', 1],
            ['keymap', 'game', 'fn', 2],
            ['keymap', 'game', 'fn', 3],
            ['keymap', 'game', 'fn', 4],
            ['keymap', 'game', 'fn', 5],
            ['keymap', 'game', 'fn', 6],
            ['keymap', 'game', 'raise', 0],
            ['keymap', 'game', 'raise', 1],
            ['keymap', 'game', 'raise', 2],
            ['keymap', 'game', 'raise', 3],
            ['keymap', 'game', 'raise', 4],
            ['keymap', 'game', 'raise', 5],
            ['keymap', 'game', 'raise', 6],
            ['keymap', 'game', 'lower', 0],
            ['keymap', 'game', 'lower', 1],
            ['keymap', 'game', 'lower', 2],
            ['keymap', 'game', 'lower', 3],
            ['keymap', 'game', 'lower', 4],
            ['keymap', 'game', 'lower', 5],
            ['keymap', 'game', 'lower', 6],
            ['keymap', 'default', 'default', 7],
            ['keymap', 'default', 'default', 8],
            ['keymap', 'default', 'default', 9],
            ['keymap', 'default', 'default', 10],
            ['keymap', 'default', 'default', 11],
            ['keymap', 'default', 'default', 12],
            ['keymap', 'default', 'default', 13],
            ['keymap', 'default', 'fn', 7],
            ['keymap', 'default', 'fn', 8],
            ['keymap', 'default', 'fn', 9],
            ['keymap', 'default', 'fn', 10],
            ['keymap', 'default', 'fn', 11],
            ['keymap', 'default', 'fn', 12],
            ['keymap', 'default', 'fn', 13],
            ['keymap', 'default', 'raise', 7],
            ['keymap', 'default', 'raise', 8],
            ['keymap', 'default', 'raise', 9],
            ['keymap', 'default', 'raise', 10],
            ['keymap', 'default', 'raise', 11],
            ['keymap', 'default', 'raise', 12],
            ['keymap', 'default', 'raise', 13],
            ['keymap', 'default', 'lower', 7],
            ['keymap', 'default', 'lower', 8],
            ['keymap', 'default', 'lower', 9],
            ['keymap', 'default', 'lower', 10],
            ['keymap', 'default', 'lower', 11],
            ['keymap', 'default', 'lower', 12],
            ['keymap', 'default', 'lower', 13],
            ['keymap', 'game', 'default', 7],
            ['keymap', 'game', 'default', 8],
            ['keymap', 'game', 'default', 9],
            ['keymap', 'game', 'default', 10],
            ['keymap', 'game', 'default', 11],
            ['keymap', 'game', 'default', 12],
            ['keymap', 'game', 'default', 13],
            ['keymap', 'game', 'fn', 7],
            ['keymap', 'game', 'fn', 8],
            ['keymap', 'game', 'fn', 9],
            ['keymap', 'game', 'fn', 10],
            ['keymap', 'game', 'fn', 11],
            ['keymap', 'game', 'fn', 12],
            ['keymap', 'game', 'fn', 13],
            ['keymap', 'game', 'raise', 7],
            ['keymap', 'game', 'raise', 8],
            ['keymap', 'game', 'raise', 9],
            ['keymap', 'game', 'raise', 10],
            ['keymap', 'game', 'raise', 11],
            ['keymap', 'game', 'raise', 12],
            ['keymap', 'game', 'raise', 13],
            ['keymap', 'game', 'lower', 7],
            ['keymap', 'game', 'lower', 8],
            ['keymap', 'game', 'lower', 9],
            ['keymap', 'game', 'lower', 10],
            ['keymap', 'game', 'lower', 11],
            ['keymap', 'game', 'lower', 12],
            ['keymap', 'game', 'lower', 13]
        ],
        'keymap': {
            'default': {
                'default': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'fn': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'raise': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'lower': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
            },
            'game': {
                'default': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'fn': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'raise': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
                'lower': [
                    #left
                    ['ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'NONE'],
                    ['`',   '1',  '2',  '3',  '4',  '5',  '6',  'NONE'],
                    ['TAB', 'Q',  'W',  'E',  'R',  'T',  '(',  'NONE'],
                    ['CAPS_LOCK',   'A',   'S',   'D',   'F',   'G',   '{',   'NONE'],
                    ['LEFT_SHIFT',    'Z',   'X',   'C',   'V',   'B',   '____',   'NONE'],
                    ['LEFT_CONTROL',    'LEFT_GUI',   'FN',   'LEFT_ALT',   'RAISE',   'RIGHT_SHIFT',   'DELETE',   '____' ],
                    ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'SPACE', 'NONE'],
                    #right
                    ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'DUAL_CONNECT_MODE', 'CHANGE_PROFILE'],
                    ['\\', '7',  '8',  '9',  '0',  '-',  '=',  'BACKSPACE'],
                    [')', 'Y',  'U',  'I',  'O',  'P',  '[',  ']'],
                    ['}', 'H',  'J',  'K',  'L',  ';',  '\'', 'ENTER'],
                    ['____', 'N',  'M',  ',',  '.',  '/',  'ARROW_UP', 'RIGHT_SHIFT'],
                    ['BACKSPACE', 'LEFT_SHIFT', 'LOWER', 'RIGHT_ALT', 'FN', 'ARROW_LEFT', 'ARROW_DOWN', 'ARROW_RIGHT'],
                    ['ENTER', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE']
                ],
            }
        }
    }




def main():
    # keycode_list_path = 'keycodeList.json'
    # with open(keycode_list_path, 'w') as f:
    #     json.dump(keyList, f, indent=4, sort_keys=False)
    
    with open('layouts/separate.layout', 'w') as f:
        json.dump(separate_layout, f, indent=4, sort_keys=False, separators=(',', ': '))

    with open('keymaps/separate.keymap', 'w') as f:
        json.dump(separate_keymap, f, indent=4, sort_keys=False, separators=(',', ': '))


if __name__ == '__main__':
    main()