from django.shortcuts import render

from .forms import VisitForm
from .models import Visit

def get_all_visits(request):
    visits = Visit.objects.all()

    return render(
        request,
        template_name= 'vizite.html',
        context={'visits': visits},
    )

def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            visit = Visit(
                visitor=form.cleaned_data['visitor'],
                email=form.cleaned_data['email'],
            )

            visit.save()

            context = {
                'visit': visit,
            }

            return render(
                request,
                template_name='visit.html',
                context=context,
            )

    return render(
        request,
        template_name='visit_form.html',
        context={'form': form}
    )
