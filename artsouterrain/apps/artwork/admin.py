from django.contrib import admin

from artsouterrain.apps.artwork.models import Partner, PartnerType, Artist, \
    Place, ArtworkType, Artwork

admin.site.register(Partner)
admin.site.register(PartnerType)
admin.site.register(Artist)
admin.site.register(Place)
admin.site.register(ArtworkType)
admin.site.register(Artwork)
