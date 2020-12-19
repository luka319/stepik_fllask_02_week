from flask import Flask, render_template

app = Flask(__name__)
import data

@app.route('/')
def hello_main():
    tours = data.tours
    return render_template("index.html",tours=tours,
                           departures = data.departures)

#пример: https://stp-flask-0.herokuapp.com/departure/msk
@app.route('/departures/<departure>/')
def hello_departure(departure):
    tours = data.tours
    departures = data.departures
    dep = departure
    dep2 = "/departures/"+dep+"/"
    count = 0
    prices_min = 0
    prices_max = 0
    prices = []
    nights = []
    nights_min = 0
    nights_max = 0

    for val01 in tours.values():
        for ke, va in val01.items():
            if va == dep:
                # print(f"{ke =}")
                # print(f"{val01['country'] =}")

                prices.append(val01['price'])
                # print(f"{prices = }")

                nights.append(val01['nights'])
                # print(f"{nights = }")

                count += 1

    prices_max = max(prices)
    prices_min = min(prices)
    nights_max = max(nights)
    nights_min = min(nights)

    return render_template("departure.html",tours=tours, dep=dep,
            count = count,prices_min=prices_min, prices_max = prices_max,
            nights_min=nights_min, nights_max = nights_max,
                        dep2=dep2, departures=departures)

import pprint
@app.route('/tours/<id>/')
def hello_tours(id):
    tours = data.tours
    departures = data.departures

    for key, val01 in tours.items():
        if key == int(id):
             for ke, va in val01.items():
                  if ke == "title":
                     title = va
                  if ke == "stars":
                     stars = "★" * int(va)
                  if ke == "country":
                     country = va
                  if ke == "price":
                     price = va
                  if ke == "picture":
                      picture = va
                  if ke == "nights":
                      nights = va
                  if ke == "description":
                      description = va
                  if ke == "departure":
                      departure = va

    return render_template("tour.html",tours=tours, title=title, stars=stars,
            price=price, country=country,picture=picture,nights=nights, departure=departure,
            description=description,
            departures=departures)

@app.route('/data/departures/<departure>/')
def data_departures_departure(departure):
    # d = {}
    for z, x in data.tours.items():
         if x['departure'] == departure:
             print(f"{x['country']}")
             print(f"{x['title']}")
             print(f"{x['price']}")
             print(f"{x['stars']}")

    tours = data.tours
    dep_res = data.departures
    dep = departure
    print(f"{dep_res=}")
    print(f"{dep=}")
    return render_template("data_departures_departure.html",tours=tours, 
                            dep=dep, dep_res=dep_res)

@app.route('/data/')
def hello_data():
    # >> > data.tours[1]['title']
    # 'Marina Lake Hotel & Spa'
    # >> > data.tours[1]['price']
    # 62000
    # >> > data.tours[1]['stars']
    # '4'
    # >> > data.tours[1]['country']
    # 'Куба'
    #

    tours = data.tours
    return render_template("data.html",tours=tours, departures = data.departures)



# @app.route("/data/")

if __name__ == '__main__':
    app.run(debug=True)
