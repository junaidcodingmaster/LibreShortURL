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

echo "[=] Setting up virtual environment..."
python3 -m venv venv
echo "[+] Virtual environment created at './venv'"

echo "[=] Installing requirements..."
./venv/bin/pip install -r requirements.txt
echo "[+] Requirements installed!"

echo "[=] Running setup script..."
./venv/bin/python setup.py
echo "[+] Setup completed!"

echo
echo "To activate manually:"
echo "  source ./venv/bin/activate"
echo "  python app.py"
echo
