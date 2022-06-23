#!/usr/bin/env python3 
# pclish - Python Command Line Shell

import os
import subprocess
import psutil
import platform
import socket

RAM = psutil.virtual_memory()
CPU = platform.processor()
OS = platform.system()
HOST = socket.gethostname()
VER = "pclish v0.1.0-devPreview"

PROMPT = "shell@{}$ ".format(HOST)

def execute_command(command):
    try:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)
            
            for cmd in command.split("|"):
                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("pclish: command not found, run the help command for a list of commands: {}".format(cmd.strip()))

            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("pclish: command not found: {}".format(command))

def pclish_help():
    print("""pclish: here are the commands available
             help: shows this page
             ver: displays shell version
             system: shows system information
             shtdwnsubsys: shuts down the sub system""")

def pclish_ver():
    print(VER)


def pclish_system():
    print("HOSTNAME:" + HOST)
    print("System: PCLISH SUBSYSTEM")
    print("RAM:" + RAM)
    print("CPU:" + CPU)
    print("OS:" + OS)
    print("SHELL:" + VER)
    


def main():
    while True:
        inp = input(PROMPT)
        if inp == "exit":
            break
        elif inp == "help":
            pclish_help()
        elif inp == "ver":
            pclish_ver()
        elif inp == "system":
            pclish_system()
        else:
            os.system("SHELL='pclish' && " + inp)

#  Main
if '__main__' == __name__:
    main()
