from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ChatGroup)
#admin.site.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    # Affichez dans la liste uniquement l'auteur, le message chiffré et la date de création
    list_display = ('author', 'encrypted_body', 'created')
    
    # Rendre le champ 'encrypted_body' en lecture seule pour éviter toute modification manuelle
    readonly_fields = ('encrypted_body',)
    
    # Exclure le champ 'body' de l'interface d'administration pour qu'il ne soit pas visible
    exclude = ('body',)

admin.site.register(GroupMessage, GroupMessageAdmin)






"""
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'encrypted_body', 'created')
    readonly_fields = ('encrypted_body',)  # Empêche l'édition du texte chiffré

    def get_readonly_fields(self, request, obj=None):
        # Vous pouvez aussi rendre tous les champs en lecture seule, si nécessaire.
        if obj:
            return self.readonly_fields + ('body',)
        return self.readonly_fields

admin.site.register(GroupMessage, GroupMessageAdmin)
"""
