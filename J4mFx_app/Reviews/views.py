from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Reviews
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def ReviewsView(request):
	context = {

	       'reviews': Reviews.objects.all()
	}

	return render(request, 'reviews.html',context)

'''Reviews view'''
class ReviewListView(LoginRequiredMixin, ListView):
	model = Reviews
	template_name = 'reviews.html'
	context_object_name = 'reviews'
	ordering = ['-date_posted']
	paginate_by = 3

'''User Reviews view'''
class UserReviewListView(LoginRequiredMixin, ListView):
	model = Reviews
	template_name = 'user_reviews.html'
	context_object_name = 'reviews'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Reviews.objects.filter(author=user).order_by('-date_posted')


''' single Review view'''
class ReviewDetailView(LoginRequiredMixin, DetailView):
	model = Reviews
	template_name = 'review_details.html'


'''create Review view'''
class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Reviews
	fields = ['title', 'content', 'image']
	template_name = 'review_form.html'

	'''obtain user'''
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


'''Update Review view'''
class ReviewUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Reviews
	fields = ['title', 'content', 'image']
	template_name = 'review_form.html'

	'''obtain user'''
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	'''ensure user who update the review is author of review'''
	def test_func(self):
	    review = self.get_object()
	    if self.request.user == review.author:
	        return True
	    return False   	
	
'''Delete Review view'''
class ReviewDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Reviews
	template_name = 'reviews_confirm_delete.html'
	success_url = '/Reviews/'
	
	'''ensure user who delete the review is author of review'''
	def test_func(self):
	    review = self.get_object()
	    if self.request.user == review.author:
	        return True
	    return False  

'''add followers view'''
# class AddFollowerView(LoginRequiredMixin, View):
# 	def post(self, request, pk, *args, **kwargs):
# 		profile = Profile.objects.get(pk=pk)
# 		profile.followers.add(request.user)

# 	def get(self, request, pk, *args, **kwargs):
# 		if request.method == "GET":
# 			profile = Profile.objects.get(pk=pk)
# 			user = Profile.user
# 			followers = profile.followers.all()
# 			if len(followers) == 0:
# 				is_following = False
# 				for follower in followers:
# 					if follower == request.user:
# 						is_following = True
# 						break
# 					else:
# 					    is_following = False	

# 				total_followers = len(followers)
# 		return {'user':user, 'total_followers':total_followers, 'is_following':is_following}

# 	context = {
# 		'user': user,
# 		'u_form': u_form,
# 		'p_form': p_form,
# 		'total_followers': total_followers,
# 		'is_following': is_following
# 	}	
# 	return redirect('profile', pk=profile.pk)



# '''Remove followers view'''
# class RemoveFollowerView(LoginRequiredMixin, View):
# 	def post(self, request, pk, *args, **kwargs):
# 		profile = Profile.objects.get(pk=pk)
# 		profile.followers.remove(request.user)
# 		return redirect('profile', pk=profile.pk)

