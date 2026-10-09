from django.shortcuts import render
from Statusapp.models import status
from Statusapp.serializer import StatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import mixins
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# class MyClass(APIView):
#     def get(self,request):
#         qs = status.objects.all()
#         serializer = StatusSerializer(qs,many=True)
#         return Response(serializer.data)


# class AllStatusList(ListAPIView):
#     queryset = status.objects.all()
#     serializer_class = StatusSerializer

# class GetOneStatus(RetrieveAPIView):
#     queryset = status.objects.all()
#     serializer_class = StatusSerializer
#     # lookup_field = id

# class CreateStatus(CreateAPIView):
#     queryset = status.objects.all()
#     serializer_class = StatusSerializer

# class UpdateStatus(UpdateAPIView):
#     queryset = status.objects.all()
#     serializer_class = StatusSerializer

# class DelateStatus(DestroyAPIView):
#     queryset = status.objects.all()
#     serializer_class = StatusSerializer

#model mixining cocept
class AllStatusAddViews(ListAPIView,mixins.CreateModelMixin):
    queryset = status.objects.all()
    serializer_class = StatusSerializer


    def post(self ,request, *args, **kwargs):
        return self.create(request,*args, **self.kwargs)


class StatusRetriveUpdateDeleteView(RetrieveAPIView,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = status.objects.all()
    serializer_class = StatusSerializer
    
    
    def put(self ,request, *args, **kwargs):
        return self.update(request,*args, **self.kwargs)

    def delete(self ,request, *args, **kwargs):
            return self.destroy(request,*args, **self.kwargs)

