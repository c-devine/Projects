---
layout: project
title: Java FX GCODE Generator
---
![java](https://forthebadge.com/images/badges/made-with-java.svg)
![certified](https://forthebadge.com/images/badges/approved-by-george-costanza.svg)


## Overview

JavaFX / Spring Boot application used to create GCODE files for 4 axis hotwire cutting machine. The application can import Selig and Lednicer format airfoil .dat
files from the University of Illinois [UIUC Airfoil Database]( http://m-selig.ae.illinois.edu/ads/coord_database.html) and other sites. Airfoil, chord length, twist,
and offset are editable for both the tip and root.  There is a 2D view of the airfoils, as well as a 3D view of the wing half or whole
wing. G-code can be generated for both the right and left (mirrored) wings. Created to generate GCODE for low cost (?) hotwire foam
cutter.  See [wiki](https://github.com/c-devine/WingGcodeBuilder/wiki).

- Go to  [GitHub](https://github.com/c-devine/WingGcodeBuilder) for full description, instructions, and software.

### Snapshots

<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/2D.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/3D-v101.png?raw=true" width="180" height="120">
<img src="https://raw.githubusercontent.com/c-devine/WingGcodeBuilder/snapshots/assets/img/GCODE.png?raw=true" width="180" height="120">

### Video

[![WGB](img/jfx_youtube-small.png?raw=true)](https://youtu.be/wDMPSKyfra0 "WGB in Action")

### Software

Built with:
* [Java8/JavaFX](https://www.oracle.com/technetwork/java/javase/overview/java8-2100321.html) - Language and UI toolkit
* [toxiclibs](http://toxiclibs.org/) - Geometry manipulation routines
* [Spring Boot](https://projects.spring.io/spring-boot/) - Application framework
* [Gradle](https://gradle.org/) - Dependency Management
* [e\(fx\)clipse](http://www.eclipse.org/efxclipse/index.html) - IDE
* [updatefx](https://github.com/bitgamma/updatefx) - Automatic application updates

### Hardware

Created to drive 3D printed GCODE capable 4-axis CNC machine [here](https://github.com/c-devine/WingGcodeBuilder/wiki).
Releases created for Win32 and Win64 PCs.





