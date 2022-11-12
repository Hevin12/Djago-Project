from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.models import DailyNav

class dashboard_home(LoginRequiredMixin, ListView):
    """ 
        Summary line. 
        This class shows table of daily nav summary 

    """ 
    model = DailyNav
    template_name = 'public/record.html'  
    



def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    id = request.user.id
    print('id',id)
    print(request.user.username)
    return redirect("home_page")