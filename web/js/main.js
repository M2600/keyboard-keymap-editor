
//keyName = { 'key_name': ['label', 'key_code', 'description'], ... }
var keyName = {
    'NONE': ['NONE', 'NONE', ''],
    'FN': ['FN', 'KEY_FN',''],
    'CHANGE_PROFILE': ['CHPRFL', 'KEY_CPFL', 'Change profile.'], // Change Profile
    'CHANGE_COLOR': ['CHCPRFL', 'KEY_CLPF', 'Change LED color.'],  // Change LED Color
    'RAISE': ['RAISE', 'KEY_RAIS', 'Keyboard\'s profile change to \"RAISE\" while holding this key.'],
    'LOWER': ['LOWER', 'KEY_LOWE', 'Keyboard\'s profile change to \"LOWER\" while holding this key.'],
    
    'MAIL': ['MAIL', 'KEY_MAIL', ''],
    'FOR': ['FOR', 'KEY_FOR', ''],
    'IF': ['IF', 'KEY_IF', ''],

    'MUTE_SOUND': ['MUTE', 'KEY_MUTE', ''],
    'VOLUME_UP': ['VOLUP', 'KEY_VOLUMEUP', ''],
    'VOLUME_DOWN': ['VOLDOWN', 'KEY_VOLUMEDOWN', ''],

    'MOUSE_UP': ['MUP', 'KEY_MUP', 'Mouse move up.'], // Mouse move up
    'MOUSE_DOWN': ['MDOWN', 'KEY_MDWN', 'Mouse move down.'], // Mouse move down
    'MOUSE_LEFT': ['MLEFT','KEY_MLFT', 'Mouse move left.'], // Mouse move left
    'MOUSE_RIGHT': ['MRIGHT', 'KEY_MRIT', 'Mouse move right.'], // Mouse move right
    'MOUSE_LEFT_CLICK': ['MLCLk', 'KEY_MLCL', 'Mouse left click.'], // Mouse left click
    'MOUSE_RIGHT_CLICK': ['MRCLK', 'KEY_MRCL', 'Mouse right click.'], // Mouse right click
    'MOUSE_WHEEL_UP': ['MWUP', 'KEY_MHUP', 'Mouse wheel up.'], // Mouse wheel up
    'MOUSE_WHEEL_DOWN': ['MWDOWN', 'KEY_MHDW', 'Mouse wheel down.'], // Mouse wheel down

    'DUAL_CONNECT_MODE': ['DUAL', 'KEY_KLCK', ''], // 左右どちらかのArudinoからしか信号が送信されないようにするためのモード

    'ALL_RELEASE': ['ARELEASE', 'KEY_ARLS', 'Release all key. For development.'], // 全てのキーをリリースする

    'ENTER': ['ENTER', 'KEY_ENT', ''], // Enter
    'ESCAPE': ['ESC', 'KEY_ESCP', ''], // Escape
    'BACKSPACE': ['BACK', 'KEY_BSPC', ''], // Backspace
    'DELETE': ['DEL', 'KEY_DEL', ''], // Delete
    'TAB': ['TAB', 'KEY_TB', ''], // Tab
    'CAPS_LOCK': ['CAPS', 'KEY_CAPS', ''], // Caps Lock
    'LEFT_CONTROL': ['LCTRL', 'KEY_LCTL', ''], // Left Control
    'LEFT_SHIFT': ['LSHIFT', 'KEY_LSFT', ''], // Left Shift
    'LEFT_ALT': ['LALT', 'KEY_LALT', ''], // Left Alt
    'LEFT_GUI': ['LGUI', 'KEY_LGUI', ''], // Left GUI
    'RIGHT_CONTROL': ['RCTRL', 'KEY_RCTL', ''], // Right Control
    'RIGHT_SHIFT': ['RSHIFT', 'KEY_RSFT', ''], // Right Shift
    'RIGHT_ALT': ['RALT', 'KEY_RALT', ''], // Right Alt
    'RIGHT_GUI': ['RGUI', 'KEY_RGUI', ''], // Right GUI

    'PRINT_SCREEN': ['PSCR', 'KEY_PSCR', ''], // Print Screen
    'SCROLL_LOCK': ['SCRLK', 'KEY_SLCK', ''], // Scroll Lock
    'PAUSE': ['PAUSE', 'KEY_PAUS', ''], // Pause
    'INSERT': ['INS', 'KEY_INS', ''], // Insert

    'PAGE_UP': ['PGUP', 'KEY_PGUP', ''], // Page Up
    'PAGE_DOWN': ['PGDOWN', 'KEY_PGDN', ''], // Page Down
    'HOME': ['HOME', 'KEY_HOM', ''], // Home
    'END': ['END', 'KEY_EN', ''], // End
    'ARROW_UP': ['UP', 'KEY_UP', ''], // Arrow Up
    'ARROW_DOWN': ['DOWN', 'KEY_DOWN', ''], // Arrow Down
    'ARROW_LEFT': ['LEFT', 'KEY_LEFT', ''], // Arrow Left
    'ARROW_RIGHT': ['RIGHT', 'KEY_RIGHT', ''], // Arrow Right

    '0': ['0', 'KEY_0', ''], // 0
    '1': ['1', 'KEY_1', ''], // 1
    '2': ['2', 'KEY_2', ''], // 2
    '3': ['3', 'KEY_3', ''], // 3
    '4': ['4', 'KEY_4', ''], // 4
    '5': ['5', 'KEY_5', ''], // 5
    '6': ['6', 'KEY_6', ''], // 6
    '7': ['7', 'KEY_7', ''], // 7
    '8': ['8', 'KEY_8', ''], // 8
    '9': ['9', 'KEY_9', ''], // 9

    '!': ['!', 'KEY_EXLM', ''], // !
    '@': ['@', 'KEY_AT', ''], // @
    '#': ['#', 'KEY_HASH', ''], // #
    '$': ['$', 'KEY_DLR', ''], // $
    '%': ['%', 'KEY_PERC', ''], // %
    '^': ['^', 'KEY_CIRC', ''], // ^
    '&': ['&', 'KEY_AMPR', ''], // &
    '*': ['*', 'KEY_ASTR', ''], // *
    '(': ['(', 'KEY_LPRN', ''], // (
    ')': [')', 'KEY_RPRN', ''], // )

    '-': ['-', 'KEY_MINS', ''], // -
    '=': ['=', 'KEY_EQL', ''], // =
    'SPACE': ['SPACE', 'KEY_SPC', ''], // Space
    '[': ['[', 'KEY_LBRC', ''], // [
    ']': [']', 'KEY_RBRC', ''], // ]
    '{': ['{', 'KEY_LCBR', ''], // {
    '}': ['}', 'KEY_RCBR', ''], // }
    '\\': ['\\', 'KEY_BSLS', ''], // \
    ';': [';', 'KEY_SCLN', ''], // ;
    '\'': ['\'', 'KEY_QUOT', ''], // '
    '`': ['`', 'KEY_GRV', ''], // `
    ',': [',', 'KEY_COMM', ''], // ,
    '.': ['.', 'KEY_DOT', ''], // .
    '/': ['/', 'KEY_SLSH', ''], // /

    'A': ['A', 'KEY_A', ''], // A
    'B': ['B', 'KEY_B', ''], // B
    'C': ['C', 'KEY_C', ''], // C
    'D': ['D', 'KEY_D', ''], // D
    'E': ['E', 'KEY_E', ''], // E
    'F': ['F', 'KEY_F', ''], // F
    'G': ['G', 'KEY_G', ''], // G
    'H': ['H', 'KEY_H', ''], // H
    'I': ['I', 'KEY_I', ''], // I
    'J': ['J', 'KEY_J', ''], // J
    'K': ['K', 'KEY_K', ''], // K
    'L': ['L', 'KEY_L', ''], // L
    'M': ['M', 'KEY_M', ''], // M
    'N': ['N', 'KEY_N', ''], // N
    'O': ['O', 'KEY_O', ''], // O
    'P': ['P', 'KEY_P', ''], // P
    'Q': ['Q', 'KEY_Q', ''], // Q
    'R': ['R', 'KEY_R', ''], // R
    'S': ['S', 'KEY_S', ''], // S
    'T': ['T', 'KEY_T', ''], // T
    'U': ['U', 'KEY_U', ''], // U
    'V': ['V', 'KEY_V', ''], // V
    'W': ['W', 'KEY_W', ''], // W
    'X': ['X', 'KEY_X', ''], // X
    'Y': ['Y', 'KEY_Y', ''], // Y
    'Z': ['Z', 'KEY_Z', ''], // Z

    'F1': ['F1', 'KEY_FU1', ''], // F1
    'F2': ['F2', 'KEY_FU2', ''], // F2
    'F3': ['F3', 'KEY_FU3', ''], // F3
    'F4': ['F4', 'KEY_FU4', ''], // F4
    'F5': ['F5', 'KEY_FU5', ''], // F5
    'F6': ['F6', 'KEY_FU6', ''], // F6
    'F7': ['F7', 'KEY_FU7', ''], // F7
    'F8': ['F8', 'KEY_FU8', ''], // F8
    'F9': ['F9', 'KEY_FU9', ''], // F9
    'F10': ['F10', 'KEY_FU10', ''], // F10
    'F11': ['F11', 'KEY_FU11', ''], // F11
    'F12': ['F12', 'KEY_FU12', ''], // F12
    'F13': ['F13', 'KEY_FU13', ''], // F13
    'F14': ['F14', 'KEY_FU14', ''], // F14
    'F15': ['F15', 'KEY_FU15', ''], // F15
    'F16': ['F16', 'KEY_FU16', ''], // F16
    'F17': ['F17', 'KEY_FU17', ''], // F17
    'F18': ['F18', 'KEY_FU18', ''], // F18
    'F19': ['F19', 'KEY_FU19', ''], // F19
    'F20': ['F20', 'KEY_FU20', ''], // F20
    'F21': ['F21', 'KEY_FU21', ''], // F21
    'F22': ['F22', 'KEY_FU22', ''], // F22
    'F23': ['F23', 'KEY_FU23', ''], // F23
    'F24': ['F24', 'KEY_FU24', ''], // F24
    
    'KEYPAD_0': ['KP0', 'KEY_KEYPAD_0', ''], // Keypad 0
    'KEYPAD_1': ['KP1', 'KEY_KEYPAD_1', ''], // Keypad 1
    'KEYPAD_2': ['KP2', 'KEY_KEYPAD_2', ''], // Keypad 2
    'KEYPAD_3': ['KP3', 'KEY_KEYPAD_3', ''], // Keypad 3
    'KEYPAD_4': ['KP4', 'KEY_KEYPAD_4', ''], // Keypad 4
    'KEYPAD_5': ['KP5', 'KEY_KEYPAD_5', ''], // Keypad 5
    'KEYPAD_6': ['KP6', 'KEY_KEYPAD_6', ''], // Keypad 6
    'KEYPAD_7': ['KP7', 'KEY_KEYPAD_7', ''], // Keypad 7
    'KEYPAD_8': ['KP8', 'KEY_KEYPAD_8', ''], // Keypad 8
    'KEYPAD_9': ['KP9', 'KEY_KEYPAD_9', ''], // Keypad 9

    'KEYPAD_DECIMAL': ['KP.', 'KEY_KEYPAD_DECIMAL', ''], // Keypad .
    'KEYPAD_ENTER': ['KPENT', 'KEY_KEYPAD_ENTER', ''], // Keypad Enter
    'KEYPAD_PLUS': ['KP+', 'KEY_KEYPAD_PLUS', ''], // Keypad +
    'KEYPAD_MINUS': ['KP-', 'KEY_KEYPAD_MINUS', ''], // Keypad -
    'KEYPAD_MULTIPLY': ['KP*', 'KEY_KEYPAD_MULTIPLY', ''], // Keypad *
    'KEYPAD_DIVIDE': ['KP/', 'KEY_KEYPAD_DIVIDE', ''], // Keypad /
    'KEYPAD_NUM_LOCK': ['KPNUM', 'KEY_KEYPAD_NUMLOCK', ''] // Keypad Num Lock
}

