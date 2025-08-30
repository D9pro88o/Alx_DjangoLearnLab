# Book Model Permissions and Groups

Custom permissions:
- can_view: Allows viewing books
- can_create: Allows creating books
- can_edit: Allows editing books
- can_delete: Allows deleting books

Groups:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Views are secured using the @permission_required decorator.
