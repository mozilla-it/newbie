from wtforms import Form, StringField, validators, BooleanField, SelectMultipleField
from forms.add_admin_role_form import AddAdminRoleForm
from database.admin_roles import AdminRoles


class AddAdminForm(Form):
    emp_id = StringField('Employee ID', [validators.required()])
    name = StringField('Employee Name', [validators.required()])
    super_admin = BooleanField('Super Admin', default=False)
    roles = SelectMultipleField('Roles', [validators.required()])
    # roles = FieldList(FormField(AddAdminRoleForm), min_entries=2)