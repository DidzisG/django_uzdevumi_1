from django.shortcuts import render

from .forms import VisitForm
from .models import Visit

def get_all_users(request):
    visits = Visit.objects.all()

    return render(
        request,
        template_name= 'user_list.html',
        context={'visits': visits},
    )

def add_user(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = Visit(
                user=form.cleaned_data['user'],
                email=form.cleaned_data['email'],
            )

            visit.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='user.html',
                context=context,
            )

    return render(
        request,
        template_name='form.html',
        context={'form': form}
    )
