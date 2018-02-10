import re


def word_count(file_path):
	with open(file_path) as f:
		text = f.read()
		print(len(re.findall('\w+',text)))


if __name__ == "__main__":
	file_path = 'english.txt'
	word_count(file_path)