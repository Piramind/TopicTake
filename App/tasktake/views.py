from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthentificationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


class RegisterView(APIView):
	def post(self, request):
		serializer = UserSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)


class LoginView(APIView):
	def post(self, request):
		last_name = request.data['user_last_name']
		first_name = request.data['user_first_name']
		password = request.data['password']

		user = User.objects.filter(last_name=last_name).first()

		if user is None:
			raise AuthentificationFailed('User not found!')

		if not user.check_password(password):
			raise AuthentificationFailed('Incorrect password!')

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedata(minutes=60),
			'iat': datetime.datetime.utcnow()
		}

		token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

		response = Response()

		response.set_cookie(key='jwt', value=token, httponly=True)
		response.data = {
			'jwt': token
		}


		return response


class UserView(APIView):

	def get(self, request):
		token = request.COOKIES.get('jwt')

		if not token:
			raise AuthentificationFailed('Unauthentificated!')

		try:
			payload = jwt.decode(token, 'secret', algorithm=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthentificationFailed('Unauthentificated!')

		user = User.objects.filter(id=payload['id']).first()
		serializer = UserSerializer(user)
		return Response(serializer.data)


class LogoutView(APIView):

	def post(self, request):
		response = Response()
		response.delete_cookie('jwt')
		response.data = {
			'message': 'success'
		}
		return response