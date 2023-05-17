import random

from flask import Flask, render_template, redirect, url_for, request
import flask
from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
import flask
from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from sqlalchemy.exc import DatabaseError



from datetime import date
from functools import wraps


from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


# b=True
# c="safe content"
def tor_csam(url):
    def check_csam(imagePath):
        import os
        os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
        import tensorflow as tf
        
        


        from tensorflow import keras
        from keras import Sequential
        from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,BatchNormalization,Dropout
        import json
        from os import listdir
        from os.path import isfile, join, exists, isdir, abspath

        import numpy as np
        import tensorflow as tf
        from tensorflow import keras
        import tensorflow_hub as hub



        def age(image_path):   
            import cv2
            import math
            import argparse


            def highlightFace(net, image, conf_threshold=0.7):
                
                imageOpencvDnn=image
                imageHeight=imageOpencvDnn.shape[0]
                imageWidth=imageOpencvDnn.shape[1]
                blob=cv2.dnn.blobFromImage(imageOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

                net.setInput(blob)
                detections=net.forward()
                faceBoxes=[]
                for i in range(detections.shape[2]):
                    confidence=detections[0,0,i,2]
                    if confidence>conf_threshold:
                        x1=int(detections[0,0,i,3]*imageWidth)
                        y1=int(detections[0,0,i,4]*imageHeight)
                        x2=int(detections[0,0,i,5]*imageWidth)
                        y2=int(detections[0,0,i,6]*imageHeight)
                        faceBoxes.append([x1,y1,x2,y2])
                        cv2.rectangle(imageOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(imageHeight/150)), 8)
                return imageOpencvDnn,faceBoxes




            faceProto="opencv_face_detector.pbtxt"
            faceModel="opencv_face_detector_uint8.pb"
            ageProto="age_deploy.prototxt"
            ageModel="age_net.caffemodel"
            genderProto="gender_deploy.prototxt"
            genderModel="gender_net.caffemodel"

            MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
            ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
            genderList=['Male','Female']

            faceNet=cv2.dnn.readNet(faceModel,faceProto)
            ageNet=cv2.dnn.readNet(ageModel,ageProto)
            genderNet=cv2.dnn.readNet(genderModel,genderProto)

            image = cv2.imread(image_path)
            
            padding=20

            resultImg,faceBoxes=highlightFace(faceNet,image)
            if not faceBoxes:
                print("No face detected")

            for faceBox in faceBoxes:
                face=image[max(0,faceBox[1]-padding):
                
        
                        min(faceBox[3]+padding,image.shape[0]-1),max(0,faceBox[0]-padding)
                        :min(faceBox[2]+padding, image.shape[1]-1)]
                if face.size == 0:
                    continue

                blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds=genderNet.forward()
                gender=genderList[genderPreds[0].argmax()]
                print(f'Gender: {gender}')

                ageNet.setInput(blob)
                agePreds=ageNet.forward()
                age=ageList[agePreds[0].argmax()]
                print(f'Age: {age[1:-1]} years')
                if age==ageList[0] or age==ageList[1] or age==ageList[2] or age==ageList[3]:
                    print("It has csam content")
                    global b
                    global c
                    b=False
                    c="csam content"
                    break
                    
                else:
                    print("The provided link has no csam content")

                cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
                


        IMAGE_DIM = 224   # required/default image dimensionality

        def load_images(image_paths, image_size, verbose=True):
            '''
            Function for loading images into numpy arrays for passing to model.predict
            inputs:
                image_paths: list of image paths to load
                image_size: size into which images should be resized
                verbose: show all of the image path and sizes loaded
            
            outputs:
                loaded_images: loaded images on which keras model can run predictions
                loaded_image_indexes: paths of images which the function is able to process
            
            '''
            loaded_images = []
            loaded_image_paths = []

            if isdir(image_paths):
                parent = abspath(image_paths)
                image_paths = [join(parent, f) for f in listdir(image_paths) if isfile(join(parent, f))]
            elif isfile(image_paths):
                image_paths = [image_paths]

            for img_path in image_paths:
                try:
                    if verbose:
                        print(img_path, "size:", image_size)
                    image = keras.preprocessing.image.load_img(img_path, target_size=image_size)
                    image = keras.preprocessing.image.img_to_array(image)
                    if not image.size:
                       print("Error: input image size is empty!")



                    image /= 255
                    loaded_images.append(image)
                    loaded_image_paths.append(img_path)
                except Exception as ex:
                    print("Image Load Failure: ", img_path, ex)
            
            return np.asarray(loaded_images), loaded_image_paths


        def load_model(model_path):
            if model_path is None or not exists(model_path):
                raise ValueError("saved_model_path must be the valid directory of a saved model to load.")
            
            # model = tf.keras.models.load_model(model_path)
            model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})
            # model.summary()
            print(model.summary())
            return model


        def classify(model, input_paths, image_dim=IMAGE_DIM):
            """ Classify given a model, input paths (could be single string), and image dimensionality...."""
            images, image_paths = load_images(input_paths, (image_dim, image_dim))
            probs = classify_nd(model, images,input_paths)
            return dict(zip(image_paths, probs))


        def classify_nd(model, nd_images,input_paths):
            """ Classify given a model, image array (numpy)...."""
            global a
            model_preds = model.predict(nd_images)
            # preds = np.argsort(model_preds, axis = 1).tolist()
            
            categories = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']

            probs = []
            for i, single_preds in enumerate(model_preds):
                single_probs = {}
                for j, pred in enumerate(single_preds):
                    single_probs[categories[j]] = float(pred)
                probs.append(single_probs)
                print(probs)
                list=[]
                
                for prob in probs:
                    for key,value in prob.items():
                        list.append(value)
                    max_value=(max(list))
                    for prob in probs:
                        for key,value in prob.items():
                            if value==max_value:
                                print(key)
                                a= key
                                if a=="porn":
                                    print(input_paths)
                                    age(input_paths)
                                    exit
                                    

                                else:
                                    print("It has no csam content")
                            
                    
                
                
            
            return probs

            
                
            


        def main():   

            img_path=imagePath
            
            model = load_model("Nudity-Detection-Model-Not-safe-for-work-NSFW-/Nudity-Detection-Model-zipped/Nudity-Detection-Model.h5")
            image_preds = classify(model, img_path, IMAGE_DIM)
            
            # print(json.dumps(image_preds, indent=2), '\n')


        if __name__ == "__main__":
            main()





    def torSearcher(url):
        import requests
        import random
        import os
        from bs4 import BeautifulSoup
        
        os.startfile(r"C:\Users\Hp Laptop\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe")
        
        def get_tor_session():
            session = requests.session()
            session.proxies = {'http': 'socks5h://127.0.0.1:9050',
                            'https': 'socks5h://127.0.0.1:9050'}
            return session

        session = get_tor_session()

        ua_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
            , "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
            ,
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
            ,
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
        ua = random.choice(ua_list)
        headers = {'User-Agent': ua}
        print("Getting ...", url)

        result = session.get(url).text
        soup = BeautifulSoup(result)

        # Find all image tags in the HTML
        img_tags = soup.find_all("img")

        # Extract the URLs of the images
        urls = [img['src'] for img in img_tags]



        # Create folder to save images
        folder_name = "images"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Remove all files from folder
        for file in os.listdir(folder_name):
         os.remove(os.path.join(folder_name, file))

        # Download the images and save in folder
        for url in urls:
            response = session.get(url)
            with open(os.path.join(folder_name, url.split("/")[-1]), "wb") as f:
                f.write(response.content)

        file_list = os.listdir(folder_name)

        # loop over the list of files and perform some function on each file
        for file_name in file_list:
         if file_name.endswith('.jpg'):  # check if the file is a JPEG image
            file_path = os.path.join(folder_name, file_name)  # get the full file path
            check_csam(file_path)
            
        if b:
            print("it has no csam")
        else:
            print("it has  csam")
            # exit(1)
            

    # url = "http://model-sandra.ch3r6uefdo4obnnamhcc3tmjgshtfvrezqvejmg2ypz6nukmwxrkdiyd.onion/20.html"
    torSearcher(url)

    import sys
    import os

    programname = os.path.basename(sys.argv[0])

    try:
        thelist = sys.argv[1]
        print("Opening ...", thelist)
        with open(thelist, "r", encoding="utf-8") as newfile:
            data = newfile.readlines()
            try:
                
                for k in data:
                    k = k.replace("\n", "")
                    k = "http://" + k
                    torSearcher(k)
            except Exception as E:
                print(E)
    except:
        print("Usage : {} <newlineSeperatedList.txt>".format(programname))

