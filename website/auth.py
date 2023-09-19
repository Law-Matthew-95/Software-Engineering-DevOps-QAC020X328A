import json
from flask import Blueprint, jsonify, render_template, request, flash, redirect, url_for
from sqlalchemy import text
from . models import User, Ticket
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
        
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template("users.html", user=current_user, users=users)

@auth.route('/all-tickets')
@login_required
def alltickets():
    tickets = Ticket.query.all()
    return render_template("all_tickets.html", user=current_user, tickets=tickets)

@auth.route('/edit-ticket', methods=['POST'])
@login_required
def edittickets():
    if request.method == 'POST':
        ticket = request.form
        ticketId = ticket['editTicket']
        ticket = db.session.query(Ticket).filter(Ticket.id == ticketId).first()
        return render_template("edit_ticket.html", user=current_user, ticket=ticket)
    return redirect('/edit-ticket')

@auth.route('/edit_ticket_check', methods=['POST'])
@login_required
def editTicketCheck():
    if request.method == 'POST':
        tickeruser = request.form.get('ticket.userid')
        ticketId = request.form.get('ticket.id')
        ticket = db.session.query(Ticket).filter(Ticket.id == ticketId).first()
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

@auth.route('/new-ticket', methods=['GET', 'POST'])
@login_required
def newticket():
    if request.method == 'POST':
        subject = request.form.get('subject')
        description = request.form.get('description')
        
        if len(subject) < 1:
            flash('Subject is too short.', category='error')
        elif len(description) < 1:
            flash('Description is too short.', category='error')
        else:
            new_ticket = Ticket(subject=subject, description=description, user_id=current_user.id, status='Open', requester=current_user.first_name + ' ' + current_user.last_name)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("new_ticket.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
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
        elif User.query.filter_by(isAdmin=True).first() == None:
            new_user = User(email=email, first_name=first_name, last_name=last_name ,password=generate_password_hash(password1, method='sha256'), isAdmin=True)
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name ,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)