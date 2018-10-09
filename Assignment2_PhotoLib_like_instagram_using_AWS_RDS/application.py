#Name : Virti Bipin Sanghavi
#Student Id : 1001504428
#Assignment 2 - CSE 6331 Cloud Computing
#Reference to the code used from some online blogs, websites and repositories

from flask import Flask, render_template, request,session,redirect, url_for, escape, request
import pymysql

from config import s3Client


application = Flask(__name__)

application.secret_key = 'sFjoZq/GmeWfFu9yPmKzNwNAn92iMDyurRDl3tEt'
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format('vbsbucket')


db = pymysql.connect(host='vbsdbinstance.cgntbdpkzpds.us-east-2.rds.amazonaws.com', user='user', passwd='test1234',
                             db='vbsdatabase')
cursor = db.cursorsor()

@application.route('/')
def index():
    if 'name' in session:
        username = session['name']
        return render_template('homepage.html',user_name = username)

    return render_template('index.html')

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['username']
        return redirect(url_for('index'))

    else:
        name = request.form['username']
        query = "INSERT INTO users(user_name) VALUES (%s)"
        print(query)
        cursor.execute(query,name)
        db.commit()
        return render_template('homepage.html', user_name=name)

    return render_template('index.html')



@application.route('/upload', methods=['GET', 'POST'])
def upload():
    f = request.files['file']
    #Give public access permissions to the user download S3 bucket list
    s3Client.upload_fileobj(
        f,
        'vbsbucket',
        f.filename,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": f.content_type
        }
    )
    url = "{}{}".format(S3_LOCATION, f.filename)

    if request.method == 'POST':
        title_form = request.form['title']
        print(url,title_form)
     # timestamp of files:
        for key in s3Client.list_objects(Bucket='vbsbucket')['Contents']:
            filename = key['Key']
            date = key['LastModified']


        query = "INSERT INTO images(img_url,title,likes,stars,timestamp) VALUES (%s,%s,%s,%s,%s)"
        print(query)
        cursor.execute(query,(url,title_form,5,2,date))
        db.commit()
    return render_template("homepage.html", msg="Image uploaded suceesfully")

@application.route('/view', methods=['GET', 'POST'])
def view():
    query = "SELECT * from images"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template("view.html",data = data)

@application.route('/ratings', methods=['GET', 'POST'])
def ratings():
    star = request.form['star']
    print(star)
    cursor.execute("""
       UPDATE images  
       SET stars=%s
       WHERE img_id= '1'""",star)
    db.commit()
    query = "SELECT * from images"
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template("view.html", data=data)

@application.route('/logout',methods=['GET', 'POST'])
def logout():
   # remove the username from the session if it is there
   session.pop('name', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)