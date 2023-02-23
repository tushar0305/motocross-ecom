from store.models import Company, Bikes


def all_companies(request):
    return {
        'company': Company.objects.all()
    }


def all_bikes(request):
    return {
        'bikes': Bikes.objects.all()
    }