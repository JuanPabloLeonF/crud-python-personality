from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Curse, Person
from .serializers import CurseSerializer, PersonSerializer
from rest_framework import status
from .response import ResponseCourseError
from django.core.exceptions import ObjectDoesNotExist, ValidationError
    
@api_view(["GET"])
def getAllCourse(request):
    lisCurse = Curse.objects.all()
    serializer = CurseSerializer(lisCurse, many=True)
    return Response(serializer.data)
    
@api_view(["GET"])
def getByIdCourse(request, id):
    try:
        curse = Curse.objects.get(id=id)
        serializer = CurseSerializer(curse)
        return Response(serializer.data, status=200)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(505)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def createCourse(request):
    try:
        serializer = CurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error en los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(status.HTTP_400_BAD_REQUEST)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail("Error en el servidor")
        responseError.setStatus("Server Error")
        responseError.setCode(505)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   
@api_view(["PUT"])
def updateCourse(request, id):
    try:
        curse = Curse.objects.get(id=id)
        serializer = CurseSerializer(curse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(400)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["PATCH"])
def updateCoursePatch(request, id):
    try:
        curse = Curse.objects.get(id=id)
        serializer = CurseSerializer(curse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(400)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["DELETE"])
def deleteCourseById(request, id):
    try:
        curse = Curse.objects.get(id=id)
        curse.delete()
        return Response(status=200)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(404)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["GET"])
def getAllPerson(request):
    try:
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail("Error en el servidor")
        responseError.setStatus("Server Error")
        responseError.setCode(505)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
@api_view(["GET"])
def getByIdPerson(request, id):
    try:
        person = Person.objects.get(id=id)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(status.HTTP_404_NOT_FOUND)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(status.HTTP_400_BAD_REQUEST)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

@api_view(["POST"])
def createPerson(request):
    try:
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(status.HTTP_400_BAD_REQUEST)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail("Error en el servidor")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["PUT"])
def updatePerson(request, id):
    try:
        person = Person.objects.get(id=id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(status.HTTP_400_BAD_REQUEST)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(status.HTTP_404_NOT_FOUND)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(status.HTTP_400_BAD_REQUEST)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["PATCH"])
def updatePersonPatch(request, id):
    try:
        person = Person.objects.get(id=id)
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            responseError = ResponseCourseError()
            responseError.setDetail("Error los datos no son validos")
            responseError.setStatus("Bad Request")
            responseError.setCode(status.HTTP_400_BAD_REQUEST)
            return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(status.HTTP_404_NOT_FOUND)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(status.HTTP_400_BAD_REQUEST)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["DELETE"])
def deletePersonById(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Not Found")
        responseError.setCode(status.HTTP_404_NOT_FOUND)
        return Response(responseError.to_dict(), status=status.HTTP_404_NOT_FOUND)
    except ValidationError:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Bad Request")
        responseError.setCode(status.HTTP_400_BAD_REQUEST)
        return Response(responseError.to_dict(), status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        responseError = ResponseCourseError()
        responseError.setDetail(f"No encontrado con el id: {id}")
        responseError.setStatus("Server Error")
        responseError.setCode(status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(responseError.to_dict(), status=status.HTTP_500_INTERNAL_SERVER_ERROR)