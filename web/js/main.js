
const keyCapWidth = 54;
const keyCapHeight = 54;

var currentKeymap = null;
var currentKeymapLayer = null;
var keycodeList = null;


var saveSetTimeoutId = null;
var writeConfig = {
    'keymap': null,
    'board': null
};

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
    keyCap.style.transformOrigin = keyCapWidth * ranchorX + 'px ' + keyCapHeight * ranchorY + 'px';
    
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
    keyLabel.style.fontSize = '12px';
    keyLabel.style.fontFamily = 'sans-serif';
    keyLabel.style.fontWeight = 'bold';

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
    })
    Button.addEventListener('mouseout', function() {
        keyBorder.style.borderWidth = '1px';
        keyBorder.style.borderColor = 'black';
    });
    Button.addEventListener('click', function() {
        //キーの色を変更
        let oldActiveKey = document.getElementsByClassName('active-key');
        if (oldActiveKey.length > 0) {
            oldActiveKey[0].classList.remove('active-key');
        }
        keyBorder.classList.add('active-key');


        keyIndexes = key.id.replace('key-', '').split(':');

        //キーのプロパティを表示
        let keyPropertyTabs = document.getElementById('key-labels');

        clearKeyProperty();

        if(currentKeymap != null){
            for (let keyLayer in currentKeymap['keymap']) {
                keyInputBlock = document.createElement('div');
                keyInputBlock.className = 'key-input-block';

                keyBlockLabel = document.createElement('p');
                keyBlockLabel.className = 'key-input-block-label';
                keyBlockLabel.innerHTML = keyLayer;
                keyInputBlock.appendChild(keyBlockLabel);

                keyPropertyTabs.appendChild(keyInputBlock);
                for (let key in currentKeymap['keymap'][keyLayer]) {

                    keyInputItem = document.createElement('div');
                    keyInputLabel = document.createElement('label');
                    keyInputSelect = document.createElement('select');

                    keyInputBlock.appendChild(keyInputItem);
                    keyInputItem.appendChild(keyInputLabel);
                    keyInputItem.appendChild(keyInputSelect);

                    keyInputItem.className = 'key-input-item';
                    
                    keyInputLabel.className = 'key-input-label';
                    keyInputLabel.innerHTML = key  + ': ';
                    
                    keyInputSelect.className = 'key-input-select';
                    keyInputSelect.addEventListener('change', function() {
                        //console.log(this.value);
                        currentKeymap['keymap'][keyLayer][key][keyIndexes[0]][keyIndexes[1]] = this.value;
                        reloadLabel(currentKeymap['keymap'][currentKeymapLayer['profile']][currentKeymapLayer['layer']]);
                    });

                    // option = document.createElement('option');
                    // option.value = '>==select keycode==<';
                    // option.innerHTML = '>==select keycode==<';
                    // keyInputSelect.appendChild(option);
                    for (let keyname in keycodeList['keyList']) {
                        let option = document.createElement('option');
                        option.value = keyname;
                        option.title = keycodeList['keyList'][keyname][2];
                        option.innerHTML = keyname;
                        option.className = 'key-input-option';
                        keyInputSelect.appendChild(option);
                    }

                    try {
                        keyInputSelect.value = currentKeymap['keymap'][keyLayer][key][keyIndexes[0]][keyIndexes[1]];
                    }
                    catch {
                        console.log('error: key ' + keyIndexes[0] + ',' + keyIndexes[1] + ' is not found.');
                    }
                    //keyInputSelect.value = 'NONE';

                }
            }
        }

        //console.log('click: ' + id);
    });


    keyboardBg.appendChild(key);
    key.appendChild(keyCap);
    keyCap.appendChild(keyBorder);
    keyCap.appendChild(keyTop);
    keyCap.appendChild(keyLabel);
    keyCap.appendChild(Button);
}


