import random

from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

from .forms import VisitForm
from .models import Visit

from .forms import NewPostForm

def show_hello(request):
    return HttpResponse('Hello!')


def show_html(request):

    context = {
        'something': 'THIS IS CONTEXT'
    }

    return render(
        request,
        template_name='show_html.html',
        context=context
    )


def show_datetime(request):

    current_datetime = datetime.now()

    context = {
        'datetime': current_datetime,
    }

    return render(
        request,
        template_name='show_datetime.html',
        context=context,
    )


def show_name(request):

    if request.method == 'POST':

        context = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name']
        }

        return render(
            request,
            template_name='show_name.html',
            context=context,
        )

    return render(
        request,
        template_name='show_name_form.html',
    )


def add_post(request):

    # ja ir POST, formā ieliek datus, ja nav POST
    # neliek neko
    form = NewPostForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            context = {
                'title': form.cleaned_data['title'],
                'content': form.cleaned_data['content'],
                'created_at': datetime.now(),
            }

            return render(
                request,
                template_name='show_post.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='create_post.html',
        context=context,
    )


def motivate(request):

    motivations = [
        '1',
        '2',
        '3',
        '4',
        '5',
    ]

    motivation = random.choice(motivations)

    return HttpResponse(motivation)


def university(request):

    if request.method == 'POST':

        name = request.POST['name']

        maths = int(request.POST['maths'])
        latvian = int(request.POST['latvian'])
        foreign = int(request.POST['foreign'])

        if maths > 40 and latvian > 40 and foreign > 40:
            result = 'can not'

        else:
            result = 'can'

        return HttpResponse(f'{name} {result} apply yo university')

    return render(
        request,
        template_name='university_form.html',
    )


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = Visit(
                visitor=form.cleaned_data['visitor'],
                reason=form.cleaned_data['reason'],
                date_time=form.cleaned_data['date_time'],
            )

            return render(
                request,
                template_name='visit.html',
                context={'visit': visit},
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )
