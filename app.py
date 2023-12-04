from flask import Flask, render_template, request
from nhl_api import get_player_stats, parse_player_stats
import logging as log

log.basicConfig(filename='app.log', level=log.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():

    if request.method =='POST':
        player_id = request.form['player_id']
        stats_types = request.form.getlist('stats')

        api_response = get_player_stats(player_id)

        if api_response:
            player_stats = parse_player_stats(api_response, stats_types)
            app.logger.info(f"Player stats retrieved: {player_stats}")

            return render_template('index.html', player_stats=player_stats)
        else:
            app.logger.error("error fetching player stats")
            return "Error fetching player stats"
    
    return render_template('index.html', player_stats=None)

if __name__ == '__main__':
    app.run(debug=True)