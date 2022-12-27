from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from app.models import BodyMassIndex, Calories, Diet
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

#главная
def index(request):
    return render(request,'index.html')

#регистрация
def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,"Аккаунт был зарегестрирован "+ user)
				return redirect('login')

		context = {'form':form}
		return render(request,'signup.html',context)

#вход
def LoginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('index')
			else:
				messages.info(request,'Username or password is incorrect')
		context = {}
		return render(request,'login.html',context)

#выход
def LogOutPage(request):
	logout(request)
	return redirect('login')

#расчет имт
@login_required(login_url="/login/")
def bmi(request):
	if request.method == "POST":
		height = request.POST['height']
		height = int(height)
		weight = request.POST['weight']
		weight = int(weight)
		pip = (height/100)**2
		ind = weight / pip
		BMI = round(ind, 2)
		inss = BodyMassIndex(BMI=BMI)
		inss.save()

		if BMI <= 18.5:
			return render(request, 'bmi.html',
						  {'xyz': 'Ваш ИМТ', 'bmi': f'{BMI:g}', 'abc': 'Недостаточная масса тела'})
		elif 18.5 < BMI <= 25:
			return render(request, 'bmi.html',
						  {'xyz': 'Ваш ИМТ', 'bmi': f'{BMI:g}', 'abc': 'Нормальная масса тела'})
		elif 25 < BMI <= 29.9:
			return render(request, 'bmi.html',
						  {'xyz': 'Ваш ИМТ', 'bmi': f'{BMI:g}', 'abc': 'Избыточная масса тела'})
		else:
			BMI >= 30
		return render(request, 'bmi.html',
					  {'xyz': 'Ваш ИМТ', 'bmi': f'{BMI:g}', 'abc': 'Ожирение'})
		return render(request, 'bmi.html', {'bmi': BMI})

	else:
		return render(request, 'bmi.html')

#расчет калорий
@login_required(login_url="/login/")
def calorie(request):
	if request.method == "POST":
		users = request.user.username
		age = request.POST['age']
		height = request.POST['height']
		gender = request.POST['gender']
		activity = request.POST["activity"]
		weight = request.POST['weight']
		ins = Diet(users=users, age=age, height=height, gender=gender, activity=activity, weight=weight)
		ins.save()
		if gender == 'Мужской':
			result = 88.362 + (13.397 * int(weight)) + (4.799 * int(height)) - (4.330 * int(age))
			abc = result
			if activity == "Сидячий образ жизни":
				defg = abc * 1.2
			elif activity == "Умеренная активность":
				defg = abc * 1.375
			elif activity == "Средняя активность":
				defg = abc * 1.55
			else:
				defg = abc * 1.725
			defg = round(defg, 2)
			inx = Calories(defg=defg)
			inx.save()
			return render(request, 'calorie.html', {'xyz': 'Ваша ежедневная потребность в калориях = ', 'calories': defg})

		elif gender == 'Женский':
			result = 447.593 + (9.247 * int(weight)) + (3.098 * int(height)) - (4.330 * int(age))
			abc = result
			if activity == "Сидячий образ жизни":
				defg = abc * 1.2
			elif activity == "Умеренная активность":
				defg = abc * 1.375
			elif activity == "Средняя активность":
				defg = abc * 1.55
			else:
				defg = abc * 1.725
			defg = round(defg, 2)
			inx = Calories(defg=defg)
			inx.save()
			return render(request, 'calorie.html', {'xyz': 'Ваша ежедневная потребность в калориях = ', 'calories':defg})

	return render(request, 'calorie.html')

#подробности
@login_required(login_url="/login/")
def detail(request):
	if request.user.is_superuser:
		dobj = Diet.objects.all()
		dobjs = BodyMassIndex.objects.all()
		dobjss = Calories.objects.all()
		lll = zip(dobj,dobjs,dobjss)
		return render(request,'detail.html',{'lll':lll})

#удалить  данные
@login_required(login_url="/login/")
def deleteAll(request):
	if request.user.is_superuser:
		Diet.objects.all().delete()
		BodyMassIndex.objects.all().delete()
		Calories.objects.all().delete()

		return render(request,'detail.html')
