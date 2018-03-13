from django.shortcuts import redirect, HttpResponseRedirect, render_to_response
from django.core.urlresolvers import reverse
from .models import Services, Vacancies, Contacts, Countries, Companies, Specializations
from django_filters.views import FilterView
from django_filters import FilterSet, ModelChoiceFilter
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import MessageForm
from django.http import JsonResponse


class VacanciesFilter(FilterSet):
    country = ModelChoiceFilter(queryset=Countries.objects.all(), empty_label='All countries')
    company = ModelChoiceFilter(queryset=Companies.objects.all(), empty_label='All companies')
    specialization = ModelChoiceFilter(queryset=Specializations.objects.all(), empty_label='All specializations')

    class Meta:
        model = Vacancies
        fields = ('country', 'company', 'specialization')


class HomeListView(FilterView):
    template_name = 'index.html'
    filterset_class = VacanciesFilter

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['contacts'] = Contacts.objects.all()
        context['form'] = MessageForm
        return context


class MessageCreateView(CreateView):
    form_class = MessageForm

    def form_valid(self, form):
        response_data = {}
        self.obj = form.save(commit=False)
        self.obj.save()
        response_data['success'] = 'Your e-mail was successfully submitted!'
        return JsonResponse(response_data)









