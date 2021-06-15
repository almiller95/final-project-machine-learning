import os
import csv
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cancer_data.sqlite"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ################################################
# Create class to get data
# ################################################
class Data(db.Model):
    __tablename__ = 'cancer_data'
        
    id = db.Column(db.Integer, primary_key = True)
    diagnosis = db.Column(db.String(50))
    radius_mean = db.Column(db.Numeric(2,6))
    texture_mean = db.Column(db.Numeric(2,6))
    perimeter_mean = db.Column(db.Numeric(2,6))
    area_mean = db.Column(db.Numeric(2,6))
    smoothness_mean = db.Column(db.Numeric(2,6))
    compactness_mean = db.Column(db.Numeric(2,6))
    concavity_mean = db.Column(db.Numeric(2,6))
    concave_points_mean = db.Column(db.Numeric(2,6))
    symmetry_mean = db.Column(db.Numeric(2,6))
    fractal_dimension_mean = db.Column(db.Numeric(2,6))
    radius_se = db.Column(db.Numeric(2,6))
    texture_se = db.Column(db.Numeric(2,6))
    perimeter_se = db.Column(db.Numeric(2,6))
    area_se = db.Column(db.Numeric(2,6))
    smoothness_se = db.Column(db.Numeric(2,6))
    compactness_se = db.Column(db.Numeric(2,6))
    concavity_se = db.Column(db.Numeric(2,6))
    concave_points_se = db.Column(db.Numeric(2,6))
    symmetry_se = db.Column(db.Numeric(2,6))
    fractal_dimension_se = db.Column(db.Numeric(2,6))
    radius_worst = db.Column(db.Numeric(2,6))
    texture_worst = db.Column(db.Numeric(2,6))
    perimeter_worst = db.Column(db.Numeric(2,6))
    area_worst = db.Column(db.Numeric(2,6))
    smoothness_worst = db.Column(db.Numeric(2,6))
    compactness_worst = db.Column(db.Numeric(2,6))
    concavity_worst = db.Column(db.Numeric(2,6))
    concave_points_worst = db.Column(db.Numeric(2,6))
    symmetry_worst = db.Column(db.Numeric(2,6))
    fractal_dimension_worst = db.Column(db.Numeric(2,6))



# #################################################
# # Create data page w/ sqlite connection
# #################################################

@app.route("/data")
def data():

    results = db.session.query(Data.id, Data.diagnosis, Data.radius_mean, Data.texture_mean, Data.perimeter_mean, Data.area_mean,
    Data.smoothness_mean, Data.compactness_mean, Data.concavity_mean, Data.concave_points_mean, Data.symmetry_mean,
    Data.fractal_dimension_mean, Data.radius_se, Data.texture_se, Data.perimeter_se, Data.area_se,
    Data.smoothness_se, Data.compactness_se, Data.concavity_se, Data.concave_points_se, Data.symmetry_se,
    Data.fractal_dimension_se, Data.radius_worst, Data.texture_worst, Data.perimeter_worst, Data.area_worst,
    Data.smoothness_worst, Data.compactness_worst, Data.concavity_worst, Data.concave_points_worst, Data.symmetry_worst,
    Data.fractal_dimension_worst).all()

    print(results[0])

    return render_template('data.html', data = results)



################################################
# Create home page
#################################################
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
