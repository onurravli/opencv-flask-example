import base64

from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    # formdan gelen dosyayı al
    file = request.files['file']

    # opencv ile dosyayı oku
    img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

    # istediğiniz işlemleri yapın
    # Örnek bir işlem olarak resmin boyutunu yazdırıyorum
    height, width, channels = img.shape
    text = f"Resim boyutu: {width}x{height}"

    # işlenmiş görüntüyü geri döndürün
    retval, buffer = cv2.imencode('.png', img)
    img_str = base64.b64encode(buffer).decode()

    # HTML sayfasında görüntüyü ve işlenmiş veriyi gösterin
    return render_template('index.html', image=img_str, text=text)


if __name__ == '__main__':
    app.run(debug=True)
