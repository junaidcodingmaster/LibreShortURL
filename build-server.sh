#!/bin/bash
echo
echo "   _        _   _                      _____   _                      _     _    _   _____    _      "
echo "  | |      (_) | |                    / ____| | |                    | |   | |  | | |  __ \  | |     "
echo "  | |       _  | |__    _ __    ___  | (___   | |__     ___    _ __  | |_  | |  | | | |__) | | |     "
echo "  | |      | | | '_ \  | '__|  / _ \  \___ \  | '_ \   / _ \  | '__| | __| | |  | | |  _  /  | |     "
echo "  | |____  | | | |_) | | |    |  __/  ____) | | | | | | (_) | | |    | |_  | |__| | | | \ \  | |____ "
echo "  |______| |_| |_.__/  |_|     \___| |_____/  |_| |_|  \___/  |_|     \__|  \____/  |_|  \_\ |______|"
echo  
echo " ~ Junaid[abujuni.dev]"

echo "[=] Installing requirements..."
pip install -r requirements.txt
echo "[+] Requirements installed!"

echo "[=] Running setup script..."
python setup.py
echo "[+] Setup completed!"
