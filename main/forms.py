# -*- coding: utf-8 -*-

from django import forms

class StagiaireForms(forms.Form):
	_choix = ( (1, 'Stagiaire'), (2, 'Classe'),)
	choisir = forms.ChoiceField(choices =_choix, widget = forms.RadioSelect, required = True, initial = '1', label = '')
	chercher = forms.CharField(max_length=100, required=False, label = '')

	def __init__(self, *args, **kwargs):
		super(StagiaireForms, self).__init__(*args, **kwargs)
		self.fields['chercher'].widget.attrs.update({'autofocus': 'autofocus', 'placeholder': 'Nom, prénom ou classe'})
