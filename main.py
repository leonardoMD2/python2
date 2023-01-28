import game.main as game
import chars.charts as graph

print("Welcome")
rounds = input("set the plays: ")
game.run_game(int(rounds))
#print(game.results.values(),game.results.keys())
graph.pieChart(game.results.values(),game.results.keys())
