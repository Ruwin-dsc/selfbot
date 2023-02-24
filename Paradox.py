#Importations Système
import os
import base64
import sys
import platform
import argparse
from os import system, get_terminal_size
from sys import stderr, stdout

#Importations Discord
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import youtube_dl
from asyncio.windows_events import ERROR_CONNECTION_REFUSED

#Importations Style
import colorama
from colorama import Fore, Style, init
import pystyle
from pystyle import *

#Importations Randoms
import random, string
from random import choice, choices, randint
from string import ascii_letters, digits, ascii_lowercase

#Importations Temps
import time
from time import sleep
from time import strftime
import datetime
temps = datetime.datetime.utcnow()

#Importations HTTPS
import json
import json as js2
import http
import http.client
import httpagentparser
import urllib
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib import parse

#Importations Threading
import threading
from threading import Thread

#Importations Connexion
import socket

#---------------------------------------------------------------------------------------------

#Compte
os.system("title Connexion")
os.system("cls")

print("{}\n> {}[1] : {}Se Connecter".format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))
print("{}\n> {}[2] : {}Quitter".format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))

connexion = input('{}\n> {} Choisissez : {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))

if connexion == '1':
    pseudo_connexion = input('{}\n> {} Pseudo : {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))

if connexion == '2':
        quit()

#Config
os.system("title Configuration")
os.system("cls")

prefix = input('{}\n> {} Prefix : {}'.format(Fore.RESET, Fore.LIGHTMAGENTA_EX, Fore.RESET))
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
musics = {}
ytdl = youtube_dl.YoutubeDL()
print(f"{Fore.LIGHTCYAN_EX}[/] {Fore.LIGHTMAGENTA_EX}Veuillez patienter{Fore.LIGHTCYAN_EX}...{Fore.RESET}")

#---------------------------------------------------------------------------------------------

#Headers
all_headers = [
    'Mozilla/5.0 (Windows NT 6.1; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.3; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 OPR/81.0.4196.54',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.37',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.72',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 OPR/80.0.4170.40',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.16',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.66',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.56',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 OPR/79.0.4143.22',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 OPR/77.0.4054.90'
]

aealbn = choice(all_headers)

#PC
plat = platform.processor()
systeme = platform.system()
machine = platform.machine()

#Infos
token = open("data\Token.txt", "rt").read()
client.remove_command('help')
header = {"Authorization": f'{token}'}

intents = discord.Intents.all()
intents.members = True

#Couleurs
Violette = 0x8317FF
Verte = 0x2ecc71
Orange = 0xe67e22
Rouge = 0xe74c3c
Gris = 0x95a5a6
Doré = 0xf1c40f

Bleu = 0x00008B
BleuFoncé = 0x206694
BleuCanard = 0x1abc9c

#---------------------------------------------------------------------------------------------

#Bienvenue
Write.Print(f"""

██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██    ██ ███████ 
██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██    ██ ██      
██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██    ██ █████   
██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██    ██ ██      
██████  ██ ███████ ██   ████   ████   ███████ ██   ████  ██████  ███████ """, Colors.black_to_white, interval=0.00001)

sleep(0.8)

Write.Print(f"""

███████ ██    ██ ██████  
██      ██    ██ ██   ██ 
███████ ██    ██ ██████  
     ██ ██    ██ ██   ██ 
███████  ██████  ██   ██ """, Colors.black_to_white, interval=0.00001)

sleep(1)

#---------------------------------------------------------------------------------------------

#SelfBot
@client.event
async def on_ready():
    os.system("title whitehall")
    os.system("cls")

    ping = int(client.latency * 1000)
    target = int(client.user.id)

    url_infos = "http://ip-api.com/json/"
    values = json.load(urlopen(url_infos))

    Write.Print(f"""

 ██▓███   ▄▄▄       ██▀███   ▄▄▄      ▓█████▄  ▒█████  ▒██   ██▒
▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒░░  █   ░
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░""", Colors.blue_to_purple, interval=0.00001)
    print(f"")
    Write.Print(f"""By : GxToM""", Colors.blue_to_purple, interval=0.00001)
    print(f"")


    print(f"")
    print(f"{Fore.WHITE}whitehall{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}Pseudo : {Fore.GREEN}{pseudo_connexion}{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}Prefix : {Fore.GREEN}{prefix}{Fore.RESET}")
    print(f"")
    print(f"{Fore.WHITE}DISCORD{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}ID : {Fore.GREEN}" + str(client.user.id) + f"{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}Latence :{Fore.GREEN} {ping}ms{Fore.RESET}")
    print(f"")
    print(f"{Fore.WHITE}IRL{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}Pays :{Fore.GREEN}", values['country'])
    print(f"{Fore.LIGHTGREEN_EX}Continent :{Fore.GREEN}", values['timezone'])
    print(f"{Fore.LIGHTGREEN_EX}Date : {Fore.GREEN}{temps}{Fore.RESET}")
    print(f"")
    print(f"{Fore.WHITE}PC{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}Système : {Fore.GREEN}{systeme}")
    print(f"{Fore.LIGHTGREEN_EX}Machine : {Fore.GREEN}{machine}")
    print(f"{Fore.LIGHTGREEN_EX}Processeur : {Fore.GREEN}{plat}")
    print(f"")

    async def status_ping():
        while True:
            ping = int(client.latency * 1000)
            ping2 = f"whitehall Ping : " + str(ping) + f"ms"
            await client.change_presence(activity=discord.Game(name=ping2))
            await asyncio.sleep(2)

    client.loop.create_task(status_ping())

#---------------------------------------------------------------------------------------------

#Serveurs
@client.command()
async def whitehall_copier(ctx, id):
    await ctx.message.delete()

    serveur_a_copier = client.get_guild(int(id))
    copier_serv = await client.create_guild(f'Backup-{serveur_a_copier.name}')

    print(f"{Fore.BLUE}5{Fore.RESET}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}4{Fore.RESET}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}3{Fore.RESET}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}2{Fore.RESET}")
    await asyncio.sleep(1)
    print(f"{Fore.BLUE}1{Fore.RESET}")
    await asyncio.sleep(1)
    print(f"{Fore.CYAN}[/] {Fore.LIGHTBLUE_EX}Copie du Serveur en cours...{Fore.RESET}")
    for g in client.guilds:
        if f'Backup-{serveur_a_copier.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in serveur_a_copier.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in serveur_a_copier.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    for role in serveur_a_copier.roles[::-1]:
        if role.name != "@everyone":
            try:
                await copier_serv.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
            except:
                break

    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Serveur copié avec Succès !{Fore.RESET}")

#Musique
class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@client.command()
async def whitehall_quitter(ctx):
    await ctx.message.delete()
    
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Vocale quittée avec Succès !{Fore.RESET}")

def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), client.loop)

    client.play(source, after=next)

