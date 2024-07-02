from django.urls import path
from .views import MenuCategoryView, MenuProductView, MenuOrderView, menu_order, update_order, delete_order
urlpatterns = [
    path('menu_category/', MenuCategoryView.as_view(), name='menu_category'),
    path('menu_product/<int:pk>/', MenuProductView.as_view(), name='menu_product'),
    path('menu_order_list/', MenuOrderView.as_view(), name='menu_order'),
    path('update_order/<int:pk>/', update_order, name='menu_order_update'),
    path('menu_order/<int:pk>/', menu_order, name='menu_order'),
    path('update_order/<int:pk>/', update_order, name='menu_order_update'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),
]