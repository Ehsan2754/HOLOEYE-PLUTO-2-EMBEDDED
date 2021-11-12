# Classes
## ```class HoloeyeSLM```
### Description
This class has the main role in commmunication with the Holoeye device. This class inherits the ```SSHClient``` class from ```paramiko``` package and has all the properties from the same package. 
### Methods
* ```HoloeyeSLM() ``` aka constructor
    * Description 

        Initializes the connection to your Holoeye SLM device
    * Parameters: 
        > *```parameter=default```          description*
        * ```logging=False ```      Enables the logs from your HOLOEYE device.

        * ```RSA_Keys=None ```      Path to your prefered RSA keys.  

        * ```width=1920```          Width of your HOLOEYE device.  

        * ```height=1080```         Width of your HOLOEYE device.  

        * ```min=0```               Minimum intensity withing the Holoeye device supporting range  

        * ```max=255```             Maximum intensity withing the Holoeye device supporting range 

        * ```hostname=10.10.70.1``` Your device hostname/IP address 

        * ```port=22```             Your device listening port  

        * ```username=root```       Your device end username

        * ```password=''```         Your device end password 

* ```flush_RSA_Keys()```
    * Description 

        Deletes the current RSA keys.


* ```prepare_connect()```
    * Description 
    
        Reinitialize and connect to the device with new changes in device parameters. e.g. changing the device IP address.

* ```connect()```
    * Description 
    
        Connects to the device.

* ```changeIP(new_IP,mask)```
    * Description
        
        Changes the device IP configuration to the given IP and network submask and closes the connection. It is recommentded to set your IP addresses with default submask. After changing the device IP configuration, you need to **re-plug** the device to your computer **without turning off** the Holoeye device.
    * Parameters
        * ```new_IP='10.10.70.2'``` Desisered IPv4 address for the device
        * ```mask='255.0.0.0'```    Desisered mask for the device

* ```diconnectHDMI()```
    * Description 
    
        Disconnects the HDMI port access from the Holoeye device.

* ```sendImage(FILE_PATH)```
    * Description 
    
        Sends the image at given path to the Holoeye device output.
    * Parameters    
        > *```parameter```          description*
        * ```FILE_PATH```           path to image file. * image file must be a bitmap of 2-D array with dimentions equal to ```width``` and ```height``` attributes of the class as well as pixel values withing the class ```min``` and ```max``` parameters.

* ```sendData(data)```
    * Description 
    
        Sends the given array values to the Holoeye device output.
    * Parameters    
        > *```parameter```          description*
        * ```data```                numput 2-D array with dimentions equal to ```width``` and ```height``` attributes of the class as well as pixel values withing the class ```min``` and ```max``` parameters.