@client.command()
async def whitehall_musique(ctx, url):
    await ctx.message.delete()

    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        play_song(client, musics[ctx.guild], video)
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Musique envoyée avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_rejoindre(ctx):
    await ctx.message.delete()

    channel = ctx.author.voice.channel
    await channel.connect()
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Vocale rejoint avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_crash(ctx):
    await ctx.message.delete()

    nombre_crash = Write.Input(f"Nombre : ", Colors.purple_to_blue, interval=0.00001)
    
    for i in range(int(nombre_crash)):
        channel = ctx.author.voice.channel
        await channel.connect()

        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Vocale rejoint avec Succès !{Fore.RESET}")

        client = ctx.guild.voice_client
        await client.disconnect()

        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Vocale quittée avec Succès !{Fore.RESET}")

#Infos
@client.command()
async def whitehall_membre(ctx, id):
    await ctx.message.delete()

    target = await client.fetch_user(id)
    
    ping = int(client.latency * 1000)

    await ctx.send(f"""
***Utilisateur : {target.mention}***
***ID : {target.id}***
***Nom : {target.display_name}***
***Bot : {target.bot}***
***Crée le : {target.created_at}***
***Latence : {ping}ms***""")
    await ctx.send(target.avatar_url)

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Member - Successfully Completed***")

    print(f"""
{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}whitehall_Membre !{Fore.RESET}

{Fore.GREEN}[+] Utilisateur : {Fore.LIGHTGREEN_EX}{target.mention}
{Fore.GREEN}[+] ID : {Fore.LIGHTGREEN_EX}{target.id}
{Fore.GREEN}[+] Nom : {Fore.LIGHTGREEN_EX}{target.display_name}
{Fore.GREEN}[+] Bot : {Fore.LIGHTGREEN_EX}{target.bot}
{Fore.GREEN}[+] Crée le : {Fore.LIGHTGREEN_EX}{target.created_at}
{Fore.GREEN}[+] Latence : {Fore.LIGHTGREEN_EX}{ping}ms""")

@client.command()
async def whitehall_serveur(ctx, id):
    await ctx.message.delete()

    infos_serveur = client.get_guild(int(id))

    serveur = infos_serveur
    salons = len(serveur.text_channels)
    vocales = len(serveur.voice_channels)
    personnes = serveur.member_count
    nom = serveur.name
    
    ping = int(client.latency * 1000)

    await ctx.send(f"""
***Serveur : {nom} - :eyes:***
***Salons : {salons} - :eyes:***
***Vocales : {vocales} - :eyes:***
***Membres : {personnes} - :eyes:***
***Latence : {ping}ms - :eyes:***""")
    await ctx.send(infos_serveur.icon_url)
    
    print(f"""
{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}whitehall_Serveur !{Fore.RESET}

{Fore.GREEN}[+] Serveur : {Fore.LIGHTGREEN_EX}{nom}
{Fore.GREEN}[+] Salons : {Fore.LIGHTGREEN_EX}{salons}
{Fore.GREEN}[+] Vocales : {Fore.LIGHTGREEN_EX}{vocales}
{Fore.GREEN}[+] Membres : {Fore.LIGHTGREEN_EX}{personnes}
{Fore.GREEN}[+] Latence : {Fore.LIGHTGREEN_EX}{ping}ms""")

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Server - Successfully Completed***")

#Spam
@client.command()
async def whitehall_spam1(ctx):
    await ctx.message.delete()
    
    print(f"")
    message = Write.Input(f"Message : ", Colors.purple_to_blue, interval=0.00001)
    nombre = Write.Input(f"Nombre : ", Colors.purple_to_blue, interval=0.00001)

    for i in range(int(nombre)):
        await ctx.send(f"{message}")
        print(f"{Fore.GREEN}[+] {i + 1}{Fore.LIGHTGREEN_EX} |-{message}---> a été envoyé avec Succès !{Fore.RESET}")

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Spammer - Successfully Completed***")

