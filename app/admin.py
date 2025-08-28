# Tiedosto: suppliers/app/admin.py
# Admin käyttöliittymän määrittelyt.
# Admin käyttöliittymä on Django:n sisäänrakennettu työkalu,
# jolla voi hallinnoida sovelluksen tietoja web-käyttöliittymässä.
# Admin käyttöliittymä on hyödyllinen työkalu kehityksen aikana
# ja pienimuotoisissa projekteissa, joissa ei tarvita erillistä
# hallintapaneelia.

# Jos rekisteröi tällä tavalla adminille oman appin
# modelit, voi myös admin sivuilta muokata näitä tietoja.

from django.contrib import admin

from app.models import Supplier, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass