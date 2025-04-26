from flask import render_template, request, Blueprint, redirect, url_for, flash, get_flashed_messages
from .models import db, Register ,Event ,EventDetails,ContactForm,Result
from flask import *
views = Blueprint('views', __name__)



@views.route('/')
def home():
    flash('Logout successful!',category='success')
    return render_template('home.html', messages=get_flashed_messages(with_categories=True))

@views.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Register.query.filter_by(email=email, password=password).first()
       
        
        if  (email =="admin@gmail.com" and password =="admin"):
            flash("You are successfully logged Out ",category='success')
            # Redirect to the admin page or perform admin-specific actions
            return redirect(url_for("views.admin_dashboard"))
        elif user :
            flash("You are successfully logged Out !",category='success')
            return redirect(url_for("views.dashboard"))

        else:
            flash('Invalid email or password. Please try again.', category='error')
    
    return render_template('home.html')

@views.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        
        existing_user = Register.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', category='error')
            return render_template('home.html', message='Email already registered')

       
        register_user = Register(username=username, email=email, password=password)
        db.session.add(register_user)
        db.session.commit()
        flash('Registration successful! Now Login!', category='success')
        #return render_template('home.html')
        

    return render_template('home.html',messages=get_flashed_messages(with_categories=True))

@views.route('/logout')
def logout():
    # You can use Flask-Login's logout_user function
    flash('Login successful!',category= 'success')
    return redirect(url_for('views.home'))


@views.route('/dashboard', methods=['POST','GET'])
def dashboard():
    return render_template("dashboard.html")

@views.route('/event', methods=['POST','GET'])
def event():
    data = EventDetails.query.all()
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        reg_no = request.form.get('reg_no')
        gender = request.form.get('gender')
        semester = request.form.get('semester')
        event1 = request.form.get('event1')
        event2 = request.form.get('event2')
        event3 = request.form.get('event3')

        new_event = Event(
            full_name=full_name,
            reg_no=reg_no,
            gender=gender,
            semester=semester,
            event1=event1,
            event2=event2,
            event3=event3
        )

        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for("views.dashboard"))

    return render_template('event.html',data=data)
 

@views.route('/participants', methods=['POST','GET'])
def participants():
    data = Event.query.all()
    return render_template("participants.html",data=data)



@views.route('/admin_dashboard', methods=['POST','GET'])
def admin_dashboard():
    data = ContactForm.query.all()
    return render_template("admin_dashboard.html",data=data)




@views.route('/eventdetails', methods=['POST','GET'])
def eventdetails():
    if request.method == 'POST':
        tournament_name = request.form.get('tournament_name')
        sport_name = request.form.get('sport_name')  # Corrected field name
        gender = request.form.get('gender')
        venue_date = request.form.get('venue_date')
        venue = request.form.get('venue')


        from datetime import date
        venue_date_str = "2023-12-23"
        venue_date = date.fromisoformat(venue_date_str)
        new_event = EventDetails(
            tournament_name=tournament_name,
            sport_name=sport_name,
            gender=gender,
            venue_date=venue_date,
            venue=venue,
        )
        print(new_event)

        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for("views.admin_dashboard"))

    return render_template('event_details.html')

@views.route('/view_events', methods=['POST','GET'])
def view_events():
    data = EventDetails.query.all()
    return render_template("view_events.html",data=data)

@views.route('/contactus', methods=['POST','GET'])
def contactus():

    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']

        new_contact = ContactForm(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            message=message
        )

        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('views.dashboard'))

    return render_template('contactus.html')

@views.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        
        sport_name = request.form.get('sport_name') 
        
        full_name = request.form.get('full_name')
        result= request.form.get('result')


        
        new_event = Result(
            full_name=full_name,
            sport_name=sport_name,
            result= result
            
            
        )
        print(new_event)

        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('views.admin_dashboard'))
    
    return render_template("result.html")


@views.route('/view_result', methods=['POST','GET'])
def view_result():
    data = Result.query.all()
    return render_template("view_result.html",data=data)


@views.route('/delete_event/<int:event_id>', methods=['GET', 'POST'])
def delete_event(event_id):
    # Get the event from the database based on the provided event_id
    event_to_delete = Event.query.get(event_id)

    if event_to_delete:
        # Delete the event from the database
        db.session.delete(event_to_delete)
        db.session.commit()
        flash('Event deleted successfully')
    else:
        flash('Event not found')

    return redirect(url_for('views.participants'))


@views.route('/update_participant/<int:participant_id>', methods=['GET'])
def update_participant(participant_id):
    participant = Event.query.get(participant_id)
    return render_template('update_participants.html', participant=participant)


@views.route('/update_participants/<int:participant_id>', methods=['POST'])
def update_participants(participant_id):
    participant = Event.query.get(participant_id)

    if not participant:
        return "Participant not found", 404

    # Update participant details based on the form data
    participant.full_name = request.form['full_name']
    participant.reg_no = request.form['reg_no']
    participant.gender = request.form['gender']
    participant.semester = request.form['semester']
    participant.event1 = request.form['event1']
    participant.event2 = request.form['event2']
    participant.event3 = request.form['event3']
    # Update other fields similarly

    # Commit changes to the database
    db.session.commit()

    # Redirect to the participants page or wherever appropriate
    return redirect(url_for('views.participants'))

   
