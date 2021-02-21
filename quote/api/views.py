from rest_framework import generics
# from rest_framework.response import response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.permissions import IsAdminUserOrReadOnly
from quote.api.pagination import SmallSetPagination

# Concreate View Classes
# ENDPOINTS 
class QuoteListCreateAPIVew(generics.ListCreateAPIView):
    
    queryset = Quote.objects.all().order_by('id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]