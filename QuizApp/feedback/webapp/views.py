from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback, Question,Choice
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, FeedbackForm
from django.urls import reverse

# Create your views here.

def homepage(request):
    return render(request=request,template_name = 'webapp/home.html', context = {'feedbacks':Feedback.objects.all})

def register(request):
    if request.method == "POST":
        form =  NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}") 
            login(request, user)
            messages.info(request, f"you are now logged in as {username}")
            return redirect('webapp:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form =  NewUserForm
    return render(request, "webapp/register.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect('webapp:homepage')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user =  authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}")
                return redirect('webapp:homepage')
            else:
                messages.error(request,"invalid username or password")
        else:
            messages.error(request,"invalid username or password")


    form = AuthenticationForm()
    return render(request,"webapp/login.html",{"form":form})

def feedback_detail(request):
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = FeedbackForm()
    return render(request, 'webapp/form.html', {'form':form})
            
def question_list(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, id=question_id)
    context = {'question':question}
    return render(request, 'webapp/question_list.html', context)

    """ render the question_list.html template which list all the currently available question 
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, "webapp/question_list.html", context)"""

def question_detail(request):
    return HttpResponse("you are looking for question with id off: {}".format(question_id))
    """questions = Question.objects.get(id= question_id)
    context = {'questions' : questions}
    return render(requwst, 'webapp/')"""


def question_submit(request, question_id):
    print(request.POST)
    quiz = get_object_or_404(Question, id=question_id)
    choice_id = request.POST.get('choice')
    if choice_id:
        choice = Choice.objects.get(id=choice_id )
        if int(choice_id) in [3,5] :
            messages.error(request, 'correct answer')
            question_id = question_id+1
            return HttpResponseRedirect(reverse('webapp:question', args=(question_id,)))
        print(choice_id)
        print(choice)
    else:
        messages.error(request, 'No Choice was Found!')
        return HttpResponseRedirect(reverse("webapp:question", args=(question_id,)))
    messages.error(request, 'wrong answer')
    return HttpResponseRedirect(reverse('webapp:question', args=(question_id,)))
    
