# keyboard-layout-editor
Graphical keyboard layout editor for [numeric-keypad](https://github.com/m2600/numeric-keypad)


## Requirements
Linux based systems need to install following packages.

- Python3
- Arduino-cli

### pip packages

- [pyduinocli](https://github.com/Renaud11232/pyduinocli)
- [Eel](https://github.com/python-eel/Eel)

### Arduino packages

- [HID-Project](https://github.com/NicoHood/HID)
- [Adafruit_NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)



## Setup (Linux)


Linux based systems need to add user account to system group to access USB device.


### Arch Linux

```shell
sudo gpasswd -a $USER uucp
sudo gpasswd -a $USER lock
```

## Usage

```shell
python3 main.py
```