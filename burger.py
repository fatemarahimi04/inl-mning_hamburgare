""" burgare_meny = {
    "DemureChicken": {
        "pris": 40,
        "ingredienser": ["kyckling", "sallad", "tomat", "majonnäs"]
    },
    "HeroBurger": {
        "pris": 60,
        "ingredienser": ["nöttkött", "ost", "lök", "sallad", "tomat", "senap"]
    },
    "CutieVeggie": {
        "pris": 50,
        "ingredienser": ["vegetariskt kött", "ost", "sallad", "lök", "tomat", "avokado"]
    }
}

def visa_burgare_meny():
    return burgare_meny

def beställ_burgare(burger):
    if request.method == 'POST':
        borttagna_ingredienser = request.form.getlist('borttagna')
        kvarvarande_ingredienser = [ing for ing in burgare_meny[burger]['ingredienser'] if ing not in borttagna_ingredienser]

        skicka_till_kitchenview(burger, kvarvarande_ingredienser, borttagna_ingredienser)
        return redirect(url_for('tack'))

    return render_template('bestall.html', burger=burger, ingredienser=burgare_meny[burger]['ingredienser'])

def skicka_till_kitchenview(burger, ingredienser, borttagna_ingredienser):
    url = f"http://localhost:5000/buy/{burger}"
    params = {
        'kvarvarande': ingredienser,
        'borttagna': borttagna_ingredienser
    }
    respons = requests.get(url, params=params)
    print(respons.text)
 """