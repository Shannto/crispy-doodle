from django.urls import path

from . import views

urlpatterns = [
    path("index/",views.index, name="index"),
    path("stockin/",views.stockIn, name="stock_In"),
    path("create/",views.createProduct, name="create_product"),
    path("history/",views.showHistory, name="show_history"),
    path("",views.stock, name="show_stock"),
    path("sales/",views.sales, name="create_sales"),
    path("products/",views.showProducts, name="show_products"),
    path("new/<str:pk>",views.newview, name="new_view"),


    #path("orderagain/",views.orderAgain, name="order_Again"),

]