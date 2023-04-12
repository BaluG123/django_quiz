from .serializers import  SixSerializers,SevenSerializers,EightSerializers,NineSerializers,TenSerializers,CurrentSerializers,GeneralSerilizers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from testapp.models import six,seven,eight,nine,ten,CurrentAffairs,GeneralKnowledge

class Six_View(ModelViewSet):
    queryset=six.objects.all()
    serializer_class=SixSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class Seven_View(ModelViewSet):
    queryset=seven.objects.all()
    serializer_class=SevenSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class Eight_View(ModelViewSet):
    queryset=eight.objects.all()
    serializer_class=EightSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class Nine_View(ModelViewSet):
    queryset=nine.objects.all()
    serializer_class=NineSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class Ten_View(ModelViewSet):
    queryset=ten.objects.all()
    serializer_class=TenSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]  

class Current_View(ModelViewSet):
    queryset=CurrentAffairs.objects.all()
    serializer_class=CurrentSerializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]  

class General_View(ModelViewSet):
    queryset=GeneralKnowledge.objects.all()
    serializer_class=GeneralSerilizers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]  

