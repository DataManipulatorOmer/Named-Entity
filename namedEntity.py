from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    text = request.json.get('text', '')
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True)
