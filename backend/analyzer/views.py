from rest_framework import viewsets, status
import yfinance as yf
import pandas as pd
import json
from rest_framework.response import Response

from .serializers import StockHistorySerializer
# Create your views here.


class DataAnalyzer(viewsets.ViewSet):
    """
    Viewsets for listing or retrieving stock data.
    """
    lookup_field = "symbol"

    def list(self, request):
        pass

    def retrieve(self, request, symbol=None):
        bond_data = yf.Ticker(symbol).history()
        bond_data.reset_index(inplace=True)
        serializer = StockHistorySerializer(
            bond_data.to_dict(orient='records'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
