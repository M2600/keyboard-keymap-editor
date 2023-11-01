
const keyCapWidth = 54;
const keyCapHeight = 54;



eel.expose(keyBoard_bg_resize);
function keyBoard_bg_resize() {
    let maxKeyPosX = 0;
    let maxKeyPosY = 0;
    keyboardBg = document.getElementById('keyboard-bg');
    keyBorders = keyboardBg.getElementsByClassName('key-border');

    // No key exists and keyboard-bg resize to 1 x 1 size.
    if (keyBorders.length == 0) {
        keyboardBg.style.width = keyCapWidth + 'px';
        keyboardBg.style.height = keyCapHeight + 'px';
    }
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
function createKey(id, xrate, yrate, wrate, hrate, rotate = 0, ranchorX = 0, ranchorY = 0) {

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


eel.expose(createKeyboard);
function createKeyboard(layout_name) {
    getLayout(layout_name).then((value) => {
        let layout = value;
        if (typeof layout !== 'object') {
            return;
        }
        clearKeyboard();
        layout.forEach((e, i) => {
            e.forEach((e, j) => {
                if (e.length < 4) {
                    console.log('warning: key ' + i + ',' + j + ' is not enough length. Skip this key.');
                }
                else if (e.length < 7){
                    e.concat([0, 0, 0]);
                }
                createKey(String(i) + String(j), e[0], e[1], e[2], e[3], rotate = e[4], ranchorX = e[5], ranchorY = e[6]);
    })});
    keyBoard_bg_resize();
    });
}

eel.expose(clearKeyboard)
function clearKeyboard(){
    const keyboardBg = document.getElementById('keyboard-bg');
    let keys = keyboardBg.getElementsByClassName('key');
    while (keys.length > 0) {
        keyboardBg.removeChild(keys[0]);
    };
    keyBoard_bg_resize();
}

eel.expose(justOutput);
function justOutput(val) {
    console.log(val);
}




async function pythonPrint() {
    let ret = await eel.just_print()
    console.log(ret);
}

async function getlayouts() {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let layoutList = await eel.get_layout_list('_')()
    console.log(layoutList);
    return layoutList;
}

async function getLayout(layoutName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let layout = await eel.get_layout('_', layoutName)();
    console.log(layout);
    return layout;
}

async function loadKeymap(keymapName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let ret = await eel.load_keymap('_', keymapName)();
    console.log(ret);
}

async function saveKeymap(keymap, kaymapName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let ret = await eel.save_keymap('_', keymap, kaymapName)();
    console.log(ret);
}

function main(){
    
}

main();