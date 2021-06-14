from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRestigerForm, Profile_pic_UpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView
from .models import Profile
from django.contrib.auth.models import User
from Reviews.models import Reviews

'''Register view'''
def RegisterView(request):
	# if request.user.is_authenticated:
	# 	return redirect('reviews')
	if request.method == 'POST':
		form = UserRestigerForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! your now able to login')
			return redirect('login')

	else:
		form = UserRestigerForm()
	return render(request,'users/register.html', {'form':form})

@login_required
def UpdateProfileView(request):
	if request.method == 'POST':
	    #populate form data
	    u_form = UserUpdateForm(request.POST, instance=request.user)
	    p_form = Profile_pic_UpdateForm(request.POST,request.FILES,instance=request.user.profile)
	    #validate form data
	    if u_form.is_valid() and p_form.is_valid():
	    	u_form.save()
	    	p_form.save()
	    	messages.success(request, f'Account successful updated!')
	    	return redirect('profile')
	else:
	    u_form = UserUpdateForm(instance=request.user)
	    p_form = Profile_pic_UpdateForm(instance=request.user.profile)


	context = {
		'u_form': u_form,
		'p_form': p_form,
		}

	return render(request,'users/profile.html', context)

'''User Account view'''
class UserAccountView(LoginRequiredMixin, ListView):
	model = Reviews
	template_name = 'users/account.html'
	context_object_name = 'reviews'
	paginate_by = 3

	# profile = Profile.objects.get(pk=pk)
	# user = profile.user

	# followers = profile.followers.all()
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Reviews.objects.filter(author=user).order_by('-date_posted')

'''Add followers view'''
class AddFollowersView(LoginRequiredMixin, View):
	def post(self, request, pk, *args, **kwargs):
		profile = Profile.object.get(pk=pk)
		profile.followers.add(request.user)

		return redirect('user-reviews',pk=profile.pk)


'''Add followers view'''
class RemoveFollowersView(LoginRequiredMixin, View):
	def post(self, request, pk, *args, **kwargs):
		profile = Profile.object.get(pk=pk)
		profile.followers.remove(request.user)

		return redirect('user-reviews',pk=profile.pk)
