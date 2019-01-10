from django.contrib import admin
from django.urls import (
    path, 
    include
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # "127.0.0.1:8000" 으로 요청이 들어오면(path의 url이 ''이기 때문에) blog/urls.py에 정의된 경로를 읽습니다.
    path('', include('blog.urls')),
]
