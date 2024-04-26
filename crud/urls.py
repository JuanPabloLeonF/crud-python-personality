from django.urls import path
from .views import createCourse, getAllCourse, getByIdCourse, updateCourse, updateCoursePatch, deleteCourseById, getAllPerson, createPerson, getByIdPerson, updatePerson, updatePersonPatch, deletePersonById

urlpatterns = [
    path("curse/getAll", getAllCourse),
    path("curse/getById/<str:id>", getByIdCourse),
    path("curse/create", createCourse),
    path("curse/update/<str:id>", updateCourse),
    path("curse/updatePatch/<str:id>", updateCoursePatch),
    path("curse/deleteById/<str:id>", deleteCourseById),
    path("person/getAll", getAllPerson),
    path("person/create", createPerson),
    path("person/getById/<str:id>", getByIdPerson),
    path("person/update/<str:id>", updatePerson),
    path("person/updatePatch/<str:id>", updatePersonPatch),
    path("person/deleteById/<str:id>", deletePersonById),
]