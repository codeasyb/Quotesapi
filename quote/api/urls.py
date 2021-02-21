from django.urls import path
from quote.api.views import QuoteListCreateAPIVew, QuoteDetailAPIView

urlpatterns = [
    path("quotes/", QuoteListCreateAPIVew.as_view(), name="quote-list"),
    path("quotes/<int:pk>", QuoteDetailAPIView.as_view(), name="quote-detail")
]
