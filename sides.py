""" tillbehor_meny = {
    "Pommes frites": 25,
    "Lökringar": 30,
    "Kycklingvingar": 50,
    "Mozzarella sticks": 35,
    "Sallad": 20,
}

def visa_tillbehor_meny():
    return tillbehor_meny

def beställ_tillbehör():
    if request.method == 'POST':
        val = request.form.get('tillbehor')
        if val in tillbehor_meny:
            return f"Du har beställt {val}. Det kostar {tillbehor_meny[val]} kr."
        else:
            return "Tyvärr, vi har inte det tillbehöret."
    return render_template('bestall.html', meny=tillbehor_meny)
 """