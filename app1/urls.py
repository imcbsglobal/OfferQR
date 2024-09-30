 # Import the views from your app
from django.urls import path
from . import views
from .views import shop_admin_logout,delete_shop_admin


urlpatterns = [
    # Authentication
    path('', views.login_view, name='shop_admin_login'),
    path('index/', views.index, name='index'),
    path('logout/', views.shop_admin_logout, name='shop_admin_logout'),
    path('superuser_logout/', views.superuser_logout, name='superuser_logout'),

    # Shop Admin views
    path('shop_admin_dashboard/', views.shop_admin_dashboard, name='shop_admin_dashboard'),
    path('upload_image/', views.upload_image_view, name='upload_image'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('toggle_status/<int:profile_id>/', views.toggle_status, name='toggle_status'),

    # Superuser views
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('create_shop_admin/', views.create_shop_admin, name='create_shop_admin'),
    path('edit_shop_admin/<int:profile_id>/', views.edit_shop_admin, name='edit_shop_admin'),
    path('toggle_status/<int:profile_id>/', views.toggle_status, name='toggle_status'),
    path('delete_shop_admin/<int:profile_id>/', delete_shop_admin, name='delete_shop_admin'),
    path('logout/', shop_admin_logout, name='shop_admin_logout'),
    

    # Other views
    






    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),

    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),
    path('index/<str:uid>/', views.index_with_uid, name='index_with_uid'),

    path('download-qr-code/', views.download_qr_code, name='download_qr_code'),





   
]
