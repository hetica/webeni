#!/usr/bin/python
# *-* coding: utf-8 -*-

import sys, os
import cisco_clt

server = os.path.dirname(sys.argv[0]) + '/pytacad-server'
cwd = '/var/local/pytacad/'
dirClasses = cwd + 'classes'
os.chdir(cwd)

# envoyer en argument le premier argument de la commande
search_str = sys.argv[1]
search = cisco_clt.find_user(search_str)

if search[0] == 0:
	mesg = "Aucune occurence trouvée"
if search[0] == 1:
	mesg = cisco_clt.afficher_stags(search[1])
if search[0] > 1:
	mesg = cisco_clt.afficher_stags(search[1])

print(mesg)