@client.command()
async def whitehall_spam2(ctx):
    await ctx.message.delete()

    print(f"")
    nombre = Write.Input(f"(x5) Nombre : ", Colors.purple_to_blue, interval=0.00001)

    for i in range(int(nombre)):
        mots_spam = open("data/autres/mots_spam.txt", "rt").read().splitlines()
        messages = choices(["¯\_(ツ)_/¯", " ͡° ͜ʖ ͡°", "( ͡° ͜ʖ ͡°)", "(╯°□°）╯︵ ┻━┻", "╯︵╯", "゜-゜", "*-*", "*o*", "(:", "(;", "(=", "8===D", "8---D", ""], k=150)
        messages_ascii = choice(["""
   oo_    ))          \\\    /// 
  /  _)-<(o0)-.   /)  ((O)  (O)) 
  \__ `.  | (_))(o)(O) | \  / |  
     `. | | .-'  //\\  ||\\//||  
     _| | |(    |(__)| || \/ ||  
  ,-'   |  \)   /,-. | ||    ||  
 (_..--'   (   -'   ''(_/    \_) """, """

 ██▓███   ▄▄▄       ██▀███   ▄▄▄      ▓█████▄  ▒█████  ▒██   ██▒
▓██░  ██▒▒████▄    ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██░  ██▒░░  █   ░
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  """, """

░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  ░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  
░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  ░░         ░   ▒     ░░   ░   ░   ▒    ░ ░  ░ ░ ░ ░ ▒   ░    ░  
""", """

 ██░ ██  ▄▄▄       ██░ ██  ▄▄▄      
▓██░ ██▒▒████▄    ▓██░ ██▒▒████▄    
▒██▀▀██░▒██  ▀█▄  ▒██▀▀██░▒██  ▀█▄  
░▓█ ░██ ░██▄▄▄▄██ ░▓█ ░██ ░██▄▄▄▄██ 
░▓█▒░██▓ ▓█   ▓██▒░▓█▒░██▓ ▓█   ▓██▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒   ▓▒█░
 ▒ ░▒░ ░  ▒   ▒▒ ░ ▒ ░▒░ ░  ▒   ▒▒ ░
 ░  ░░ ░  ░   ▒    ░  ░░ ░  ░   ▒   
 ░  ░  ░      ░  ░ ░  ░  ░      ░  ░""", ""])
        messages_mdps = choices(mots_spam, k=50)
        messages_textes = choices(["Bloody", "software", "tag", "taag", "bite", "haha", "cheh", "raid", "dox", "uuuu", "nenene", "face", "zizi", "penis", "pussy", "LOL", "mdrrr", "karma", "c drole", "ah batard tu fumes", "ma bite!", "kobalad du 7", "oeoeoe tu connais", "gxtom le plus beau", "toi même tu l'sais!"], k=20)
        messages_dictionnaires = choice(["""
tout
ORTHOGRAPHE
Locutions et expressions.
Avec tout au singulier : à toute allure, à tout bout de champ, à toute force, à tout hasard, à toute heure, à tout prix, à tout propos, à toute vitesse ; de tout cœur, de toute façon, de tout genre, de toute manière, de tout temps ; en tout cas, en tout point, en tout temps ; en toute saison, en toute hâte.

Avec tout au pluriel : à tous égards, à toutes jambes ; de tous côtés, de toutes pièces ; en toutes lettres, en tous sens ; toutes proportions gardées ; toutes choses égales par ailleurs.

Avec tout au singulier ou au pluriel : à tout moment ou à tous moments ; de toute part ou de toutes parts ; de toute sorte ou de toutes sortes ; en tout genre ou en tous genres (le singulier est plus fréquent ; de même pour en tout lieu ou en tous lieux ; en toute chose ou en toutes choses ; tout compte fait ou tous comptes faits.""", """
Les mots de la francophonie
séraphin morbier poussine cacaille capitaine pils séré débattue achigan sicler

Les mots d'origine étrangère
dazibao didjeridoo chum Sprechgesang skärgård bokmål via ferrata badminton binturong biwa

Les prononciations difficiles
mandrill impala base-ball indomptable coccyx oyat vasistas stagnation chinchilla ignominie

""", """Biochimie

1. Désigne un groupe de vitamines liposolubles.
Médecine

2. Désigne un groupe sanguin du système ABO.
Métrologie

3. Symbole de l'ampère.
Musique

4. Désigne dans certains pays (Allemagne, Grande-Bretagne) la note la, sixième note de la gamme majeure en ut.
5. Sur une partition, désigne l'alto.
Pédologie

6. Désigne l'ensemble des horizons superficiels des sols, enrichis en matière organique par les litières et racines des végétaux et par les fumures enfouies par le labour.
Physique

7. Désigne le nombre de masse d'un noyau.
VOUS CHERCHEZ PEUT-ÊTRE
A.
Désigne un groupe de vitamines liposolubles.

a n.m. inv.
Première lettre de l'alphabet français notant la première des voyelles...

a.
Symbole de l'are et du préfixe atto-.

a-.
Préfixe d'origine grecque entrant dans la composition de nombreux mots...""", """

Voirplus

Contenus SponsorisésÀ Découvrir Aussi
Excès de sucre ? Problème de glycémie ? Faites ceci 1 fois par jour
Science Actualité
La pompe à chaleur hybride : le duo gagnant
GRDF
IPHONE 14 PRO MAX 128GO VIOLET
819 €
SFR
Attention! Ce jeu rendra même votre petite amie jalouse !
MMOHAVEN.COM
Les 5 aliments à éviter (genoux)
Découverte Santé
par Taboola

À DÉCOUVRIR DANS L'ENCYCLOPÉDIE 
absorption intestinale. [MÉDECINE]
Afrique.
Ave, Caesar, morituri te salutant.
avulsion dentaire. [MÉDECINE]
Belgique.
Copernic. Nicolas Copernic.
girafe. [FAUNE]
guerre froide. [DOSSIER].
Haïti.
hernie de la paroi abdominale. [MÉDECINE]
l'opinion (publique).
ornithorynque. [FAUNE]
saumon. [FAUNE]
Stendhal. Henri Beyle, dit Stendhal.
synapse.
tourisme.""", """Données utilisées pour vous suivre
Les données suivantes peuvent être utilisées pour vous suivre dans plusieurs apps et sites web appartenant à d’autres sociétés :

Emplacement
Identifiants
Données d’utilisation
Diagnostic
Données établissant un lien avec vous
Les données suivantes peuvent être collectées et liées à votre identité :

Emplacement
Identifiants
Données d’utilisation
Diagnostic
Données n’établissant aucun lien avec vous
Les données suivantes peuvent être collectées, mais elles ne sont pas liées à votre identité :

Diagnostic
Les pratiques en matière de confidentialité peuvent varier, notamment en fonction des fonctionnalités que vous utilisez ou de votre âge. En savoir plus

Informations
Vente
Farlex, Inc.
 
Taille
98,2 Mo""", """
 
Catégorie
Références 
Compatibilité
iPhone
Nécessite iOS 13.0 ou version ultérieure.
iPad
Nécessite iPadOS 13.0 ou version ultérieure.
iPod touch
Nécessite iOS 13.0 ou version ultérieure.
Mac
Nécessite macOS 11.0 ou version ultérieure et un Mac avec la puce Apple M1 ou version ultérieure.
 
Langues
 
Âge
4+ 
Copyright
© 2021 Farlex, Inc.
 
Prix
Gratuit
 
Achats intégrés
Ad-free upgrade
1,19 €
Site web du développeur 
Assistance 
Engagement de confidentialité 
Du même développeur
Tout afficher

Deutsch Wörterbuch & Thesaurus
Références

Diccionario español.
Références

French Dictionary & Thesaurus
Références

Dizionario Italiano e Sinonimi
Références

قاموس عربي
Références

Acronym Finder
Références
Vous aimerez peut-être aussi
Tout afficher

Traduction Anglais Français et Dictionnaire
Éducation

Anglais-Français Dict. - DIC-o
Références

Conjugaison Française
Éducation

Dictionnaire Littré Français
Éducation

Dictionnaire Linternaute
Éducation

La conjugaison française L'OBS
Éducation""", """AFRIQUE
D’une superficie de 30  millions de km2 pour une population de 1,110  milliard d...


MOYEN ÂGE
On désigne sous ce nom la période de quelque mille ans qui va de la chute de Rom...


PRÉHISTOIRE
La préhistoire désigne la période chronologique de la vie de l’humanité qui va d...


ENVIRONNEMENT
Entourée par la fine couche de l’atmosphère, la Terre abrite des millions d’espè...


IMMUNITÉ
Résistance à un agent infectieux (microbes ou virus) ou toxique (venins et toxin...


ÉLECTRICITÉ
Le courant électrique est constitué par un déplacement d’électrons. Sa productio...


MONDIALISATION
Le terme de «  mondialisation  » se définit comme une internationalisation de l’...


DÉCOLONISATION
Issue des mouvements nationalistes qui émergent à la suite des deux grandes guer...


RÉVOLUTION FRANÇAISE
À la fin du XVIIIe  siècle, la bourgeoisie, dont le rôle économique s’est accru,...


INVASIONS
Dès le milieu du IIIe  s., les peuples germaniques se mettent en mouvement, et c...


ÉNERGIE
Les sources d’énergie utilisées dans le monde sont essentiellement des combustib...


PATRIMOINE
Héritages culturels de générations qui se sont succédé, les vestiges du passé év...


INFORMATIQUE
Science du traitement automatique et rationnel de l’information, l’informatique ...


GENRES ET REGISTRES LITTÉRAIRES
Dans la littérature prise au sens de production des écrivains, on distingue deux...


GRANDES DÉCOUVERTES
Après la chute de Byzance en 1453, le commerce vers l’Orient devient très diffic...""", """

EN CE MOMENT

Jean-Luc Godard
Godard. Jean-Luc Godard.
Cinéaste français et suisse...

Charles de Gaulle
France.
Vie politique depuis 1958

Mésange
mésange. [FAUNE]
Les mésanges se sont répandues dans le monde entier il...

Papillon de nuit
papillon de nuit. [FAUNE]
La plupart des milliers d'espèces de papillons de nuit actuelles...

Libellule
libellule. [FAUNE]
Avec leurs superbes couleurs et leurs ailes en dentelle finement...

Colibri
passereau.
Petit oiseau, au cou court, souvent chanteur et nidifiant.

L'État de Kiev
Ukraine.
Histoire

Aubrey Beardsley, Isolde
Art nouveau.
Nom le plus généralement donné au mouvement de rénovation des...

Ludwig van Beethoven
Beethoven. Ludwig van Beethoven.
Compositeur allemand...""", """

Nos médias à découvrir

Amiens
Amiens
Zèbre
Zèbre
Airbus A-340
Airbus A-340
zébrâne
zébrâne
Æthuse
Æthuse
Alouette
Alouette
Abaca
Abaca
Acéras
Acéras
Agrippine l'Aînée
Agrippine l'Aînée
Amanites
Amanites
Ægopodium
Ægopodium
Alose
Alose"""])
        await ctx.send(f"***{messages}***")
        await ctx.send(f"***{messages_mdps}***")
        await ctx.send(f"***{messages_ascii}***")
        await ctx.send(f"***{messages_textes}***")
        await ctx.send(f"***{messages_dictionnaires}***")
        print(f"{Fore.GREEN}[+] {i + 1}{Fore.LIGHTGREEN_EX} Message(s) Spam2 envoyé(s) avec Succès !{Fore.RESET}")
    
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Spammer - Successfully Completed***")

