class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        return [p for p in self._players if p.team == team_name]

    def top(self, how_many):
        # pisteet = goals + assists (olettaen Player.points on jo olemassa
        # muutoi p.goals + p.assists)
        sorted_players = sorted(self._players, key=lambda p: p.points, reverse=True)
        return sorted_players[:how_many]  # ei mene listan yli
