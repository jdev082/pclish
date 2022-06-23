#!/usr/bin/env python3 
# pclish - Python Command Line Shell

# Modules
from subprocess import call, run, getoutput
from psutil import virtual_memory
from platform import processor, system
from socket import gethostname
from colorama import Fore, Back

# Do not modify any of this.
RAM = virtual_memory()
CPU = processor()
OS = system()
HOST = gethostname()
VER = "pclish v0.1.0-beta.1"
USER = getoutput("/usr/bin/echo $USER")

# Here you'll customize your prompt, know its hardcoded though.
PROMPT = Back.BLUE + Fore.WHITE + USER + "@{}$ ".format(HOST) + Back.RESET + Fore.RESET + " "

def execute_command(command): # this function is what executes the command and handles pipes.
    run(command.split(" "))

def pclish_ver():
    print(VER)

def main():
    while True:
        inp = input(PROMPT)
        if inp == "exit":
            break
        elif inp == "ver":
            pclish_ver()
        elif "cd" in inp:
          print("pclish unfortunately does not support cd")
        else:
            call(inp, shell=True)

#  Main
if '__main__' == __name__:
    main()
