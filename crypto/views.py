from django.shortcuts import render

def home(request):
    import requests
    import json

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,ETC,LTC,EOS,BSV,ADA&tsyms=USD")
    price = json.loads(price_request.content)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html',{'api':api, 'price':price})

def prices(request):
    if(request.method=='POST'):
        param = request.POST['param']
        param = param.upper()
        import requests
        import json

        crypto_request = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+param+"&tsyms=USD,JPY,EUR,INR,GBP,AED,CNY,KRW,ZAR")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'param':param, 'crypto':crypto})
    else:
        return render(request, 'prices.html',{})