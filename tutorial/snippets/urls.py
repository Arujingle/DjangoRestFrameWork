from snippets.views import SnippetViewSet, UserViewSet
from rest_framework import renderers
from snippets import views
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.schemas import get_schema_view


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    url('', include(router.urls)),
    url('schema/', schema_view),
]


