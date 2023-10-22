# keybord-layout-editor
guraphical keyboard layout editor for [numeric-keypad](https://github.com/m2600/numeric-keypad)

## Usage (Linux)

You need your user account add to system group to access USB device.

### Debian/Ubuntu

```shell
$ sudo adduser $USER dialout
$ sudo adduser $USER lock
```

### Arch Linux

```shell
$ sudo gpasswd -a $USER uucp
$ sudo gpasswd -a $USER lock
```
