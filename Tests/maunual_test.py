import sys

import subprocess

sys.path.append('/home/poison_8o8/Pr0gr4ms/Projects/Poison-utils')

import Poison_utils as pu

pu.Console.config()



if pu.Files.path_exist(".venv"):
	pu.Files.delete_file_at_path(".venv")

input("> ") # Per rendere il test manuale

pu.Console.clear()

Venv = pu.Dependencies.Virtual_environment()
Venv.activate()

print(pu.Dependencies.is_library_importable("tk"))

pu.Dependencies.install_component("tk")

print(pu.Dependencies.is_library_importable("tk"))

