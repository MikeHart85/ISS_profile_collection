import uuid
from collections import namedtuple
import os
import time as ttime
from ophyd import (ProsilicaDetector, SingleTrigger, Component as Cpt,
                   EpicsSignal, EpicsSignalRO, ImagePlugin, StatsPlugin, ROIPlugin,
                   DeviceStatus)
from ophyd.areadetector.base import ADComponent as ADCpt, EpicsSignalWithRBV
from ophyd import DeviceStatus, set_and_wait
from bluesky.examples import NullStatus
import filestore.api as fs

class Shutter():
	def __init__(self):
		if(pb4.do3.default_pol.value == 1):
			self.state = 'closed'
		elif(pb4.do3.default_pol.value == 0):
			self.state = 'open'
		
	def open(self):
		pb4.do3.default_pol.put(0)
		self.state = 'open'
		
	def close(self):
		pb4.do3.default_pol.put(1)
		self.state = 'closed'

shutter = Shutter()
