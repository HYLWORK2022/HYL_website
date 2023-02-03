from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello food!")
    return render(request, 'app1/index.html', {'place_nums': range(6)})