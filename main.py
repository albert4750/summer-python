import csv
import os
import sys


def main():
    playerCount = -1
    playerData = []
    info = []
    file = open("台服隊友檢閱插件.html", mode="r", encoding="utf-8")
    for line in file:
        if "class=\"player-container\"" in line:
            info.append(playerData)
            playerData = []

        if "class=\"percentage\"" in line:
            playerData.append(line)

    for data in info:
        for line in data:
            print(line)
        print()


if __name__ == "__main__":
    main()