//eel.expose(createKeyboard);
async function createKeyboard(layout_name) {
    clearKeyboard();
    clearKeyProperty();
    await getLayout(layout_name).then(async (value) => {
        let layout = value;
        if (typeof layout !== 'object') {
            return;
        }
        layout.forEach((e, i) => {
            e.forEach((e, j) => {
                if (e.length < 4) {
                    //console.log('warning: key ' + i + ',' + j + ' is not enough length. Skip this key.');
                    return;
                }
                else if (e.length < 7){
                    e.concat([0, 0, 0]);
                }
                createKey(String(i) + ':' + String(j), e[0], e[1], e[2], e[3], rotate = e[4], ranchorX = e[5], ranchorY = e[6]);
            })
        });
        keyBoard_bg_resize();
    });
    //createKeyboardChangeLayerControl(layout['layerList']);
    //reloadLabel();
}

function clearKeyProperty() {
    keyPropertyTabs = document.getElementById('key-labels');
    let oldItems = keyPropertyTabs.children;
    while (oldItems.length > 0) {
        keyPropertyTabs.removeChild(oldItems[0]);
    }
}

//eel.expose(createKeymap);
async function createKeymap(keymap_name) {
    getKeymap(keymap_name).then(async (value) => {
        let keymap = value;
        currentKeymap = keymap;
        //console.log(keymap)
        if (typeof currentKeymap !== 'object') {
            return;
        }
        await createKeyboard(currentKeymap['layout']);

        let keymap_name_input = document.getElementById('keymap-name-input');
        let keymap_description_textarea = document.getElementById('keymap-description-textarea');

        keymap_name_input.value = currentKeymap['name'];
        keymap_description_textarea.value = currentKeymap['description'];

        createKeyboardChangeLayerControl();

        for(let keyLayer in currentKeymap['keymap']) {
            for(let key in currentKeymap['keymap'][keyLayer]) {
                currentKeymapLayer = {'profile': keyLayer,
                                    'layer': key};
                reloadLabel(currentKeymap['keymap'][currentKeymapLayer['profile']][currentKeymapLayer['layer']]);
                //console.log('change layer to ' + keyLayer + ' ' + key)
                break;
            }
            break;
        }
    });
}


function createKeyboardChangeLayerControl() {
    let changeLayerControlDiv = document.getElementById('keyboard-control-change-layer-div');
    let oldItems = changeLayerControlDiv.children;
    while (oldItems.length > 0) {
        changeLayerControlDiv.removeChild(oldItems[0]);
    }

    let activateFirstLayerFlag = false;
    for (let layer in currentKeymap['keymap']) {
        let changeLayerControlProfileDiv = document.createElement('div');
        changeLayerControlProfileDiv.className = 'keyboard-control-change-layer-profile-div';
        let changeLayerControlProfileLabel = document.createElement('label');
        changeLayerControlProfileLabel.className = 'keyboard-control-change-layer-profile-label';
        changeLayerControlProfileLabel.innerHTML = layer;
        let changeLayerControlProfileUl = document.createElement('ul');
        changeLayerControlProfileUl.className = 'keyboard-control-change-layer-profile-ul';


        changeLayerControlProfileDiv.appendChild(changeLayerControlProfileLabel);
        changeLayerControlProfileDiv.appendChild(changeLayerControlProfileUl);

        
        for (let key in currentKeymap['keymap'][layer]) {
            let changeLayerControlLi = document.createElement('li');
            changeLayerControlLi.className = 'keyboard-control-change-layer-li';
        
            let changeLayerControlButton = document.createElement('button');
            changeLayerControlButton.className = 'keyboard-control-change-layer-button';
            if (!activateFirstLayerFlag) {
                changeLayerControlButton.classList.add('active-layer-button');
                activateFirstLayerFlag = true;
            }
            changeLayerControlButton.innerHTML = key;
            changeLayerControlButton.addEventListener('click', function() {
                let oldActiveButton = document.getElementsByClassName('active-layer-button');
                if (oldActiveButton.length > 0) {
                    oldActiveButton[0].classList.remove('active-layer-button');
                }
                changeLayerControlButton.classList.add('active-layer-button');
                //console.log('click: ' + layerList[i]);
                currentKeymapLayer = {'profile': layer,
                                    'layer': key};
                reloadLabel(currentKeymap['keymap'][currentKeymapLayer['profile']][currentKeymapLayer['layer']]);
                console.log('change layer to ' + layer + ' ' + key);
                //console.log(currentKeymapLayer);
            });
        
            changeLayerControlLi.appendChild(changeLayerControlButton);
            changeLayerControlProfileUl.appendChild(changeLayerControlLi);
        }
        changeLayerControlDiv.appendChild(changeLayerControlProfileDiv);
    }
}


