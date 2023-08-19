from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.main,name="main"),
    path("adminlog/",views.adminlog,name="adminlog"),
    path("adminlog/adminlogin/<int:id>",views.adminlogin,name="adminlogin"),
    path("adminlog/adminlogin/back/",views.adminback,name="adminback"),
    path("adminlog/adminlogin/take/<int:id>",views.take,name="take"),
    path("adminlog/adminlogin/action/<int:id>",views.action,name="action"),
    path("adminlog/adminlogin/nav/<int:id>",views.navigate,name="navigate"),
    path("index/",views.signin,name="signin"),
    path("index/login/",views.login,name="login"),
    path("index/login/create/",views.create,name="create"),
    path("index/login/create/create_new_ticket/",views.create_ticket,name="create_ticket"),
    path("index/login/create/cancel/",views.cancel,name="cancel"),
    path("index/login/back/",views.back,name="back"),
    path("index/signup/",views.signup,name="signup"),
    path("index/signup/createuser/",views.createuser,name="createuser"),
    path("index/signup/signin/",views.redict,name="redict"),
    

]