#url = "http://model-sandra.ch3r6uefdo4obnnamhcc3tmjgshtfvrezqvejmg2ypz6nukmwxrkdiyd.onion/20.html"
 
# output=csam(url)
# print(output)
# print(b)
# print(c)






app = Flask(__name__, template_folder="template")


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

Bootstrap(app)
##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DataBaseTables.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
UPLOAD_FOLDER='static/assets4/images'
app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
login_manager = LoginManager()
login_manager.init_app(app)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

db.create_all()

class LinkDetails(UserMixin,db.Model):
    __tablename__="LinkDetails"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    
    email=db.Column(db.String(100))
    link=db.Column(db.String(1000))
    csam=db.Column(db.String(100))


db.create_all()

@app.route("/registerUser", methods=["GET", "POST"])
def registerUser():




 if request.method == "POST":
      user=User.query.filter_by(email=request.form.get("email")).first()
      if  user:
            
            flash("You have already signed up with that email,log in instead!","error")
            return redirect(url_for("registerUser"))

      hash_and_salted_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256',
                                                              salt_length=8)
      new_user = User(email=request.form.get("email"),
                                    name=request.form.get("name"),

                                    password=hash_and_salted_password)
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user)
      return redirect(url_for("home"))

 return render_template("SignUp.html")






