from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from testapp.models import Book
from testapp.serializers import BooksSerializer


def index(request: HttpRequest) -> HttpResponse:
    turn_on_block = settings.MAINTENANCE_MODE

    return render(request, 'main/index.html', {
        "turn_on_block": turn_on_block,
    })


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
