import argparse

from live_feed import LiveFeedParser
from terminaltables import SingleTable


def get_scores():
    feed_parser = LiveFeedParser('http://static.cricinfo.com/rss/livescores.xml')
    for score in feed_parser.get_international():
        live_score = [['Match', score.description], ['Status', score.status()], ['Score', score.summary()]]
        table = SingleTable(live_score)
        table.inner_heading_row_border = True
        table.inner_row_border = True
        table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
        print table.table


def get_rankings():
    print 'No rankings available'


def get_standings():
    print 'No standings available'


# Based on: https://docs.python.org/2/library/argparse.html
def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    scores = subparsers.add_parser('scores', help='Live cricket scores')
    scores.set_defaults(func=get_scores)
    rankings = subparsers.add_parser('rankings', help='ICC player rankings')
    rankings.set_defaults(func=get_rankings)
    standings = subparsers.add_parser('standings', help='ICC team standings')
    standings.set_defaults(func=get_standings)
    return parser.parse_args()