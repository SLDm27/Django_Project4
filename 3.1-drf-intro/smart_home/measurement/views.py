from rest_framework import status
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorChangeSerializer


#получить список датчиков   #создать датчик
class SensorsListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def get(self, request):
    #     sensors = Sensor.objects.all()
    #     serializer = SensorDetailSerializer(sensors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = SensorDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#добавить измерение     #посмотреть измерения
class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


    # def get(self, request):
    #     sensors = Measurement.objects.all()
    #     serializer = MeasurementSerializer(sensors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = MeasurementSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#обновить информацию по конкретному датчику
class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


#получить информацию по конкретному датчику
class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer