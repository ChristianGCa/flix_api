# Arquivo sem uso no momento

from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Lógica de permissão
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            # Seria algo como: se user tem permissão "Can view genre", dada pelo admin, retorne True
            return request.user.has_perm('genres.view_genre') # Permissão Can view genre. É um padrão de escrita

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre') # Permissão Can add genre
        
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('genres.change_genre') # Permissão Can change genre
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre') # Permissão Can delete genre
        
        return False # por padrão
    