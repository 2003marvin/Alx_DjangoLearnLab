from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

content_type = ContentType.objects.get_for_model(Book)

groups_permissions = {
    "Viewers": ["can_view"],
    "Editors": ["can_view", "can_create", "can_edit"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}

for group_name, perms in groups_permissions.items():
    group, created = Group.objects.get_or_create(name=group_name)
    for perm_codename in perms:
        permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
        group.permissions.add(permission)

print("Groups and permissions assigned successfully.")
