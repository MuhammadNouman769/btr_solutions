from urllib import request

from django.shortcuts import render

# Create your views here.
def Strategy_and_Consulting(request):
    return render(request, 'services/strategy_&_consulting/strategy_and_consulting.html')

def Business_Optimization_Consulting(request):
    return render(request, 'services/strategy_&_consulting/business_optimization_consulting.html')

def product_strategy(request):
    return render(request, 'services/strategy_&_consulting/product_strategy.html')

def Technology_Strategy(request):
    return render(request, 'services/strategy_&_consulting/technology_strategy.html')

def learning_and_development(request):
    return render(request, 'services/strategy_&_consulting/learning_and_development.html')

def advanced_technology(request):
    return render(request, 'services/advanced_technology/advanced_technology.html')

def robotic_process_automation(request):
    return render(request, 'services/advanced_technology/robotic_process_automation.html')

def internet_of_things(request):
    return render(request, 'services/advanced_technology/internet_of_things.html')

def blockchain(request):
    return render(request, 'services/advanced_technology/blockchain.html')

def ar_vr(request):
    return render(request, 'services/advanced_technology/ar_vr.html')