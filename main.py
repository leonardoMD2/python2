import game.main as game
import chars.charts as graph

print("Welcome")
rounds = input("set the plays: ")
game.run_game(int(rounds))
graph.pieChart(game.results.values(),game.results.keys())
