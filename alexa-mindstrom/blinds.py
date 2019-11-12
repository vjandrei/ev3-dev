#!/usr/bin/env python3

import os
import sys
import time
import logging

from ev3dev2.sound import Sound
from ev3dev2.led import Leds

from agt import AlexaGadget

# set logger to display on both EV3 Brick and console
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s')
logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
logger = logging.getLogger(__name__)

class MindstormsGadget(AlexaGadget):
    """
    Enabled Alexa device communication by extending from AlexaGadget
    """

    def __init__(self):
        """
        Performs Alexa Gadget initialization
        """
        super().__init__()

        self.leds = Leds()
        self.sound = Sound()
    
    def on_connected(self, device_addr):
        """
        Gadget connected to the paired Echo device.
        :param device_addr: the address of the device we connected to
        """
        logger.info("{} connected to Echo device".format(self.friendly_name))
    
    
if __name__ == '__main__':
    
    gadget = MindstormsGadget()
    gadget.main()