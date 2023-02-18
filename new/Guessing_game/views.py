from django.shortcuts import render
from django.http import HttpResponse
import random
def index(request):
    return render(request,'index.html')
def guess(request):
    if 'guessing_number' not in request.session:
        request.session['guessing_number']=random.randint(1,100)
        request.session['num_of_guesses']=0
    result=''
    if request.method=='POST':
        try:
            guess=int(request.POST['guess'])
            request.session['num_of_guesses']+=1
            if guess==request.session['guessing_number']:
                result='Congrats, You have guessed the number!!!'
                request.session['guessing_number'] = random.randint(1, 100)
            elif guess>request.session['guessing_number']:
                result='The entered number is high, Try again!'
            else:
                result='The entered number is low, Try again'
        except ValueError:
                result='Please enter a valid number to proceed'
    context={
        'result':result,
        'num_of_guesses':request.session['num_of_guesses'],
    }
    return render(request,'home.html',context)

# Create your views here.