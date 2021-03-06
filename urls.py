"""timeoftone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#Research into the growing demand for guitar pedals


from django.urls import path
from . import views
from .views import DateHistoryListView

urlpatterns = [
    path('', views.index, name='index'),
    path('date_history', DateHistoryListView.as_view()),
    path('line_graph/', views.line_graph, name='line_graph'),
]
