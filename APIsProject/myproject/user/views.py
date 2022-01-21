from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # authenticate for loading data!
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # add filter seaching and filter Ordering!
    search_fields = ['username', 'email']  # using username and email for seaching!
    ordering = ['id']  # ordering by ASC


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name'] # using name for seaching!
    ordering = ['-id']  # ordering by DESC


#
# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['category', 'in_stock']


# class UserListView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username', 'email']
