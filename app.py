from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Banjul, The Gambia',
        'salary': 'GMD 175,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Remote',
        # 'salary': 'GMD 175,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Dakar, Senegal',
        'salary': 'GMD 100,000'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'location': 'Yarambamba, The Gambia',
        'salary': 'GMD 85,000'
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def jobs():
    return jsonify(JOBS)