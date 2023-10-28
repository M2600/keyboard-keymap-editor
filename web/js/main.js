

function createKey(id, x, y, w, h) {
    const keyboardBg = document.getElementById('keyboard-bg');


    const key = document.createElement('div');
    key.id = id+'-key';
    key.className = 'key';

    const keyCap = document.createElement('div');
    keyCap.id = id + '-cap';
    keyCap.className = 'key-cap';
    
    const keyBorder = document.createElement('div');
    keyBorder.id = id + '-border';
    keyBorder.className = 'key-border';
    keyBorder.style.position = 'absolute';
    keyBorder.style.left = x + 'px';
    keyBorder.style.top = y + 'px';
    keyBorder.style.width = w + 'px';
    keyBorder.style.height = h + 'px';
    keyBorder.style.backgroundColor = 'grey';
    keyBorder.style.border = 'solid 1px black';
    keyBorder.style.borderRadius = '5px';

    const keyTop = document.createElement('div');
    keyTop.id = id + '-top';
    keyTop.className = 'kek-top';
    keyTop.style.position = 'absolute';
    keyTop.style.left = x + (w * 0.3 / 2) + 'px';
    keyTop.style.top = y + (h * 0.3 / 3) + 'px';
    keyTop.style.width = w*0.7 + 'px';
    keyTop.style.height = h*0.7 + 'px';
    keyTop.style.backgroundColor = 'white';
    keyTop.style.borderStyle = 'solid';
    keyTop.style.borderColor = 'rgba(0, 0, 0, 0.1)';
    keyTop.style.borderWidth = '1px';
    keyTop.style.borderRadius = '5px';

    keyboardBg.appendChild(key);
    key.appendChild(keyCap);
    keyCap.appendChild(keyBorder);
    keyCap.appendChild(keyTop);
}



createKey('key_1', 0, 0, 50, 50);