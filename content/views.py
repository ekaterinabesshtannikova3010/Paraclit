from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'content/base.html')


def about(request):
    return render(request, 'content/about_us.html')


def star(request):
    return render(request, 'content/staroobrjadchestvo.html')


def potrebnic(request):
    return render(request, 'content/potrebnic.html')


def kultura(request):
    return render(request, 'content/kultura.html')


def avvacum(request):
    return render(request, 'content/avvacum.html')


def education(request):
    return render(request, 'content/education.html')


def corner(request):
    return render(request, 'content/corner.html')


def victory(request):
    return render(request, 'content/victory.html')


def Izbornik(request):
    return render(request, 'content/Izbornik.html')


def training(request):
    return render(request, 'content/training.html')


def holiday(request):
    return render(request, 'content/holiday.html')


def typology(request):
    return render(request, 'content/typology.html')


def revolution(request):
    return render(request, 'content/revolution.html')


def stiharnik(request):
    return render(request, 'content/stiharnik.html')


def engels(request):
    return render(request, 'content/engels.html')


def vnifantij(request):
    return render(request, 'content/vnifantij.html')


def pystozer(request):
    return render(request, 'content/pystozer.html')


def slatoust(request):
    return render(request, 'content/slatoust.html')


def bogoslov(request):
    return render(request, 'content/bogoslov.html'
                  )


def diary(request):
    return render(request, 'content/diary.html')


def reciter(request):
    return render(request, 'content/reciter.html')


def the_throne(request):
    return render(request, 'content/the_throne.html')


def image(request):
    return render(request, 'content/image.html')


def relocation(request):
    return render(request, 'content/relocation.html')


def distortions(request):
    return render(request, 'content/distortions.html')

def entrepreneurs(request):
    return render(request, 'content/entrepreneurs.html')
def inscription(request):
    return render(request, 'content/inscription.html')

def penetration(request):
    return render(request, 'content/penetration.html')

def variant(request):
    return render(request, 'content/variant.html')

def new_year(request):
    return render(request, 'content/new_year.html')

def star(request):
    return render(request, 'content/star.html')

def years_old(request):
    return render(request, 'content/years_old.html')
def map(request):
    return render(request, 'content/map.html')
