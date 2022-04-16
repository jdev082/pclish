#!/usr/bin/env python3 
# PCLISH - Python Command Line Shell

import os
import subprocess
import psutil
import platform
import socket

RAM = psutil.virtual_memory()
CPU = platform.processor()
OS = platform.system()
HOST = socket.gethostname()
VER = "PCLISH v0.0.6a-hotfix1a"

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


def pclish_cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: no such file or directory: {}".format(path))

def pclish_echo():
    TXT = input("ARGS: ")
    print(TXT)

def pclish_oscmd():
    CMD = input("ARGS: ")
    os.system(CMD)

def pclish_help():
    print("""pclish: here are the commands available
             help: shows this page
             cd: change directory
             ver: displays shell version
             ls: lists files in current dir
             system: shows system information
             mkdir: creates a directory
             shtdwnsubsys: shuts down the sub system
             oscmd: allows you to run an OS level command""")

def pclish_ls():
    print("pclish: this feature is not yet supported")

def pclish_ver():
    print(VER)

def pclish_mkdir():
    DIR = input("ARGS: ")
    os.mkdir(DIR)

def pclish_system():
    print("HOSTNAME:" + HOST)
    print("System: PCLISH SUBSYSTEM")
    print("RAM:" + RAM)
    print("CPU:" + CPU)
    print("OS:" + OS)
    print("SHELL:" + VER)
    

def pclish_shtdwnsubsys():
    print("Exiting to..." + OS)
    exit()

def main():
    while True:
        inp = input(PROMPT)
        if inp == "exit":
            break
        elif inp == "cd ":
            pclish_cd(inp[3:])
        elif inp == "help":
            pclish_help()
        elif inp == "ver":
            pclish_ver()
        elif inp == "ls":
            pclish_ls()
        elif inp == "mkdir":   
            pclish_mkdir()
        elif inp == "shtdwnsubsys":
            pclish_shtdwnsubsys()
        elif inp == "system":
            pclish_system()
        elif inp == "echo":
            pclish_echo()
        elif inp == "oscmd":
            pclish_oscmd()
        else:
            execute_command(inp)

#  Main
if '__main__' == __name__:
    main()
