from django.contrib import admin
from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Med_Event',views.Med_Event,basename='Med_Event'),
router.register('Blood_Event',views.Blood_Event,basename='Blood_Event'),
router.register('Edu_Event',views.Edu_Event,basename='Edu_Event'),
router.register('CB_Event',views.CB_Event,basename='CB_Event'),
router.register('Animal_Event',views.Animal_Event,basename='Animal_Event'),
router.register('ForScribes_Event',views.ForScribes_Event,basename='ForScribes_Event'),
router.register('App_Event',views.App_Event,basename='App_Event'),
router.register('MedcampHis',views.MedcampHis,basename ='MedcampHis'),
router.register('BcampHis',views.BcampHis,basename ='BcampHis'),
router.register('EducampHis',views.EducampHis,basename ='EducampHis'),
router.register('CBEcampHis',views.CBEcampHis,basename ='CBEcampHis'),
router.register('AnmcampHis',views.AnmcampHis,basename ='AnmcampHis'),
router.register('SCcampHis',views.SCcampHis,basename ='SCcampHis'),
router.register('APcampHis',views.APcampHis,basename ='APcampHis'),

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
