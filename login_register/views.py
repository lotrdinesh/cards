from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

@login_required() # only logged in users should access this
def edit_user(request, pk):

    user = User.objects.get(pk=pk)
 

    user_form = UserForm(instance=user)
 

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('bio', 'phone', 'city', 'country'))
    formset = ProfileInlineFormset(instance=user)
 
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, instance=user)
            formset = ProfileInlineFormset(request.POST, instance=user)
 
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, instance=created_user)
 
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')
 
        return render(request, "login_register/account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
	    "formset" : formset,
	    })
    else:
	raise PermissionDenied
