from os import getcwd, chdir
from json import load, dump

if __name__ == '__main__':
	chdir("rstrnt")
	with open('./static/menu.json') as jsonfile: menu = sorted(load(jsonfile), key = lambda item: item['name'])
	with open('./static/menu.json', 'w+') as jsonfile: dump(menu, jsonfile)
	