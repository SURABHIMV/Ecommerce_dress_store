from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage_shopkeeper,name='login'),
    path('add_page/', views.add_data_page,name='add_page'),
    path('home/', views.new,name='home'),
    path('signin_user/', views.signupPage_user,name='signin_user'),
    path('login_user/', views.loginPage_user,name='login_user'),
    path('add_page1/', views.add_page1,name='add_page1'),
    path('add_page2/', views.add_page2,name='add_page2'),
    path('add_page3/', views.add_page3,name='add_page3'),
    path('add_page4/', views.add_page4,name='add_page4'),
    path('order/', views.orders,name='order'),
    path('cart/', views.view_cart, name='view_cart'),
    path('logout/',views.logoutuser,name='logout'),
    path('view_wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/<int:product_id>/', views.add_wishlist, name='add_wishlist'),
    path('payment/', views.payment, name='view_payment'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart')
    #path('demo_base/', views.base_page, name='demo_base')
]

# to view the image in web
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)