const keyCapWidth = 54;
const keyCapHeight = 54;

var maxKeyPosX = 0;
var maxKeyPosY = 0;

eel.expose(keyBoard_bg_resize);
function keyBoard_bg_resize() {
    keyboardBg = document.getElementById('keyboard-bg');
    keyBorders = keyboardBg.getElementsByClassName('key-border');
    //console.log(keyBorders);
    for (let i = 0; i < keyBorders.length; i++) {
        if (keyBorders[i].getBoundingClientRect().right > maxKeyPosX) {
            maxKeyPosX = keyBorders[i].getBoundingClientRect().right;
        }
        if (keyBorders[i].getBoundingClientRect().bottom > maxKeyPosY) {
            maxKeyPosY = keyBorders[i].getBoundingClientRect().bottom;
        }
    }
    // Sizing keyboard-bg element
    leftPos = keyboardBg.getBoundingClientRect().left;
    keyboardBg_leftSpace = 
        Number(window.getComputedStyle(keyboardBg).getPropertyValue('padding-left').replace('px', ''))
        + Number(window.getComputedStyle(keyboardBg).getPropertyValue('border-left-width').replace('px', ''))
        + Number(window.getComputedStyle(keyboardBg).getPropertyValue('margin-left').replace('px', ''));
    leftSpace = leftPos + keyboardBg_leftSpace;
    //console.log("left: " + leftSpace);
    topPos = keyboardBg.getBoundingClientRect().top;
    keyboardBg_topSpace = 
        Number(window.getComputedStyle(keyboardBg).getPropertyValue('padding-top').replace('px', ''))
        + Number(window.getComputedStyle(keyboardBg).getPropertyValue('border-top-width').replace('px', ''))
        + Number(window.getComputedStyle(keyboardBg).getPropertyValue('margin-top').replace('px', ''));
    topSpace = topPos + keyboardBg_topSpace;
    //console.log("top: " + topSpace);
    keyboardBg.style.width = maxKeyPosX - leftSpace + 'px';
    keyboardBg.style.height = maxKeyPosY - topSpace + 'px';
}


