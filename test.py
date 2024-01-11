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
