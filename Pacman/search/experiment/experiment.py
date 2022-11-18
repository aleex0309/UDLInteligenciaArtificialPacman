from pathlib import Path
import json

from optilog.running import SolverRunner
from optilog.blackbox import ExecutionConstraints


_BASE_DIR = Path(__file__).resolve().parent.parent


SEARCH = {
    "layouts": [
		"bigMaze.lay",
		"contoursMaze.lay",
		"mediumMaze.lay",
		"openMaze.lay",
		"smallMaze.lay",
		"testMaze.lay",
		"tinyMaze.lay"
	],
    "wrappers": ["bfs.sh", "dfs.sh", "ucs.sh",
                 "astar_euclidean.sh", "astar_manhattan.sh"]
}

CORNERS = {
    "layouts": [
        "bigCorners.lay",
        "mediumCorners.lay",
        "tinyCorners.lay",
    ],
    "wrappers": ["ucs_corners.sh", "astar_corners.sh"]
}

FOOD = {
    "layouts": [
        "bigSearch.lay",
        "greedySearch.lay",
        "mediumSearch.lay",
        "oddSearch.lay",
        "openSearch.lay",
        "smallSearch.lay",
        "testSearch.lay",
        "tinySearch.lay",
        "trickySearch.lay",
        "mediumDottedMaze.lay",
        "bigCorners.lay",
        "mediumCorners.lay",
        "tinyCorners.lay",
    ],
    "wrappers": ["ucs_food.sh", "astar_food.sh"]
}


# Change only the following lines
EXPERIMENT_TO_RUN = SEARCH  # Choose from (SEARCH, CORNERS, FOOD)
SUBMITTER = './submit_back.sh'
TIME_LIMIT = 300  # 5 min
SCENARIO_FOLDER = "./scenario"



# DO NOT CHANGE THIS
def create_scenario(path):
    solvers = [_BASE_DIR / "experiment" / "wrappers" / w
               for w in EXPERIMENT_TO_RUN['wrappers']]
    solvers = {
        s.with_suffix("").name: s.resolve().as_posix()
        for s in solvers
    }
    
    tasks = [_BASE_DIR / "layouts" / t
             for t in EXPERIMENT_TO_RUN['layouts']]

    runner = SolverRunner(
        solvers=solvers,
        tasks=tasks,
        scenario_dir=path,
        submit_file=SUBMITTER,
        constraints=ExecutionConstraints(
            wall_time=TIME_LIMIT,
            memory="1G",
        ),
        unbuffer=False,
        runsolver=False,
    )
    runner.generate_scenario()


def main():
    create_scenario(SCENARIO_FOLDER)


if __name__ == "__main__":
    main()

