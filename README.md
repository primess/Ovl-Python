# Ovl-Python (Owl)

Python Module for Computer Vision Object Tracking and Detection mainly for the FIRST® Robotics Competition Program

****
NOTE:
The upcoming version will stop support for python 2.7 and 3.4. Official support will be only for python 3.5+!

****

The Library was written by Ori Ben-Moshe.

Copyright (©) 2018 - 2019, Ori Ben-Moshe, all rights reserved.

The following python module dependencies are needed:

  - OpenCV Version 2.x, 3.x & 4.x ([for more information on how to install](https://github.com/1937Elysium/Ovl-Python/blob/master/Installing%20Opencv.md))
  
  - matplotlib
  
  - numpy
  
  - scipy
  
  - sklearn (0.20 for python 2.7 & 3.4)
 

OVL is officially supported for the following python versions: 2.7 and 3.4+

## Installation:

Using `pip`:
</br>
`python -m pip install ovl`

For a light weight version that does not include the calibration sub-module:
</br>
`python -m pip install ovl-light`


In order to update use the `--update` flag.
e.g:
`python -m pip install --upgrade ovl`

Download the files directly:

[Current Version](https://github.com/1937Elysium/Ovl-Python/tree/master/Archives/Current%20Release) from the Archives.

Documentation for the Library is available in [English](https://github.com/1937Elysium/Ovl-Python/tree/master/English) and [Hebrew](https://github.com/1937Elysium/Ovl-Python/blob/master/Hebrew/Introduction.md).
Great sample code (in english) is [here](https://github.com/1937Elysium/Ovl-Python/blob/master/English/ovl/Vision/Constructer%20(__init__).md).


### Known Issues:
If you find a bug please post it in the issues section!
- `Vision.json_serialize` and `Vision.json_deserialize` are not updated
