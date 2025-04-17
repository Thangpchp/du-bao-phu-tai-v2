from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result_file = None
    if request.method == "POST":
        # Nhận file Excel
        file = request.files['input_file']
        method = request.form['method']
        if file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
            
            # Dự báo thử: ví dụ đơn giản là nhân đôi giá trị cuối
            df['Du_bao'] = df.iloc[:, -1] * 2  # demo đơn giản

            output = BytesIO()
            df.to_excel(output, index=False)
            output.seek(0)
            return send_file(output, download_name="du_bao_ket_qua.xlsx", as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
