from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from netflixapp.models import Movies,Home,payment
from django.shortcuts import get_object_or_404, redirect, render
import razorpay
# Create your views here.
def frontpage(request):
    return render(request,"front.html")
def registerpage(request):
    b={}
    if request.method=='POST':
        u=request.POST['uname']
        l=request.POST['email']
        p=request.POST['upass']
        cp=request.POST['ucpass']
        if u=='' or l=='' or p=='' or cp=='':
            b['err']='the empty feild'
            return render (request,'register.html',b)
        elif p!=cp:
            b['err']='password didnt match'
            return render(request,'register.html',b)            
        else:
            try:
                b['success']="sucessfully register"
                a=User.objects.create(username=u,email=l,password=p,)
                a.set_password(p)
                a.save()
                return redirect('/log')
            except:
                b['err']="user already"
                return render(request,'register.html',b)
    else:
        return render(request,'register.html',b)
def loginpage(request):
    a={}
    if request.method=='GET':
        return render (request,'login.html')
    else:
        u=request.POST['uname']
        p=request.POST['upass']
        if u=='' or p=='':
            a['err']="feilds are empty"
            return render (request,'login.html',a)
        else:
            b=authenticate(username=u,password=p)
            print('credential',b)
            if b is not None:
                login(request,b)
                return redirect('/home')
            else:
                a['err']="password and username invalid"
                return render (request,'login.html',a)     
def header(request):
    return render(request,"head.html")
def signout(request):
    return render(request,"signout.html")
def tv(request):
    Imaginative_Adventures =Movies.objects.filter(genre=1) 
    New_to_Stremia= Movies.objects.filter(genre=2)
    Action_Movies = Movies.objects.filter(genre=3) 
    Us_action_Adventure_Movies= Movies.objects.filter(genre=4)
    Us_movie_dubbed_in_Tamil= Movies.objects.filter(genre=5)
    Blockbuster_Us_Comidies= Movies.objects.filter(genre=6)
    context = {
        'ImaginativeAdventures': Imaginative_Adventures,
        'New_to_Stremia': New_to_Stremia,
        'Action_Movies':Action_Movies,
        'Us_action_Adventure_Movies': Us_action_Adventure_Movies,
        'Us_movie_dubbed_in_Tamil':Us_movie_dubbed_in_Tamil,
        'Blockbuster_Us_Comidies':Blockbuster_Us_Comidies,
    }
    return render(request,"tv.html",context)
def movie(request):
    Tv_show=Home.objects.filter(genre=1) 
    Violent_movies= Home.objects.filter(genre=2)
    Only_on_Streamia = Home.objects.filter(genre=3) 
    Sci_Fi_Films= Home.objects.filter(genre=4)
    Crime_action= Home.objects.filter(genre=5)
    Epics= Home.objects.filter(genre=6)
    context = {
        'Tv_show': Tv_show,
        'Violent_movies': Violent_movies,
        'Only_on_Streamia':Only_on_Streamia,
        'Sci_Fi_Films': Sci_Fi_Films,
        'Crime_action':Crime_action,
        'Epics':Epics,
    }
    return render(request,"movies.html",context)
def about_detail(request, id):
    movies = get_object_or_404(Home, id=id)
    return render(request, 'moviedetail.html', {'movies': movies})

#movie show
def watchvideo(request, id):
    movie = get_object_or_404(Home, id=id)
    return render(request, 'vedio.html', {'movies': movie})
#home vedio show
def watchmovie(request, id):
    cinema = get_object_or_404(Movies, id=id)
    return render(request, 'homevedio.html', {'cinema': cinema})




def series_detail(request, id):
    cinema = get_object_or_404(Movies, id=id)
    return render(request, 'movieseries.html', {'cinema': cinema})
#payments and plans
from django.shortcuts import render
import razorpay

# Initialize Razorpay client with your key and secret
razorpay_client = razorpay.Client(auth=("rzp_test_W1F1EWIPGpmCRP", "aLdEEIU85UXDYBeBqRICZIco"))

def plans_view(request):
    plans = [
        {
            'id': 'premium',
            'name': 'Premium',
            'description': '4K + HDR',
            'price': 999,
            'quality': 'Best',
            'resolution': '4K (Ultra HD) + HDR',
            'devices': 'TV, computer, mobile phone, tablet',
            'simultaneous_streams': 4
        }
    ]
    return render(request, 'plans.html', {'plans': plans})

def payment_view(request, plan_id, amount):
    # Create an order in Razorpay
    order_amount = amount * 100  # Convert to subunits
    order_currency = 'INR'
    order_receipt = f'order_rcptid_{plan_id}'
    notes = {'plan': plan_id}

    order = razorpay_client.order.create({
        'amount': order_amount,
        'currency': order_currency,
        'receipt': order_receipt,
        'notes': notes
    })

    context = {
        'amount': order_amount,
        'order_id': order['id'],
        'plan': plan_id
    }
    return render(request, 'payment.html', context)

