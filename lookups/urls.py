from django.urls import path,include
from . import views

urlpatterns=[
    path('firstcategorycreate/',views.FirstCategoryAPIView.as_view(), name='first-category-create'),
    path('firstcategorylist/',views.FirstCategoryList.as_view(), name='firstcategory-list'),
    path('secondcategorycreate/',views.SecondCategoryAPIView.as_view(), name='second-category-create'),
    path('secondcategorylist/',views.SecondCategoryList.as_view()),
    path('secondcategoryupload/<int:firstcategoryid>',views.FileUploadView.as_view(), name='second-category-upload'),
    path('thirdcategorycreate/',views.ThirdCategoryAPIView.as_view(), name='third-category-create'),
    path('thirdcategorylist/',views.ThirdCategoryList.as_view()),
    #path('<int:id>',views.IncidentRetrieveUpdateDestroy.as_view(), name='update-delete-incident')
]