import numpy as np
import pandas as pd
from flask import jsonify, Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/priceIndex", methods=["POST"])
@cross_origin()
def restbyPriceandRating() : 
    if request.method == "POST" : 
        data = request.get_json()
        R = data['R']
        P = data['P']
        
        df = pd.read_csv('review_tags.csv')
    
        concat_string = R + " Rating " + "and " + P + " Price"
        df_filter = df[(df['cluster_description'] == concat_string)]
        df_filter = df_filter.sort_values(by=['tags_count'], ascending=False)
        
        dict_string = []
        
        
        for i in range(len(df_filter)) : 
            restaurant = df_filter.iloc[i].to_dict()
            dict_string.append(restaurant)
                    
        return jsonify(dict_string)

@app.route("/colName", methods=["GET"])
@cross_origin(supports_credentials=True)
def colName() : 
    if request.method == "GET" : 
        df = pd.read_csv('review_tags.csv')
        colName = df.columns.tolist()
        return jsonify(colName[48:57])
    
@app.route("/filterTags", methods=["GET"])
@cross_origin(supports_credentials=True)
def filterTags() : 
    if request.method == "POST" : 
        df = pd.read_csv('review_tags.csv')
        data = request.get_json()
        
        for i in range(len(data)) : 
            if data[i] == True : 
                df = df[df[data[i]] == True]
                
        df = df.sort_values(by=['Rating'], ascending=False)
            
        output = []
            
        for i in range(len(df)) : 
            restaurant = df.iloc[i].to_dict()
            output.append(restaurant)
        
        return jsonify(output)
    
@app.route("/ratingFilter", methods=["GET"])
@cross_origin(supports_credentials=True)
def ratingFilter() : 
    if request.method == "GET" : 
        df = pd.read_csv('review_tags.csv')
        df = df.sort_values(by=['Rating'], ascending=False)
        
        output = []
        
        for i in range(len(df)) : 
            restaurant = df.iloc[i].to_dict()
            output.append(restaurant)
        
        return jsonify(output)
    
if __name__ == "__main__" : 
    app.run(debug=True)