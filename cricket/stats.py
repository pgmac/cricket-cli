import argparse
from .live_feed import LiveFeedParser
from .rankings import IccRankingsParser
from terminaltables import AsciiTable, SingleTable

LIVE_FEED_URL = 'http://static.cricinfo.com/rss/livescores.xml'
PLAYER_RANKINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211270.html'
TEAM_STANDINGS_URL = 'http://www.espncricinfo.com/rankings/content/page/211271.html'


def get_scores(args):
    """
    Get the current scores
    """
    if args.team:
        live_feeds = LiveFeedParser(LIVE_FEED_URL, args).get_my_team_scores()
    else:
        live_feeds = LiveFeedParser(LIVE_FEED_URL, args).get_all_scores()

    # Sort scores to show international scores first
    live_feeds = sorted(live_feeds, key=lambda live_feed: ~live_feed.is_international())
    _print_scores(live_feeds, args)


def _print_scores(live_feeds, args):
    if len(live_feeds) == 0:
        print('No live matches at this time')
        return

    live_scores = []
    for feed in live_feeds:
        # Add the team scores to the display object
        live_scores.append(['Match', feed.description])
        live_scores.append(['Status', feed.status()])
        live_scores.append(['Summary', feed.summary()])
        if feed != live_feeds[-1]:
            live_scores.append([])
    table = SingleTable(live_scores)
    table.inner_row_border = True
    table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    print(table.table)


def get_rankings():
    """
    Get the current player rankings and print them out in a table
    """
    rankings = _get_rankings_parser(PLAYER_RANKINGS_URL).player_rankings()
    for category, ranking in rankings.items():
        table = AsciiTable(ranking, category)
        print(table.table)


def get_standings():
    """
    Get the current standings for teams and print them out in a table
    """
    standings = _get_rankings_parser(TEAM_STANDINGS_URL).team_standings()
    for championship, standing in standings.items():
        table = AsciiTable(standing, championship)
        print(table.table)


def _get_rankings_parser(url):
    return IccRankingsParser(url)


# Based on: https://docs.python.org/2/library/argparse.html
def parse_args():
    """
    Parse the command line arguments
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    subparsers.add_parser('scores', help='Live cricket scores').set_defaults(func=get_scores)
    parser.add_argument("--team", help='Only return matches where this team is playing')
    subparsers.add_parser('rankings', help='ICC player rankings').set_defaults(func=get_rankings)
    subparsers.add_parser('standings', help='ICC team standings').set_defaults(func=get_standings)
    parser.add_argument("--debug", help="Enable debug mode", default=False, action='store_true')
    parser.add_argument("--refresh", help="Refresh scores every x seconds", type=int, default=0)
    parser.add_argument("--series", help="Get live scores for all matches in a series")
    return parser.parse_args()
