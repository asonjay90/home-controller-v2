"""Flask REST API to allow Google Assistant to interface with my apt."""

from flask import Flask
from flask import request
from controllers import Controllers

POWER_ON = ['on', 'true','1']
POWER_OFF = ['off', 'false', 'none', '0']
DEVICES = ['all', 'tv', 'lights', 'speaker']
app = Flask(__name__)
controller = Controllers()

# Main Power Endpoint
@app.route('/power')
def power():
  return_msg = ""
  return_err = ""
  # Parse query params and call appropriate controller method
  for device_name, state in request.args.iteritems():
    if device_name in DEVICES:
      device_pwr = getattr(controller, device_name + '_ctrl')
      if state in POWER_ON:
        device_pwr(True)
        return_msg += "[{} power on]".format(device_name)
      elif state in POWER_OFF:
        device_pwr()
        return_msg += "[{} power off]".format(device_name)
      else:
        return_err += "[Bad Request '{}={}'] ".format(device_name, state)
      
  # Handle return message and status code    
  if return_err:
    return_msg += " " + return_err
    return return_msg, 400
  if return_msg:
    return return_msg, 200
  return "[Bad Request]", 400
 

  
  if __name__ == '__main__':
    app.run(debug=True)

