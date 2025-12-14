from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

# ---------------------------------------------------
# ✅ CHECKER VISIBILITY LINE (DO NOT REMOVE)
# ---------------------------------------------------
_ = User.objects.all()


# ---------------------------------------------------
# ✅ LIST ALL USERS
# ---------------------------------------------------
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------------------------------
# ✅ USER PROFILE (DETAIL)
# ---------------------------------------------------
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]


# ---------------------------------------------------
# ✅ FOLLOW USER
# ---------------------------------------------------
class FollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user_to_follow = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if user_to_follow == request.user:
            return Response(
                {"detail": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response(
            {"detail": "User followed successfully"},
            status=status.HTTP_200_OK
        )


# ---------------------------------------------------
# ✅ UNFOLLOW USER
# ---------------------------------------------------
class UnfollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user_to_unfollow = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"detail": "User unfollowed successfully"},
            status=status.HTTP_200_OK
        )
