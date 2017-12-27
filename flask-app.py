"""Flask REST API to allow Google Assistant to interface with my apt."""

from flask import Flask
from flask import request
from controllers import Controllers

POWER_ON = ['on', 'true','1']
POWER_OFF = ['off', 'false', 'none', '0']
app = Flask(__name__)
controller = Controllers()

# Main Power Endpoint
@app.route('/power')
def power():
  return_msg = ""
  return_err = ""
  # Handle request to TV
  if 'tv' in request.args:
    state = request.args.get('tv').replace(' ', '').lower()
    if state in POWER_ON:
      controller.tv_ctrl(True)
      return_msg += "[TV Power On]"
    elif state in POWER_OFF:
      controller.tv_ctrl()
      return_msg += "[TV Power Off]"
    else:
      return_err += "Bad Request 'tv={} '".format(state)
  # Handle request to lights
  if 'lights' in request.args:
    state = request.args.get('lights').replace(' ', '').lower()
    if state in POWER_ON:
      controller.light_ctrl(True)
      return_msg += "[Lights On]"
    elif state in POWER_OFF:
      controller.light_ctrl()
      return_msg += "[Lights Off]"
    else:
      return_err += "Bad Request 'lights={} '".format(state)
  # Handle request to lights
  if 'speaker' in request.args:
    state = request.args.get('speaker').replace(' ', '').lower()
    if state in POWER_ON:
      controller.speaker_ctrl(True)
      return_msg += "[Speaker On]"
    elif state in POWER_OFF:
      controller.speaker_ctrl()
      return_msg += "[Speaker Off]"
    else:
      return_err += "Bad Request 'speaker={}'".format(state)
  # Handle request for all
  if 'all' in request.args:
    state = request.args.get('all').replace(' ', '').lower()
    if state in POWER_ON:
      controller.tv_ctrl(True)
      controller.light_ctrl(True)
      controller.speaker_ctrl(True)
      return_msg += "[Everything On]"
    elif state in POWER_OFF:
      controller.tv_ctrl()
      controller.light_ctrl()
      controller.speaker_ctrl()
      return_msg += "[Everything Off]"
    else:
      return_err += "Bad Request 'all={}'".format(state)
  # Handle return message and status code    
  if return_msg:
    return return_msg
  if return_err:
    return return_err, 400
  return "Bad Request", 400
  
  if __name__ == '__main__':
    app.run(debug=True)
