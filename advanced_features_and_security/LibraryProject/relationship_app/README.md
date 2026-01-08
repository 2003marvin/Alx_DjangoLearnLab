# Permissions and Groups in Django

## Custom Permissions
- `can_view`: Can view books
- `can_create`: Can add books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## User Groups
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can perform all actions.

## How to Test
1. Create users and assign them to groups.
2. Log in with different users and verify access.
3. Restricted users should see a 403 error for unauthorized actions.

## How to Run
1. Apply migrations:
