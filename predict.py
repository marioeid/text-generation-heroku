from happytransformer import HappyGeneration
from flask import Flask, render_template, request, jsonify
from happytransformer import GENSettings
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

args=GENSettings(no_repeat_ngram_size=2)
top_k_sampling=GENSettings(do_sample=True,early_stopping=False,top_k=50,temperature=0.7)
generic_sampling=GENSettings(do_sample=True,early_stopping=False,top_k=0,temperature=0.7)
model=HappyGeneration("model")

app = Flask(__name__)
CORS(app)

api=Api(app)


class prediction1(Resource):
    def get(self,text):
         result1= model.generate_text(text,args=args)
         return result1.text
class prediction2(Resource):
    def get(self,text):
         result2=model.generate_text(text,args=top_k_sampling)
         return result2.text

class prediction3(Resource):
    def get(self,text):
         result3=model.generate_text(text,args=generic_sampling)
         return result3.text

api.add_resource(prediction1,'/prediction1/<string:text>')
api.add_resource(prediction2,'/prediction2/<string:text>')
api.add_resource(prediction3,'/prediction3/<string:text>')



@app.route('/')
def home():
    return render_template('Text-Generation.html')

'''
@app.route('/predict1')
def predict1():
    text = request.args.get('Generate-Text')
    # text=request.form['Generate-Text']
    result = model.generate_text(text,args=args)
    #return render_template('prediction.html',data=result.text)
    #return jsonify({'result',result.text})
    return jsonify(result=result.text)

@app.route('/predict2')
def predict2():
    text = request.args.get('Generate-Text')
    #text=request.form['Generate-Text']
    result2=model.generate_text(text,args=top_k_sampling)
    #return render_template('prediction.html',data=result.text)
    #return jsonify({'result',result.text})
    return jsonify(result2=result2.text)

@app.route('/predict3')
def predict3():
    text = request.args.get('Generate-Text')
    #text=request.form['Generate-Text']
    result3=model.generate_text(text,args=generic_sampling)
    #return render_template('prediction.html',data=result.text)
    #return jsonify({'result',result.text})
    return jsonify(result3=result3.text)
'''

if __name__ == "__main__":
    app.run(debug=True)
    
'''if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
'''