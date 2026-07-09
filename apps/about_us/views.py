from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Team

""" =============== Team ApiView ================ """

class TeamView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'about/about.html'

    def get(self, request):
        teams = Team.objects.filter(
            is_active=True
        ).order_by("display_order")
        
        return Response({
            'teams': teams
        })