from rest_framework.permissions import SAFE_METHODS, BasePermission
from core.models import RegistrationPresence


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    


class IsOrganizerOrReadOnly(BasePermission):
    """
    Permissão customizada para permitir que qualquer usuário autenticado possa dar GET,
    mas apenas organizadores possam realizar ações de escrita.
    """

    def has_permission(self, request, view):
        # Esta permissão é garantida apenas se o usuário estiver autenticado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permitir GET para qualquer usuário autenticado
        if request.method in SAFE_METHODS:  # SAFE_METHODS inclui GET, HEAD, OPTIONS
            return True

        # Verifica se o usuário é organizador do evento para outros métodos
        try:
            registration = RegistrationPresence.objects.get(event=obj, user=request.user)
            return registration.type == 'organizer'
        except RegistrationPresence.DoesNotExist:
            return False