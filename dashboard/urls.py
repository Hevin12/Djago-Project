
from django.conf.urls import url
from django.urls import path

from dashboard import views as FT_view

urlpatterns = [
url(r"login_success/$", FT_view.login_success, name="login_success"),
path(
        "dashboard/",
        FT_view.dashboard_home.as_view(),
        name="home_page",
    )
]