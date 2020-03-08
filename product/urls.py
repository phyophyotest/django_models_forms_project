from django.urls import path
from product import views as pro_view
urlpatterns=[
    path('',pro_view.home,name="pro-home"),
    path('pro/create',pro_view.create,name="pro-create"),
    path('pro/edit/<int:id>',pro_view.edit,name="pro-edit"),
    path('pro/delete/<int:id>',pro_view.delete,name="pro-delete")
]