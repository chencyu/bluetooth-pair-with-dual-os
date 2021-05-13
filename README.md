
# Bluetooth device pair with dual os

[Reference](https://desktopi18n.wordpress.com/2018/02/02/bluetooth-mouse-in-dual-boot-of-windows-10-and-linux/)

1. Pair with Linux
2. Pair with Win10
3. Export secret regedit in Win10 via [PsTools](https://docs.microsoft.com/en-us/sysinternals/downloads/pstools)
4. `mv` old pair config to correspond directory
   - Example: `mv /var/lib/bluetooth/${device}/${old_address} /var/lib/bluetooth/${device}/${new_address}`
   - Find new address in exported .reg file
5. Use this tool to get converted `${LTK}`, `${ERand}`, `${EDiv}`
