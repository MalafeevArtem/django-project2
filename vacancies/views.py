from django.views import View

from django.http import HttpResponse


class MainView(View):
    def get(self, request):
        return HttpResponse('Здесь будет поиск и вакансии по рубрикам (Главная страница)')


class VacanciesView(View):
    def get(self, request):
        return HttpResponse('Здесь будет список вакансий')


class SpecialtyView(View):
    def get(self, request, specialization):
        return HttpResponse('Здесь будет список вакансий по специальности')


class CompanyView(View):
    def get(self, request, id):
        return HttpResponse('Здесь будет карточка компании')


class VacancyView(View):
    def get(self, request, id):
        return HttpResponse('Здесь будет выведена конкретная вакансия')