function reloadLabel(keymap) {
    let keymap_default = currentKeymap['keymap']['default']['default'];
    //console.log(keymap_default)
    keymap.forEach((e, i) => {
        e.forEach((f, j) => {
            //console.log(String(i) + String(j) + f);
            keyLabel = document.getElementById('label-' + String(i) + ':' + String(j));
            if(keyLabel === null) {
                return;
            }
            //console.log(keyLabel)
            try {
                keyLabel.innerHTML = keycodeList['keyList'][String(f)][0];
            }
            catch {
                console.log('error: keyname ' + f + ' is not found.');
            }
        })
    });
}

function createLoadingBlock() {
    let loadingBlock = document.createElement('div');
    loadingBlock.className = 'loading-block';
    let loadingIcon = document.createElement('i');
    loadingIcon.className = 'fas fa-spinner fa-spin';
    loadingBlock.appendChild(loadingIcon);
    return loadingBlock;
}


async function saveKeymap() {
    let keymap = currentKeymap;
    let keymap_name = currentKeymap['name'];
    ret = await saveKeymap_py(keymap, keymap_name);
    return ret;
}

function checkWriteConfig(writeConfig) {
    for (let key in writeConfig) {
        if (writeConfig[key] === null) {
            return false;
        }
    }
    return true;
}

async function showKeymapsWriteWindow() {
    let keymapListDiv = document.getElementById('write-window-body-select-keymap-body');
    let writeButton = document.getElementById('write-window-footer-write-button');

    if(!checkWriteConfig(writeConfig)) {
        writeButton.disabled = true;
    }

    let oldOptions = keymapListDiv.getElementsByClassName('write-window-body-select-keymap-body-item');
    while (oldOptions.length > 0) {
        keymapListDiv.removeChild(oldOptions[0]);
    }

    let loadingBlock = createLoadingBlock();
    keymapListDiv.appendChild(loadingBlock);

    let keymapList = await getKeymaps();
    //console.log(keymapList);
    loadingBlock.remove();

    if (keymapList.length == 0) {
        let option = document.createElement('div');
        option.className = 'write-window-body-select-keymap-body-item';
        let optionName = document.createElement('div');
        optionName.className = 'write-window-body-select-keymap-body-item-keymap-name';
        let optionSelect = document.createElement('div');
        optionSelect.className = 'write-window-body-select-keymap-body-item-keymap-select';
        let optionButton = document.createElement('button');
        optionButton.className = 'write-window-body-select-keymap-body-item-keymap-button';

        optionName.innerHTML = 'No keymap exists.';
        optionButton.innerHTML = 'Select';
        optionButton.disabled = true;

        option.appendChild(optionName);
        optionSelect.appendChild(optionButton);
        option.appendChild(optionSelect);
        keymapListDiv.appendChild(option);
        return;
    }

    for (let i = 0; i < keymapList.length; i++) {
        let option = document.createElement('div');
        option.className = 'write-window-body-select-keymap-body-item';
        let optionName = document.createElement('div');
        optionName.className = 'write-window-body-select-keymap-body-item-keymap-name';
        let optionSelect = document.createElement('div');
        optionSelect.className = 'write-window-body-select-keymap-body-item-keymap-select';
        let optionButton = document.createElement('button');
        optionButton.className = 'write-window-body-select-keymap-body-item-keymap-button';

        optionName.innerHTML = keymapList[i];
        optionButton.innerHTML = 'Select';
        optionButton.addEventListener('click', async function() {
            let selectButtons = keymapListDiv.getElementsByTagName('button');
            for (let i = 0; i < selectButtons.length; i++) {
                selectButtons[i].innerHTML = 'Select';
                selectButtons[i].disabled = false;
            }
            optionButton.innerHTML = 'Selected';
            optionButton.disabled = true;

            writeConfig['keymap'] = keymapList[i];
            if (checkWriteConfig(writeConfig)) {
                writeButton.disabled = false;
            }
        });

        option.appendChild(optionName);
        optionSelect.appendChild(optionButton);
        option.appendChild(optionSelect);
        keymapListDiv.appendChild(option);
    }
}

