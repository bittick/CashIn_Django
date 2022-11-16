import json
from datetime import datetime
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dispatcher, Courier, Operator


@api_view(['GET'])
def get_user_data(request, tg_id):
    if Dispatcher.objects.filter(tg_id=tg_id).exists():
        data = model_to_dict(Dispatcher.objects.get(tg_id=tg_id))
        data['type'] = 'dispatcher'
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )
    elif Courier.objects.filter(tg_id=tg_id).exists():
        data = model_to_dict(Courier.objects.get(tg_id=tg_id))
        data['type'] = 'courier'
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def accept_courier_cash_in(request):
    data = json.loads(request.body.decode("utf-8"))
    cur_courier = data.get('tg_id', None)
    cur_operator = data.get('operator_id', None)
    if cur_courier and cur_operator:
        cour = Courier.objects.get(tg_id=cur_courier)
        operator = Operator.objects.get(id=cur_operator)
        operator.account_balance = operator.account_balance + data['amount']
        cour.account_balance = cour.account_balance - data['amount']
        cour.logs += f'[{datetime.now()}] Кэшин. Cумма: {data["amount"]}. Оператор: {operator}\n'
        operator.logs += f'[{datetime.now()}] Кэшин. Cумма: {data["amount"]}. Курьер: {cour}\n'
        operator.save()
        cour.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def accept_courier_cash_out(request):
    data = json.loads(request.body.decode("utf-8"))
    user = data.get('tg_id', None)
    if user:
        cour = Courier.objects.get(tg_id=user)
        cour.account_balance = cour.account_balance + data['amount']
        cour.logs += f'[{datetime.now()}] Забор средств с Garantex. Cумма: {data["amount"]}\n'
        cour.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_operators(request):
    data = Operator.objects.all()
    return Response(
        data=[model_to_dict(i) for i in data],
        status=status.HTTP_200_OK,
    )


@api_view(['GET'])
def get_one_operator(req, operator_id):
    if Operator.objects.filter(id=operator_id).exists():
        return Response(
            data=model_to_dict(
                Operator.objects.get(id=operator_id)
            ),
            status=status.HTTP_200_OK
        )
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_couriers(request):
    couriers = Courier.objects.all()
    return Response(
        data=[model_to_dict(i) for i in couriers],
        status=status.HTTP_200_OK,
    )


@api_view(['GET'])
def get_all_dispatchers(request):
    couriers = Dispatcher.objects.all()
    return Response(
        data=[model_to_dict(i) for i in couriers],
        status=status.HTTP_200_OK,
    )
