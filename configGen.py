import configparser
import discord

def generate(server, roles):
    config = configparser.ConfigParser()
    config['Server Information'] = {'Server Name': server}
    for role in roles:
        config[role] = {}
        config[role]['Basic Commands'] = 'True'
        config[role]['Music Commands'] = 'False'
        config[role]['Stat Commands'] = 'True'
        config[role]['Game Commands'] = 'True'
        config[role]['Admin Commands'] = 'False'
    with open('config/' + server + '_conf.ini', 'w') as configfile:
        config.write(configfile)
