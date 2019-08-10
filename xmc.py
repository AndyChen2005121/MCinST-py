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
# For Debian 8+/Ubuntu 16.04+/CentOS 7+/Others Linux & Windows 7+ & MacOS 10.7.3+

from os import system

def main():
	print("")

def init():
	print("Select language and press [Enter]:\
	\n请选择语言并按回车：\
	\n1. English\
	\n2. 简体中文")
	
	lang = input()
	if lang == 1:
		from lang_en import lang
	elif lang == 2:
		print("暂不支持中文")
	else:
		print("Please Re-Enter the right choice / 请重新输入选择")
		input("Press [Enter] to continue... / 请按回车键继续...")
		init()

	
init()