from django.urls import path

from vacancies.views import CompanyView, MainView, SpecialtyView, VacanciesView, VacancyView


urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:specialization>/', SpecialtyView.as_view()),  # fff
    path('companies/<int:id>/', CompanyView.as_view()),
    path('vacancies/<int:id>/', VacancyView.as_view()),
]
