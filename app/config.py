from config.default import *


# Database configuration

DBSERVER = ''
DBPORT = ''
DBUSER = ''
DBPASSW = ''
DBNAME = ''

DBURI = f'mongodb://{DBUSER}:{DBPASSW}@{DBSERVER}:{DBPORT}'


# Server configuration

HOST = '192.168.0.90'
PORT = 5150     # Integer
CERTFOLDER = None

FONAWESOMETOKEN = 'AA9826AF-A195-4445-B35D-418F6D4CBBF1'