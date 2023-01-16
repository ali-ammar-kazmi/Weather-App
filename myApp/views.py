from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
	return render(request, 'home.html')

def weather(request):
	data=list(map(int,datetime.date.today().isoformat().split('-')))
	months = ["Jan","Feb","Mar","Apr",'May',"June","July","Aug","Sept","Oct","Nov","Dec"]
	weekdays =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	month=months[data[1]-1]
	weekday=datetime.datetime(data[0], data[1], data[2],0,0,0)
	week=weekdays[weekday.weekday()]
	day=data[2]

	context = { 'cityName' : 'Given Output Show Here',
			'country':'',
			'temp':0,
			'temp_status':'',
			'month':month,
			'week':week,
			'day':day,
			}
	if request.method=='POST':
		cityName=request.POST['cityName']
		try:
			URL = f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid=23d4504c288ca54df86f0096c3a99dce'
			res = requests.get(URL)
			data=res.json()
			temp=data['main']['temp']
			country = data['sys']['country']
			tempMood = data['weather'][0]['main']
			cityName=data['name']
			context = {
				'cityName': cityName,
				'country':country,
				'temp': temp,
				'temp_status':tempMood,
				'month':month,
				'week':week,
				'day':day,
				}
		except:
			context = { 'cityName' : 'Plz write the Valid Name before search',
			'country':'',
			'temp':0,
			'temp_status':'',
			'month':month,
			'week':week,
			'day':day,
			}
	return render(request, 'weather.html', context)

def about(request):
	return render(request, 'about.html')