# Device Driver Installation and Configuration
## Windows
### Installing RNDIS Driver on Windows 
1. Connect the HoloeyeSLM USB-OTG port to your computer. *Do not connect HDMI to your computer*
2. Open DeviceManager on your computer. 
    
    > To open DeviceManager on your pc, open run(win+R) and type ```devmgmt.msc``` and press Enter button.
    
    If you don't have the RNDIS driver installed on your computer for that port, you are supposed to following:  
 
    ![RNDIS](https://i.ibb.co/kDqpwzD/RNDIS1.png) 
 
3. Right click on RNDIS and choose ```Update Driver```
    
    ![RNDIS](https://i.ibb.co/SsnBTC2/RNDIS2.png)
4. Click on ```Browse my computer for drivers```
    ![RNDIS](https://i.ibb.co/k6Qd067/RNDIS3.png)
5. Click on ``` Let me pick from a list of ... ``` and click on ``` Next ```
    ![RNDIS](https://i.ibb.co/m4VQkK3/RNDIS4.png)
6. From the list choose ```Network adapters``` as your decive type and click on ``` Next ```
    ![RNDIS](https://i.ibb.co/hsN5Fg7/RNDIS5.png)
7. From the list of Manufactures, choose ``` Microsoft ``` and from Model list choose USB RNDIS Adapter and click on ``` Next ``` 
    ![RNDIS](https://i.ibb.co/TRMx6mm/RNDIS6.png)
8. At this step you would have a warning about the possibility of uncompatibality of the chose driver with your device .(**Disclaimer**: I verified to compatibility with with **Holoeye Pluto-2**). Choose ```yes``` for the poping warning dialog.  
    ![RNDIS](https://i.ibb.co/cQqxc37/RNDIS7.png)
9. Now you have installed the RNDIS network driver.Now, you can close the window and proceed with Network Configuration.
    ![RNDIS](https://i.ibb.co/SdRpPzD/RNDIS8.png)
10. Currently, you should be able to see your RNDIS network adapter in thus section
    > Number of RNDIS adapter is equal to number of the devices connected to your computer.
    ![RNDIS](https://i.ibb.co/kJT4gwm/RNDIS9.png)

### Configuring RNDIS network address and gateway

1. Open ```Control Panel```
    ![RNDIS](https://i.ibb.co/17R33LF/RNDIS10.png)
2. Click on ```Network and Internet```
    ![RNDIS](https://i.ibb.co/pwrNMVG/RNDIS11.png)
3. Click on ```Network and Sharing Center```
    ![RNDIS](https://i.ibb.co/FJggyQG/RNDIS12.png)
4. Click on ```Change adapter setting```
    ![RNDIS](https://i.ibb.co/GFcHz7H/RNDIS13.png)
5. Right click on network adapter which corresponds to your desiered RNDIS adapter and click on ```Properties```.
    ![RNDIS](https://i.ibb.co/BLNQVcR/RNDIS14.png)
6. From list items choose ```Internet Portocol Version 4(TCP/IPv4)``` and click on ```Properties```.
    ![RNDIS](https://i.ibb.co/Gs1b0kH/RNDIS15.png)

7. Click on ```Use the following IP address```. Enter IP address regarding your device assigned IP. The default IP configuration for device is ```10.10.70.1/8```. Thus you may use any IP address which does not conflict with your other RNDIS network configurations and devices and click on ```Ok```. E.g : 
    ``` 
    # device IP on RNDIS adapter 1 ->  10.10.70.1
    IP address : 10.10.70.254 # RNDIS adapter 1 IP addr 
    Subnet mask : 255.0.0.0   # RNDIS adapter 1 Subnet mask 
    
    # device IP on RNDIS adapter 2 ->  10.10.70.2
    IP address : 10.10.70.253 # RNDIS adapter 2 IP addr 
    Subnet mask : 255.0.0.0   # RNDIS adapter 2 Subnet mask 

    ...
    ```
    ![RNDIS](https://i.ibb.co/0yV3smD/RNDIS16.png)
8. Click on ```Close``` and exit. Now you are set up with your devices.
    ![RNDIS](https://i.ibb.co/60PsR7b/RNDIS17.png)

## Linux 
You may use [```ifconfig```](https://man7.org/linux/man-pages/man8/ifconfig.8.html) for configuing your device. In order to assign the IP address, consider the following example: 
``` 
    # device IP on usb0 ->  10.10.70.1
    IP address : 10.10.70.254 # usb0 adapter  IP addr 
    Subnet mask : 255.0.0.0   # usb0 adapter  Subnet mask 
    
    # device IP on usb1 adapter  ->  10.10.70.2
    IP address : 10.10.70.253 # usb1 adapter IP addr 
    Subnet mask : 255.0.0.0   # usb1 adapter Subnet mask 
    ...
```
## MACOS
You may use [HoRNDIS](https://www.joshuawise.com/horndis) for configuring your device connection. Make sure you preserver the address assignment for your different devices. Please refer to linux instruction or step 7 of windows instrction for a more clear example. 


# [CHANGELOG](CHANGELOG.RST)

# [CONTRIBUTING](CONTRIBUTING.RST)