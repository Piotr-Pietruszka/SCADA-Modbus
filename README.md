# SCADA-Modbus

## Installation
First of all you need to clone this repo:

```console
git clone git@github.com:Piotr-Pietruszka/SCADA-Modbus.git
```

Then you need to use programs defined below to run the program from source

## Used programs

### SCARA symulator
To simulate object we used `SCADA_symulator.exe` that we received from lecturer.

### Python program
The program providing GUI and all technicallity is written in Python using PyCharm.
You may download this software [here](https://www.jetbrains.com/pycharm/download/#section=windows).

In order to download required python packages navigate to project root directory and run `pip install -U -r python_requirements.txt` from command line.
You might be forced to change Python interpreter in PyCharm project to your native interpreter.

### Virtual Coms
To connect `SCADA_symulator.exe` to Python program we'll use virtual com software `com0com`.
You may download this software [here](https://sourceforge.net/projects/com0com/).