import csv
from datetime import datetime

from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import Deal, Customer
from api.serializers import DealSerializer


class DealViewSet(GenericViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    @action(detail=False, methods=['post'])
    def set_deals_from_csv(self, request):
        try:
            a = request.FILES.get('deals').read()
            b = a.decode('utf-8').split('\r\n')
            reader = csv.reader(b)
            for row in reader:
                if not row or row == ['customer', 'item', 'total', 'quantity', 'date']:
                    continue
                customer = Customer.objects.get_or_create(username=row[0])[0]
                Deal.objects.create(customer=customer, item=row[1], total=row[2], quantity=row[3],
                                    date=make_aware(datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')))
        except (IndexError, ValueError):
            raise ParseError('Отправленный файл невалиден')
        return Response(status=status.HTTP_200_OK)