eel.expose(createKey);
function createKey(id, xrate, yrate, wrate, hrate, rotate = 0, ranchor = 0) {

    const x = keyCapWidth * xrate;
    const y = keyCapHeight * yrate;
    const w = keyCapWidth * wrate;
    const h = keyCapHeight * hrate;


    const keyboardBg = document.getElementById('keyboard-bg');


    const key = document.createElement('div');
    key.id = 'key-' + id;
    key.className = 'key';

    const keyCap = document.createElement('div');
    keyCap.id = 'cap-' + id;
    keyCap.className = 'key-cap';
    keyCap.style.transform = 'rotate(' + rotate + 'deg)';
    
    const keyBorder = document.createElement('div');
    keyBorder.id = 'border-' + id;
    keyBorder.className = 'key-border';
    keyBorder.style.left = x + 'px';
    keyBorder.style.top = y + 'px';
    keyBorder.style.width = w + 'px';
    keyBorder.style.height = h + 'px';
    keyBorder.style.backgroundColor = '#cccccc';
    keyBorder.style.border = 'solid 1px black';
    keyBorder.style.borderRadius = '5px';

    const keyTop = document.createElement('div');
    keyTop.id = 'top-' + id;
    keyTop.className = 'key-top';
    keyTop.style.left = x + (w * 0.25 / 2 / wrate) + 'px';
    keyTop.style.top = y + (h * 0.25 / 3 / hrate) + 'px';
    keyTop.style.width = w - (w * 0.25 / wrate) + 'px';
    keyTop.style.height = h - (h * 0.25 / hrate) + 'px';
    keyTop.style.backgroundColor = 'white';
    keyTop.style.borderStyle = 'solid';
    keyTop.style.borderColor = 'rgba(0, 0, 0, 0.1)';
    keyTop.style.borderWidth = '1px';
    keyTop.style.borderRadius = '3px';


    const keyLabel = document.createElement('div');
    keyLabel.id = 'label-' + id;
    keyLabel.className = 'key-label';
    keyLabel.style.left = x + (w * 0.25 / 2 / wrate) + 'px';
    keyLabel.style.top = y + (h * 0.25 / 3 / hrate) + 'px';
    keyLabel.style.width = w - (w * 0.25 / wrate) + 'px';
    keyLabel.style.height = h - (h * 0.25 / hrate) + 'px';
    keyLabel.style.backgroundColor = 'rgba(0, 0, 0, 0)';
    keyLabel.style.borderStyle = 'solid';
    keyLabel.style.borderColor = 'rgba(0, 0, 0, 0)';
    keyLabel.style.borderWidth = '1px';
    keyLabel.style.borderRadius = '3px';

    const Button = document.createElement('div');
    Button.id = 'button-' + id;
    Button.className = 'key-button';
    Button.style.left = x + 'px';
    Button.style.top = y + 'px';
    Button.style.width = w + 'px';
    Button.style.height = h + 'px';
    Button.style.backgroundColor = 'rgba(0, 0, 0 ,0)';
    Button.style.borderStyle = 'solid';
    Button.style.borderColor = 'rgba(0, 0, 0, 0)';
    Button.style.borderWidth = '1px';
    Button.style.borderRadius = '3px';
    Button.addEventListener('mouseover', function() {
        keyBorder.style.borderWidth = '2px';
        keyBorder.style.borderColor = 'lightgreen';
    });
    Button.addEventListener('mouseout', function() {
        keyBorder.style.borderWidth = '1px';
        keyBorder.style.borderColor = 'black';
    });
    Button.addEventListener('click', function() {
        console.log('click: ' + id);
    });


    keyboardBg.appendChild(key);
    key.appendChild(keyCap);
    keyCap.appendChild(keyBorder);
    keyCap.appendChild(keyTop);
    keyCap.appendChild(keyLabel);
    keyCap.appendChild(Button);
}

