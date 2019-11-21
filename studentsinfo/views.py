from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from studentsinfo.serializers import StudentSerializer
from studentsinfo.models import student
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin,ListModelMixin,UpdateModelMixin
# Create your views here.
from rest_framework.decorators import action

from rest_framework.response import Response
#class StudentViewSet(ModelViewSet):
    #permission_classes = (AllowAny,)
    #permission_classes = (check_branch,)
    #queryset = student.objects.all()
    #serializer_class = StudentSerializer

class MyViewSet( RetrieveModelMixin, CreateModelMixin, DestroyModelMixin,ListModelMixin,UpdateModelMixin, GenericViewSet):
    pass


class OwnViewSet(MyViewSet):
    permission_classes=(AllowAny,)
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    def create(self, request, *args, **kwargs):
        print(request.data)
        if request.data and request.data.get("sbranch")=="IT":
            return super().create(request,args,kwargs)
        else:
            status = {"error" : "INvalid branch "}
            return Response(status)

    def destroy(self, request, *args, **kwargs):
        #instance = self.get_object()
        #instance.scollege='NA'
        #instance.save()
        return Response({"status" : "This method is restricted for time being..!"})

    def list(self, request, *args, **kwargs):
        #queryset = self.filter_queryset(self.get_queryset())
        allstudents = student.objects.all()
        studDicts = {}
        for st in allstudents:
            st.__dict__.pop('_state')
            studDicts[st.sid]=st.__dict__
        return Response(studDicts)