@app.route("/",methods=["GET", "POST"])
def loginUser():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("That email does not exist,please try again","error")
            return redirect(url_for("loginUser"))

        elif not check_password_hash(user.password, password):
            print(user.password)
            flash("Password incorrect,please try again","error")
            return redirect(url_for("loginUser"))
        else:

            login_user(user)
            print(user.name)
            print(current_user.name)




            return redirect(url_for("home"))
    return render_template("Login.html")




@app.route("/tableUser")
def tableUser():
    user=current_user.name
    userLink=LinkDetails.query.filter_by(name=user).all()
    return render_template("tableUser.html",user=user,links=userLink)
    

@app.route("/home",methods=["GET","POST"])
def home():
    user=current_user.name
    

    if request.method=="POST":
        link=request.form.get("link")
        name=current_user.name
        email=current_user.email
        csam="Null"
        
        if LinkDetails.query.filter_by(link=link,name=name).first() :
            a= LinkDetails.query.filter_by(link=link,name=name).first()
            print(a)
            d= LinkDetails.query.filter_by(link=link,name=name).first()
            print(d.csam)

            return redirect(url_for("output",id=a.id))

        else:    
            new_link=LinkDetails(link=link,name=name,email=email,csam=csam)
            db.session.add(new_link)
            db.session.commit()
            global b
            global c
            b=True
            c="safe content"
            tor_csam(link)
            print(b)
            print(c)
            a= LinkDetails.query.filter_by(link=link,name=name).first()
            print(a)
            a.csam=c
            db.session.commit()
            print(a.csam)
            
            return redirect(url_for("output",id=a.id))
    return render_template("index.html",user=user)

@app.route("/output<int:id>")
def output(id):
    a= LinkDetails.query.filter_by(id=id).first()
    csam=a.csam
    link=a.link
    print(csam)
    print(link)
    return render_template("output.html",link=link,user=current_user.name,csam=csam)


# def output(link):
#     print(link)
    
    
#     name=current_user.name
    
#     return render_template("output.html",user=name,link=link,csam=c)



@app.route("/table")
def table():
    links= LinkDetails.query.all()
    return render_template("table.html",links=links)

  

# @app.route("/2")
# def home2():
#     return render_template("index2.html")

# @app.route("/3")
# def home3():
#     return render_template("Login.html")

# @app.route("/4")
# def home4():
#     return render_template("SignUp.html")

if __name__ == "__main__":
    app.run(debug=True)
app.app_context()






