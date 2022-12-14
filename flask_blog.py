from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Michael Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    },
    {
        'author': 'Robert Doe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 21, 2022'
    },
    {
        'author': 'Jane Williams',
        'title': 'Blog Post 4',
        'content': 'Forth post content',
        'date_posted': 'April 21, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
