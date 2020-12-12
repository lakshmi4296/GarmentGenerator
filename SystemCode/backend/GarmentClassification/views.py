from rest_framework import views, status
from rest_framework.response import Response

from GarmentClassification.deployment.test.test import cnn_classification


class EnsembleClassification(views.APIView):

    def post(self, request):
        classification_response = cnn_classification(request)
        return Response(data=classification_response, status=status.HTTP_200_OK)

