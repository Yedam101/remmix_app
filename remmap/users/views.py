# from django.conf import settings
# from django.contrib.auth import authenticate, login, logout
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.exceptions import ParseError, NotFound
# from rest_framework.permissions import IsAuthenticated

# from users.models import User
# from . import serializers



# class KakaoLogIn(APIView):
#     def post(self, request):
#         try:
#             code = request.data.get("code")
#             access_token = requests.post(
#                 "https://kauth.kakao.com/oauth/token",
#                 headers={"Content-Type": "application/x-www-form-urlencoded"},
#                 data={
#                     "grant_type": "authorization_code",
#                     "client_id": "c5faa6465d2032b32a9df057d3c74c1b",
#                     "redirect_uri": "http://127.0.0.1:3000/social/kakao",
#                     "code": code,
#                 },
#             )
#             access_token = access_token.json().get("access_token")
#             user_data = requests.get(
#                 "https://kapi.kakao.com/v2/user/me",
#                 headers={
#                     "Authorization": f"Bearer {access_token}",
#                     "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
#                 },
#             )
#             user_data = user_data.json()
#             kakao_account = user_data.get("kakao_account")
#             profile = kakao_account.get("profile")
#             try:
#                 user = User.objects.get(email=kakao_account.get("email"))
#                 login(request, user)
#                 return Response(status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 user = User.objects.create(
#                     email=kakao_account.get("email"),
#                     username=profile.get("nickname"),
#                     name=profile.get("nickname"),
#                     avatar=profile.get("profile_image_url"),
#                 )
#                 user.set_unusable_password()
#                 user.save()
#                 login(request, user)
#                 return Response(status=status.HTTP_200_OK)
#         except Exception:
#             return Response(status=status.HTTP_400_BAD_REQUEST)