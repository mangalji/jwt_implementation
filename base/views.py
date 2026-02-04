from django.shortcuts import render, redirect
from django.http import JsonResponse

# def endpoints(request):
#     data = ['/adovacates','advocates/:username']
#     return JsonResponse(data,safe=False)

# def advocate_list(request):
#     data = ["raj","yuvraj","aman"]
#     return JsonResponse(data,safe=False)

# def advocate_details(request, username):
#     data = username
#     return JsonResponse(data,safe=False)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Advocate
from .serializers import AdvocateSerializer
from django.db.models import Q
from rest_framework.views import APIView


@api_view(['GET'])
def endpoints(request):
    data = ['/advocates',"advocates/username","/companies",'companies/name']
    return Response(data)


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def advocates_list(request):

#     if request.method == 'GET':

#         query = request.GET.get("query")
#         # print(query)

#         if query == None:
#             query = ''

#         # advocates = Advocate.objects.all()
#         # advocates = Advocate.objects.filter(username__icontains=query)
#         advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
#         serializer = AdvocateSerializer(advocates,many=True)
#         # data = ["raj","yuvraj","aman"]
#         # return Response(advocates)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         print(request.data)
#         # return Response('done')
#         advocate = Advocate.objects.create(
#             username = request.data['username'],
#             bio = request.data['bio']
#         )
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)

# above code is function based views 
# now we write it in class based manner

class AdvocateList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        query = request.GET.get("query")
        # print(query)
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates,many=True)
        
        return Response(serializer.data)

    def post(self,request):

        print(request.data)
        advocate = Advocate.objects.create(
            username = request.data.get('username'),
            bio = request.data.get('bio')
        )
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
        


# @api_view(['POST'])
# def add_advocate(request):
#     advocates = Advocate.objects.create(username=request.data['username'])

#     return Response('added')


# @api_view(['GET','PUT','DELETE'])
# def advocates_details(request, username):
#     advocate = Advocate.objects.get(username=username)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         advocate.save()
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':

#         advocate.delete()
#         return Response('successfully deleted')
#         # return redirect('/advocates')

# above code are the function based views
# now we create a class based views


class AdvocateDetail(APIView):
    
    def get_object(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist():
            return JsonResponse("Advocate doesn't exists.")

    def get(self,request,username):
        
        # advocate = Advocate.objects.get(username=username)
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    
    def put(self,request,username):

        # advocate = Advocate.objects.get(username=username)
        advocate = self.get_object(username)
        # advocate.username = request.data['username']
        # advocate.bio = request.data['bio']

        # advocate.save()
        serializer = AdvocateSerializer(advocate,data=request.data,partial=True,many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    def delete(self,request,username):

        advocate = Advocate.objects.get(username=username)
        advocate.delete()

        return Response('successfully deleted')
    
from .models import Company
from .serializers import CompanySerializer


# ---------------------------------------------------------------------------------------
# views for companies model
# ---------------------------------------------------------------------------------------


@api_view(['GET','POST'])
def company_list(request):

    if request.method == 'GET':
        # query = request.GET.get('query')
        # print(query)
        # if query == None:
        #     query = ''
        company = Company.objects.all()
        # company = Company.objects.filter(Q(name__icontains='query') | Q(bio__icontains='query'))
        serializer = CompanySerializer(company,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        
        company = Company.objects.create(
            name = request.data.get('name'),
            bio = request.data.get('bio')
        )
        serializer = CompanySerializer(company,many=False)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def company_detail(request,pk):
    company = Company.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CompanySerializer(company,many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        
        # company.name = request.data.get('name')
        # company.bio = request.data.get('bio')
        # company.save()
        serializer = CompanySerializer(company,data=request.data,many=False,partial=True)
        return Response(serializer.data)
    
    if request.method == 'DELETE':
        company.delete()
        return Response("company detail deleted successfully.")