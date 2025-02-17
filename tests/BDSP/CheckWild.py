# Go to root of PyNXReader
import signal
import sys
import json
sys.path.append('../../')

from nxreader import BDSPReader
from structure import PK8


config = json.load(open("../../config.json"))
reader = BDSPReader(config["IP"],usb_connection=config["USB"])

def signal_handler(signal, advances): #CTRL+C handler
    print("Stop request")
    reader.close()

signal.signal(signal.SIGINT, signal_handler)

while True:
    pk8 = PK8(reader.readWild())
    if pk8.isValid and pk8.ec != 0:
        print(pk8)
    else:
        print("No battle started\n")
    stop = input("Check again? (y/n): ")
    print()
    if stop == 'n' or stop == 'N':
        reader.close()