#Comptes - Codes
@client.command()
async def whitehall_spotify(ctx):

    await ctx.message.delete()

    comptes = [
        'bojaced164@emailnube.com - boj12345',
        'capagef110@mailezee.com - cap12345',
        'mipebe3388@mailezee.com - mip12345',
        'dexoxoj460@mailernam.com - dex12345',
        'moxowo5246@sweatmail.com - mox12345',
        'giboli9578@mrisemail.com - gib12345',
        'roramid110@emailnube.com - ror12345',
        'cahoy87828@newe-mail.com - cah12345',
        'gacef20772@newe-mail.com - gac12345',
        'yatewi8352@newe-mail.com - yat12345',
        'namoba7127@newe-mail.com - nam12345',
        'bixak92762@upcmaill.com - bix12345',
        'tolidiy197@sweatmail.com - tol12345',
        'fofec34077@provamail.com - fof12345',
        'bitawix539@mrisemail.com - bit12345']

    random_comptes = choice(comptes)

    await ctx.send(f"***[:white_check_mark:] {random_comptes} :eyes:***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Spotify - Successfully Completed***")
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Spotify généré avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_carte(ctx):
    await ctx.message.delete()

    code = "" + ('').join(choices(string.digits, k=16))
    mois = "" + ('').join(choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]))
    année = "" + ('').join(choice(["24", "25", "26", "27", "28", "29"]))
    ccv = "" + ('').join(choices(string.digits, k=3))

    await ctx.send(f"""
***CODE : {code} :eyes:***
***EXP : {mois}/{année} :eyes:***
***CCV : {ccv} :eyes:***""")

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Card - Successfully Completed***")

    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Carte générée avec Succès !{Fore.RESET}")

