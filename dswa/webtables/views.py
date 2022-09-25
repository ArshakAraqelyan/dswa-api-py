from django.http import HttpResponse
from django.http import JsonResponse
import requests
import bs4
import json

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import WebTableSerializer

# #




class WebtableBeautifulSoup(APIView):
                def post(self, request):
                            data = (json.loads(request.body.decode("utf-8")))
                            url = data.get("url")
                            tag = data.get("tag")

                            page=requests.get(url)

                            soup= bs4.BeautifulSoup(page.text,'html.parser')

                            table=soup.find(tag)

                            headers=[ heading.text for heading in table.find_all('th')]

                            table_rows=[ row for row in table.find_all('tr')]

                            results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all("td")) }for row in table_rows]

                            return Response(results)


