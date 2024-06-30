# filename: install_libraries.py
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install("pandas")
    install("pandas_datareader")
    install("matplotlib")