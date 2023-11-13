from django.http import JsonResponse
from rest_framework.views import APIView

from detection.modules import IpDetectionProcess
from detection.serializer import IpDetectionSerializer


class IpDetection(APIView):
    def post(self, request):
        serializer = IpDetectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = IpDetectionProcess.get_info(serializer.validated_data['ip'])
        return JsonResponse({'result': result})
