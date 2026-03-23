#!/usr/bin/env python3


def get_players() -> list[dict]:
    return [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": [
                "first_kill", "level_10", "boss_slayer",
                "speed_demon", "collector"
            ]
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": [
                "first_kill", "level_10", "collector"
            ]
        },
        {
            "name": "charlie",
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": [
                "level_10", "boss_slayer", "treasure_hunter",
                "strategist", "perfectionist", "speed_demon", "survivor"
            ]
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": [
                "first_kill", "team_player", "support_master", "healer"
            ]
        }
    ]


def get_events() -> list[dict]:
    return [
        {"player": "alice", "achievement": "first_kill"},
        {"player": "bob", "achievement": "collector"},
        {"player": "charlie", "achievement": "boss_slayer"},
        {"player": "alice", "achievement": "speed_demon"},
        {"player": "diana", "achievement": "team_player"},
        {"player": "charlie", "achievement": "strategist"}
    ]


def list_examples(
    players: list[dict]
) -> tuple[list[str], list[int], list[str]]:
    high_sc: list[str] = [
        player["name"] for player in players if player["score"] > 2000
    ]
    dbl_sc: list[int] = [player["score"] * 2 for player in players]
    act_players: list[str] = [
        player["name"] for player in players if player["active"]
    ]
    return high_sc, dbl_sc, act_players


def dict_examples(
    players: list[dict]
) -> tuple[dict[str, int], dict[str, int], dict[str, int]]:
    player_sc: dict[str, int] = {
        player["name"]: player["score"] for player in players
    }
    ach_counts: dict[str, int] = {
        player["name"]: len(player["achievements"]) for player in players
    }
    sc_categories: dict[str, int] = {
        "high": len([player for player in players if player["score"] >= 2200]),
        "medium": len(
            [player for player in players if 1900 <= player["score"] < 2200]
        ),
        "low": len([player for player in players if player["score"] < 1900]),
    }
    return player_sc, sc_categories, ach_counts


def set_examples(
    players: list[dict], events: list[dict]
) -> tuple[set[str], set[str], set[str]]:
    unique_players: set[str] = {event["player"] for event in events}
    unique_ach: set[str] = {
        achievement
        for player in players
        for achievement in player["achievements"]
    }
    act_regions: set[str] = {
        player["region"] for player in players if player["active"]
    }
    return unique_players, unique_ach, act_regions


def combined_analysis(
    players: list[dict], unique_ach: set[str]
) -> tuple[int, int, float, dict]:
    total_players: int = len(players)
    total_unique_ach: int = len(unique_ach)
    avg_sc: float = sum(
        [player["score"] for player in players]
    ) / len(players)
    top_player: dict = max(players, key=lambda player: player["score"])
    return total_players, total_unique_ach, avg_sc, top_player


def main() -> None:
    players: list[dict] = get_players()
    events: list[dict] = get_events()

    print("=== Game Analytics Dashboard ===")
    print()

    high_sc, dbl_sc, act_players = list_examples(players)
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_sc}")
    print(f"Scores doubled: {dbl_sc}")
    print(f"Active players: {act_players}")
    print()

    player_sc, sc_categories, ach_counts = dict_examples(
        players
    )
    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_sc}")
    print(f"Score categories: {sc_categories}")
    print(f"Achievement counts: {ach_counts}")
    print()

    unique_players, unique_ach, act_regions = set_examples(
        players, events
    )
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_ach}")
    print(f"Active regions: {act_regions}")
    print()

    total_players, total_unique_ach, avg_sc, top_player = combined_analysis(
        players, unique_ach
    )
    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_sc:.1f}")
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, "
        f"{len(top_player['achievements'])} achievements)"
    )


if __name__ == "__main__":
    main()
