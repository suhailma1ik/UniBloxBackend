from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.decorators import api_view
import uuid

listOfCoupons = []
listOfusedCoupons = []
totalNumberOfItemsSold=0
totalAmount=0
totalDiscount=0

@api_view(['GET'])
def discounts(request, ordernumber):
    if(ordernumber%3==0):
        id=str(uuid.uuid4())
        listOfCoupons.append(id)
        # print(listOfCoupons)
        return Response({
            'code': id
        })
    else:
        return Response({
            'code': 'No code'
        })

@api_view(['POST'])
def applyDiscount(request):
    global totalNumberOfItemsSold
    global totalAmount
    global totalDiscount
    # print(listOfCoupons,request.data['coupon'])
    if(request.data['coupon'] in listOfCoupons):
        totalNumberOfItemsSold+=request.data['numberOfItems']
        totalAmount+=request.data['amount']
        discount=request.data['amount']/10
        totalDiscount+=discount
        listOfusedCoupons.append(request.data['coupon'])
        listOfCoupons.remove(request.data['coupon'])
        return Response({
            'status': 'Coupon applied',
            'discount': discount
        })
    else:
        return Response({
            'status': 'Invalid coupon'
        })