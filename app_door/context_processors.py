from .models import Detail

def property_count(request):
    property_count = 0
    if request.user.is_authenticated:
        property_count = Detail.objects.filter(Ownername=request.user.username).count()
    return {'property_count': property_count}