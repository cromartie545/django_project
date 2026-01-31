from django.shortcuts import render
from django.http import HttpResponseNotFound
import random


monthly_challenges = {
    'January':  "Do strenth exercises on Tuesday at 3:00 PM.",
    'February': 'VA fit classes on Monday, Tuesday and Fridays at 9:00 AM.',
    'March':    'Lets Door Dash.',
    'April':    'Play Pool.',
    'May':      'Start back out to Ridley Park and  start walking.',
    'June':     'Practice Django.',
    'July':     'Practice JavaScript, and HTML.',
    'August':   'Use the elliptical machine.',
    'September':'Use the treadmill.',
    'October':  'Finish a project on Udemy.',  
    'November': 'JavaScript, Django, Christmas Shopping and HTML',
    'December': 'Finish Christmas Shopping' 


}

def monthly_challenge(request):
    month = request.GET.get('month')
    
    '''
    try:
        challenge_text = monthly_challenges[month]
        context = {
            'challenge_text':challenge_text
        } 

        return render(request, 'challenges/challenge.html', context)
    except:
    
    '''
    if month:
        context = {
            'month':month
        }
        return render(request, 'challenges/list.html', context)
    return render(request, 'challenges/challenges.html')


    
