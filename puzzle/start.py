#coding = utf-8
#! python3
import puzzle


def game_intro():
	print (
	"This is a 4*4 puzzle game.\n"
	+ "You can move the pieces around the blank piece.\n"
	+ "Please input the site with the style - col raw(e.g. 1 2) if you want to move it \n"
	)

def game_help():
	print(
	"e - exit the game\n"
	+ "h - show this help\n"
	+ "r - restart the game\n"
	+ "s - show the puzzle\n"
	)

def main():	
	puzzle_game = puzzle.Puzzle()
	game_intro()
	game_help()
	print(str(puzzle_game))
	site = raw_input("please input the site: ")
	while "e" <> site:
		if "h" == site:
			game_help()
		elif "r" == site:
			puzzle_game.refresh()
			print(str(puzzle_game))
		elif "s" == site:
			print(str(puzzle_game))
		elif len(site) != 3 or not site[0].isdigit() or not site[2].isdigit() or site[1] <> " ":
			print("please with the correct style")
		elif not puzzle_game.move_block( int(site[0]), int(site[2]) ):
			print("please with the correct site")
		else:
			print(str(puzzle_game))
			if puzzle_game.if_finished():
				print("congratulation!!")
				break	
		site = raw_input("please input the site: ")

if __name__ == "__main__":
    main()