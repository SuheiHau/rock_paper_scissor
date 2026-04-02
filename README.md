# Rock Paper Scissors Game - Flask Version

A fully responsive web-based Rock Paper Scissors game built with Flask. Features the same design as the Streamlit version with a modern, mobile-friendly interface.

## Features

✅ **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
✅ **Session Management** - Tracks wins, losses, and ties across sessions
✅ **Beautiful UI** - Gradient buttons with smooth animations
✅ **Interactive Gameplay** - Real-time score updates
✅ **Mobile Optimized** - Touch-friendly buttons and readable text on all screen sizes

## Installation

1. Make sure you have Flask installed. If not, install it:
```bash
pip install flask
```

2. Ensure you have the `game.py` module in the same directory (it contains the game logic)

## Running the Flask App

From the project directory, run:

```bash
python app_flask.py
```

The app will start on `http://localhost:5000`

Open your browser and navigate to `http://localhost:5000` to play!

## How to Play

1. Click one of the three buttons: **Rock**, **Paper**, or **Scissors**
2. The computer will randomly choose
3. The result will be displayed showing what you and the computer chose
4. Your stats (Wins, Ties, Losses) are updated automatically
5. Click **Reset Stats** to start fresh

## Game Rules

- **Rock** 👊 beats **Scissors** ✌️
- **Scissors** ✌️ beats **Paper** 🤚
- **Paper** 🤚 beats **Rock** 👊

## File Structure

```
Rock_Paper_Scissor/
├── app_flask.py              # Main Flask application
├── game.py                   # Game logic module
├── templates/
│   └── index.html           # HTML template with CSS and JavaScript
└── README_FLASK.md          # This file
```

## Technical Details

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Session Management**: Flask sessions stored in secure cookies
- **Game Logic**: Uses the existing `game.py` module

## Responsive Breakpoints

- **Desktop** (> 768px): Full-width layout with optimal button sizes
- **Tablet** (≤ 768px): Adjusted spacing and font sizes
- **Mobile** (≤ 480px): Compact layout with touch-optimized buttons

## Browser Support

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Notes

- Session data is stored in secure cookies
- Change the `app.secret_key` in `app_flask.py` for production use
- The app runs by default on `0.0.0.0:5000` making it accessible from other devices on your network
