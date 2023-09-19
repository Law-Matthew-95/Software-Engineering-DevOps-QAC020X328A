from flask import Blueprint, flash, redirect, render_template, jsonify, request, url_for
from flask_login import login_required, current_user
import json

from pytest import console_main
from .models import Ticket , User
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/delete-ticket', methods=['POST'])
def delete_ticket():
    ticket = json.loads(request.data)
    ticketId = ticket['ticketId']
    ticket = Ticket.query.get(ticketId)
    if ticket:
        if ticket.user_id == current_user.id or current_user.isAdmin:
            print(current_user.id)
            print(ticket.user_id)
            db.session.delete(ticket)
            db.session.commit()
        else:
            flash('You need to be the ticket Requester or an Admin to delete a ticket.', category='error')
    return jsonify({})

@views.route('/delete-user', methods=['POST'])
def delete_user():
    user = json.loads(request.data)
    userId = user['userId']
    user = User.query.get(userId)
    if user:
        if user.isAdmin:
            flash('Cannot delete an admin.', category='error')
        elif user.id == current_user.id:
            flash('Cannot delete yourself.', category='error')
        else:
            db.session.delete(user)
            db.session.commit()
    return jsonify({})

@views.route('/create-admin', methods=['POST'])
def create_admin():
    user = json.loads(request.data)
    userId = user['userId']
    user = User.query.get(userId)
    if user:
        if user.isAdmin:
            flash('User is already an admin.', category='error')
        else:
            user.isAdmin = True
            db.session.commit()
            flash('User is now an admin.', category='success')
    return jsonify({})


    