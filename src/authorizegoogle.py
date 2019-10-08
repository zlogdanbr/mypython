# these will import the ids to our machine so google
# knows you are ok

from gmusicapi import Mobileclient
from gmusicapi import Musicmanager

def machineautn():

    mm = Mobileclient()
    mm.perform_oauth()

    mm2 = Musicmanager()
    mm2.perform_oauth()

machineautn()