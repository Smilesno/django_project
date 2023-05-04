import random

from django.shortcuts import render
from rest_framework.views import APIView
from random import randint
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework import status
import logging


# Create your views here.

logger = logging.getLogger("django")

# 发送短信验证码
class SMSCodeView(APIView):

    def get(self, request, mobile):
        # 1. 判断60s内是否发送短信
        redis_conn = get_redis_connection('verify_codes')
        is_push = redis_conn.get(f'send_{str(mobile)}')
        if is_push:
            return Response({'message': '频繁发送短信'}, status=status.HTTP_400_BAD_REQUEST)
        sms_code = randint(100000, 999999)
        logger.info(f"验证码: {str(sms_code)}")


        redis_conn.setex(f'sms_{str(mobile)}', 300, sms_code)
        # 发送短信

        redis_conn.setex(f'send_{str(mobile)}', 60, 1)

        return Response({'message': 'ok'})

