#!/usr/bin/python3
class Team:
    def __init__(self, team_name, coach_name):
        self.team_name = team_name
        self.coach_name = coach_name

    def display_info(self):
        print("Team name: {}".format(self.team_name))
        print("Coach name: {}".format(self.coach_name))

class FootballTeam(Team):
    def __init__(self, team_name, coach_name, total_touchdowns, quarterback_name):
        super().__init__(team_name, coach_name)
        self.total_touchdowns = total_touchdowns
        self.quarterback_name = quarterback_name

    def display_info(self):
        super().display_info()
        print("Total touchdowns: {}".format(self.total_touchdowns))
        print("Quarterback name: {}".format(self.quarterback_name))

class BasketballTeam(Team):
    def __init__(self, team_name, coach_name, total_three_pointers, star_player):
        super().__init__(team_name, coach_name)
        self.total_three_pointers = total_three_pointers
        self.star_player = star_player

    def display_info(self):
        super().display_info()
        print("Total 3-pointers: {}".format(self.total_three_pointers))
        print("Star player: {}".format(self.star_player))


class BaseballTeam(Team):
    def __init__(self, team_name, coach_name, total_home_runs, pitcher_name):
        super().__init__(team_name, coach_name)
        self.total_home_runs = total_home_runs
        self.pitcher_name = pitcher_name

    def display_info(self):
        super().display_info()
        print("Total home runs: {}".format(self.total_home_runs))
        print("Pitcher name: {}".format(self.pitcher_name))

