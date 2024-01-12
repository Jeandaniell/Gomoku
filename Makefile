.PHONY: all clean convert re

all: pbrain-gomoku-ai

pbrain-gomoku-ai:
	echo '#!/usr/bin/env python3' > pbrain-gomoku-ai
	cat game.py >> pbrain-gomoku-ai
	chmod +x pbrain-gomoku-ai

clean:
	rm -f pbrain-gomoku-ai
	rm -rf dist build __pycache__
	rm -f pbrain-gomoku-ai.exe.spec

convert:
	pyinstaller --onefile pbrain-gomoku-ai
	mv ./dist/pbrain-gomoku-ai ./dist/pbrain-gomoku-ai.exe

re: clean all
  