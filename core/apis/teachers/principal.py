from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from core.models.teachers import Teacher

from .schema import TeacherSchema

principal_teachers_resources = Blueprint('principal_teachers_resources', __name__ ,url_prefix='/teachers')

@principal_teachers_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teachers"""
    
    teacher_list = Teacher.list_teachers(p)
    principal_teachers_dump = TeacherSchema().dump(teacher_list, many=True)
    return APIResponse.respond(data=principal_teachers_dump)