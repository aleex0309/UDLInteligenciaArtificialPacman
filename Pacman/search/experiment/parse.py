from optilog.running import parse_scenario, ParsingInfo


parsing_info = ParsingInfo()
parsing_info.add_filter(
    name="cost", cast_to=int,
    expression=r"Path found with total cost of (\d+)",
)
parsing_info.add_filter(
    name="time", cast_to=float,
    expression=r"Path found with total cost of \d+ in (.*) seconds",
)
parsing_info.add_filter(
    name="expanded", cast_to=int,
    expression=r"Search nodes expanded: (\d+)",
)
parsing_info.add_filter(
    name="score", cast_to=int,
    expression=r"(?:Pacman died! )?Score: (-?\d+)",
)


df = parse_scenario("./scenario", parsing_info)
df = df.drop(["seed"], axis=1, level=1)

print("\n======================================")
print("Times:")
print(df.xs("time", level=1, axis=1))

print("\n======================================")
print("Cost of the path:")
print(df.xs("cost", level=1, axis=1))

print("\n======================================")
print("Expanded nodes:")
print(df.xs("expanded", level=1, axis=1))

print("\n======================================")
print("Score:")
print(df.xs("score", level=1, axis=1))
