from rest_framework import serializers


class StockHistorySerializer(serializers.Serializer):
    Date = serializers.DateTimeField()
    Open = serializers.DecimalField(max_digits=7, decimal_places=2)
    High = serializers.DecimalField(max_digits=7, decimal_places=2)
    Low = serializers.DecimalField(max_digits=7, decimal_places=2)
    Close = serializers.DecimalField(max_digits=7, decimal_places=2)
    Volume = serializers.IntegerField()
    Dividends = serializers.FloatField()
    Stock_Splits = serializers.FloatField(source='Stock Splits')
