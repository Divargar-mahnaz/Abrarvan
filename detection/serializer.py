from rest_framework import serializers


class IpDetectionSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()
