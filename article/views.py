# -*- coding: utf-8 -*-
import re
import smtplib

import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from re import findall

from django.template.defaulttags import register

from article.models import *
from django.db import connection, connections
import random
from django.contrib.auth import login, authenticate, logout
from article.models import Profile, Documents as Docs, Contract
from article.forms import SignUpForm, LoginForm

def home(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
    }
    return render(request, 'article/index.html', context)


def documents(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'

    docs = Docs.objects.all()

    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
        'docs': docs
    }
    return render(request, 'article/documenty.html', context)


def info(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
    }
    return render(request, 'article/informaciya.html', context)


def contacts(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
    }
    return render(request, 'article/kontakty.html', context)


def lich_cab(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
        redirect(home)

    profile = get_object_or_404(Profile, email=email_cookie)
    contract = get_object_or_404(Contract, number=profile.contract)
    docs = Docs.objects.filter(contract=contract)
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
        'profile': profile,
        'docs': docs,
    }
    return render(request, 'article/lich-kab.html', context)


def zab_parol(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
    }
    return render(request, 'article/zab-parol.html', context)


def zayavka(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form = LoginForm()
    context = {
        'form_l': form,
        'auth_p': auth_p,
    }
    return render(request, 'article/zayavka.html', context)


def signin(request):
    error = ''
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie:
        profile = Profile.objects.filter(email=email_cookie).first()
        if profile:
            if findall(profile.password, password_cookie):
                return redirect(lich_cab)
        else:
            response = HttpResponseRedirect('/')
            response.delete_cookie('email')
            response.delete_cookie('password')
            return response

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            passwordform = form.data['password']
            profile = Profile.objects.filter(email=email).first()
            if profile:
                if profile.password == passwordform:
                    response = HttpResponseRedirect('/lich_cab')
                    response.set_cookie('email', email)
                    response.set_cookie('password', profile.password)
                    return response
                else:
                    error = 'Incorrect email or password'
                    return redirect(home)
            else:
                error = 'No Profile'
                return redirect(home)
        else:
            return redirect(home)
    else:
        return redirect(home)


def signout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('email')
    response.delete_cookie('password')
    return response

def registration(request):
    email_cookie = request.COOKIES.get('email')
    password_cookie = request.COOKIES.get('password')
    if email_cookie and password_cookie:
        profile = get_object_or_404(Profile, email=email_cookie)
        if password_cookie == profile.password:
            auth_p = 'ok'
    else:
        auth_p = 'no'
    form_l = LoginForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            contract = form.data['contract']
            profile = Profile.objects.filter(email=email)
            contracts = Contract.objects.filter(number=contract)
            if profile:
                return redirect(home)
            else:
                if contracts:
                    form.save()
                    profile = Profile.objects.filter(email=email).first()
                    response = HttpResponseRedirect('/lich_cab')
                    response.set_cookie('email', email)
                    response.set_cookie('password', profile.password)
                    return response
                else:
                    error = 'В системе нет договора Купли-Продажи с таким номером'
                    return render(request, 'article/registraciya.html',
                                  {'form': form, 'form_l': form_l, 'auth_p': auth_p, 'error': error})
        else:
            return redirect(home)
    else:
        form = SignUpForm()



    return render(request, 'article/registraciya.html', {'form': form, 'form_l': form_l, 'auth_p': auth_p})


