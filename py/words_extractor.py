import os
import re


class Words_Extractor:

    __output = []
    __raw_text = ""

    def __init__(self):
        __output = []
        __raw_text = ""

    def __make_item(self, key, value):
        # create one output line
        self.__output.append(str(value) + "\t : \t" + str(key).lower() + "\n")

    def __calc_key(self, elem):
        return elem[1]

    def __load_file(self, filename):
        # load the file
        in_file = open(filename, 'r')
        self.__raw_text = in_file.read()
        in_file.close()

    def __process_data(self):
        # remove all new line characters: \n and \N
        raw_text_without_n = self.__raw_text.replace(
            '\n', ' ').replace('\\N', ' ')
        # find all words at least 3 characteres long
        result = re.findall("[a-zA-Z]{3,}", raw_text_without_n)
        # count the number of occurences of each word
        unsorted_words = {}
        for word in result:
            if not word in unsorted_words:
                unsorted_words[word] = 0
            value = unsorted_words[word]
            unsorted_words[word] = value + 1
        # [make_item(key, value) for (key, value) in sorted(
        #    dict.items(), reverse=False, key=calc_key)]
        # sort words
        sorted_words = dict(
            sorted(unsorted_words.items(), key=lambda x: (x[1], x[0]), reverse=False))
        # create output items: number of occurences : word
        [self.__make_item(key, value) for (key, value) in sorted_words.items()]

    def __save_file(self, filename):
        # make sure the subdirectories in output folder exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        # save the file
        out_file = open(filename, 'w')
        out_file.write(''.join(self.__output))
        out_file.close()

    def extract(self, file_input, file_output):
        self.__raw_text = ""
        self.__output = []
        print('Loading ' + file_input)
        self.__load_file(file_input)
        print('Processing... ')
        self.__process_data()
        print('Saving ' + file_output)
        self.__save_file(file_output)
