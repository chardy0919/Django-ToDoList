# from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth import authenticate
# from .models import Person
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_201_CREATED,
#     HTTP_404_NOT_FOUND,
#     HTTP_204_NO_CONTENT,
# )
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

# #
# class Sign_up(APIView):
#     def post(self, request):
#         request.data["username"] = request.data["email"]
#         person = Person.objects.create_user(**request.data)
#         token = Token.objects.create(user=person)
#         return Response(
#             {"person": person.email, "token": token.key}, status=HTTP_201_CREATED
#         )

# class Log_in(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         person = authenticate(username=email, password=password)
#         if person:
#             token, created = Token.objects.get_or_create(user=person)
#             return Response({"token": token.key, "person": person.email})
#         else:
#             return Response("No person matching credentials", status=HTTP_404_NOT_FOUND)
        
# class Info(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"email": request.user.email})
    
# class Log_out(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
    
# # class Master_Sign_Up(APIView):

# #         def post(self, request):
# #             master_person = Person.objects.create_user(**request.data)
# #             master_person.is_staff = True
# #             master_person.is_superuser = True
# #             master_person.save()
# #             token = Token.objects.create(user=master_person)
# #             return Response(
# #                 {"master_person": master_person.email, "token": token.key}, status=HTTP_201_CREATED
# #             )