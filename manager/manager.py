import os
import dotenv
from espn_api.basketball import *

def main():
    l = League(
        2096137612,
        2023,
        os.getenv("ESPN_S2_COOKIE"),
        os.getenv("SWID_COOKIE"),
        debug=True
    )

    print(l.get_team_data(1))

if __name__ == "__main__":
    main()