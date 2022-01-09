#! /bin/bash

# turns on bluetooth
sudo rfkill unblock bluetooth

# opens connection con channel 1
sudo rfcomm watch hci0