function keyboard_1(){
    
}


function testKey() {
    createKey('11', 0, 0, 1, 1);
    createKey('12', 1.5, 0, 1, 1);
    createKey('13', 2.5, 0, 1, 1);
    createKey('14', 3.5, 0, 1, 1);
    createKey('15', 4.5, 0, 1, 1);
    createKey('16', 5.5, 0, 1, 1);
    createKey('17', 6.5, 0, 1, 1);

    createKey('21', 0.5, 1.5, 1, 1);
    createKey('22', 1.5, 1.5, 1, 1);
    createKey('23', 2.5, 1.375, 1, 1);
    createKey('24', 3.5, 1.25, 1, 1);
    createKey('25', 4.5, 1.375, 1, 1);
    createKey('26', 5.5, 1.5, 1, 1);
    createKey('27', 6.5, 1.5, 1, 1);

    createKey('31', 0, 2.5, 1.5, 1);
    createKey('32', 1.5, 2.5, 1, 1);
    createKey('33', 2.5, 2.375, 1, 1);
    createKey('34', 3.5, 2.25, 1, 1);
    createKey('35', 4.5, 2.375, 1, 1);
    createKey('36', 5.5, 2.5, 1, 1);
    createKey('37', 6.5, 2.5, 1, 1);



    createKey('41', 0, 3.5, 1.5, 1);
    createKey('42', 1.5, 3.5, 1, 1);
    createKey('43', 2.5, 3.375, 1, 1);
    createKey('44', 3.5, 3.25, 1, 1);
    createKey('45', 4.5, 3.375, 1, 1);
    createKey('46', 5.5, 3.5, 1, 1);
    createKey('47', 6.5, 3.5, 1, 1);

    createKey('51', 0, 4.5, 1.5, 1);
    createKey('52', 1.5, 4.5, 1, 1);
    createKey('53', 2.5, 4.375, 1, 1);
    createKey('54', 3.5, 4.25, 1, 1);
    createKey('55', 4.5, 4.375, 1, 1);
    createKey('56', 5.5, 4.5, 1, 1);
    createKey('57', 6.5, 4.5, 1, 1);

    createKey('61', 0, 5.5, 1.5, 1);
    createKey('62', 1.5, 5.5, 1, 1);
    createKey('63', 2.5, 5.375, 1, 1);
    createKey('64', 3.5, 5.25, 1, 1);
    createKey('65', 4.5, 5.375, 1, 1, rotate=15, ranchor=0.5);

    createKey('101', 10, 0, 1, 1, rotate=15);

    keyBoard_bg_resize();
}



function main(){
    val = 1;
    
    eel.test(keyName);
}

main();