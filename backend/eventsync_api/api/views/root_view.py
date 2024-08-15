from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class ApiRootView(APIView):
    def get(self, request, format=None):
        data = {
            'users-list': reverse('user_list', request=request, format=format),
            'user-detail': reverse('user_detail', request=request, args=[1], format=format),
            'register': reverse('register', request=request, format=format),
            'login-token': reverse('token_obtain_pair', request=request, format=format),
            'refresh-token': reverse('token_refresh', request=request, format=format),
            'swagger-json': reverse('schema', request=request, format=format),
            'swagger-ui': reverse('swagger-ui', request=request, format=format),
            'redoc-ui': reverse('redoc', request=request, format=format),
            'locals-list': reverse('local_list', request=request, format=format),
            'locals-detail': reverse('local_detail', request=request, args=[1], format=format),
            'events-list': reverse('event_list', request=request, format=format),
            'events-detail': reverse('event_detail', request=request, args=[1], format=format),
            'form-list': reverse('form_list', request=request, format=format),
            'form-detail': reverse('forms_detail', request=request, args=[1], format=format),
            'question-list': reverse('question_list', request=request, format=format),
            'question-detail': reverse('question_detail', request=request, args=[1], format=format)
            # adicione mais endpoints aqui
        }
        return Response(data)
    