async function showArduinosWriteWindow() {
    

    let arduinoListDiv = document.getElementById('write-window-body-select-board-body');
    let writeButton = document.getElementById('write-window-footer-write-button');

    if (!checkWriteConfig(writeConfig)) {
        writeButton.disabled = true;
    }

    let oldOptions = arduinoListDiv.getElementsByClassName('write-window-body-select-board-body-item');
    while (oldOptions.length > 0) {
        arduinoListDiv.removeChild(oldOptions[0]);
    }

    let loadingBlock = createLoadingBlock();
    arduinoListDiv.appendChild(loadingBlock);

    let arduinoList = await getArduinoList();
    //console.log(arduinoList);
    loadingBlock.remove();

    if (typeof(arduinoList)!= 'object' || arduinoList['result'].length == 0) {
        let optionElem = document.createElement('div');
        let boardNameElem = document.createElement('div');
        let boardPortElem = document.createElement('div');
        let boardSelectElem = document.createElement('div');
        let boardSelectButton = document.createElement('button');
        optionElem.className = 'write-window-body-select-board-body-item';
        boardNameElem.className = 'write-window-body-select-board-body-item-board-name';
        boardPortElem.className = 'write-window-body-select-board-body-item-board-port';
        boardSelectElem.className = 'write-window-body-select-board-body-item-board-select';
        boardSelectButton.className = 'write-window-body-select-board-body-item-board-button';

        boardNameElem.innerHTML = 'No board exists.';
        boardPortElem.innerHTML = 'No port exists.';
        boardSelectButton.innerHTML = 'Select';
        boardSelectButton.disabled = true;

        optionElem.appendChild(boardNameElem);
        optionElem.appendChild(boardPortElem);
        boardSelectElem.appendChild(boardSelectButton);
        optionElem.appendChild(boardSelectElem);
        arduinoListDiv.appendChild(optionElem);
        return;
    }

    for (let i = 0; i < arduinoList['result'].length; i++) {
        try {
            boardName = arduinoList['result'][i]['matching_boards'][0]['name'];
        }
        catch {
            boardName = 'unknown';
        }
        try {
            boardPort = arduinoList['result'][i]['port']['address'];
        }
        catch {
            boardPort = 'unknown';
        }


        let optionElem = document.createElement('div');
        let boardNameElem = document.createElement('div');
        let boardPortElem = document.createElement('div');
        let boardSelectElem = document.createElement('div');
        let boardSelectButton = document.createElement('button');
        optionElem.className = 'write-window-body-select-board-body-item';
        boardNameElem.className = 'write-window-body-select-board-body-item-board-name';
        boardPortElem.className = 'write-window-body-select-board-body-item-board-port';
        boardSelectElem.className = 'write-window-body-select-board-body-item-board-select';
        boardSelectButton.className = 'write-window-body-select-board-body-item-board-button';

        boardNameElem.innerHTML = boardName;
        boardPortElem.innerHTML = boardPort;
        boardSelectButton.innerHTML = 'Select';
        boardSelectButton.addEventListener('click', async function() {

            let selectButtons = arduinoListDiv.getElementsByTagName('button');
            for (let i = 0; i < selectButtons.length; i++) {
                selectButtons[i].innerHTML = 'Select';
                selectButtons[i].disabled = false;
            }
            boardSelectButton.innerHTML = 'Selected';
            boardSelectButton.disabled = true;

            writeConfig['board'] = arduinoList['result'][i];
            if (checkWriteConfig(writeConfig)) {
                writeButton.disabled = false;
            }
        });
        

        optionElem.appendChild(boardNameElem);
        optionElem.appendChild(boardPortElem);
        boardSelectElem.appendChild(boardSelectButton);
        optionElem.appendChild(boardSelectElem);
        arduinoListDiv.appendChild(optionElem);
    }
    
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

eel.expose(createKeyboard_py);
function createKeyboard_py(layout_name) {
    createKeyboard(layout_name);
}


async function pythonPrint() {
    let ret = await eel.just_print()
    console.log(ret);
}

async function getKeycodes() {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let keycodeList = await eel.get_keycode_list('_')();
    //console.log(keycodeList);
    return keycodeList;
}

async function getlayouts() {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let layoutList = await eel.get_layout_list('_')();
    //console.log(layoutList);
    return layoutList;
}

async function getLayout(layoutName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let layout = await eel.get_layout('_', layoutName)();
    //console.log(layout);
    return layout;
}

async function getKeymaps() {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let keymapList = await eel.get_keymap_list('_')();
    //console.log(keymapList);
    return keymapList;
}

async function getKeymap(keymapName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let keymap = await eel.get_keymap('_', keymapName)();
    //console.log(keymap);
    return keymap;
}

async function getArduinoList() {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let arduinoList = await eel.get_arduino_list('_')();
    //console.log(arduinoList);
    return arduinoList;
}

async function saveKeymap_py(keymap, kaymapName) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let ret = await eel.save_keymap('_', keymap, kaymapName)();
    console.log(ret);
    return ret;
}

