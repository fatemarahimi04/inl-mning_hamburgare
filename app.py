""" from flask import Flask, render_template, request, redirect, url_for
from burger import visa_burgare_meny, beställ_burgare, skicka_till_kitchenview
from sides import visa_tillbehor_meny, beställ_tillbehör
from drinks import visa_dryck_meny, beställ_dryck

app = Flask(__name__)

@app.route('/')
def visa_meny():
    burgare_meny = visa_burgare_meny()
    tillbehor_meny = visa_tillbehor_meny()
    dryck_meny = visa_dryck_meny()
    return render_template('meny.html', burgare_meny=burgare_meny, tillbehor_meny=tillbehor_meny, dryck_meny=dryc>

@app.route('/bestall_burgare/<burger>', methods=['GET', 'POST'])
def beställ_burgare_route(burger):
    return beställ_burgare(burger)

@app.route('/bestall_tillbehor', methods=['GET', 'POST'])
def beställ_tillbehor_route():
    return beställ_tillbehör()

   @app.route('/bestall_dryck', methods=['GET', 'POST'])
def beställ_dryck_route():
    return beställ_dryck()

if __name__ == '__main__':
    app.run(debug=True)
 """


