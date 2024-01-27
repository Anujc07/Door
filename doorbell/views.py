from django.shortcuts import render,  HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from app_door.models import Detail, Booking
from django.db.models import Q
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from .settings import EMAIL_HOST_USER
from django.contrib import messages

def product_detail(request, product_id):
    if request.user.is_authenticated:
        prod = get_object_or_404(Detail, pk=product_id)
        return render(request, 'pro-detail.html', {'prod': prod})
    else:
        messages.info(request, 'Please log in to view this page.')
        return redirect('index')

@login_required(login_url='login')
def Dashboard(request):
    return render(request, 'dashboard.html')

def Register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST['password1']
        user_type = request.POST.get('userType')
        otp = get_random_string(length=6, allowed_chars='1234567890')
        send_mail(
            'OTP Verification',
            f'Your OTP is: {otp}',
            settings.EMAIL_HOST_USER,
            [uname],
            fail_silently=False,
        )
        request.session['otp'] = otp
        request.session['email'] = email
        request.session['uname'] = uname
        request.session['password'] = password
        request.session['user_type'] = user_type
        return render(request, 'otp.html')
    return render(request, 'dashboard.html')


def verify_otp_view(request):
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')
        entered_otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
        stored_otp = request.session.get('otp')
        if entered_otp == stored_otp:

            email = request.session.get('email')
            uname = request.session.get('uname')
            password = request.session.get('password')
            user_type = request.session.get('user_type')

            # print("email:",email)
            # print("uname:",uname)
            # print("pass:",password)

            user = User.objects.create_user(
                username=uname, password=password, email=email)
            user.is_active = True
            user.save()

            if user_type == 'owner':
                owner_group = Group.objects.get(name='Owner')
                user.groups.add(owner_group)
            elif user_type == 'tenant':
                tenant_group = Group.objects.get(name='Tenant')
                user.groups.add(tenant_group)

            login(request, user)
            del request.session['otp']
            del request.session['email']
            del request.session['uname']
            del request.session['password']
            del request.session['user_type']
            return redirect('index')

        else:

            messages.error(request, 'Invalid OTP!')
            return redirect('index')

    return redirect('index')


def Login(request):
    if request.method == 'POST':
        # email = request.POST.get('email')
        email = request.POST.get('username')
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged In')
        else:
            messages.error(request, 'Wrong email or password')

    return render(request, 'index.html')


def Logout(request):
    logout(request)
    return redirect('index')


def delete_user(request, user_id):
    if request.user.id == user_id:
        user_to_delete = get_object_or_404(User, id=user_id)
        user_to_delete.delete()
        return redirect('index')
    return HttpResponse("error")


def Index(request):

    detail = Detail.objects.all()[:8]

    context = {
        'detail': detail,
    }
    return render(request, 'index.html', context)


# ====================== About page ==========================


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


@login_required
def Add_property(request):

    if request.method == 'POST':
        user = request.user
        if Detail.objects.filter(Q(Ownername=user.username) | Q(Email=user.email)).exists():
            messages.error(request, "You have already added a property.")
        else:
            listingtype = request.POST.get('listingtype')
            cityname = request.POST.get('cityname')
            ownername = request.POST.get('email')
            email = request.POST.get('ownername')
            address = request.POST.get('address')
            # state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            phonenumber = request.POST.get('phonenumber')
            Image = request.FILES.get('Image')
            roomprice = request.POST.get('roomprice')
            nroom = request.POST.get('nroom')
            nbath = request.POST.get('nbath')
            area = request.POST.get('area')
            propertydes = request.POST.get('propertydes')
            property_year = request.POST.get('property_year')
            room_var = request.POST.get('room_var')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            Data = Detail(Listingtype=listingtype, City=cityname, Ownername=ownername, Email=email, Address=address, Pincode=pincode, Contactnumber=phonenumber, Image=Image, Room_var=room_var,
                          Price=roomprice, Area=area, Bath_room=nbath, Room_description=propertydes, Number_of_rooms=nroom, Propert_age=property_year, Latitude=latitude, Longitude=longitude)
            Data.save()
            messages.success(request, 'Property Added')
        return redirect("index")
    return render(request, 'add-property.html')


# ====================Search Engine================================


def Search_eng(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    st = request.GET.get('servicename')
    city = request.GET.get('city')
    roomtype = request.GET.get('roomtype')

    detail1 = Detail.objects.all()
    detail = Detail.objects.all()

    filters = Q()
    if roomtype is not None:
        filters &= Q(Listingtype__icontains=roomtype)

    if min_price is not None:
        try:
            min_price = int(min_price)
            filters &= Q(Price__gte=min_price)
        except ValueError:
            pass

    if max_price is not None:
        try:
            max_price = int(max_price)
            filters &= Q(Price__lte=max_price)
        except ValueError:
            pass

    if st is not None:
        filters &= Q(Address__icontains=st)

    if city is not None:
        filters &= Q(City__iexact=city)

    if not any([min_price, max_price, st]):
        detail = detail.filter(City__iexact=city)

    detail = detail.filter(filters)
    detail1 = detail1.filter(filters)

    context = {
        'detail': detail,
        'detail1': detail1,
    }

    return render(request, 'more-property.html', context)


def profile_modal(request):
    if request.user.is_authenticated:
        user = request.user
        user_properties = Detail.objects.filter(Ownername=user.username)
        print(user_properties)
        context = {'user_properties': user_properties}
        return render(request, 'base.html', context)


@login_required
def Add_booking(request, property_id):

    if request.user.is_authenticated:
        user = request.user
        property = get_object_or_404(Detail, pk=property_id)

        if Booking.objects.filter(user=user, room_book=property).exists():
            return HttpResponse("You have already booked a property.")

        if property.is_booked:
            return HttpResponse("This property is already booked.")
        else:
            booking = Booking(user=request.user,
                              email=request.user.username, room_book=property)
            booking.save()

            property.is_booked = True
            property.save()

            messages.success(request, "Booking Successfully Done!")
    else:
        messages.warning(request, "Please log in to book a property.")
    return redirect(request, 'index')
