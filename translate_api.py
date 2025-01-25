from flask import Flask, request
from translate import translate



app = Flask(__name__)
lang_map = {"Telugu": "tel_Telu", "Hindi": "hin_Deva"}

# API endpoint to handle POST request to create a new post
@app.route('/translate', methods=['POST'])
def translate_api():
    data = request.get_json()
    input_text = data.get('text')
    tgt_language = data.get('tgt_language')
    tgt_language = lang_map.get(tgt_language)

    if not input_text or not tgt_language:
        return {'error': 'Input text and target langugae are required', 'status': 400}
    # translated_text = "Hello World"
    translated_text = translate(input_text, tgt_language)
    return {'translated_text': translated_text, "status": 200}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