#Générateurs
@client.command()
async def whitehall_nitrocl(ctx):
    await ctx.message.delete()

    nitros_cl = choice([
    "discord.gift/7th7mh5A9tJrRPhNW6ZpUbJX",
    "discord.gift/Wygkb4GxTWhvuqv4EWZRYtTD",
    "discord.gift/WJB8We4YA7V6tfGGutx6pcdy",
    "discord.gift/GsBuUhTzkTb53Z5am4QHk5bm",
    "discord.gift/VFGzvZbvrqfA6AwvRmaN6DtS",
    "discord.gift/quxE9tGYkCmnHDfWZsXqA2QR",
    "discord.gift/wWuqfwAnh6Ju5fFQzDHHE7az",
    "discord.gift/BAhNG3KyavJ9zxmX6anmyS4x",
    "discord.gift/zjpv22zKakM4QN3EB42ucHWJ",
    "discord.gift/5vg2S3gabgqmucBw7qfqFTCT",
    "discord.gift/7YhkBXb7taf5QM9XpNPk73UU",
    "discord.gift/vRB2PhdHWPeG556Ps5Pc293u",
    "discord.gift/gfY3kc7jwWHMjcbcNGyCTJJS",
    "discord.gift/upEsagrXswCEBNwZhUEFT8NM",
    "discord.gift/H5CMpHJTvPbhXNNbcemdRV33",
    "discord.gift/NWA7MgAyhNtDBQ4e8Z9uwDEu",
    "discord.gift/mmAazdwwfCeMbB7dnNc2Cz39",
    "discord.gift/3ccBzws8S5T6Rd9Jr2WE2HWy",
    "discord.gift/bChVbZ6XSRdyTvcpSEg4VBKB"])

    await ctx.send(nitros_cl)

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Nitro - Successfully Completed***")

    print(f"\n{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Nitro Classique : généré avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_nitrocl_https(ctx):
    await ctx.message.delete()

    nitros_cl_https = choice([
    "https://discord.gift/mmAazdwwfCeMbB7dnNc2Cz39",
    "https://discord.gift/6BYPsgPePFvWaK64Ny4jaquY",
    "https://discord.gift/mPeF5ynyGFtzv6Nnw6DWZZrc",
    "https://discord.gift/jZ7AqkJmmsfpA6zxhvc2NBE4",
    "https://discord.gift/WGXWyVpQHVSdgJwfDErtqF9E",
    "https://discord.gift/7YhkBXb7taf5QM9XpNPk73UU",
    "https://discord.gift/Aq27VNbtAY8Pcw36htyXC5jq",
    "https://discord.gift/9uxpqUKb57KsbTbJtBbFwsy9",
    "https://discord.gift/7g2WpH4etZu52wupfATSFugP",
    "https://discord.gift/AVr8k2h9tnynRyjDArtZBU7M",
    "https://discord.gift/6eyPp6m7NAfZ6dYn8TEZuRPG"])

    await ctx.send(nitros_cl_https)

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Nitro - Successfully Completed***")

    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Nitro Classique HTTPS : généré avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_nitrobt(ctx):
    await ctx.message.delete()

    nitros_bt = choice([
    "discord.gift/qKcD2te6KAYQhtAQtWhjT7F4",
    "discord.gift/duHW5XPgE8AYsvWD2qCZ4EcH",
    "discord.gift/duHW5XPgE8AYsvWD2qCZ4EcH",
    "discord.gift/RhTDFPvvTEjkDj6ASCNtVWhC",
    "discord.gift/VnSBNjdBTBfNbrjap8DpVcfK",
    "discord.gift/mTdWkcc2EqCmkHyCv5qgzWhU",
    "discord.gift/qKcD2te6KAYQhtAQtWhjT7F4",
    "discord.gift/M5JHkmkjZjpNXMz22gZtyWDa",
    "discord.gift/VuhvmktzSgsGbAUsR8UFmxqU",
    "discord.gift/32C9geMzvC7CgXpAGevCUYwY",
    "discord.gift/xMcTbwD3ftkVHrsduqSUppqJ",
    "discord.gift/nVkCUwZVCn9cSrHMA5Fms6SH",
    "discord.gift/dzTxg85zSxQHY9SSKw9ah7a2",
    "discord.gift/jFtfJ9ZMTEuHXxqPM35YBPMH",
    "discord.gift/y6KmADg5R8HeGw5DFwDwCmSr",
    "discord.gift/xD5eZY2aQFnaUwe9MYwkuzTE",
    "discord.gift/q48AQJVYfXmJUyhY85vzpR6k",
    "discord.gift/qw2Xekmt6pSJvNKTwZJNZfU2",
    "discord.gift/7mhdAxFp2dHBh45D4r5fdje5",
    "discord.gift/vxjHvBxYSDK7RrHjSXrZf8Bf",
    "discord.gift/RWmQYU8zrFw7UNttMDuEAdXT",
    "discord.gift/FyvqGSRj8zJEu98CtQrhwhwW",
    "discord.gift/gn4785ehBez9RYmA4cV4W6Xz",
    "discord.gift/bdWdAmArJybHZZXPCK7CnzWz",
    "discord.gift/HU9CJE9bAXXJDtetWTaMhNbS",
    "discord.gift/rZwVTh92DUDcRGx4CQskDd3S",
    "discord.gift/4F85BQyXEzPXABpQVTSkKsXP",
    "discord.gift/MvqrkkHMmBXfhpPBZJ5Hb69q"])

    await ctx.send(nitros_bt)

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Nitro - Successfully Completed***")

    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Nitro Boost : généré avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_nitrobt_https(ctx):
    await ctx.message.delete()

    nitros_bt_https = choice([
    "https://discord.gift/qKcD2te6KAYQhtAQtWhjT7F4",
    "https://discord.gift/mTdWkcc2EqCmkHyCv5qgzWhU",
    "https://discord.gift/VnSBNjdBTBfNbrjap8DpVcfK",
    "https://discord.gift/RhTDFPvvTEjkDj6ASCNtVWhC",
    "https://discord.gift/duHW5XPgE8AYsvWD2qCZ4EcH",
    "https://discord.gift/y6CvDKeV4eCg7SVqUjbzy5fa",
    "https://discord.gift/Qby6Guh9xCbgHfmkDa7ZzNnj",
    "https://discord.gift/NgfhgjwJEZfeVCm6aET5UAyK",
    "https://discord.gift/NgfhgjwJEZfeVCm6aET5UAyK",
    "https://discord.gift/EG744yzeQZuMGxq3xeSfqJ53",
    "https://discord.gift/3ZzAymHBtjJRVZfvNFFxZ7Gx",
    "https://discord.gift/xD5eZY2aQFnaUwe9MYwkuzTE",
    "https://discord.gift/DHEerCX9fPuGA6WVRGagxsHb",
    "https://discord.gift/PZ76qKbfX8G8hjTKUKYjZntk",
    "https://discord.gift/nVkCUwZVCn9cSrHMA5Fms6SH",
    "https://discord.gift/T2xKVwHXS9prmQrnA3kJP7eY",
    "https://discord.gift/mTdWkcc2EqCmkHyCv5qgzWhU"])

    await ctx.send(nitros_bt_https)

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Nitro - Successfully Completed***")

    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Nitro Boost HTTPS : généré avec Succès !{Fore.RESET}")

#Personnalisation
@client.command()
async def whitehall_ping(ctx):
    await ctx.message.delete()
    ping = int(client.latency * 1000)
    await ctx.send(f"***[:white_check_mark:] Ping : {ping}ms***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Status - Successfully Completed***")
    print(f"{Fore.GREEN}[+] Ping :{Fore.LIGHTGREEN_EX}{ping}ms !{Fore.RESET}")

@client.command()
async def whitehall_status1(ctx, jeu):
    await ctx.message.delete()
    await client.change_presence(status=discord.Status, activity=discord.game(jeu))
    await ctx.send(f"***[:white_check_mark:] Status changé avec Succès !***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Status - Successfully Completed***")
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Status changé avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_status2(ctx, song):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{song}"))
    await ctx.send(f"***[:white_check_mark:] Status changé avec Succès !***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Status - Successfully Completed***")
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Status changé avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_status3(ctx, twitch):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Streaming(name="My Stream", url=f'https://www.twitch.tv/{twitch}'))
    await ctx.send(f"***[:white_check_mark:] Status changé avec Succès !***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Status - Successfully Completed***")
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Status changé avec Succès !{Fore.RESET}")

