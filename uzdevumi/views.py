from django.shortcuts import render

from .forms import UserForm
from .models import User

def get_user(request, user_id):

    user = User.objects.get(id=user_id)

    context = {
        'user': user,

    }

    return render(
        request,
        template_name='user.html',
        context=context,

    )

def get_all_users(request):
    users = User.objects.all()

    return render(
        request,
        template_name= 'user_list.html',
        context={'users': users},
    )

def add_user(request):

    form = UserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = User(
                user=form.cleaned_data['user'],
                email=form.cleaned_data['email'],
            )

            user.save()

            context = {
                'user': user,
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
