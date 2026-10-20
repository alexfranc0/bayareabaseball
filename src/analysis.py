def home_away_record(games):
    """Count wins and losses at home vs. away."""
    return games.groupby(["Home_Away", "W/L"]).size()