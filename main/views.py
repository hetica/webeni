# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.encoding import smart_unicode
import sys, os, locale
from datetime import datetime, timedelta
from main.forms import StagiaireForms

# Create your views here.
def home(request):
	
	# CISCO
	
	# Ajouter au path
	_path = os.path.dirname(os.path.dirname(__file__)) + "/static/lib"
	sys.path.append(_path)

	import unicodedata
	import cisco_clt
	
	# définir le répertoire des fichiers
	ciscofic = "/var/local/pytacad"
	ciscoliststags = ciscofic + "/liste_stagiaires"
	ciscorepclasses = ciscofic + "/classes"
	
	# date de dernière modif du fichier "liste_stagiaires"
	locale.setlocale(locale.LC_ALL,"fr_FR.UTF-8")
	sm_fic = os.stat(ciscoliststags).st_mtime
	last_update = datetime.fromtimestamp(sm_fic).strftime('%A %d %B %Y à %Hh%m')
	# nombre de classes
	nb_classes = sum(1 for _ in os.listdir(ciscorepclasses))	
	# nombre de stagiaires
	nb_stags = sum(1 for _ in open(ciscoliststags))
	
	# La dernière mise à jour date t-elle de plus de plus de 24 heures ?
	one_days_ago = datetime.now() - timedelta(hours=1)
	filetime = datetime.fromtimestamp(os.path.getctime(ciscoliststags))
	to_old = one_days_ago > filetime

	# Formulaire de recherche de stagiaires
	if request.method == 'POST':
		form = StagiaireForms(request.POST)
		if form.is_valid():
			choisir = form.cleaned_data['choisir']
			chercher = form.cleaned_data['chercher']
			# mesg = type(choisir)
			
			if choisir == "1":
				# Si le choix est stagiaire
				search = cisco_clt.find_user(chercher)
				entete = str(search[0]) + " occurences trouvées"	
				if search[0] == 1:
					# Si un stagiaire trouvé, afficher ses caractéristiques
					mesg = cisco_clt.afficher_stags(search[1])
				if search[0] > 1:
					# Si plusieurs stagiaires sont trouvés, afficher leurs caractéristiques
					mesg = cisco_clt.afficher_stags(search[1])
					
			if choisir == "2":
				mesg = cisco_clt.find_classe(chercher)

			envoi = "stag_post"
	else:
		form = StagiaireForms()	
		
	return render(request, 'main/home.html', locals() )

	
def cisco(request):
	return render(request, 'main/cisco.html')

