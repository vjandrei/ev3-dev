# Copyright 2019 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
# 
# You may not use this file except in compliance with the terms and conditions 
# set forth in the accompanying LICENSE.TXT file.
#
# THESE MATERIALS ARE PROVIDED ON AN "AS IS" BASIS. AMAZON SPECIFICALLY DISCLAIMS, WITH 
# RESPECT TO THESE MATERIALS, ALL WARRANTIES, EXPRESS, IMPLIED, OR STATUTORY, INCLUDING 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

import time
import logging

from ev3dev2.sound import Sound
from ev3dev2.led import Leds

from agt import AlexaGadget

# Set the logging level to INFO to see messages from AlexaGadget
logging.basicConfig(level=logging.INFO)


class MindstormsGadget(AlexaGadget):
    """
    An Mindstorms gadget that will react to the Alexa wake word.
    """

    def __init__(self):
        """
        Performs Alexa Gadget initialization routines and ev3dev resource allocation.
        """
        super().__init__()

        self.leds = Leds()
        self.sound = Sound()

    def on_connected(self, device_addr):
        """
        Gadget connected to the paired Echo device.
        :param device_addr: the address of the device we connected to
        """
        self.leds.set_color("LEFT", "GREEN")
        self.leds.set_color("RIGHT", "GREEN")
        print("{} connected to Echo device".format(self.friendly_name))

    def on_disconnected(self, device_addr):
        """
        Gadget disconnected from the paired Echo device.
        :param device_addr: the address of the device we disconnected from
        """
        self.leds.set_color("LEFT", "BLACK")
        self.leds.set_color("RIGHT", "BLACK")
        print("{} disconnected from Echo device".format(self.friendly_name))

    def on_alexa_gadget_statelistener_stateupdate(self, directive):
        """
        Listens for the wakeword state change and react by turning on the LED.
        :param directive: contains a payload with the updated state information from Alexa
        """
        color_list = ['BLACK', 'AMBER', 'YELLOW', 'GREEN']
        for state in directive.payload.states:
            if state.name == 'wakeword':

                if state.value == 'active':
                    print("Wake word active - turn on LED")
                    self.sound.play_song((('A3', 'e'), ('C5', 'e')))
                    for i in range(0, 4, 1):
                        self.leds.set_color("LEFT", color_list[i], (i * 0.25))
                        self.leds.set_color("RIGHT", color_list[i], (i * 0.25))
                        time.sleep(0.25)

                elif state.value == 'cleared':
                    print("Wake word cleared - turn off LED")
                    self.sound.play_song((('C5', 'e'), ('A3', 'e')))
                    for i in range(3, -1, -1):
                        self.leds.set_color("LEFT", color_list[i], (i * 0.25))
                        self.leds.set_color("RIGHT", color_list[i], (i * 0.25))
                        time.sleep(0.25)


if __name__ == '__main__':

    # Startup sequence
    gadget = MindstormsGadget()
    gadget.sound.play_song((('C4', 'e'), ('D4', 'e'), ('E5', 'q')))
    gadget.leds.set_color("LEFT", "GREEN")
    gadget.leds.set_color("RIGHT", "GREEN")

    # Gadget main entry point
    gadget.main()

    # Shutdown sequence
    gadget.sound.play_song((('E5', 'e'), ('C4', 'e')))
    gadget.leds.set_color("LEFT", "BLACK")
    gadget.leds.set_color("RIGHT", "BLACK")
