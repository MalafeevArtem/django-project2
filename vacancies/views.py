import random

from django.db.models import Count

from django.shortcuts import render

from django.views import View

from vacancies.models import Company, Specialty, Vacancy


class MainView(View):
    def get(self, request):
        context = {
            'specialties': (Vacancy.objects.values('specialty__code', 'specialty__title', 'specialty__picture')
                            .annotate(count=Count('specialty__title'))
                            ),

            'companies': (Vacancy.objects.values('company__id', 'company__name', 'company__logo')
                          .annotate(count=Count('company__name'))
                          ),

            'random_specialties': random.sample(list(Specialty.objects.all()), 4)
        }

        return render(request, 'vacancies/index.html', context=context)


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/vacancies.html', context=context)


class SpecialtyView(View):
    def get(self, request, specialization):
        vacancies = Vacancy.objects.filter(specialty__code=specialization)

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/vacancies.html', context=context)


class CompanyView(View):
    def get(self, request, id):
        company = Company.objects.get(pk=id)
        company_name = company.name
        vacancies = Vacancy.objects.filter(company__name=company_name)

        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')

        context = {
            'company': company,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }

        return render(request, 'vacancies/company.html', context=context)


class VacancyView(View):
    def get(self, request, id):
        vacancy = Vacancy.objects.get(pk=id)

        vacancy.skills = vacancy.skills.split(', ')

        context = {
            'vacancy': vacancy,
        }

        return render(request, 'vacancies/vacancy.html', context=context)
