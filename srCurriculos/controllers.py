import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from srCurriculos.components.resumes import get, add

class ResumesAPI(APIView):

    def get(self, request):
        try:
            payload = request.GET
            if not payload:
                return JsonResponse({'response': get()}, status = 200) # GET all resumes

            if 'id' in payload:
                resumes = get(payload.get('id'))
                return JsonResponse({'response': resumes}, status = 200) # GET specific resume

            invalidKeys = []
            for key in payload:
                invalidKeys.append(key)
            
            raise ValueError('Keys: ' + ", ".join(invalidKeys) + ' are invalid')
        except ValueError as e:
            return JsonResponse({'response': str(e)}, status = 400)

    def post(self, request):    
        try:
            payload = json.loads((request.body).decode('utf-8'))
            requiredKeys = {'first_name', 'last_name', 'age', 'email', 'desired_profession', 'phone_number'}
            if not all (key in payload for key in requiredKeys): # Validate obligatory parameters
                raise ValueError('Invalid request body')

            address = payload['address'] if 'address' in payload else []
            pastExperience = payload['past_experience'] if 'past_experience' in payload else []

            add(payload['first_name'], payload['last_name'], payload['age'], payload['email'], payload['desired_profession'], payload['phone_number'], address, pastExperience)

            # print(payload)  
            if 'address' in payload:
                print('as')

            if 'past_experience' in payload:
                print('yay')

            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    def delete(self, request):
        try:
            payload = json.loads((request.body).decode('utf-8'))
            if 'id' not in payload:            
                raise ValueError('Resume \'id\' not specified')
            
            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)