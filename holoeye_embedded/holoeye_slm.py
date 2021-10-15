from _typeshed import Self
import numpy as np
import imageio
import os
import paramiko
from paramiko import SSHClient


class HoloeyeSLM (SSHClient):
    class Commands:
        SET_LIBRARY = "export LD_LIBRARY_PATH=/mnt"
        DISABLE_HDMI = "./mnt/ControlExample -a"

    invalid_input_err = "INVALID input: the size of input image/array must be({0},{1}) and the indices/pixels values must be a number between ({2},{3})"
    CACHE_PATH = "./cache"
    
    '''
    Initializes and establishes the connection to the device
    '''
    def __init__(self, host='10.10.70.1', port=22, username='root', password='', width=1920, height=1080, min=0, max=255):
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
        super.__init__()
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connect()
        self._set_library_path()

    '''
    Setups the libraries path in SLM
    '''
    def _set_library_path(self):
        stdin, stdout, stderr = self.exec_command(self.Commands.SET_LIBRARY)
        return stdout.readlines()
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
        stdin, stdout, stderr = self.exec_command(self.Commands.DISABLE_HDMI)
        return stdout.readlines()
    
    '''
    Sends an image at a given path to HoloeyeSLM
    '''
    def sendImage(self, FILE_PATH):
        try:
            im = imageio.imread(FILE_PATH)
            array = self._validateImage(FILE_PATH)
            self._saveImage(array)
            # TODO : SEND IMAGE TO HOME DIRECTORY
            # TODO : RUN SHOW COMMAND ON 
            self._removeImage()
        except Exception as ex:
            raise ex
