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

import matplotlib.pyplot as plt

def plot_win_pct_by_site(t, title="Win % by site"):
    p = t["win_pct"]
    se = (p * (1 - p) / t["games"]) ** 0.5   # standard error of a proportion

    fig, ax = plt.subplots(figsize=(5, 4))
    bars = ax.bar(t.index, p, yerr=1.96 * se, capsize=6,
                  color=["#FF5F02", "#000000"])
    ax.axhline(0.5, color="gray", linestyle="--", linewidth=1)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Win percentage")
    ax.set_title(title)

    for bar, w, g in zip(bars, t["wins"], t["games"]):
        ax.text(bar.get_x() + bar.get_width() / 2, 0.05,
                f"{int(w)}-{int(g - w)}", ha="center",
                color="white", fontweight="bold")
    fig.tight_layout()
    return fig