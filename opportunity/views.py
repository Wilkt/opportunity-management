from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import User, Account, Opportunity
from django.contrib import messages

def signup(request):

	if request.method == "POST":
		print(request.POST)
		username = request.POST["username"]
		password = request.POST["password"]
		if not User.objects.filter(username=username).exists():

			User.objects.create(username=username, password=password)
			request.session["username"] = username
			return redirect("index")

		messages.error(request, "User with the username already exists")

		# request.session["username"] = username

		# return redirect("index")

	return render(request,'signup.html')

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		try:
			user = User.objects.get(username=username, password=password)
			request.session["username"] = username
			# messages.success(request, "Created account successfully")
			return redirect("index")
		except:
			messages.error(request, "Wrong credentials")
			return redirect("login")


	return render(request,'login.html')

def account(request):
	if request.method == "POST":

		print(request.POST)
		name = request.POST["name"]
		address = request.POST["address"]

		new_account = Account.objects.create(name=name, address=address)

		messages.success(request, "Created account successfully")
		# print("aaaaaaaaaaaaaaaa", new_account.id)


		if "create2" in request.POST:
			return redirect("opportunity", account=new_account.id)
		else:
			return redirect("index")

		# messages.success(request, "Created account successfully")
		# return redirect("index")



	return render(request,'account.html')

def opportunity(request, account=None):
	if request.method == "POST":
		print(request.POST)
		account_id = request.POST["account"]
		name = request.POST["name"]
		amount = request.POST["amount"]
		stage = request.POST["stage"]

		account_obj = Account.objects.get(id=account_id)
		# print(account)



		Opportunity.objects.create(name=name, amount=amount, stage=stage, account=account_obj)
		messages.success(request, "Created opportunity successfully")
		return redirect("index")

	accounts = Account.objects.all()
	# print(accounts[0].name)
	# account_names = [account.name for account in accounts]
	# return render(request, 'opportunity.html', {"account_names":account_names})
	return render(request, 'opportunity.html', {"accounts":accounts, "account":account})

def index(request):
	if request.method == "POST":
		keyword = request.POST["keyword"]
		opportunities = Opportunity.objects.filter(name__icontains = keyword)
	else:
		opportunities = Opportunity.objects.all()
	return render(request, 'home.html', {"opportunities": opportunities})


def logout(request):
	del(request.session["username"])
	return redirect("login")