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
        try:
            self.arduino = pyduinocli.Arduino(arduinoCli_path)
        except Exception as e:
            print(e)
            return

    def hardware_selecter(self):
        self.boards = self.arduino.board.list()
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
        while True:
            self.input = input('select board: ')
            try:
                print('Selected: \"' + self.boards['result'][int(self.input)]['matching_boards'][0]['name'] + '\": \"' + self.boards['result'][int(self.input)]['port']['address'] + '\"')
                return int(self.input)
            except(Exception):
                print('Invalid input')
                continue

    def upload(self, sketch_dir, board_index):
        try:
            print('Compiling ' + sketch_dir + ' with ' + self.boards['result'][board_index]['matching_boards'][0]['fqbn'])
            self.compile_result = self.arduino.compile(sketch_dir, fqbn=self.boards['result'][board_index]['matching_boards'][0]['fqbn'])
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
            print('Uploading ' + sketch_dir + ' with ' + self.boards['result'][board_index]['matching_boards'][0]['name'] + ' ' + self.boards['result'][board_index]['port']['address'])
            self.arduino.upload(sketch_dir, fqbn=self.boards['result'][board_index]['matching_boards'][0]['fqbn'], port=self.boards['result'][board_index]['port']['address'])
        except pyduinocli.ArduinoError as e:
            print(e.result['__stderr'])
            print('Upload failed')
            return
        except KeyError as e:
            print('Can\'t upload with this board')
            return
        else:
            print('Upload success')
