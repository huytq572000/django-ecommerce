from django.urls import path

from . import views
app_name = 'store'
urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('productdetail/<slug:slug>/',views.productdetail,name="productdetail"),
    path('listcategory/<slug:category_slug>/',views.category_list,name="category_list"),
	path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),
]