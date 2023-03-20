
# py_no_cam
A small and lightweight Python application that disables all attached cameras. The purpose is:
- To allow people to disable their cameras without having to use their BIOS or UEFI tool.
- Make it easy to enable (and disable)
> Note that you might have to install usb_modeswitch from your package repository of choice.

## Run as sudo!
Program **will not work** without elevated permissions because it works with device buses

## Dependencies
- Python >= 3.6
- usb_modeswitch
