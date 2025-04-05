from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    print("Data masuk:", data)
    # Di sini kamu bisa proses data atau trigger ke sistem kamu
    return {'status': 'oke diterima'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
