from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet

# Creating views for detail and list view (Implementing CRUD) Create,read,updt,del
# Function Based
# def tweet_detail_view(request):
#     obj = Tweet.objects.get(id=1) #< this is for Query
#     print(obj)
#     context = {
#         'object': obj,
#     }
#     return render(request, "tweets/detail_view.html", {})
#
# def tweet_list_view(request):
#     qs = Tweet.objects.all() #< Query as well
#     print(qs)
#     context = {
#         'query': qs,
#     }
#     return render(request, "tweets/list_view.html", {})

# Class Based
class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"

    def get_object(self, queryset=Tweet.objects.all()):
        return Tweet.objects.get(id=1)
# ^ The block above is a class based view
# Update tweets in urls.py
# url patterns for Function based
# urlpatterns = [
#     path('', tweet_list_view, name='list_view'),
#     path('1/', tweet_detail_view, name='detail_view'),
# ]
# url patterns for Class based
#     path('', TweetListView.as_view(), name='list_view'),
#     path('1/', TweetDetailView.as_view(), name='detail_view'),
# update html file after switching to class based