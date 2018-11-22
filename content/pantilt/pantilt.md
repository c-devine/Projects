---
layout: project
title: Various Pan Tilt controller plugins and firmware implementations for OctoPrint server
---

## Overview

The projects below extend the plugin controls developed by Salandora and add support for a simple and
low cost 2 axis gimbal bracket. The plugins use the web cam controls (added through the
Octoprint-PanTilt plugin) located on the control tab.

Two plugins, and associated firmware files were created:
 - [Arduino Nano](https://github.com/c-devine/OctoPrint-PanTilt-Nano) used as the controller for the gimbal. The Nano is controlled
and powered through the USB port. Firmware is located [Here](https://github.com/c-devine/OctoPrint-PanTilt-Nano-Firmware)
 - [ESP8266](https://github.com/c-devine/OctoPrint-PanTilt-ESP8266) used as the controller for the gimbal. The ESP8266 is controlled
and powered through the USB port. Firmware is located [Here](https://github.com/c-devine/OctoPrint-PanTilt-ESP8266-Firmware)


### Snapshots

<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-Nano/snapshots/assets/img/pantilt.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-Nano/snapshots/assets/img/webcam.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-Nano-Firmware/snapshots/assets/img/nano.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266-Firmware/snapshots/assets/img/board_top.png?raw=true" width="180" height="120">


### Video of Pan/Tilt plugin in action
[![PanTilt ESP8266 Video](img/pantilt-youtube-small.png?raw=true)](https://www.youtube.com/watch?v=sj92Br_dFW8 "PanTilt-ESP8266")


### Hardware

The 2 axis servo gimbals can be found on ebay and other online locations. Nano and ESP8266 development boards
are also pretty easy to find.


