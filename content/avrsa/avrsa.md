---
layout: project
title: AVR Smart Audio for RC Aircraft without a Flight Controller (FC)
---

## Overview

The goal of this project was to buid a miniature controller device that would enable the use of Smart Audio
on aircraft without needing a full blown FC running betaflight.  FPVWRA wings for example do not have
controller boards, but, do have FPV VTXs that may have Smart Audio capability.  An Adafruit trinket was
used as the controller board since it is cheap (< $9.00) and has a pretty powerful chip (SAMD21)
This project is documented [Here](https://github.com/c-devine/AvrSmartAudio) on GitHub as well.

### Snapshots

![AvrSA](img/avrsa-overview.png)
[![Demo](img/youtube-prototype-small.png?raw=true)](https://www.youtube.com/watch?v=tcKi-m7yl1k "Adafruit Trinket Smart Audio Prototype on Breadboard")


### Software

Uses the Arduino C++ libraries, as well as some custom half-duplex software serial code, to handle both the inverted
and non-inverted serial protocols used by FrSky and SmartAudio.

### Hardware
AVR SAMD21.....


Firmware and other info can be found here [AvrSmartAudio](https://github.com/c-devine/AvrSmartAudio) on GitHub.
