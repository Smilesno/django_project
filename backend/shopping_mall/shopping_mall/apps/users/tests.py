from django.test import TestCase

# Create your tests here.

import base64

input_str = "123465"
print(base64.b64encode(input_str.encode('utf-8')))
print(base64.b64decode('MTIzNDY1').decode('utf-8'))