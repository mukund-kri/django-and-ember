from django.shortcuts import render_to_response

# Index view that will load all the html/js/css for the single page app
def index(request):    
    return render_to_response('simple/index.html')


