from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Movie, Profile

class Home(View):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/profile/')
        ul_list= {
            'What is Netflix?':'Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries and more – on thousands of internet-connected devices./nYou can watch as much as you want, whenever you want, without a single ad – all for one low monthly price. There\'s always something new to discover, and new TV shows and movies are added every week!',
            'How much does Netflix cost?':"Watch Netflix on your smartphone, tablet, Smart TV, laptop, or streaming device, all for one fixed monthly fee. Plans range from ₹ 149 to ₹ 649 a month. No extra costs, no contracts.",
            'Where can I watch?':'Watch anywhere, anytime. Sign in with your Netflix account to watch instantly on the web at netflix.com from your personal computer or on any internet-connected device that offers the Netflix app, including smart TVs, smartphones, tablets, streaming media players and game consoles./n You can also download your favourite shows with the iOS, Android, or Windows 10 app. Use downloads to watch while you\'re on the go and without an internet connection. Take Netflix with you anywhere.',
            'How do I cancel?':'Netflix is flexible. There are no annoying contracts and no commitments. You can easily cancel your account online in two clicks. There are no cancellation fees – start or stop your account anytime.',
            'What can I watch on Netflix?':'Netflix has an extensive library of feature films, documentaries, TV shows, anime, award-winning Netflix originals, and more. Watch as much as you want, anytime you want.',
            'Is Netflix good for kids?':'The Netflix Kids experience is included in your membership to give parents control while kids enjoy family-friendly TV shows and films in their own space./n Kids profiles come with PIN-protected parental controls that let you restrict the maturity rating of content kids can watch and block specific titles you don’t want kids to see.',}
        return render(request,'index.html',{'list':ul_list})

@method_decorator(login_required,name='dispatch')
class ProfileList(View):
    
    def get(self,request,*args, **kwargs):

        profiles=request.user.profiles.all()

        print(profiles)


        return render(request,'profileList.html',{
            'profile':profiles
        })


@method_decorator(login_required,name='dispatch')
class ProfileCreate(View):
    def get(self,request,*args, **kwargs):
        form=ProfileForm()

        return render(request,'profileCreate.html',{
            'form':form
        })

    def post(self,request,*args, **kwargs):
        form=ProfileForm(request.POST or None)

       
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch/{profile.uuid}')

        return render(request,'profileCreate.html',{
            'form':form
        })

@method_decorator(login_required,name='dispatch')
class Watch(View):
    def get(self,request,profile_id,*args, **kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)

            movies=Movie.objects.filter(age_limit=profile.age_limit)

            try:
                showcase=movies[0]
            except :
                showcase=None
            

            if profile not in request.user.profiles.all():
                return redirect(to='app:profile_list')
            return render(request,'movieList.html',{
            'movies':movies,
            'show_case':showcase
            })
        except Profile.DoesNotExist:
            return redirect(to='app:profile_list')


@method_decorator(login_required,name='dispatch')
class ShowMovieDetail(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            return render(request,'movieDetail.html',{
                'movie':movie
            })
        except Movie.DoesNotExist:
            return redirect('app:profile_list')

@method_decorator(login_required,name='dispatch')
class ShowMovie(View):
    def get(self,request,movie_id,*args, **kwargs):
        try:
            
            movie=Movie.objects.get(uuid=movie_id)

            movie=movie.videos.values()
            

            return render(request,'showMovie.html',{
                'movie':list(movie)
            })
        except Movie.DoesNotExist:
            return redirect('app:profile_list')