# Tenny TUJR Thermal Chamber Details

![](images/chamber-main.jpg)

This repo holds some various documentation collected around our Tenny TUJR thermal chamber.

Note that there appear to be *many* options on these units, so be aware your unit may have different controllers, wiring, options, etc.

## Interface Board

Our thermal chamber had what appeared to be Ethernet, RS232 (DB9), and GPIB ports on the backside. On opening the wiring these units are connected to the [Synergy488](https://www.tidaleng.com/synergy488.htm) board:

![](images/chamber-wiring.jpg)

Unfortunately the software caused Windows to blue-screen, and it does not appear it has any well documented commands. The description of this board is primary just as an interface board and *not* related to the control (which is handled entirely by the Watlow F4).

As other users already had interfaces to the Watlow F4, I haven't explored using the Synergy488 board directly. [yet]. The initial plan is to bypass the board and route the RS232 from the Watlow F4 to the exterior DB9 connector.

It looks litke the Synergy488 can be used to forward commands from Ethernet, which would be handy if possible. More work is needed to check if this will work.

## 