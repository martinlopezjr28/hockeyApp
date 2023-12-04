from flask import Flask, render_template, request
from nhl_api import get_player_stats, parse_player_stats
import logging as log
from flask_sqlalchemy import SQLAlchemy

log.basicConfig(filename='app.log', level=log.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hockey_stats.db'
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'Players'
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    plus_minus = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def home():

    if request.method =='POST':
        player_id = request.form['player_id']
        stats_types = request.form.getlist('stats')

        api_response = get_player_stats(player_id)

        if api_response:
            player_stats = parse_player_stats(api_response, stats_types)

            new_player = Player(
                player_id=player_id,
                name="Name",
                goals=player_stats.get('goals', None),
                assists=player_stats.get('assists', None),
                plus_minus=0,
                team_id=0
            )

            db.session.add(new_player)
            db.session.commit()

            app.logger.info(f"Player stats retrieved: {player_stats}")

            return render_template('index.html', player_stats=player_stats)
        else:
            app.logger.error("error fetching player stats")

            return "Error fetching player stats"
        
    return render_template('index.html', player_stats=None)

if __name__ == '__main__':
    app.run(debug=True, threaded=False)