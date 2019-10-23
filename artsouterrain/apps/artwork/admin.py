from django.contrib import admin

from artsouterrain.apps.artwork.models import Partner, PartnerType, Artist, \
    Place, ArtworkType, Artwork

admin.register(Partner)
admin.register(PartnerType)
admin.register(Artist)
admin.register(Place)
admin.register(ArtworkType)
admin.register(Artwork)
