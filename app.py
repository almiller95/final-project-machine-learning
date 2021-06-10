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

    results = db.session.query(Data.overall_rank, Data.country_or_region, Data.happiness_score, 
    Data.gdp_per_capita, Data.social_support, Data.life_expectancy, Data.freedom, Data.generosity, 
    Data.perception_of_government_corruption, Data.year).all()

    print(results[0])

    return render_template('data.html', data = results)



################################################
# Create home page
#################################################
@app.route("/")
def home():
    return render_template("index.html")


# #################################################
# # Create visualization page 1
# #################################################

# @app.route("/happiness_by_country")
# def country():
#     return render_template("happiness_by_county.html")

# #################################################
# # Create visualization page 2
# #################################################

# @app.route("/the_last_5_years")
# def years():
#     return render_template("the_last_5_years.html")

# #################################################
# # Create visualization page 2
# #################################################

# @app.route("/drews_page")
# def drew():
#     return render_template("drews_page.html")

# #################################################
# # test
# #################################################

# @app.route("/test")
# def test():
#     return render_template("test.html")

# #################################################
# # test
# #################################################

# @app.route("/2017")
# def test2():
#     return render_template("2017_map.html")

# # #################################################
# # # test
# # #################################################

# @app.route("/2018")
# def test3():
#     return render_template("2018_map.html")

# # #################################################
# # # test
# # #################################################

# @app.route("/2019")
# def test4():
#     return render_template("2019_map.html")









if __name__ == "__main__":
    app.run(debug=True)
