
const keyCapWidth = 54;
const keyCapHeight = 54;

var maxKeyPosX = 0;
var maxKeyPosY = 0;


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

        'ENTER': ['ENTER', 'KEY_ENT', ''],
        'ESCAPE': ['ESC', 'KEY_ESCP', ''],
        'BACKSPACE': ['BACK', 'KEY_BSPC', ''],
        'DELETE': ['DEL', 'KEY_DEL', ''],
        'TAB': ['TAB', 'KEY_TB', ''],
        
    }
}

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
