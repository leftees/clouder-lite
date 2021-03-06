"""
You can specify only the values that you'd like to have different from that of the default.
At least an empty dictionary of flask and app is a must for each configuration.

Instructions for configuring the app:
flask settings::
host: 0.0.0.0,
port: 5000- recommended, 80- if you're accessing from outside the local network. May need su permission.
threaded: True- handles multiple requests simultaneously, False- only one request at a time.
debug: True- opens a terminal in case of error. DO NOT set it to True if you're accessing the server from outside.

app settings::
content_folder: the directory that will be used as root for uploads and downloads.
                Moving 'UP' from this directory will not be allowed for security reasons.
qr_code_external: whether or not a qr code should be generated for the external IP address.
qr_code_internal: whether or not a qr code should be generated for the internal IP address.
interface: the interface through which the computer is connected.
theme: the front-end theme that is being used.
"""

from os import getcwd

configurations = {
  'default': {
    'flask': {
      'host': '0.0.0.0',
      'port': 5000,
      'threaded': True,
      'debug': False,
    },
    'app': {
      'content_folder': getcwd() + '/content/',
      'qr_code_external': False,
      'qr_code_internal': False,
      'interface': 'wlan0',
      'theme': 'default',
    },
  },

  'dev': {
    'flask': {
      'debug': True,
    },
    'app': {
      'qr_code_external': True,
      'qr_code_internal': True,
    },
  },

  'external': {
    'flask': {
      'port': 80,
    },
    'app': {
      'qr_code_external': True,
      'qr_code_internal': True,
    },
  },

  'me': {
    'flask': {
      'port': 9001,
    },
    'app': {
      'content_folder': '/home/rpr/code/clouder-lite/content/',
      # 'content_folder': '/home/rpr/Downloads/'
    },
  },
}
