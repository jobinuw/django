from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from rango.models import Artist

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context",
                    'varia': "aqui la variacion"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/socialprofile.html', context_dict)
	
def about(request):
    return render(request, 'rango/about.html') 
	 
# formato  return render_to_response('template.html', {'variable_name': value}) es un diccionario type
def artists(request):
    artista = Artist.objects.all();
    return render_to_response('rango/rangos.html', {'artists': artista})
	 
	 
#pk es for PrimaryKey
def artistdetails(request, id):
   artist = Artist.objects.get(pk=id);
   return render_to_response('rango/rangosdet.html', {'artist': artist})
#otra forma de mandar la view seria esta

#def artists(request):
    #artista = Artist.objects.all();
    #context_dict = {'artists': artista}
    #return render(request, 'rango/rangos.html', context_dict)

#def artistdetails(request, name):
    #output = '<html><body>' + name +'</body></html>'
    #return HttpResponse(output);	