async function writeKeymap_py(keymap, board) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let ret = await eel.write('_', keymap, board)();
    console.log(ret);
    return ret;
}

async function openLinkInDefaultBrowser(url) {
    // Python function requires "self" argument. But it can't from JS. So, I use "_" instead of "self".
    let ret = eel.link_opener(url);
}


function showSaveDialog(message, color) {
    let saveDialog = document.getElementById('save-dialog');
    let saveDialogArrow = document.getElementById('save-dialog-arrow');
    let saveDialogMessage = document.getElementById('save-dialog-message');
    if (saveSetTimeoutId !== null) {
        clearTimeout(saveSetTimeoutId);
    }
    saveDialogMessage.innerHTML = message;
    saveDialog.style.backgroundColor = color;
    saveDialogArrow.style.borderBottomColor = color;
    saveDialog.style.display = 'block';
    saveDialog.style.left = 'calc(50% - ' + saveDialog.getBoundingClientRect().width / 2 + 'px)';
    saveSetTimeoutId = setTimeout(() => {
        saveDialog.style.display = 'none';
        saveSetTimeoutId = null;
    }, 3000)

}

function showDeleteKeymapDialog(message, color) {
    let deleteKeymapDialog = document.createElement('div');
    deleteKeymapDialog.id = 'delete-keymap-dialog';
    deleteKeymapDialog.className = 'delete-keymap-dialog';
    let deleteKeymapDialogArrow = document.createElement('div');
    deleteKeymapDialogArrow.id = 'delete-keymap-dialog-arrow';
    deleteKeymapDialogArrow.className = 'delete-keymap-dialog-arrow';
    let deleteKeymapDialogMessage = document.createElement('p');
    deleteKeymapDialogMessage.id = 'delete-keymap-dialog-message';
    deleteKeymapDialogMessage.className = 'delete-keymap-dialog-message';
    deleteKeymapDialogMessage.innerHTML = message;

    deleteKeymapDialog.style.backgroundColor = color;
    deleteKeymapDialogArrow.style.borderRightColor = color;

    deleteKeymapDialog.appendChild(deleteKeymapDialogArrow);
    deleteKeymapDialog.appendChild(deleteKeymapDialogMessage);
    
    return deleteKeymapDialog;
}

function deleteKeymapDialogReposition(parentObj, dialogObj) {
    let parentPos = parentObj.getBoundingClientRect();
    let right= Number(parentPos.left) + Number(parentObj.getBoundingClientRect().width);
    let top = Number(parentPos.top) - 49;
    dialogObj.style.left = Number(right) + 'px';
    dialogObj.style.top = Number(top) + 'px';
}


function closeWriteWindow() {
    writeWindow = document.getElementById('write-window-bg');
    writeWindow.style.display = 'none';
    writeConfig = {
        'keymap': null,
        'board': null
    };
}



