#!/usr/bin/env python

#App para copiar arquivos de uma estacao linux para windows atraves do samba

import os, sys


def copyFiles(dir, destino, user, passwd):
	os.chdir(dir)
	FILES = os.listdir("./")
	
	for x in FILES:
		if "txt" in x:
			os.system("smbclient //", destino, "-N -c 'put ", x , "' -U",user,"\%",passwd)
	os.system("mv *.txt backup/")
	

dirTest = "/home/user"
user = "tmp"
passwd = "admin"
destino = "192.168.1.10/recepcao"
copyFiles(dirTest, destino, user, passwd)

