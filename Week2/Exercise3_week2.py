# Counting words in a file and then create a dictionary reflecting
import string
import gdown

file_path = './Data_June29.txt'
word_count_dict = {}

url = 'https://drive.google.com/uc?id=1a5taZh6aLIH_DRnXcbP-4YVYg0bA29XD'
gdown.download(url, file_path, quiet=False)


def count_word(file_path):
    # Open file and read the content
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            # Eliminate full stops, commands and convert into lower cases
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.replace('-', ' ')
            line = line.lower()

            # Split lines into words
            words = line.split()

            # Count the word in words
            for word in words:
                if (word in word_count_dict):
                    word_count_dict[word] = word_count_dict[word] + 1
                else:
                    word_count_dict[word] = 1

    return word_count_dict


if __name__ == "__main__":
    file_path_ex = "Data_June29.txt"
    print(count_word(file_path_ex))
