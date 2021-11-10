from django.shortcuts import render

from .forms import VisitForm


def add_visit(request):

    form = VisitForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            context = {
                'visitor': form.cleaned_data['visitor'],
                'reason': form.cleaned_data['reason'],
                'date_time': form.cleaned_data['date_time'],
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
