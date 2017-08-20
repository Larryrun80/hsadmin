# System will load configs with following sequence:
#   1. this file (/config.py)
#   2. /instance/default.py (if exists)
#   3. config file defined in enviroment variable "APP_CONFIG_FILE"
#
# Write insensitive settings here and secret ones in /instance/default.py
# Write distribute concerned settings in envvar path:
#   1. Create instance folder in Project root directory
#   2. Add distribution config files
#      like default.py / development.py / production.py
# System will read these via using app.config.from_envvar()
# /instance/default.py will overload this config file
# envvar settings will overload /instance/default.py

DEBUG = True  # disable Flask debug mode
BCRYPT_LEVEL = 13  # config Flask-Bcrypt
