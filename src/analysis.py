def home_away_record(games):
    """Count wins and losses at home vs. away."""
    return games.groupby(["Home_Away", "W/L"]).size()

def clean_results(games):
    """Keep completed games and add 'won' and 'site' columns."""
    df = games[games["W/L"].str[0].isin(["W", "L"])].copy()
    df["won"] = df["W/L"].str.startswith("W")
    df["site"] = df["Home_Away"].map({"Home": "Home", "@": "Away"})
    return df

def win_pct_by_site(games):
    df = clean_results(games)
    return df.groupby("site")["won"].agg(wins="sum", games="count", win_pct="mean")