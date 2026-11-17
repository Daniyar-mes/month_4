from django.urls import path
from abiturients.views import (
    CreateAbitView,
    UpdateAbitView,
    DeleteView,
    AbitListView
)

urlpatterns = [
    path('create_abit/', CreateAbitView.as_view(), name='add_abit'),
    path('abit_list/', AbitListView.as_view(), name='abit_list'),
    path('abit_list/<int:id>/edit/', UpdateAbitView.as_view(), name='update_abit'),
    path('abit_list/<int:id>/drop/', DeleteView.as_view(), name='drop_abit'),
]