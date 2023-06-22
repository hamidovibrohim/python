#1-ish
# import requests

# url = "https://openai80.p.rapidapi.com/chat/completions"

# matn = str(input("Matnni kiriting:"))

# payload = {
# 	"model": "gpt-3.5-turbo",
# 	"messages": [
# 		{
# 			"role": "user",
# 			"content": f"{matn}"
# 		}
# 	]
# }
# headers = {
# 	"content-type": "application/json",
# 	"X-RapidAPI-Key": "6803a12da6mshab34cc086194f6bp1be22djsn93edeaa16426",
# 	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
# }

# response = requests.post(url, json=payload, headers=headers)
# a = response.json()['choices'][0]['message']['content']
# print(a)


#2-ish
# import requests

# url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
# f = str(input("Davlatni kiriting:"))

# querystring = {"city":f"{f}"}

# headers = {
# 	"X-RapidAPI-Key": "6803a12da6mshab34cc086194f6bp1be22djsn93edeaa16426",
# 	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)



# b = response.json()['temp']
# c = response.json()['feels_like']
# e = response.json()['humidity']
# d = response.json()['wind_speed']


# print(f"{f}da harorat {b} gradusni tashkil etadi, harorat {c} gradusgacha kotarilishi mumkin. Havo namligi {e}% , Shamol tezligi {d}m/s ni tashkil etadi")


#3-ish

# import requests
# try:
#  url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

#  f = str(input("Davlatni kiriting:"))


#  payload = {
# 	"q": f"{f}",
# 	"target": "uz",
# 	"source": "en"
#  }
#  headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": "6803a12da6mshab34cc086194f6bp1be22djsn93edeaa16426",
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
#  }

#  response = requests.post(url, data=payload, headers=headers)

#  print(response.json())
# except:
#     print("iltimos to'g'ri soz kiriting")