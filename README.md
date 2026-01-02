# NetworkAutomation
A repo which will have automation scripts for network automation. 

1. Cisco NX-OS SSH Automation using Paramiko
A simple and secure Python script to connect to a Cisco NX-OS device via SSH, execute CLI commands, and fetch outputs — without hardcoding credentials.

This project demonstrates real-world network automation fundamentals using Paramiko, suitable for learning, demos, and interviews.

🚀 Features

Secure SSH connection using Paramiko

Password input hidden using getpass

Interactive shell handling for NX-OS

Paging disabled (terminal length 0)

Clean and readable output

Safe to share (no hardcoded secrets)

🛠️ Prerequisites

Python 3.8+

SSH access to a Cisco NX-OS device (or lab)

Basic knowledge of Python & networking

📦 Installation

Install Paramiko using pip:

python -m pip install paramiko


Verify installation:

python -m pip show paramiko

📂 Project Structure
paramiko-nxos-ssh/
│
├── nxos_ssh.py
└── README.md
