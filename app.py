# import necessary libraries
import pandas as pd
import Pybiodiversity

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    data = Pybiodiversity.getSampleList()
    return  jsonify(data)

@app.route("/sample/<sample_number>")
def sample(sample_number):
    personal = Pybiodiversity.getPersonInfo(sample_number)
    washing_frequency = Pybiodiversity.getWashingFrequency(sample_number)
    otu_distribution = Pybiodiversity.getOtuDistribution(sample_number)
    otu_sample = Pybiodiversity.getOtuSampleRelation(sample_number)
    data = {
        'personal':personal,
        'washing_frequency':washing_frequency,
        'otu_distribution':otu_distribution,
        'otu_sample':otu_sample
    }
    return  jsonify(data)


# @app.route('/wfreq/<sample>')
#     """Weekly Washing Frequency as a number.

#     Args: Sample in the format: `BB_940`

#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """

# @app.route('/metadata/<sample>')
#     """MetaData for a given sample.

#     Args: Sample in the format: `BB_940`

#     Returns a json dictionary of sample metadata in the format

#     {
#         AGE: 24,
#         BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940
#     }
    

# @app.route('/otu')
#     List of OTU descriptions.

#     Returns a list of OTU descriptions in the following format

#     [
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Bacteria",
#         "Bacteria",
#         "Bacteria",
#         ...
#     ]



if __name__ == "__main__":
    app.run(debug=True)