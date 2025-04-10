from flask import Flask, render_template
import qrcode
import os

app = Flask(__name__)

pedido = {
    "pedido_id": "BR-9645107825",
    "cliente": "PAMELLA SOARES SILVA",
    "valor": "10.966,57",
    "status": "pendente",
}

@app.route('/')
def pagamento():
    payload_pix = f"00020126580014BR.GOV.BCB.PIX0136seu-pix@palmeiras.com.br5204000053039865407{pedido['valor']}5802BR5925Palmeiras Futebol LTDA6009Sao Paulo62100506Pedido{pedido['pedido_id']}6304"

    if not os.path.exists('static'):
        os.makedirs('static')
    img = qrcode.make(payload_pix)
    img.save('static/pix_qr.png')

    return render_template("pedido.html", **pedido)

if __name__ == '__main__':
    app.run(debug=True)