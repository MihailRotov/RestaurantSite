from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
from django.template.loader import get_template


def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')


def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['subject'],
                         form.cleaned_data['message'])
            context = {'success': 1}

    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'home/contacts.html',
        context=context)


def send_message(name, email, subject, message):
    text = get_template('home/message.html')
    html = get_template('home/message.html')
    context = {'name': name, 'email': email, 'subject': subject, 'message': message}
    data = 'Повідомлення!'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(data, text_content, from_email, ['manager@mail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()