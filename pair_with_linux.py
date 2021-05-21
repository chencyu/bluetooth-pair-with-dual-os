#!/usr/bin/env python3

import os
import time
import lsb_release

ROOT = os.sep
HOME = os.getenv("HOME")
DATA_PATH = os.path.join(ROOT, "usr", "local", "share", "bluetooth-pair-with-dual-os")
NEW_ADDR = os.path.join(DATA_PATH, "new_addr.txt")

def pair():

    if os.geteuid() != 0:
        print("Please execute as sudo")
        return 1

    print("Make sure you've already remove the connected setting if you pair the device previously.")
    input("Press [Enter] to continue.")

    bfh = BluetoothProfileHandler()

    print("Please pair your new bluetooth devices now.")

    bfh.get_new_addr()
    new_num = len(bfh.new_paired_addr)
    if new_num == 1:
        os.makedirs(DATA_PATH, exist_ok=True)
        with open(file=NEW_ADDR, mode='w') as new_addr_f:
            for item in bfh.new_paired_addr:
                new_addr_f.write(item)




class BluetoothProfileHandler():


    def __init__(self):

        self.distro = lsb_release.get_distro_information()
        self.host_addr = self.host_bt_address()
        self.paired_dir = self.get_paired_dir()
        self.old_paired_set = self.get_paired_set()
        self.new_paired_addr = set()


    def host_bt_address(self):
        '''
        [Source](https://unix.stackexchange.com/questions/165192/extract-bluetooth-mac-address-hcitool-dev)

        [:xdigit:]    -->   hexadecimal
        [:xdigit:]:   -->   hexadecimal + :
          {11,17}     -->   pick 11 <= string <= 17
        '''
        return os.popen("hciconfig -a | grep -o \"[[:xdigit:]:]\{11,17\}\"").read().replace("\n","")


    def get_paired_dir(self):

        if self.distro["ID"] == "Ubuntu":
            if self.distro["RELEASE"] == "20.04":
                return os.path.join(ROOT,"var","lib","bluetooth",self.host_addr)


    def get_paired_set(self):

        paired_profile_list = os.listdir(self.paired_dir)
        paired_profile_list.remove("settings")
        paired_profile_list.remove("cache")
        return set(paired_profile_list)


    def if_new_paired(self):
        new_paired_set = self.get_paired_set()
        if self.old_paired_set == new_paired_set:
            return (False, new_paired_set - self.old_paired_set)
        else:
            return (True, new_paired_set - self.old_paired_set)


    def get_new_addr(self):

        SUC, self.new_paired_addr = self.if_new_paired()
        while(SUC != True):
            time.sleep(1)
            SUC, self.new_paired_addr = self.if_new_paired()


if __name__ == '__main__':
    pair()
