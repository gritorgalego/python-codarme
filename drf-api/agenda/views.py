from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)
