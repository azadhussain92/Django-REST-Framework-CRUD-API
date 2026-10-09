from django.urls import path
from Statusapp import views

urlpatterns = [
    # path('',views.MyClass.as_view()),
    # path('',views.AllStatusList.as_view()),
    # path('<int:pk>',views.GetOneStatus.as_view()),
    # path('create/',views.CreateStatus.as_view()),
    # path('update/<int:pk>',views.UpdateStatus.as_view()),
    # path('delate/<int:pk>',views.DelateStatus.as_view()),
    path('',views.AllStatusAddViews.as_view()),
    path('<int:pk>',views.StatusRetriveUpdateDeleteView.as_view()),
]
