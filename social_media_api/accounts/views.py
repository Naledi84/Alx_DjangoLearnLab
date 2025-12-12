from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

User = get_user_model()


# ---------------------------
# REGISTER API
# ---------------------------
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # FIX — Create token correctly
        token, _ = Token.objects.get_or_create(user=user)

        data = UserSerializer(user).data
        data["token"] = token.key
        return Response(data, status=status.HTTP_201_CREATED)


# ---------------------------
# LOGIN API
# ---------------------------
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]  # validate() already authenticates

        token, _ = Token.objects.get_or_create(user=user)

        data = UserSerializer(user).data
        data["token"] = token.key
        return Response(data, status=status.HTTP_200_OK)


# ---------------------------
# PROFILE VIEW/UPDATE
# ---------------------------
class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ============================================================
# NEW — FOLLOW AND UNFOLLOW VIEWS
# ============================================================

# FOLLOW USER
class FollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if target_user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)

        request.user.following.add(target_user)

        return Response(
            {"message": f"You are now following {target_user.username}"},
            status=200
        )


# UNFOLLOW USER
class UnfollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if target_user == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=400)

        request.user.following.remove(target_user)

        return Response(
            {"message": f"You unfollowed {target_user.username}"},
            status=200
        )

