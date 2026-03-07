def ft_analytics_dashboard() -> None:
    """
    Processes game data using list, dict, and set comprehensions.
    Generates an analytics dashboard showcasing data transformations,
    filtering, and aggregations.
    """

    players = [
        {
            "name": "alice",
            "score": 2300,
            "achievements": [
                "first_kill", "level_10", "boss_slayer",
                "speed_demon", "perfectionist"
            ],
            "region": "north",
            "active": True
        },
        {
            "name": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_10", "collector"],
            "region": "east",
            "active": True
        },
        {
            "name": "charlie",
            "score": 2150,
            "achievements": [
                "first_kill", "level_10", "speed_demon",
                "boss_slayer", "treasure_hunter", "explorer", "survivor"
            ],
            "region": "central",
            "active": True
        },
        {
            "name": "diana",
            "score": 1500,
            "achievements": ["first_kill"],
            "region": "north",
            "active": False
        }
    ]

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players}
    print(f"Player scores: {player_scores}")

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")

    active_regions = {p["region"] for p in players}
    print(f"Active regions: {active_regions}")

    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achievements = {ach for p in players for ach in p["achievements"]}
    print(f"Unique achievements: {all_achievements}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    print(f"Total players: {total_players}")

    print(f"Total unique achievements: {len(all_achievements)}")

    total_score = sum([p["score"] for p in players])
    average_score = total_score / total_players
    print(f"Average score: {average_score}")

    max_score = max([p["score"] for p in players])
    top_performer = [p for p in players if p["score"] == max_score][0]

    print(f"Top performer: {top_performer['name']} "
          f"({top_performer['score']} points, "
          f"{len(top_performer['achievements'])} achievements)")


if __name__ == "__main__":
    ft_analytics_dashboard()
