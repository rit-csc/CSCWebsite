from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

class EventSignin(forms.Form):
	dce = forms.CharField(max_length=10)
	
def eventSignin(request):
	if request.method == 'POST':
		form = EventSignin(request.POST):
		if form.is_valid():
			return HttpResponseRedirect('eventSigninLoop')
	else:
		form = EventSignin()
		
	return render(request, 'member/eventSignin.html', {
		'form': form,
	})
