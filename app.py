from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user_data = {
        'name': 'Vadim Dmitriev',
        'title': 'IS master student at ITMO University',
        'about': 'Working with Github Pages for the second time in his life'
    }
    return render_template('profile.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)