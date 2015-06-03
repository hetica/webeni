#!/usr/bin/python
# *-* coding: utf-8 -*-

import sys, os
import cisco_clt

# envoyer en argument le premier argument de la commande
search_str = sys.argv[1]
search = cisco_clt.find_classe(search_str)

print search
