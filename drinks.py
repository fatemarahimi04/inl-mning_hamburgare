""" dryck_meny = {
    "Coca-Cola": 20,
    "Pepsi": 18,
    "Fanta": 17,
    "Sprite": 19,
    "Vatten": 10,
}

def visa_dryck_meny():
    return dryck_meny

def beställ_dryck():
    if request.method == 'POST':
        val = request.form.get('dryck')
        if val in dryck_meny:
            return f"Du har beställt {val}. Det kostar {dryck_meny[val]} kr."
        else:
            return "Tyvärr, vi har inte den drycken."
    return render_template('bestall.html', meny=dryck_meny)
 """