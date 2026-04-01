from flask import Flask, render_template, request, session, jsonify
from game import validate_choice, get_computer_choice, determine_winner
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this'
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/')
def index():
    if 'wins' not in session:
        session['wins'] = 0
        session['losses'] = 0
        session['ties'] = 0
        session['game_count'] = 0
        session['last_result'] = None
        session['last_user_choice'] = None
        session['last_computer_choice'] = None
        session['last_class'] = None
    
    return render_template('index.html', 
                         wins=session.get('wins', 0),
                         losses=session.get('losses', 0),
                         ties=session.get('ties', 0),
                         last_result=session.get('last_result'),
                         last_user_choice=session.get('last_user_choice'),
                         last_computer_choice=session.get('last_computer_choice'),
                         last_class=session.get('last_class'))

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        return jsonify({'error': 'Invalid choice'}), 400
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    # Update stats
    session['game_count'] = session.get('game_count', 0) + 1
    
    if "You win" in result:
        session['wins'] = session.get('wins', 0) + 1
        result_class = "you-win"
    elif "Computer wins" in result:
        session['losses'] = session.get('losses', 0) + 1
        result_class = "you-lose"
    else:
        session['ties'] = session.get('ties', 0) + 1
        result_class = "tie"
    
    # Store last game info
    session['last_user_choice'] = user_choice
    session['last_computer_choice'] = computer_choice
    session['last_result'] = result
    session['last_class'] = result_class
    session.modified = True
    
    return jsonify({
        'result': result,
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result_class': result_class,
        'wins': session['wins'],
        'losses': session['losses'],
        'ties': session['ties']
    })

@app.route('/reset', methods=['POST'])
def reset():
    session['wins'] = 0
    session['losses'] = 0
    session['ties'] = 0
    session['game_count'] = 0
    session['last_result'] = None
    session['last_user_choice'] = None
    session['last_computer_choice'] = None
    session['last_class'] = None
    session.modified = True
    
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
