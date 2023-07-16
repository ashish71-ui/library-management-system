from django.shortcuts import render,redirect
from . forms import Signup,StudentIDForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import Book,StudentProfile,BookRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db import IntegrityError
from django.shortcuts import render
from .models import StudentProfile
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookRequestForm, BookApprovalForm
from .models import  Book
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            try:
                student_profile = StudentProfile.objects.create(user=user)
            except IntegrityError:
                # StudentProfile already exists for the user, handle the error
                # e.g., display an error message or redirect to a different page
                pass
            return redirect('/login')  
    else:
        form = Signup()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/logged')  # Replace 'home' with the desired URL after successful login
        return redirect('/logged')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@login_required
def logged(request):
    products = Book.objects.all()
    params ={'product':products}

    return render(request,'logged.html',params)
@login_required
def product_view(request,pk):
     products =  item = get_object_or_404(Book, pk=pk)
     return render(request, 'productview.html', {'i': products})
 

# @login_required
# def update_student_id(request):
#     student_profile = StudentProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = StudentIDForm(request.POST, instance=student_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:update_student_id')
#     else:
#         form = StudentIDForm(instance=student_profile)

#     return render(request, 'studentid.html', {'form': form, 'student_profile': student_profile, })

@login_required
def update_student_id(request):
    user = request.user

    try:
        student_profile = StudentProfile.objects.get(user=user)
    except StudentProfile.DoesNotExist:
        
        student_profile = StudentProfile.objects.create(user=user)

    if request.method == 'POST':
        form = StudentIDForm(request.POST,request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('/update_student_id')
    else:
        form = StudentIDForm(instance=student_profile)

    return render(request, 'studentid.html', {'form': form, 'student_profile': student_profile})



@login_required
def book_request(request):
    if request.method == 'POST':
        form = BookRequestForm(request.POST)
        if form.is_valid():
            book_request = form.save(commit=False)
            book_request.student = request.user
            book_request.save()
            return redirect('/requests')
    
    else:
        form = BookRequestForm()
    return render(request, 'book_request.html', {'form': form})

@login_required
def book_request_list(request):
    book_requests = BookRequest.objects.filter(student=request.user)
    return render(request, 'book_request_list.html', {'book_requests': book_requests})

@staff_member_required
def book_approval_list(request):
    book_requests = BookRequest.objects.filter(approved=False)
    return render(request, 'book_approval_list.html', {'book_requests': book_requests})

@staff_member_required
def approve_book_request(request, request_id):
    book_request = get_object_or_404(BookRequest, id=request_id)
    if request.method == 'POST':
        form = BookApprovalForm(request.POST, instance=book_request)
        if form.is_valid():
            form.save()
            return redirect('book_approval_list')
    else:
        form = BookApprovalForm(instance=book_request)
    return render(request, 'approve_book_request.html', {'form': form})