function main(){
    //初期のキーボードの大きさを設定
    let keyboardBg = document.getElementById('keyboard-bg');
    keyboardBg.style.width = keyCapWidth + 'px';
    keyboardBg.style.height = keyCapHeight + 'px';

    // キーコードリストを取得
    getKeycodes().then((value) => {
        keycodeList = value;
        //console.log(keycodeList);
    });

    // ロードキーマップボタンとロードレイアウトボタンのクリック時の動作
    let selectLayoutButton = document.getElementById('select-layout-button');
    let layoutDropdown = document.getElementById('select-layout-list');
    let selectKeymapButton = document.getElementById('select-keymap-button');
    let keymapDropdown = document.getElementById('select-keymap-list');
    selectLayoutButton.onclick = () => {
        //console.log('show layout list')
        layoutDropdown.style.display = 'block';
        oldOptions = layoutDropdown.getElementsByTagName('li');
        while (oldOptions.length > 0) {
            layoutDropdown.removeChild(oldOptions[0]);
        }
        document.addEventListener('click', function(e) {
            if (e.target.id != 'select-layout-button') {
                layoutDropdown.style.display = 'none';
            }
        });
        getlayouts().then((value) => {
            value.forEach((e) => {
                let option = document.createElement('li');
                option.className = 'dropdown-item';
                option.innerHTML = e;

                option.addEventListener('mouseover', function() {
                    option.style.backgroundColor = '#eee';
                    option.style.cursor = 'pointer';
                });
                option.addEventListener('mouseout', function() {
                    option.style.backgroundColor = 'white';
                    option.style.cursor = 'default';
                });
                option.addEventListener('click', function() {
                    createKeyboard(e);
                });
                layoutDropdown.appendChild(option);
            }
        )}
    )};

    selectKeymapButton.onclick = () => {
        keymapDropdown.style.display = 'block';
        //dropmenuResize();
        oldOptions = keymapDropdown.getElementsByTagName('li');
        while (oldOptions.length > 0) {
            keymapDropdown.removeChild(oldOptions[0]);
        }
        document.addEventListener('click', function(e) {
            if (e.target.id != 'select-keymap-button' && e.target.className != 'fas fa-trash-alt' && e.target.className != 'delete-keymap-button') {
                //console.log(e.target.className)
                keymapDropdown.style.display = 'none';
            }
        });
        getKeymaps().then((value) => {
            value.forEach((e) => {
                let optionDiv = document.createElement('li');
                optionDiv.className = 'dropdown-item-div';
                let option = document.createElement('p');
                option.className = 'dropdown-item';
                option.innerHTML = e;
                let deleteButton = document.createElement('button');
                deleteButton.className = 'delete-keymap-button';
                deleteButton.innerHTML = '<i class="fas fa-trash-alt" style="color: #777"></i>';


                deleteButton.addEventListener('click', async function() {
                    let ret = await eel.delete_keymap('_', e)();
                    //let ret=-1; //for debug
                    if (ret === 0) {
                        let dialog = showDeleteKeymapDialog('Deleted', '#5cb85c')
                        dialog.style.width = '50%'
                        deleteButton.appendChild(dialog);
                        deleteKeymapDialogReposition(deleteButton, dialog);
                        setTimeout(() => {
                            optionDiv.remove();
                        }, 1000);
                    }
                    else {
                        let dialog = showDeleteKeymapDialog('Failed to delete', '#d9534f')
                        deleteButton.appendChild(dialog);
                        dialog.style.width = '90%'
                        deleteKeymapDialogReposition(deleteButton, dialog);
                        setTimeout(() => {
                            dialog.remove();
                        }, 1000);
                    }
                });

                option.addEventListener('mouseover', function() {
                    optionDiv.style.backgroundColor = '#eee';
                    optionDiv.style.cursor = 'pointer';
                });
                option.addEventListener('mouseout', function() {
                    optionDiv.style.backgroundColor = 'white';
                    optionDiv.style.cursor = 'default';
                });
                option.addEventListener('click', function() {
                    createKeymap(e);
                });
                optionDiv.appendChild(option);
                optionDiv.appendChild(deleteButton);
                keymapDropdown.appendChild(optionDiv);
            })
        })
    };


    // キーマップの保存ボタンの設定
    saveKeymapButton = document.getElementById('save-keymap-button');
    saveKeymapButton.addEventListener('click', async function() {
        let saveDialog = document.getElementById('save-dialog');
        let saveDialogMessage = document.getElementById('save-dialog-message');
        if (currentKeymap === null) {
            showSaveDialog('No keymap is loaded.', '#d9534f');
            return;
        }
        ret = await saveKeymap();
        if (ret === 0) {
            showSaveDialog('Saved keymap ' + currentKeymap['name'], '#5cb85c');
        }
        else {
            showSaveDialog('Failed to save keymap ' + currentKeymap['name'], '#d9534f');
        }
    });


    //キーマップ書き込みボタンの設定
    let writeKeymapButton = document.getElementById('write-keymap-button');
    writeKeymapButton.addEventListener('click', async function() {
        let writeWindow = document.getElementById('write-window-bg');
        writeWindow.style.display = 'block';

        showKeymapsWriteWindow();
        showArduinosWriteWindow();
    });
    

    //キーマップ書き込みウィンドウの設定
    let writeWindowCloseButton = document.getElementById('write-window-close-button');
    writeWindowCloseButton.addEventListener('click', function() {
        closeWriteWindow();
    });
    let writeWindowFooterWriteButton = document.getElementById('write-window-footer-write-button');
    writeWindowFooterWriteButton.addEventListener('click', async function() {
        writeWindowFooterWriteButton.disabled = true;
        writeWindowFooterWriteButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        let writeMessage = document.getElementById('write-window-footer-message-text');
        writeMessage.innerHTML = 'Compiling and writing...';

        ret = await writeKeymap_py(writeConfig['keymap'], writeConfig['board']);
        writeMessage.innerHTML = ret;
        writeWindowFooterWriteButton.innerHTML = 'Write';
        writeWindowFooterWriteButton.disabled = false;
    });





    // キーボードプロパティのタブボタンの設定
    let defaultTab = 0;
    let keyboardPropertyTabButtons = document.getElementsByClassName('key-property-menu-item');
    //console.log(keyboardPropertyTabButtons);
    for (i=0; i<keyboardPropertyTabButtons.length; i++) {
        if (i == defaultTab) { 
            keyboardPropertyTabButtons[i].classList.add('active');
            document.getElementById(keyboardPropertyTabButtons[i].id + '-body').style.display = 'block';
        }
        else {
            document.getElementById(keyboardPropertyTabButtons[i].id + '-body').style.display = 'none';
        }
        keyboardPropertyTabButtons[i].addEventListener('click', function() {
            let keyboardPropertyTabButtons = document.getElementsByClassName('key-property-menu-item');
            for (j=0; j<keyboardPropertyTabButtons.length; j++) {
                keyboardPropertyTabButtons[j].classList.remove('active');
            }
            this.classList.add('active');
            let keyboardPropertyTabs = document.getElementsByClassName('key-property-body-item');
            for (j=0; j<keyboardPropertyTabs.length; j++) {
                keyboardPropertyTabs[j].style.display = 'none';
            }
            let currentTab = document.getElementById(this.id + '-body');
            //console.log(currentTab);
            currentTab.style.display = 'block';
        });
    }

    //キーマッププロパティの入力欄の設定
    let keymap_name_input = document.getElementById('keymap-name-input');
    let keymap_description_textarea = document.getElementById('keymap-description-textarea');

    keymap_name_input.addEventListener('change', function() {
        currentKeymap['name'] = this.value;
    });
    keymap_description_textarea.addEventListener('change', function() {
        currentKeymap['description'] = this.value;
    });

    //リンクの設定 aタグをそのままクリックするとeelのウィンドウやeelで使用しているブラウザで開いてしまうので、
    //　python経由でデフォルトブラウザで開くようにする。（どうしてもデフォルトブラウザで開くようにしたい）
    let aElems = document.getElementsByTagName('a');
    for (let i = 0; i < aElems.length; i++) {
        link = aElems[i].href;
        aElems[i].href = 'javascript:void(0)';
        aElems[i].addEventListener('click', () => {
            openLinkInDefaultBrowser(link);
            //console.log(aElems[i].href)
            
        });
    }

    

}

main();