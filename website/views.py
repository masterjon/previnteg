from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from website.models import example
def generic_view(request,template):
	return render(request,template)
def contact(request):
	return HttpResponse("Solicitud enviada. En breve nos pondremos en conatcto con usted.")
def exa(request):
	text=example.objects.all()
	return render(request,'text.html',{'text':text})
