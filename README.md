# keyboard-keymap-editor
Graphical keyboard keymap editor for [numeric-keypad](https://github.com/m2600/numeric-keypad)


## Requirements


- Python3
- Arduino-cli

### pip packages

- [pyduinocli](https://github.com/Renaud11232/pyduinocli)
- [Eel](https://github.com/python-eel/Eel)

### Arduino packages

- [HID-Project](https://github.com/NicoHood/HID)
- [Adafruit_NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)



## Setup (Linux)


Linux based systems need to add user account to some system group to access USB devices.

### Ubuntu
```shell
sudo adduser $USER dialout
```

### Arch Linux

```shell
sudo gpasswd -a $USER uucp
sudo gpasswd -a $USER lock
```

## Usage

```shell
python3 main.py
```
