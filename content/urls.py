from django.urls import path

from . import views
from .apps import ContentConfig

app_name = ContentConfig.name

urlpatterns = [
       path('', views.home, name='home'),
       path('about/', views.about, name='about'),
       path('star/', views.star, name='star'),
       path('potrebnic/', views.potrebnic, name='potrebnic'),
       path('kultura/', views.kultura, name='kultura'),
       path('avvacum/', views.avvacum, name='avvacum'),
       path('education/', views.education, name='education'),
       path('corner/', views.corner, name='corner'),
       path('victory/', views.victory, name='victory'),
       path('Izbornik/', views.Izbornik, name='Izbornik'),
       path('training/', views.training, name='training'),
       path('holiday/', views.holiday, name='holiday'),
       path('typology/', views.typology, name='typology'),
       path('revolution/', views.revolution, name='revolution'),
       path('stiharnik/', views.stiharnik, name='stiharnik'),
       path('engels/', views.engels, name='engels'),
       path('vnifantij/', views.vnifantij, name='vnifantij'),
       path('pystozer/', views.pystozer, name='pystozer'),
       path('slatoust/', views.slatoust, name='slatoust'),
       path('bogoslov/', views.bogoslov, name='bogoslov'),
       path('diary/', views.diary, name='diary'),
       path('reciter/', views.reciter, name='reciter'),
       path('the_throne/', views.the_throne, name='the_throne'),
       path('image/', views.image, name='image'),
       path('relocation/', views.relocation, name='relocation'),
       path('distortions/', views.distortions, name='distortions'),
       path('entrepreneurs/', views.entrepreneurs, name='entrepreneurs'),
       path('inscription/', views.inscription, name='inscription'),
       path('penetration/', views.penetration, name='penetration'),
       path('variant/', views.variant, name='variant'),
       path('new_year/', views.new_year, name='new_year'),
       path('star/', views.star, name='star'),
       path('years_old/', views.years_old, name='years_old'),
       path('map/', views.map, name='map'),

       ]