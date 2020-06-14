from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from django.views import View


def custom_handler404(request, exception):

    return HttpResponseNotFound('<h1>Wrong destination!</h1> \
    <h2>Check your route, please<h/2>')


def custom_handler500(request):

    return HttpResponseServerError()


def MainView(request):

    return render(request, 'index.html')


class DepartureView(View):

    def get(self, request, departure):

        return render(request, 'departure.html')


class TourView(View):

    def get(self, request, id):

        return render(request, 'tour.html')
