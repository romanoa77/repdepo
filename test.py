from flask import Flask, render_template
from flask import jsonify
#import json
app=Flask(__name__)

#definisco un dizionario con lo stato del datastore
buf_stats={

"buf_size":0,
"ds_state":"OPERATIONAL"
}

@app.route('/')
def index():
    return render_template('index.html',size=buf_stats['buf_size'],state=buf_stats['ds_state'])

@app.route('/stream')
def pushStream():

    temp=buf_stats['buf_size']
    temp+=1

    buf_stats.update({"buf_size":temp})

    return '200'



@app.route('/bufstat',methods=['GET'])
def getBufStat():
     
     #resp_str="{\'buf_size\':"+"\'"+buf_count+"\'"+"}"
     


     #Serve usare i dizionari
     #resp_f=json.dumps(resp_dict)
     
     return jsonify(buf_stats)

if __name__=='__main__':
    app.run(debug=True)