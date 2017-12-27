"""Module to control the many devices of my apt."""
from phue import Bridge
import cec
import pychromecast


class Controllers(object):
  # setup
  LIVING_ROOM = [2,3]
  BEDROOM = [1]
  BRIDGE_IP = '10.0.0.109'
  SPEAKER_IP = '10.0.0.135'

  def __init__(self):
    self.cast = pychromecast.Chromecast(self.SPEAKER_IP)
    self.phue = Bridge(self.BRIDGE_IP)
    self.tv = cec.Device(cec.CECDEVICE_TV)
    cec.init()

  def tv_ctrl(self, power=None):
    if power:
      return self.tv.power_on()
    return self.tv.standby()
    
  def light_ctrl(self, power=None):
    if power:
      return self.phue.set_light(self.LIVING_ROOM, 'on', True)
    return self.phue.set_light(self.LIVING_ROOM, 'on', False)

  def speaker_ctrl(self, power=None):
    if power:
      return self.cast.media_controller.play()
    return self.cast.media_controller.pause()
