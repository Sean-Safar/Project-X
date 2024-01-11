from smbus2 import SMBus
from tools.find_i2c import find_axi_i2c
import keyboard
import textwrap

SLICE_ADDR = 0x22  # I2C addr of TR slice

# Mapping heater names to SW numbers
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


