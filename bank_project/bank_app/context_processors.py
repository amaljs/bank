from .models import  Branches

def menu_links(request):
    links=Branches.objects.all()
    return dict(links=links)