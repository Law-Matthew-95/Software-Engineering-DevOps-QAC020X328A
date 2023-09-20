from flask import Blueprint, flash, redirect, render_template, jsonify, request, url_for
from flask_login import login_required, current_user
import json

from pytest import console_main 
from .models import Ticket , User
from . import db

views = Blueprint('views', __name__)

# intercepts the request and checks if the user is logged in
@views.route('/')
@login_required
# if the user is logged in, it will render the home page
def home():
    return render_template("home.html", user=current_user)

# intercepts the request when the user clicks the delete ticket button
@views.route('/delete-ticket', methods=['POST'])
# the delete_ticket function will load the ticket data from the request then get the ticket id
def delete_ticket():
    ticket = json.loads(request.data)
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        # if the user is the ticket requester or an admin, the ticket will be deleted
        if ticket.user_id == current_user.id or current_user.isAdmin:
            db.session.delete(ticket)
            db.session.commit()
        else:
            flash('You need to be the ticket Requester or an Admin to delete a ticket.', category='error')
    return jsonify({})

# intercepts the request when the user clicks the delete user button
@views.route('/delete-user', methods=['POST'])
# the delete_user function will load the user data from the request then get the user id
def delete_user():
    user = json.loads(request.data)
    userId = user['userId']
    user = User.query.get(userId)
    if user:
        # if the user is an admin or the user is trying to delete themselves, the user will not be deleted
        if user.isAdmin:
            flash('Cannot delete an admin.', category='error')
        elif user.id == current_user.id:
            flash('Cannot delete yourself.', category='error')
        else:
            db.session.delete(user)
            db.session.commit()
    return jsonify({})

# intercepts the request when the user clicks the create admin button
@views.route('/create-admin', methods=['POST'])
# the create_admin function will load the user data from the request then get the user id
def create_admin():
    user = json.loads(request.data)
    userId = user['userId']
    user = User.query.get(userId)
    if user:
        # if the user is already an admin, the user will not be made an admin
        if user.isAdmin:
            flash('User is already an admin.', category='error')
        else:
            user.isAdmin = True
            db.session.commit()
            flash('User is now an admin.', category='success')
    return jsonify({})


    