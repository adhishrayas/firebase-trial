from django.shortcuts import render
import pyrebase
# Create your views here.
config = {
    "apiKey": "AIzaSyARq1oTDr5s0H3xC2MjH35kZC2xSU_zfTs",
    "authDomain": "fir-tut-e4c3b.firebaseapp.com",
    "databaseURL": "https://fir-tut-e4c3b-default-rtdb.firebaseio.com",
    "projectId": "fir-tut-e4c3b",
    "storageBucket": "fir-tut-e4c3b.appspot.com",
    "messagingSenderId": "919889125772",
    "appId": "1:919889125772:web:d73b37f3827e6ada4736a9",
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
def index(request):
    name_person = database.child('data').child('name2').get().val()
    last_name = database.child('data').child('lastname').get().val()
    age_ = database.child('data').child('age').get().val()
    return render(request,'index.html',{
        "lastname":last_name,
        "age_":age_,
        "name_person":name_person,
    })