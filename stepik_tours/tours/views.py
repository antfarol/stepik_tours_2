import random

from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from stepik_tours.data import title, subtitle, description, departures, tours

for key, value in tours.items():
    value['ID'] = key


def custom_handler404(request, exception):

    return HttpResponseNotFound('<h1>Wrong destination!</h1> \
    <h2>Check your route, please<h/2>')


def custom_handler500(request):

    return HttpResponseServerError()


class MainView(View):

    def get(self, request):

        context = {
            'tours': random.sample(list(tours.values()), 6),
            'departures': departures,
            'title': title,
            'subtitle': subtitle,
            'description': description
        }

        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):

        tours_list = list(tours.values())
        tours_list = list(filter(lambda tours_list:
                                 tours_list['departure'] == departure,
                                 tours_list))

        context = {
            'dep': departure,
            'dep_ru': departures[departure].split(' ')[1],
            'tours': tours_list,
            'tours_count': len(tours_list),
            'min_price': min(tours_list, key=lambda x: x['price'])['price'],
            'max_price': max(tours_list, key=lambda x: x['price'])['price'],
            'min_nights': min(tours_list, key=lambda x: x['nights'])['nights'],
            'max_nights': max(tours_list, key=lambda x: x['nights'])['nights'],
            'departures': departures,
            'title': title,
            'subtitle': subtitle,
            'description': description
        }

        return render(request, 'departure.html', context=context)


class TourView(View):

    def get(self, request, id):

        tours_list = list(tours.values())
        tour = list(filter(lambda tours_list: tours_list['ID'] == id,
                           tours_list))[0]

        context = {
            'dep_ru': departures[tour['departure']].split(' ')[1],
            'tour': tour,
            'stars': '★'*int(tour['stars']),
            'departures': departures,
            'title': title,
            'subtitle': subtitle,
            'description': description
        }

        return render(request, 'tour.html', context=context)
