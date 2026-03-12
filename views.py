from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from models import db, StudentGroup

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        students_list = []
        
        i = 0
        while f'name_{i}' in form_data:
            students_list.append({
                'name': form_data.get(f'name_{i}', ''),
                'age': form_data.get(f'age_{i}', ''),
                'email': form_data.get(f'email_{i}', '')
            })
            i += 1
        
        if students_list:
            group = StudentGroup(students=students_list)
            db.session.add(group)
            db.session.commit()
            flash(f'✅ Группа №{group.id} создана!', 'success')
        
        return redirect(url_for('main.index'))
    
    return render_template('form.html')

@main.route('/api/groups')
def get_groups():
    groups = StudentGroup.query.all()
    return jsonify([group.to_dict() for group in groups])