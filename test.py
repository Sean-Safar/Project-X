from smbus2 import SMBus
import tools.command as command
from tools.find_i2c import find_axi_i2c
import keyboard
import textwrap

SLICE_ADDR = 0x22   # I2C addr of TR slice

def main():
    # get I2C string
    telemetry_I2C_port = find_axi_i2c()

    # try to open the telemetry I2C bus
    try:
        print("\nOpening I2C telemetry bus at: " + telemetry_I2C_port)
        telemetry_bus = SMBus(telemetry_I2C_port)
    except:
        print("ERROR: Failed to open I2C telemetry bus at: " + telemetry_I2C_port)
        print("Exiting...")
        exit()

    help_text = '''\
    \033[1mAll Commands to Turn On or Off Heaters\033[0m
    1. a1/a2/b1/b2/c1/c2 on/off
        Ex. "a1 on" will turn on heater a1
    2. all on/off
        Ex. "all on" will turn all heaters on
    2. done
        Ex. "done" will end the program and turn off all heaters
    '''
    while True:
        i = input('Input to turn heater on or off\n')
        if i == 'help':
            print(textwrap.indent(help_text,'')) 
        if i == 'a1 on':
            print('a1 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 4, "HIGH") #A1
        if i == 'a2 on':
            print('a2 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 5, "HIGH") #A2
        if i == 'b1 on':
            print('b1 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "HIGH") #B1
        if i == 'b2 on':
            print('b2 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'B', 0, "HIGH") #B2
        if i == 'c1 on':
            print('c1 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 2, "HIGH") #C1
        if i == 'c2 on':
            print('c2 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 3, "HIGH") #C2
        if i == 'd1 on':
            print('d1 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 0, "HIGH") #D1
        if i == 'd2 on':
            print('d2 heater is on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 1, "HIGH") #D2
        if i == 'a1 off':
            print('a1 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'a2 off':
            print('a2 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'b1 off':
            print('b1 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'b2 off':
            print('b2 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'c1 off':
            print('c1 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'c2 off':
            print('c2 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'd1 off':
            print('d1 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'd2 off':
            print('d2 heater is off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
        if i == 'all on':
            print('all heaters on')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 4, "HIGH") #A1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 5, "HIGH") #A2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "HIGH") #B1
            command.set_output(telemetry_bus, SLICE_ADDR, 'B', 0, "HIGH") #B2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 2, "HIGH") #C1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 3, "HIGH") #C2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 0, "HIGH") #D1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 1, "HIGH") #D2
        if i == 'all off':
            print('all heaters off')
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 4, "LOW") #A1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 5, "LOW") #A2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
            command.set_output(telemetry_bus, SLICE_ADDR, 'B', 0, "LOW") #B2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 2, "LOW") #C1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 3, "LOW") #C2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 0, "LOW") #D1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 1, "LOW") #D2
        if i == 'done':
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 4, "LOW") #A1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 5, "LOW") #A2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 6, "LOW") #B1
            command.set_output(telemetry_bus, SLICE_ADDR, 'B', 0, "LOW") #B2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 2, "LOW") #C1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 3, "LOW") #C2
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 0, "LOW") #D1
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', 1, "LOW") #D2
            print('testing done, all heaters off')
            break

if __name__ == "__main__":
    main()

Here are a few suggestions to make your code more efficient:

1. **Combine Common Code:** For turning off heaters, you're using the same command for all heaters. Instead of repeating similar lines, you can create a mapping between heater names and pin numbers, and then use that in a loop.

2. **Use a Dictionary for Commands:** Create a dictionary to map input commands to corresponding actions. This can simplify your code and make it more extensible.

3. **Optimize Imports:** Only import the specific functions you need from the modules to reduce unnecessary imports.

Here's a modified version incorporating these suggestions:

```python
from smbus2 import SMBus
from tools.find_i2c import find_axi_i2c
import keyboard
import textwrap

SLICE_ADDR = 0x22  # I2C addr of TR slice

# Mapping between heater names and pin numbers
HEATER_MAPPING = {
    'a1': 4, 'a2': 5, 'b1': 6, 'b2': 0, 'c1': 2, 'c2': 3, 'd1': 0, 'd2': 1
}

# Mapping between input commands and corresponding actions
COMMAND_MAPPING = {
    'on': 'HIGH',
    'off': 'LOW',
    'all': 'HIGH'  # Assuming 'all' turns on heaters, adjust if needed
}

def main():
    telemetry_I2C_port = find_axi_i2c()

    try:
        print("\nOpening I2C telemetry bus at: " + telemetry_I2C_port)
        telemetry_bus = SMBus(telemetry_I2C_port)
    except Exception as e:
        print(f"ERROR: Failed to open I2C telemetry bus at: {telemetry_I2C_port}")
        print(f"Exiting... {e}")
        exit()

    help_text = '''\
    \033[1mAll Commands to Turn On or Off Heaters\033[0m
    1. a1/a2/b1/b2/c1/c2 on/off
        Ex. "a1 on" will turn on heater a1
    2. all on/off
        Ex. "all on" will turn all heaters on
    2. done
        Ex. "done" will end the program and turn off all heaters
    '''

    while True:
        i = input('Input to turn heater on or off\n')

        if i == 'help':
            print(textwrap.indent(help_text, ''))

        words = i.split()
        if words[0] in HEATER_MAPPING and words[1] in COMMAND_MAPPING:
            heater_pin = HEATER_MAPPING[words[0]]
            command.set_output(telemetry_bus, SLICE_ADDR, 'A', heater_pin, COMMAND_MAPPING[words[1]])

        if i.startswith('all'):
            print(f'all heaters {COMMAND_MAPPING[words[1]]}')
            for heater_pin in HEATER_MAPPING.values():
                command.set_output(telemetry_bus, SLICE_ADDR, 'A', heater_pin, COMMAND_MAPPING[words[1]])

        if i == 'done':
            for heater_pin in HEATER_MAPPING.values():
                command.set_output(telemetry_bus, SLICE_ADDR, 'A', heater_pin, "LOW")
            print('testing done, all heaters off')
            break

if __name__ == "__main__":
    main()
```


