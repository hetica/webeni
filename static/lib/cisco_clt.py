#!/usr/bin/python
# *-* coding:utf-8 *-*

__appname__ = 'pytacad-clt'
__version__ = "0.1"
__author__ = "Benoit Guibert <benoit.guibert@free.fr>"
__licence__ = ""

import os, sys
import unicodedata
from django.utils.encoding import smart_unicode

server = os.path.dirname(sys.argv[0]) + '/pytacad-server'
cwd = '/var/local/pytacad/'
dirClasses = cwd + 'classes'
os.chdir(cwd)

def find_user(search_str=None):
	""" Chercher un utilisateur """
	f = open('liste_stagiaires')
	c = f.readlines()		# c : contenu avec une liste des lignes
	nb = 0
	list_stag = []
	for a in c:
		if unicodedata.normalize("NFKD", smart_unicode(search_str.lower(), 'utf-8')).encode('ascii', 'ignore') in unicodedata.normalize("NFKD", smart_unicode(a.lower(), 'utf-8')).encode('ascii', 'ignore'):
			list_stag.append(a)
			nb +=1
	return (nb, list_stag)

def afficher_stags(stags):
	""" mettre en forme l'affichage """
	result = ""
	for stag in stags:
		s = stag.split(';')
		result += 'Stagiaire : \t{0} {1} ({2})\n'.format(s[1], s[0], s[3])
		for i,a in enumerate(stag.split(';')[5].split(',')):
			if i == 0: result += 'Classes :\t' + a + '\n'
			else : result += ('\t\t{0}\n'.format(a))
	return result

def find_classe(search_str=None):
	"""Chercher une ou des classes"""
	l = os.listdir(dirClasses)
	classes_found = ""
	allclasses = ""
	nb = 0
	for i, a in enumerate(l):
		# allclasses += a.split('.')[0].split('classe_')[1] + "\n"
		allclasses += a.split('.')[0] + "\n"
		if search_str.lower() in a.lower():
			classe =  a
			# classes_found +=  a.split('.')[0].split('classe_')[1] + "\n"
			classes_found +=  a.split('.')[0] + "\n"
			nb += 1
	if nb == 0:
		# si aucune classe trouvée, les afficher toutes
		mesg = "Aucune classe n'a été trouvée\n"
		mesg += "Liste des classes de l'académie\n\n"
		mesg += allclasses
		return mesg
	if nb == 1:
		# si une classe trouvée, afficher les stagaires la composant
		fic = dirClasses + "/" + classe
		f = open(fic, 'r')
		mesg = f.read()
		f.close()
		return mesg
	if nb > 1:
		# si plusieurs classes trouvées, afficher celles trouvées
		mesg = str(nb) + " classes trouvées\n"
		mesg += "Affinez votre recherche\n\n"
		mesg += classes_found
		return mesg


"""
def infos():
	os.system('clear')
	print("\n INFOS GENERALES\n")
	f = open('liste_stagiaires').readlines()
	print(" Nombre de stagiaires : {0}".format(len(f)))
	classes = os.listdir(dirClasses)
	print(" Nombre de classes : {0}".format(len(classes)))
	c = raw_input("\n Tapez sur une touche pour revenir au menu,\n ou 'c' pour afficher les noms des classes... ")
	if c == "c":
		os.system('clear')
		for a in classes:
			fclasse = open("./classes/" + a)
			print(fclasse.readlines()[1].split(": ")[1].rstrip())
		
		raw_input("\n Tapez sur une touche pour revenir au menu")
"""
"""
def maj_bd():
	os.system('clear')
	print("\n MISE A JOUR DE LA BASE DE DONNEES")
	print(" ---------------------------------\n")
	print(' La base de données est mise à jour 2 fois par jour, à 8H30 et 13H30.')
	print(' Il est cependant possible de forcer une mise à jour ponctuelle en cas de besoin.')
	print(" Celle-ci peut durer plusieurs minutes car il faut télécharger des pages Web sur Internet")
	c = raw_input("\n Voulez-vous mettre la base de donnée à jour (taper 'y' pour accepter) ? ")
	if c == "y":
		print(" Merci de patienter...\n")
		os.system(server)
		print("\n La mise à jour est terminée")
		raw_input("\n Tapez sur une touche pour revenir au menu... ")
"""

if __name__ == "__main__" :
	menu()
