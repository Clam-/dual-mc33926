This is a module modified from:
https://github.com/pololu/dual-mc33926-motor-driver-rpi

to use the pigpio interface library.

Setup:
* Install the pigpio software from the raspi distribution:
```sudo apt install pigpio```
* Create a venv. e.g. ``` python3 -m venv ~/env```
* Clone and install this module which should also install the pigpio python dependency e.g.:  
```git clone <this URL>
cd dual-mc33926
~/env/vin/pip install .```

Or dev mode with ```~/env/bin/pip install -e .```
Note: Dev mode needs quite modern setuptools/pip.
