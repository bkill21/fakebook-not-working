from flask import render_template

from . import bp

@bp.route('/')  
def home():
    matrix = {
        'instructors' : ('Sean', 'Dylan'),
        'students' : ['gian','hamed','gian','ben','chris','alec']

    }
    return render_template('index.jinja',title='Home',instructors = matrix['instructors'],students=matrix['students'])

@bp.route('/about')
def about():
    return render_template('about.jinja')