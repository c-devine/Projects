---
layout: project
title: Java FX GCODE Generator
---
![java](https://forthebadge.com/images/badges/made-with-java.svg)
![certified](https://forthebadge.com/images/badges/approved-by-george-costanza.svg)


## Overview

I needed some way to create GCODE files for a 4 Axis CNC hotwire machine I built to cut out foam wings.  After
looking around for a while, I didn't find exactly what I was looking for, so I created this project.  All the
software and pre-buit [releases](https://github.com/c-devine/WingGcodeBuilder/releases) are saved [Here](https://github.com/c-devine/WingGcodeBuilder) on GitHub.

### Snapshots
<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/2D.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/3D-v101.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/GCODE.png?raw=true" width="180" height="120">


### Software

JavaFX / Spring Boot application used to create GCODE files for 4 axis hotwire cutting machine. The application can import Selig and Lednicer format airfoil .dat
files from the University of Illinois [UIUC Airfoil Database]( http://m-selig.ae.illinois.edu/ads/coord_database.html) and other sites. Airfoil, chord length, twist,
and offset are editable for both the tip and root.  There is a 2D view of the airfoils, as well as a 3D view of the wing half or whole
wing. G-code can be generated for both the right and left (mirrored) wings. Created to generate G-code for low cost (?) hotwire foam
cutter.  See [wiki](https://github.com/c-devine/WingGcodeBuilder/wiki).

- Go to  [GitHub](https://github.com/c-devine/WingGcodeBuilder) for full description, instructions, and software
