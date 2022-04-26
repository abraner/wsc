from django.contrib import admin
from .models import Comp, CabAcc, NumType, RoomType, WoodSpecies, DoorStyle, FinishColor, FinishOption,\
    ProdQueue, Pricing, Ultimate, WorkType, Agreement

admin.site.site_url = "/wscdatabase/main"

admin.site.site_header = 'WSC Bidding Dashboard'
admin.site.register(Comp)
admin.site.register(CabAcc)
admin.site.register(NumType)
admin.site.register(RoomType)
admin.site.register(WoodSpecies)
admin.site.register(DoorStyle)
admin.site.register(FinishColor)
admin.site.register(FinishOption)
admin.site.register(ProdQueue)
admin.site.register(Pricing)
admin.site.register(Ultimate)
admin.site.register(WorkType)
admin.site.register(Agreement)