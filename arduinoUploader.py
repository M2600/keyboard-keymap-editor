import pyduinocli 
import os


class arduino_uploader:
    def __init__(self):
        if os.name == 'nt':
            arduinoCli_path = 'arduino-cli/arduino-cli.exe'
        elif os.name == 'posix':
            arduinoCli_path = 'arduino-cli'
        else:
            print('OS not supported')
            return
        self.arduino = pyduinocli.Arduino(arduinoCli_path)
        try:
            self.arduino.board.list()
        except Exception as e:
            print(e)
            print(arduinoCli_path + 'doesn\'t work.')
            return

    def get_hardware_list(self):
        print('Detecting Arduino boards...')
        self.boards = self.arduino.board.list()
        if len(self.boards['result']) < 1:
            print('No arduino board detected.')
            return -1
        else:
            print(str(len(self.boards['result'])) + ' board(s) found. select board with index.')
        for i, board in enumerate(self.boards['result']):
            try:
                board_name = board['matching_boards'][0]['name']
            except KeyError:
                board_name = 'Unknown'
            try:
                board_port = board['port']['address']
            except KeyError:
                board_port = 'Unknown'
            print(str(i) + ': ' + board_name + '  ' + board_port)
        return self.boards

    def hardware_selecter(self):
        self.boards = self.get_hardware_list()
        while True:
            self.input = input('select board: ')
            try:
                print('Selected: \"' + self.boards['result'][int(self.input)]['matching_boards'][0]['name'] + '\": \"' + self.boards['result'][int(self.input)]['port']['address'] + '\"')
                return int(self.input)
            except(Exception):
                print('Invalid input')
                continue

    def upload(self, sketch_dir, board_dict):
        try:
            print('Compiling ' + sketch_dir + ' with ' + board_dict['matching_boards'][0]['fqbn'])
            self.compile_result = self.arduino.compile(sketch_dir, fqbn=board_dict['matching_boards'][0]['fqbn'])
        except pyduinocli.ArduinoError as e:
            print(e.result['__stderr'])
            print('Compile failed')
            return
        except KeyError as e:
            print(e)
            print('Can\'t compile with this board')
            return
        else:
            print('Compile success')

        try:
            print('Uploading ' + sketch_dir + ' with ' + board_dict['matching_boards'][0]['name'] + ' ' + board_dict['port']['address'])
            self.arduino.upload(sketch_dir, fqbn=board_dict['matching_boards'][0]['fqbn'], port=board_dict['port']['address'])
        except pyduinocli.ArduinoError as e:
            print(e.result['__stderr'])
            print('Upload failed')
            return
        except KeyError as e:
            print('Can\'t upload with this board')
            return
        else:
            print('Upload success')


