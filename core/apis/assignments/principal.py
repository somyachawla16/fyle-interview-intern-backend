from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema

principal_assignments_resources = Blueprint('principal_assignments_resources', __name__, url_prefix='/assignments')

@principal_assignments_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of graded assignments"""
    submit_and_graded_assignments = Assignment.get_assignments_submitted_graded(p)
    principal_assignments_dump = AssignmentSchema().dump(submit_and_graded_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)


@principal_assignments_resources.route('/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def principal_grade_assignment(p, incoming_payload):
    principal_grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    
    """Grade the assignments"""
    graded_assignments = Assignment.grade_assignment_principal(principal_grade_assignment_payload.id,principal_grade_assignment_payload.grade,p)
    principal_grade_assignments_dump = AssignmentSchema().dump(graded_assignments)
    db.session.commit()
    return APIResponse.respond(data=principal_grade_assignments_dump)
    


