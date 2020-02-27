from django.conf.urls import url
from home import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('<str:user_id>', views.detail, name='detail'),

]