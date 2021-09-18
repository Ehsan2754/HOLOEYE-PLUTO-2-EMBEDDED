import numpy as np
import imageio, os
class holoeye:
    DISABLE_HDMI = "./mnt/ControlExample -a"
    invalid_input_err = "INVALID input: the size of input image/array must be({0},{1}) and the indices/pixels values must be a number between ({2},{3})"
    CACHE_PATH="./cache"
    def __init__(self,width=1920,height=1080,min=0,max=255):
        if(not os.path.exists(self.CACHE_PATH)):
            os.mkdir(self.CACHE_PATH)
        self.width = width
        self.height = height
        self.min = min
        self.max = max
        self.invalid_array_err = self.invalid_input_err.format(height,width,min,max)

    def _validateArray(self,array):
        if (array.shape == (self.height,self.width)) and (array.max()<=self.max) and (array.min()>=self.min):
            return array
        raise Exception(self.invalid_input_err)

    def _validateImage(self,path):
        im = imageio.imread(path)
        return self._validateArray(im)

    def _saveImage(self,array):
        try:
            imageio.imwrite(self.CACHE_PATH+'/tmp.bmp',array)
        except Exception as ex:
            print(ex)

    def _diconnectHDMI():
        pass
    
    def sendImage(self,FILE_PATH):
        try:
            im = imageio.imread(FILE_PATH)
            array=self._validateImage(FILE_PATH)
            self._saveImage(array)
        except Exception as ex:
            raise ex