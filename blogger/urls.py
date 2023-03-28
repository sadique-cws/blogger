
from django.contrib import admin
from django.urls import path
from cms.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("/filter/<int:cat_id>/",filter,name="filter"),
    path("search/",search,name="search"),
    path("insertPost/",insertPost,name="insertPost"),
    path("insertCategory/",insertCategory,name="insertCategory"),
    path("viewPost/<int:id>/",viewPost,name="viewPost"),
    path("DeletePost/<int:id>/",deletePost,name="DeletePost"),
    path("accounts/login/",signin,name="signin"),
    path("accounts/register/",register,name="signup"),
    path("accounts/logout/",signout,name="signout"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
