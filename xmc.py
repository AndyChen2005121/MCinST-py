#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

# "MCinST is not a script", remastered in Python
# by pCloudsp
# For Linux & Windows 7+ & MacOS 10.9+ & (Possibly Android?) in case you can get jre running

# Import modules and init work
import os
import sys
import platform
import gettext
_ = gettext.gettext
CurrOS = platform.system()
CurrPath = sys.path[0]
os.chdir(CurrPath)
ver = "dev"

dependencies = ["screen", "tar"]
# from lang_en import lang
# lang()
# lang = input("Select language and press [Enter]:\
# \n请选择语言并按回车：\
# \n1. English\
# \n2. 简体中文")
# if lang == 1:
# 	from lang_en import lang
# elif lang == 2:
# 	print("暂不支持中文")
# 	# from lang_en import lang
# else:
# 	print("Please Re-Enter the right choice / 请重新输入选择")
# 	input("Press [Enter] to continue... / 请按回车键继续...")
# 	init()



def main():
	print(Greet)
	print(MainMenu)

def firsttime():
	print(InstMenu)
# def inst():
# 	print()

def init():
	if os.path.exists("~/MCinST-py/default.conf"):
		main()
	else:
		inst()

def cl():
	if CurrOS == 'Windows':
		_ = os.system('cls')
	elif CurrOS == 'Linux' or CurrOS == 'Darwin':
		_ = os.system('clear')


init()
