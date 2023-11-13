from detection.models import IpLocation
import json
import urllib.request


class IpDetectionProcess:
    GEO_IP_API_URL = 'http://ip-api.com/json/'

    @staticmethod
    def get_info(ip):
        database_info = IpLocation.objects.filter(ip=ip)
        if database_info:
            print('exist')
            return database_info.first().location
        else:
            print('get')
            server_response = IpDetectionProcess.get_ip_location(ip)
            return IpDetectionProcess.process_info(ip, server_response)

    @staticmethod
    def get_ip_location(ip):
        # Creating request object to GeoLocation API
        req = urllib.request.Request(IpDetectionProcess.GEO_IP_API_URL + ip)
        # Getting in response JSON
        response = urllib.request.urlopen(req).read()
        # Loading JSON from text to object
        json_response = json.loads(response.decode('utf-8'))
        return json_response

    @staticmethod
    def process_info(ip, server_response):
        key = 'message' if server_response['status'] == 'fail' else 'country'
        IpLocation.objects.create(ip=ip, location=server_response.get(key))
        return server_response.get(key)
