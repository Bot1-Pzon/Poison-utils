'''
	Test manuali
'''

import os
import sys

import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import Poison_utils as pu

pu.Console.config()


x = "\tx\n"

print(x.encode())

""" if pu.Files.path_exist(".venv"):
	pu.Files.delete_file_at_path(".venv")

input("> ") # Per rendere il test manuale

pu.Console.clear()

pu.Dependencies.Virtual_environment.create_virtual_environment()
pu.Dependencies.Virtual_environment.activate_virtual_environment()
pu.Dependencies.install_component("requests")

 """
