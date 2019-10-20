from django.urls import path
from .views import CheckoutView, \
    ItemDetailView, \
    HomeView, \
    add_to_card, \
    remove_from_card, \
    OrderSummaryView, \
    remove_single_item_from_card, \
    add_to_card_in_order, \
    PaymentView, \
    AddCouponView, \
    RequestRefundView

app_name = 'core'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout-page'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='products-page'),
    path('', HomeView.as_view(), name='home-page'),
    path('add-to-card/<slug>/', add_to_card, name='add-to-card'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('add-to-card-order/<slug>/', add_to_card_in_order, name='add-to-card-order'),
    path('remove_from_card/<slug>/', remove_from_card, name='remove-from-card'),
    path('remove_item_from_card/<slug>/', remove_single_item_from_card, name='remove-single-item-from-card'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')

]
