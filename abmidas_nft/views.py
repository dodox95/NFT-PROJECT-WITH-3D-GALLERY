from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import WalletUser
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import requests

def home(request):
    return render(request, 'main.html')

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def vip_page(request):
    return render(request, 'vip.html')

def contact(request):
    return render(request, 'contact.html')

def connect_wallet(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        if not address:
            return JsonResponse({"error": "No address provided"}, status=400)

        user, created = WalletUser.objects.get_or_create(address=address)
        if not created:
            user.last_login = timezone.now()
            user.save()

        # Ustawienie adresu w plikach cookie
        response = JsonResponse({"success": "Connected successfully"})
        response.set_cookie('wallet_address', address, max_age=3600)  # ustawia na 1 godzinę; dostosuj według potrzeb

        return response
    return JsonResponse({"error": "Invalid request method"}, status=400)


def check_wallet_connection(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        if not address:
            return JsonResponse({"error": "No address provided"}, status=400)
        
        try:
            user = WalletUser.objects.get(address=address)
            return JsonResponse({"connected": True})
        except ObjectDoesNotExist:
            return JsonResponse({"connected": False})

    return JsonResponse({"error": "Invalid request method"}, status=400)

def nft(request):
    return render(request, 'nft.html')


def fetch_nft_data(request):
    API_URL = "https://api.arbitrum.io/api?module=account&action=tokennfttx&startblock=0&endblock=99999999&sort=asc"
    address = request.GET.get('address')
    api_key = "9RX3PIAD7WRJNEVG88AJG574TI38J6IFAY"

    if not address:
        return JsonResponse({"error": "No address provided"}, status=400)
    
    response = requests.get(f"{API_URL}&address={address}&apikey={api_key}")

    return JsonResponse(response.json())

def handler404(request, exception):
    return render(request, '404.html', status=404)
