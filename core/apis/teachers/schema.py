from marshmallow import EXCLUDE, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from core.models.teachers import Teacher
from core.libs.helpers import GeneralObject


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE
    
    created_at = auto_field(dump_only=True)
    id = auto_field(required=False, allow_none=True)
    updated_at = auto_field(dump_only=True)
    user_id = auto_field(required=False, allow_none=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)