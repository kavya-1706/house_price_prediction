from flask import Flask, render_template, request
import pickle

app= Flask(__name__)
model = pickle.load(open('house_price_pickle.pkl','rb'))


@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='POST':
        try:
            features=[
                float(request.form['area']),
                float(request.form['bedrooms']),
                float(request.form['bathrooms']),
                float(request.form['stories']),
                request.form['mainroad'],
                request.form['guest'],
                request.form['base'],
                request.form['hotwater'],
                request.form['ac'],
                float(request.form['parking']),
                request.form['prefarea'],
                request.form['furnish'],

            ]

            prediction=model.predict([features])[0]
            return render_template('index.html',prediction=prediction)
        except ValueError:
            return render_template('index.html', error="Invalid input!")

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)