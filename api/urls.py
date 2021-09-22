
from django.urls import path
from api import views
urlpatterns = [
   
    path('get_videos',views.get_videos,name='get'),
    path('get_video/<int:id>',views.get_video,name='get_video'),
    path('set_videos',views.fileUpload.as_view(),name='uploads'),
    path('del_video/<int:id>',views.remove_videos,name='del_video'),
    path('get_file/<int:vid>',views.get_file,name='get_file'),
    path('get_json/<int:id>',views.get_json,name='get_json')
]