import threading
import numpy as np
import imageio
import os
import paramiko
from paramiko import SSHClient
from scp import SCPClient


class HoloeyeSLM (SSHClient):
    class Commands:
        PWD = 'pwd'
        GO_HOME = "cd ~"
        SET_LIBRARY = "export LD_LIBRARY_PATH=/mnt"
        DISABLE_HDMI = "/mnt/ControlExmpl -a"
        SHOW_IMAGE = "/mnt/ControlExmpl -o ~/tmp.bmp"

    invalid_input_err = "INVALID input: the size of input image/array must be({0},{1}) and the indices/pixels values must be a number between ({2},{3})"
    CACHE_PATH = "./cache"

    '''
    Initializes and establishes the connection to the device
    '''

    def __init__(self, host='10.10.70.1', port=22, username='root', password='', width=1920, height=1080, min=0, max=255, logging=True):
        self.logging = logging
        if(not os.path.exists(self.CACHE_PATH)):
            os.mkdir(self.CACHE_PATH)
        self.width = width
        self.height = height
        self.min = min
        self.max = max
        self.invalid_array_err = self.invalid_input_err.format(
            height, width, min, max)
        self.hostname = host
        self.port = port
        self.username = username
        self.password = password
        super().__init__()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()
        self.channel = self.invoke_shell()
        self._go_home()
        self._set_library_path()
        self.diconnectHDMI()
        self.logger = threading.Thread(target=self.__log,daemon=True,name='HoloeyeSLM {0} Logger'.format(self.hostname))
        # self.logger.start()

    def __log(self):
        pass
        # while (self.logging):
        #     print(">>LOG : ")
        #     while not self.channel.recv_ready():
        #         pass
        #     out = self.channel.recv(9999)
        #     print(out)

    '''
    gets the current session directory
    '''

    def _pwd(self):
        stdin, stdout, stderr = self.exec_command(self.Commands.PWD)
        lines = stdout.readlines()
        return lines

    '''
    Setups the current session directory to home
    '''

    def _go_home(self):
        self.channel.send(self.Commands.GO_HOME+'\n')
        # while not self.channel.recv_ready():
        #         pass
        # out = self.channel.recv(9999)
        # print(out.decode())


    '''
    Setups the libraries path in SLM
    '''

    def _set_library_path(self):
        self.channel.send(self.Commands.SET_LIBRARY+'\n')
        # while not self.channel.recv_ready():
        #         pass
        # out = self.channel.recv(9999)
        # print(out.decode())

    '''
    Runs the show command on slm
    '''

    def _show_image(self):
        self.channel.send(self.Commands.SHOW_IMAGE+'\n')
        # while not self.channel.recv_ready():
        #         pass
        # out = self.channel.recv(9999)
        # print(out.decode())

    '''
    Validates the array whether it is a legitimate input.
    '''

    def _validateArray(self, array):
        if (array.shape == (self.height, self.width)) and (array.max() <= self.max) and (array.min() >= self.min):
            return array
        raise Exception(self.invalid_input_err)

    '''
    Validates the input image path whether it is a legitimate input. And returns the array in case it's a correct format
    '''

    def _validateImage(self, path):
        im = imageio.imread(path)
        return self._validateArray(im)

    '''Saves the image in the temporary path'''

    def _saveImage(self, array):
        try:
            imageio.imwrite(self.CACHE_PATH+'/tmp.bmp', array)
        except Exception as ex:
            print(ex)

    '''Removes the image in the temporary path'''

    def _removeImage(self, array):
        try:
            if os.path.exists(self.CACHE_PATH+'/tmp.bmp'):
                os.remove(self.CACHE_PATH+'/tmp.bmp')
        except Exception as ex:
            print(ex)

    '''
    Establishes connection to the Holoeyes SLM device
    '''

    def connect(self):
        return super().connect(self.hostname, port=self.port, username=self.username, password=self.password)

    '''
    Disoconnects the HDMI from the HoloeyeSLM device
    '''

    def diconnectHDMI(self):
        self.channel.send(self.Commands.DISABLE_HDMI+'\n')
        # while not self.channel.recv_ready():
        #         pass
        # out = self.channel.recv(9999)
        # print(out.decode())

    '''
    Sends an image at a given path to HoloeyeSLM
    '''

    def sendImage(self, FILE_PATH):
        try:
            im = imageio.imread(FILE_PATH)
            array = self._validateImage(FILE_PATH)
            self._saveImage(array)
            # TODO : SEND IMAGE TO HOME DIRECTORY
            with SCPClient(self.get_transport()) as scp:
                scp.put(self.CACHE_PATH+'/tmp.bmp',remote_path='~')
                scp.close()
            self._show_image()
            # TODO : RUN SHOW COMMAND ON

            # self._removeImage()
        except Exception as ex:
            raise ex
