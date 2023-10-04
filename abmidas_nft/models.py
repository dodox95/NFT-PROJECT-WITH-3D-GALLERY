from django.db import models

class WalletUser(models.Model):
    address = models.CharField(max_length=42, unique=True) # Adresy Ethereum mają długość 42 znaków (0x + 40 znaków hexadecymalnych)
    last_login = models.DateTimeField(auto_now=True)  # Aktualizuje się za każdym razem, gdy użytkownik łączy się z Metamaskiem