@client.command()
async def whitehall_status4(ctx, video):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{video}"))
    await ctx.send(f"***[:white_check_mark:] Status changé avec Succès !***")
    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall Status - Successfully Completed***")
    print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}Status changé avec Succès !{Fore.RESET}")

#Self Infos
#Hacking     
@client.command()
async def whitehalling(ctx, username):
    await ctx.message.delete()
    print(f"")
    print(f"{Fore.GREEN}[+] Dox :{Fore.LIGHTGREEN_EX} Succès !{Fore.RESET}")
    print(f"{Fore.GREEN}[+] Cible :{Fore.LIGHTGREEN_EX} {username} !{Fore.RESET}")
    try:
        url = "http://instagram.com/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send(f"***[:white_check_mark:] Instagram : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Instagram : Non***")

    try:
        url = "https://www.duolingo.com/profile/" + str(username)
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send(f"***[:white_check_mark:] Duolingo : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Duolingo : Non***")

    try:
        url = "https://www.taringa.net/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send(f"***[:white_check_mark:] Taringa : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Taringa : Non***")

    try:
        url = "https://www.meetme.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send(f"***[:white_check_mark:] MeetMe : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] MeetMe : Non***")

    try:
        url = "http://linkedin.com/in/" + username.replace(" ", "-")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send(f"***[:white_check_mark:] Linkedin : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Linkedin : Non***")

    try:
        url = "http://facebook.com/" + username.replace(" ", ".")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Facebook : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Facebook : Non***")

    try:
        url = "http://peoplefinders.com/name/" + username.replace(" ", "-")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Peoplefinders : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Peoplefinders : Non***")

    try:
        url = "http://doxbin.com/upload/" + username.replace(" ", "")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Doxbin : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Doxin : Non***")

    try:
        url = "http://pinterest.com/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Pinterest : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Pinterest : Non***")

    try:
        url = "http://twitter.com/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Twitter : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Twitter : Non***")

    try:
        url = "http://youtube.com/user/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] YouTube : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] YouTube : Non***")

    try:
        url = "http://github.com/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Github : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Github : Non***")

    try:
        url = "http://stackoverflow.com/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Stackoverflow : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Stackoverflow : Non***")

    try:
        url = "http://steamcommunity.com/id/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Steam : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Steam : Non***")

    try:
        url = "http://reddit.com/user/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Reddit : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Reddit : Non***")

    try:
        url = "http://www.tiktok.com/@" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] TikTok : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] TikTok : Non***")

    try:
        url = "http://account.xbox.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Xbox : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Xbox : Non***")

    try:
        url = "https://imgur.com/user/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Imgur : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Imgur : Non***")

    try:
        url = "https://www.leboncoin.fr/profil/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Leboncoin : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Leboncoin : Non***")

    try:
        url = "https://snapchat.com/add/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Snapchat : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Snapchat : Non***")

    try:
        url = "https://www.dailymotion.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Dailymotion : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Dailymotion : Non***")

    try:
        url = "https://replit.com/@" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Replit : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Replit : Non***")

    try:
        url = "https://open.spotify.com/search/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Spotify : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Spotify : Non***")

    try:
        url = "https://picsart.com/u/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] PicsArt : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] PicsArt : Non***")

    try:
        url = "http://www.twitch.tv/" + username.replace(" ", "_")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Twitch : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Twitch : Non***")

    try:
        url = "http://whitepages.com/name/" + username.replace(" ", "-")
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Pages Blanches US/EN : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Pages Blanches US/EN : Non***")

    try:
        url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou=" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Pages Blanches FR : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Pages Blanches FR : Non***")

    try:
        url = f"https://www.pages-annuaire.net/res/search?q={username}&w=france"
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Pages Annuaires : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Pages Annuaires : Non***")

    try:
        url = "https://fr.quora.com/profile/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Quora : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Quora : Non***")

    try:
        url = "https://fr.foursquare.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Foursquare : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Foursquare : Non***")

    try:
        url = "https://www.flickr.com/photos/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Flickr : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Flickr : Non***")

    try:
        url = "https://soundcloud.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] SoundCloud : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] SoundCloud : Non***")

    try:
        url = "https://www.beatstars.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] BeatStars : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] BeatStars : Non***")

    try:
        url = "https://www.couchsurfing.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] Couchsurfing : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] Couchsurfing : Non***")

    try:
        url = "https://www.deviantart.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] DeviantArt : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] DeviantArt : Non***")

    try:
        url = "https://myspace.com/" + username
        r = urlopen(url)
        r.headers = choice(all_headers)
        await ctx.send("***[:white_check_mark:] MySpace : Oui***")
    except HTTPError:
        await ctx.send("***[:no_entry:] MySpace : Non***")

    await ctx.send(f"https://searx.org/search?q={username}")
    await ctx.send(f"https://namechk.com/namechk-plugin-search-results/?n={username}")

    await ctx.send(f"***Vérification des Serveurs Discord...***")

    try:
        discord_status = "https://discordstatus.com/"
        urlopen(discord_status)
        await ctx.send(f"***[:white_check_mark:] Discord = 100% en marche !***")
    except HTTPError:
        await ctx.send(f"***[:no_entry:] Bug Discord...***")
        pass

    await ctx.send(f"***Vérification du Serveur...***")
    try:
        invite_checker = urlopen(f'https://discord.com/api/v6/invite/{username}')
        invite_checker.headers = ({'authorization': token})
        await ctx.send(f"***[:white_check_mark:] Invitation Valide !***")
        await ctx.send(f"https://discord.gg/{username}")
    except HTTPError:
        await ctx.send(f"***[:no_entry:] Invitation Invalide... (discord.gg/{username})***")

    url_json_1 = "http://ip-api.com/json/" + 'instagram.com'
    values_1 = json.load(urlopen(url_json_1))

    url_json_2 = "http://ip-api.com/json/" + 'linkedin.com'
    values_2 = json.load(urlopen(url_json_2))

    url_json_3 = "http://ip-api.com/json/" + 'facebook.com'
    values_3 = json.load(urlopen(url_json_3))

    url_json_4 = "http://ip-api.com/json/" + 'whitepages.com'
    values_4 = json.load(urlopen(url_json_4))

    url_json_5 = "http://ip-api.com/json/" + 'peoplefinders.com'
    values_5 = json.load(urlopen(url_json_5))

    url_json_6 = "http://ip-api.com/json/" + 'doxbin.com'
    values_6 = json.load(urlopen(url_json_6))

    url_json_7 = "http://ip-api.com/json/" + 'pinterest.com'
    values_7 = json.load(urlopen(url_json_7))

    url_json_8 = "http://ip-api.com/json/" + 'twitter.com'
    values_8 = json.load(urlopen(url_json_8))

    url_json_9 = "http://ip-api.com/json/" + 'youtube.com'
    values_9 = json.load(urlopen(url_json_9))

    url_json_10 = "http://ip-api.com/json/" + 'github.com'
    values_10 = json.load(urlopen(url_json_10))

    url_json_11 = "http://ip-api.com/json/" + 'stackoverflow.com'
    values_11 = json.load(urlopen(url_json_11))

    url_json_12 = "http://ip-api.com/json/" + 'steamcommunity.com'
    values_12 = json.load(urlopen(url_json_12))

    url_json_13 = "http://ip-api.com/json/" + 'reddit.com'
    values_13 = json.load(urlopen(url_json_13))

    url_json_14 = "http://ip-api.com/json/" + 'tiktok.com'
    values_14 = json.load(urlopen(url_json_14))

    url_json_15 = "http://ip-api.com/json/" + 'account.xbox.com'
    values_15 = json.load(urlopen(url_json_15))

    url_json_16 = "http://ip-api.com/json/" + 'imgur.com'
    values_16 = json.load(urlopen(url_json_16))

    url_json_17 = "http://ip-api.com/json/" + 'leboncoin.fr'
    values_17 = json.load(urlopen(url_json_17))

    url_json_18 = "http://ip-api.com/json/" + 'snapchat.com'
    values_18 = json.load(urlopen(url_json_18))

    url_json_19 = "http://ip-api.com/json/" + 'dailymotion.com'
    values_19 = json.load(urlopen(url_json_19))

    url_json_20 = "http://ip-api.com/json/" + 'replit.com'
    values_20 = json.load(urlopen(url_json_20))

    url_json_21 = "http://ip-api.com/json/" + 'open.spotify.com'
    values_21 = json.load(urlopen(url_json_21))

    url_json_22 = "http://ip-api.com/json/" + 'picsart.com'
    values_22 = json.load(urlopen(url_json_22))

    url_json_23 = "http://ip-api.com/json/" + 'twitch.tv'
    values_23 = json.load(urlopen(url_json_23))

    url_json_24 = "http://ip-api.com/json/" + 'pagesjaunes.fr'
    values_24 = json.load(urlopen(url_json_24))

    url_json_25 = "http://ip-api.com/json/" + 'pages-annuaire.net'
    values_25 = json.load(urlopen(url_json_25))

    url_json_26 = "http://ip-api.com/json/" + 'fr.quora.com'
    values_26 = json.load(urlopen(url_json_26))

    url_json_27 = "http://ip-api.com/json/" + 'fr.foursquare.com'
    values_27 = json.load(urlopen(url_json_27))

    url_json_28 = "http://ip-api.com/json/" + 'flickr.com'
    values_28 = json.load(urlopen(url_json_28))

    url_json_29 = "http://ip-api.com/json/" + 'soundcloud.com'
    values_29 = json.load(urlopen(url_json_29))

    url_json_30 = "http://ip-api.com/json/" + 'beatstars.com'
    values_30 = json.load(urlopen(url_json_30))

    url_json_31 = "http://ip-api.com/json/" + 'couchsurfing.com'
    values_31 = json.load(urlopen(url_json_31))

    url_json_32 = "http://ip-api.com/json/" + 'deviantart.com'
    values_32 = json.load(urlopen(url_json_32))

    url_json_33 = "http://ip-api.com/json/" + 'myspace.com'
    values_33 = json.load(urlopen(url_json_33))

    url_json_34 = "http://ip-api.com/json/" + 'meetme.com'
    values_34 = json.load(urlopen(url_json_34))

    url_json_35 = "http://ip-api.com/json/" + 'taringa.net'
    values_35 = json.load(urlopen(url_json_35))

    url_json_36 = "http://ip-api.com/json/" + 'duolingo.com'
    values_36 = json.load(urlopen(url_json_36))

    await ctx.send(f"***[:white_check_mark:] Instagram : ***")
    await ctx.send(values_1['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Linkedin : ***")
    await ctx.send(values_2['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Facebook : ***")
    await ctx.send(values_3['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Pages Blanches : ***")
    await ctx.send(values_4['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Peoplefinders : ***")
    await ctx.send(values_5['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] DoxBin : ***")
    await ctx.send(values_6['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Pinterest : ***")
    await ctx.send(values_7['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Twitter : ***")
    await ctx.send(values_8['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] YouTube : ***")
    await ctx.send(values_9['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] GitHub : ***")
    await ctx.send(values_10['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Stackoverflow : ***")
    await ctx.send(values_11['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Steam : ***")
    await ctx.send(values_12['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Reddit : ***")
    await ctx.send(values_13['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] TikTok : ***")
    await ctx.send(values_14['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Xbox : ***")
    await ctx.send(values_15['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Imgur : ***")
    await ctx.send(values_16['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Leboncoin : ***")
    await ctx.send(values_17['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Snapchat : ***")
    await ctx.send(values_18['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Dailymotion : ***")
    await ctx.send(values_19['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Replit : ***")
    await ctx.send(values_20['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Spotify : ***")
    await ctx.send(values_21['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] PicsArt : ***")
    await ctx.send(values_22['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Twitch : ***")
    await ctx.send(values_23['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Pages Jaunes : ***")
    await ctx.send(values_24['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Pages Annuaires : ***")
    await ctx.send(values_25['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Quora : ***")
    await ctx.send(values_26['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] FourSquare : ***")
    await ctx.send(values_27['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Flickr : ***")
    await ctx.send(values_28['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] SoundCloud : ***")
    await ctx.send(values_29['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] BeatStars : ***")
    await ctx.send(values_30['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] Couchsurfing : ***")
    await ctx.send(values_31['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] DeviantArt : ***")
    await ctx.send(values_32['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:] MySpace : ***")
    await ctx.send(values_33['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:]MeetMe : ***")
    await ctx.send(values_34['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:]Taringa : ***")
    await ctx.send(values_35['query'])
    await ctx.send(f":arrow_down:")
    await ctx.send(f"***[:white_check_mark:]Duolingo : ***")
    await ctx.send(values_36['query'])
    await ctx.send(f"--------------------------------")

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehalling - Successfully Completed***")


@client.command()
async def whitehall_ip(ctx, ip):
    await ctx.message.delete()
    url = f"http://ip-api.com/json/{ip}"
    values = json.load(urlopen(url))
    print(f"")

    await ctx.send(f"***[:white_check_mark:] Adresse IP : " + values['query'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Status : " + values['status'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Ville : " + values['city'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Pays : " + values['country'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Code Postal : " + values['zip'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Région : " + values['regionName'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Temps de Zone : " + values['timezone'] + f"***")
    await ctx.send(f"***[:white_check_mark:] Organisation : " + values['org'] + f"***")
    await ctx.send(f"***[:white_check_mark:] AS : " + values['as'] + f"***")

    print(f"{Fore.GREEN}[+] Adresse IP :{Fore.LIGHTGREEN_EX} " + values['query'])
    print(f"{Fore.GREEN}[+] Status :{Fore.LIGHTGREEN_EX} " + values['status'])
    print(f"{Fore.GREEN}[+] Ville :{Fore.LIGHTGREEN_EX} " + values['city'])
    print(f"{Fore.GREEN}[+] Pays :{Fore.LIGHTGREEN_EX} " + values['country'])
    print(f"{Fore.GREEN}[+] Code Postal :{Fore.LIGHTGREEN_EX} " + values['zip'])
    print(f"{Fore.GREEN}[+] Région :{Fore.LIGHTGREEN_EX} " + values['regionName'])
    print(f"{Fore.GREEN}[+] Temps de Zone :{Fore.LIGHTGREEN_EX} " + values['timezone'])
    print(f"{Fore.GREEN}[+] Organisation :{Fore.LIGHTGREEN_EX} " + values['org'])
    print(f"{Fore.GREEN}[+] AS :{Fore.LIGHTGREEN_EX} " + values['as'])

    for ping_ip in range(1,255):
        address = "192.168.1." + str(ping_ip)

        try:
            hostname, alias, addresslist = socket.gethostbyaddr(address)

        except socket.herror:
            hostname = None
            alias = None
            addresslist = address

            if hostname == False:
                print(f"{Fore.RED}[-] {addresslist}", f"{Fore.WHITE}=>", f"{Fore.LIGHTRED_EX}{hostname}")
                await ctx.send(f"***[:no_entry:] {addresslist} => {hostname}***")
            else:
                print(f"{Fore.GREEN}[+] {addresslist}", f"{Fore.WHITE}=>", f"{Fore.LIGHTGREEN_EX}{hostname}")
                await ctx.send(f"***[:white_check_mark:] {addresslist} => {hostname}***")

    await ctx.send(f"↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓")
    await ctx.send(f"***[:white_check_mark:] whitehall IP - Successfully Completed***")

#Help
@client.command()
async def whitehall(ctx):
    await ctx.reply(f"***[:white_check_mark:] C'est moi !***")
    
    Write.Print(f"""
SERVEURS :
[1] whitehall_copier + id du serveur à copier = Copier un Serveur

HACKING :
[1] whitehalling + personne = Dox
[2] whitehall_ip + ip = Infos d'une adresse IP

RAIDS :
[1] whitehall_spam1 = Spammer un Message
[2] whitehall_spam2 = Spammer des caractères spéciaux

INFOS :
[1] whitehall_membre + id = Infos d'un Membre
[2] whitehall_serveur = Infos d'un Serveur

VOCALES :
[1] whitehall_rejoindre = Rejoindre la Vocale
[2] whitehall_quitter = Quitter la Vocale
[3] whitehall_musique + url = Mettre de la Musique

PERSONNALISATION
[1] whitehall_ping = Latence du Bot (Ping)
[2] whitehall_status1 + le nom = Changer le Statut (Jeu)
[3] whitehall_status2 + le nom = Changer le Statut (Ecoute)
[4] whitehall_status3 + le nom  = Changer le Statut (Stream)
[5] whitehall_status4 + le nom  = Changer le Statut (Regarde)

GÉNÉRATEURS
[1] whitehall_spotify = Générer Spotify
[2] whitehall_carte = Générér Carte

[3] whitehall_nitrocl = Générer Nitro Cl sans https
[4] whitehall_nitrocl_https = Générer Nitro Cl avec https
[5] whitehall_nitrobt = Générer Nitro Bt sans https
[6] whitehall_nitrobt_https = Générer Nitro Bt avec https

AUTRES :
[1] whitehall = Liste des Commandes""", Colors.purple_to_blue, interval=0.00001)

client.run(token, bot=False)