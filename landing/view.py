from django.views.generic import FormView
from django.http import JsonResponse
from .forms import ContactForm


class ContactFormView(FormView):
    template_name = 'landing/index.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        data = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message']
        }


        ip = self.request.META.get('HTTP_X_FORWARDED_FOR', self.request.META.get('REMOTE_ADDR')).split(',')[0]


        user_agent = self.request.META.get('HTTP_USER_AGENT')

        # Объединяем все данные
        response_data = {
            **data,
            'ip_address': ip,
            'user_agent': user_agent
        }
        # Возвращаем ответ в формате JSON
        return JsonResponse(response_data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context