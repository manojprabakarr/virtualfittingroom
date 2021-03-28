from flask import Flask,render_template
import Shirt as s



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/trail1')
def trail1():  
    return render_template('trail1.html')

  


   
       

@app.route("/forward/", methods=['POST'])
def move_forward():  
         s.run("544.jpg")



@app.route('/p3')
def p3():  
      s.run("548.jpg")
     

      
@app.route('/shop')

def shop():
    return  render_template('shop.html')



if __name__ == '__main__':
    app.run(use_reloader = True)