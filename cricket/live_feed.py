import feedparser
import grequests
from pprint import pprint

from .score import LiveScore


class LiveFeedParser:
    def __init__(self, rss_url, args):
        self.url = rss_url
        self.debug = args.debug
        self.my_team = args.team

    def get_all_scores(self):
        if self.debug:
            print("Getting all current matches")
        response = feedparser.parse(self.url)
        match_feeds = response.get('entries', [])
        return self._get_scores(match_feeds)

    def get_international_scores(self):
        return [live_score for live_score in self.get_all_scores() if live_score.is_international()]

    def get_my_team_scores(self):
        if self.debug:
            print("Filter to just 'my team'")
        return [live_score for live_score in self.get_all_scores() if live_score.is_my_team_playing(self.my_team)]

    def _get_scores(self, match_feeds):
        live_scores = []
        responses = (grequests.get(match_feed['id'].replace('html', 'json')) for match_feed in match_feeds)
        for response in grequests.map(responses):
            match = response.json()
            if self.debug:
                print("Getting live scores for {}".format(match['description']))
            live_score = LiveScore(match)
            live_scores.append(live_score)
        return live_scores
