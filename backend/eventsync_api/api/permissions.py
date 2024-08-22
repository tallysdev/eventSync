from core.models import RegistrationPresence
from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    


class IsOrganizerOrReadOnly(BasePermission):
    """
    Permissão customizada para permitir que qualquer usuário autenticado possa dar GET,
    mas apenas organizadores possam realizar ações de escrita.
    """
    def has_object_permission(self, request, view, obj):
        # Permitir GET para qualquer usuário autenticado
        if request.method in SAFE_METHODS:  # SAFE_METHODS inclui GET, HEAD, OPTIONS
            return True

        # Verifica se o usuário é organizador do evento para outros métodos
        elif request.user.is_authenticated:
            try:
                registration = RegistrationPresence.objects.get(event=obj, user=request.user)
                return registration.type == 'organizer'
            except RegistrationPresence.DoesNotExist:
                return False
        else:
            return False

class IsOrganizerOfEvent(BasePermission):
    """
    Permissão que permite adicionar, editar ou deletar um patrocínio
    apenas se o usuário for organizador do evento associado.
    """

    def has_object_permission(self, request, view, obj):
        # Permite métodos de leitura (GET) para qualquer usuário autenticado
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        # Verifica se o usuário é organizador do evento associado ao patrocínio
        elif request.user.is_authenticated:
            try:
                registration = RegistrationPresence.objects.get(event=obj.event, user=request.user)
                return registration.type == 'organizer'
            except RegistrationPresence.DoesNotExist:
                return False
        else:
            return False


class IsOrganizerForPatch(BasePermission):
    """
    Permissão que permite que apenas o organizador de um evento possa realizar o método PATCH.
    Qualquer usuário autenticado pode realizar GET e DELETE.
    """
    def has_object_permission(self, request, view, obj):
        # Permite métodos seguros (GET, HEAD, OPTIONS) e DELETE para qualquer usuário autenticado
        if request.method in SAFE_METHODS or request.method == 'DELETE':
            return True

        # Permite PATCH apenas se o usuário for o organizador do evento
        elif request.user.is_authenticated:
            try:
                registration = RegistrationPresence.objects.get(event=obj.event, user=request.user)
                return registration.type == 'organizer'
            except RegistrationPresence.DoesNotExist:
                return False
        else:
            return False