---
layout: project
title: Various Pan Tilt controller plugins and firmware implementations for OctoPrint server
---
![python](https://forthebadge.com/images/badges/made-with-python.svg)
![c++](https://forthebadge.com/images/badges/made-with-c-plus-plus.svg)
![netflix](https://forthebadge.com/images/badges/powered-by-netflix.svg)
## Overview

[OctoPrint](https://octoprint.org/) is a popular 3D printer control software package.  It has a number of built in
features, including video monitoring capabilities - but by default it can not control the position of the camera.
 But, OctoPrint is extensible through user created Python plugins. This project captures the plugins and firmware developed
to add video pan/tilt capability to the OctoPrint server.   The projects below add serial and pwm controls to the
UI controls added in the plugin [OctoPrint-PanTilt](https://github.com/Salandora/OctoPrint-PanTilt) and add support
for a simple and low cost 2 axis gimbal bracket.

## Repositories
 - [Arduino Nano Plugin](https://github.com/c-devine/OctoPrint-PanTilt-Nano) used as the controller for the gimbal. The Nano is controlled
and powered through the USB port. Firmware is located [here](https://github.com/c-devine/OctoPrint-PanTilt-Nano-Firmware)
 - [ESP8266 Plugin](https://github.com/c-devine/OctoPrint-PanTilt-ESP8266) used as the controller for the gimbal. The ESP8266 is controlled
and powered through the USB port. Firmware is located [here](https://github.com/c-devine/OctoPrint-PanTilt-ESP8266-Firmware)
- [Simple PWM Control](https://github.com/c-devine/OctoPrint-PanTilt-Script) PGIO script to use existing PWM pins on the Raspberry PI
to control the gimbal.

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


