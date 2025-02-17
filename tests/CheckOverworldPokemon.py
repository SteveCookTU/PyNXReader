# Script to read overworld pokemon
# Save the game to update the KCoordinates block

# Go to root of PyNXReader
import sys
import json
import signal
sys.path.append('../')

from nxreader import SWSHReader

# Connect to Switch
config = json.load(open("../config.json"))
r = SWSHReader(config["IP"],usb_connection=config["USB"])

def signal_handler(signal, frame): #CTRL+C handler
    print("Stop request")
    r.close()

signal.signal(signal.SIGINT, signal_handler)

last_info = []
while True:
    # Refresh KCoords block
    r.KCoordinates.refresh()
    pkms = r.KCoordinates.ReadOwPokemonFromBlock()
    info = []
    for pkm in pkms:
        info.append(hex(pkm.seed) + " " + str(pkm))
    if info != last_info:
        last_info = info
        for pkm in info:
            print(pkm)
        print("-------------------------------")
    r.pause(0.3)
r.close()
