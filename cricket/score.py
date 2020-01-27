from collections import OrderedDict


class LiveScore:
    def __init__(self, match_details):
        self.description = match_details['description']
        self.live = match_details['live']
        self.details = match_details['match']
        self.innings = match_details['innings']
        self.series = match_details['series']

    def is_international(self):
        return True if self.details.get('international_class_card') else False

    def is_my_team_playing(self, my_team):
        return True if self.details.get('team1_name') == my_team or self.details.get('team2_name') == my_team else False

    def summary(self):
        summary = self._innings_summary()
        summary.append(self.details.get('current_summary') or '')
        return '\n'.join(summary) if filter(None, summary) else 'N/A'

    def status(self):
        if self.details['present_datetime_gmt'] <= self.details['start_datetime_gmt']:
            return self.live['status']
        else:
            if self.details['result'] == '0' and self.live['innings']['innings_number'] == '2':
                return "{}\nRequired Run Rate: {}\nCurrent Run Rate: {}".format(self.live['status'], self.live['innings']['required_run_rate'], self.live['innings']['run_rate'])
            else:
                return self.live['status']
        # return self.live['status']
        # result, result_name, live_status, match_status, rain_rule, reduced

    def _innings_summary(self):
        innings_summary = []
        for team, scores in self._get_innings_scores().items():
            innings_summary.append('{} - {}'.format(team, ' & '.join(scores)))
        return innings_summary

    def _get_innings_scores(self):
        innings_scores = OrderedDict()
        team_names = self._get_team_names()
        for inning in self.innings:
            if inning['innings_number'] != "0":
                score = inning['wickets'] + '/' + inning['runs']
                team = team_names[inning['batting_team_id']]
                innings_scores.setdefault(team, []).append(score)
        return innings_scores

    def _get_team_names(self):
        match = self.details
        return {
            match['team1_id']: match['team1_name'],
            match['team2_id']: match['team2_name'],
        }

    def location(self):
        return self.details['ground_name']
