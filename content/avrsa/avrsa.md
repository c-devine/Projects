---
layout: project
title: AVR Smart Audio for RC Aircraft without a Flight Controller (FC)
---
![c++](https://forthebadge.com/images/badges/made-with-c-plus-plus.svg)
![gifs](https://forthebadge.com/images/badges/contains-cat-gifs.svg)

## Overview

The goal of this project was to write the firmware to allow a miniature controller device to enable the
use of Smart Audio on aircraft without needing a full blown FC running betaflight.  FPVWRA wings for example do not have
controller boards, but, do have FPV VTXs that may have Smart Audio capability.  An Adafruit trinket was
used as the controller board since it is cheap (< $9.00) and has a pretty powerful chip (SAMD21)
This project is documented [here](https://github.com/c-devine/AvrSmartAudio) on GitHub as well.

### Snapshots

![AvrSA](img/avrsa-overview.png)

### Video

[![Demo](img/youtube-prototype-small.png?raw=true)](https://www.youtube.com/watch?v=tcKi-m7yl1k "Adafruit Trinket Smart Audio Prototype on Breadboard")

### Software

Uses the Arduino C++ libraries, as well as some custom half-duplex software serial code, to handle both the inverted
and non-inverted serial protocols used by FrSky and SmartAudio.

### Hardware
AVR SAMD21.....


Firmware and other info can be found here [AvrSmartAudio](https://github.com/c-devine/AvrSmartAudio) on GitHub.

