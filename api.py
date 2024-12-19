from flask import Flask, jsonify, request

app = Flask(__name__)
students = [
    {"id": 1, "cognome": "Abouzahra", "nome": "Rawan", "data_nascita": "26/05/2007", "paese_residenza": "Bergamo", "mezzo_trasporto": ["Piedi"], "tempo_traversata": "15 minuti", "hobby": ["Musica", "videogiochi"]},
    {"id": 2, "cognome": "Barbato", "nome": "Simone", "data_nascita": "15/02/2007", "paese_residenza": "Stezzano", "mezzo_trasporto": ["pullman"], "tempo_traversata": "15-30 minuti", "hobby": ["basket", "palestra"]},
    {"id": 3, "cognome": "Bardhi", "nome": "Kozma", "data_nascita": "14/09/2007", "paese_residenza": "Ponte San Pietro", "mezzo_trasporto": ["Treno"], "tempo_traversata": "40-45 minuti", "hobby": ["Palestra", "Videogiochi"]},
    {"id": 4, "cognome": "Benedetti", "nome": "Edoardo", "data_nascita": "13/12/2007", "paese_residenza": "Osio Sotto", "mezzo_trasporto": ["treno"], "tempo_traversata": "20-30 minuti", "hobby": ["palestra", "film"]},
    {"id": 5, "cognome": "Bianco", "nome": "Simone", "data_nascita": "15/02/2007", "paese_residenza": "Petosino", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "30 minuti", "hobby": ["Videogiochi", "palestra"]},
    {"id": 6, "cognome": "Buttironi", "nome": "Andrea", "data_nascita": "20/10/2007", "paese_residenza": "Brembate Sotto", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "40-45 minuti", "hobby": ["Videogiochi", "scherma"]},
    {"id": 7, "cognome": "Dieni", "nome": "Pasquale", "data_nascita": "29/08/2007", "paese_residenza": "Verdello", "mezzo_trasporto": ["Treno"], "tempo_traversata": "8-12 minuti", "hobby": ["Palestra", "Basket"]},
    {"id": 8, "cognome": "El Hassani", "nome": "Ayoub", "data_nascita": "05/03/2007", "paese_residenza": "Calusco D'Adda", "mezzo_trasporto": ["Treno"], "tempo_traversata": "35 minuti", "hobby": ["Musica", "videogiochi", "tecnocraft", "economia", "politica"]},
    {"id": 9, "cognome": "El Ouahidi", "nome": "Oussama", "data_nascita": "02/01/2008", "paese_residenza": "Ponte San Pietro", "mezzo_trasporto": ["Treno"], "tempo_traversata": "45 minuti", "hobby": ["calcio"]},
    {"id": 10, "cognome": "Galante", "nome": "Santiago", "data_nascita": "26/06/2007", "paese_residenza": "Bergamo", "mezzo_trasporto": ["Piedi"], "tempo_traversata": "20 minuti", "hobby": ["Calcio", "musica"]},
    {"id": 11, "cognome": "Ghazi", "nome": "Youssef", "data_nascita": "15/02/2007", "paese_residenza": "Bergamo", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "40 minuti", "hobby": ["Calcio", "videogiochi"]},
    {"id": 12, "cognome": "Ghisalberti", "nome": "Riccardo", "data_nascita": "25/07/2007", "paese_residenza": "Zogno", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "45 minuti", "hobby": ["Musica", "Videogiochi", "Film"]},
    {"id": 13, "cognome": "Griffini", "nome": "Matteo", "data_nascita": "08/06/2007", "paese_residenza": "Sotto il Monte", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "35-45 minuti", "hobby": ["Videogiochi"]},
    {"id": 14, "cognome": "Lyesyev", "nome": "Antonio", "data_nascita": "11/10/2006", "paese_residenza": "Alzano Lombardo", "mezzo_trasporto": ["Tram", "Moto"], "tempo_traversata": "20 minuti", "hobby": ["Musica", "Videogiochi"]},
    {"id": 15, "cognome": "Palazzi", "nome": "Massimo", "data_nascita": "14/03/2007", "paese_residenza": "Oltre il Colle", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "90 minuti", "hobby": ["Sport", "Caccia", "Musica"]},
    {"id": 16, "cognome": "Ravazzi", "nome": "Myrko", "data_nascita": "10/09/2007", "paese_residenza": "Verdello", "mezzo_trasporto": ["Treno"], "tempo_traversata": "8-12 minuti", "hobby": ["Informatica", "musica"]},
    {"id": 17, "cognome": "Secchi", "nome": "Lorenzo", "data_nascita": "14/06/2007", "paese_residenza": "Brembate Sotto", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "45-50 minuti", "hobby": ["Palestra", "Videogiochi"]},
    {"id": 18, "cognome": "Sigismondi", "nome": "Gabriele", "data_nascita": "14/12/2007", "paese_residenza": "Petosino", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "25-30 minuti", "hobby": ["Calcio", "videogiochi", "sport"]},
    {"id": 19, "cognome": "Signori", "nome": "Andrea", "data_nascita": "15/10/2007", "paese_residenza": "Bergamo", "mezzo_trasporto": ["piedi"], "tempo_traversata": "30 minuti", "hobby": ["Sport", "musica", "cucina"]},
    {"id": 20, "cognome": "Tassetti", "nome": "Davide", "data_nascita": "30/11/2007", "paese_residenza": "Sorisole", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "30 minuti", "hobby": ["videogiochi", "calcio", "cucina"]},
    {"id": 21, "cognome": "Timis", "nome": "Alin Ioan", "data_nascita": "29/12/2007", "paese_residenza": "Calusco D'Adda", "mezzo_trasporto": ["Treno"], "tempo_traversata": "25-30 minuti", "hobby": ["videogiochi"]},
    {"id": 22, "cognome": "Vitali", "nome": "Matteo", "data_nascita": "25/05/2007", "paese_residenza": "Zogno", "mezzo_trasporto": ["Pullman"], "tempo_traversata": "45-60 minuti", "hobby": ["League of Legends"]}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(students)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in students if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)


@app.before_request
def block_non_get_requests():
    if request.method != 'GET':
        return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == '__main__':
    app.run(debug=True)
