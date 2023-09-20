import json
from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from sqlalchemy import text
from . models import User, Ticket
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# intercepts the request when the user logs in
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # the login function will get user email and password from the request form
        email = request.form.get('email')
        password = request.form.get('password')
        # the user will be queried from the database using the email
        user = User.query.filter_by(email=email).first()
        if user:
            # if the password is correct, the user will be logged in
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
        
    return render_template("login.html", user=current_user)

# intercepts the request when the user logs out
@auth.route('/logout')
@login_required
def logout():
    # this function will call the logout_user function from flask_login
    logout_user()
    return redirect(url_for('auth.login'))

# intercepts the request when the user clicks the users button
@auth.route('/users')
@login_required
def users():
    # it will query all the users from the database
    users = User.query.all()
    return render_template("users.html", user=current_user, users=users)

# intercepts the request when the user clicks the all tickets button
@auth.route('/all-tickets')
@login_required
def alltickets():
    # it will query all the tickets from the database
    tickets = Ticket.query.all()
    return render_template("all_tickets.html", user=current_user, tickets=tickets)

# intercepts the request when the user clicks the edit ticket button
@auth.route('/edit-ticket', methods=['POST'])
@login_required
def edittickets():
    if request.method == 'POST':
        # it will get the ticket id from the request form then query the ticket from the database where the ticket id is the same as the ticket id from the request form
        ticket = request.form
        ticketId = ticket['editTicket']
        ticket = db.session.query(Ticket).filter(Ticket.id == ticketId).first()
        return render_template("edit_ticket.html", user=current_user, ticket=ticket)
    return redirect('/edit-ticket')

# intercepts the request when the user clicks the confirm edit ticket button
@auth.route('/edit_ticket_check', methods=['POST'])
@login_required
def editTicketCheck():
    if request.method == 'POST':
        # it will first get the ticket requester id from the request form then get the ticket id from the request form 
        # then query the ticket from the database where the ticket id is the same as the ticket id from the request form
        tickeruser = request.form.get('ticket.userid')
        ticketId = request.form.get('ticket.id')
        ticket = db.session.query(Ticket).filter(Ticket.id == ticketId).first()
        # if the user is an admin or the user is the ticket requester, the ticket will be updated
        if current_user.isAdmin or current_user.id == tickeruser:
            description = request.form.get('description')
            status = request.form.get('status')
            subject = request.form.get('subject')
            ticket.description = description
            ticket.status = status
            ticket.subject = subject
            db.session.commit()
            flash('Ticket updated!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('You are not authorized to edit this ticket!', category='error')
            return redirect(url_for('views.home'))
    return redirect(url_for('views.home'))

# intercepts the request when the user clicks the new ticket button
@auth.route('/new-ticket', methods=['GET', 'POST'])
@login_required
def newticket():
    # it will get the subject and description from the request form
    if request.method == 'POST':
        subject = request.form.get('subject')
        description = request.form.get('description')
        # if the subject or description is too short, the ticket will not be created
        if len(subject) < 1:
            flash('Subject is too short.', category='error')
        elif len(description) < 1:
            flash('Description is too short.', category='error')
        else:
        # else the ticket will be created
            new_ticket = Ticket(subject=subject, description=description, user_id=current_user.id, status='Open', requester=current_user.first_name + ' ' + current_user.last_name)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("new_ticket.html", user=current_user)

# intercepts the request when the user clicks sign up button
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # it will get the email, first name, last name, password, and password confirmation from the request form
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        # if the email already exists, the email is too short, the first name is too short, the last name is too short, 
        # the passwords don't match, or the password is too short, the account will not be created
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        # if there are no admins, the user will be made an admin
        elif User.query.filter_by(isAdmin=True).first() == None:
            new_user = User(email=email, first_name=first_name, last_name=last_name ,password=generate_password_hash(password1, method='sha256'), isAdmin=True)
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        # else the user will be created but not an admin
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name ,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)