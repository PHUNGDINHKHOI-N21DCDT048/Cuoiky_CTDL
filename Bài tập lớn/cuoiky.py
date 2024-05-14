class Meaning:
    def __init__(self, part_of_speech, definition, example):
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

class Word:
    def __init__(self, word):
        self.word = word
        self.meanings = []

    def add_meaning(self, part_of_speech, definition, example):
        meaning = Meaning(part_of_speech, definition, example)
        self.meanings.append(meaning)

class Dictionary:
    def __init__(self):
        self.words = []

    def add_word(self, newword):
        file = open("dict.txt", "a")
        file.write("{}\n".format(newword))
        file.close()
        # while index < len(self.words) and self.words[index].word < word.word:
        #     index += 1
        # self.words.insert(index, word)

    def remove_word(self, word):
            # Đọc dữ liệu từ tệp văn bản
        with open('dict.txt', 'r') as file:
            data = file.readlines()
        # Chuyển đổi dữ liệu thành một danh sách
        data_list = [line.strip() for line in data]
        count = 0
        exist = -1
        # Tìm kiếm mục trong danh sách
    
        for a in data_list:
            
            # using string find() method
            pos = a.find(word)
            if pos == 0:
                exist = count
            count = count + 1
        
        if exist >= 0 :
            # print('tìm thấy từ trong từ điểnnnn: ', data_list[exist])
            lines = []
            # read file
            with open('dict.txt', 'r') as fp:
                # read an store all lines into list
                lines = fp.readlines()

            # Write file
            with open('dict.txt', 'w') as fp:
                # iterate each line
                for number, line in enumerate(lines):
                    # delete line 5 and 8. or pass any Nth line you want to remove
                    # note list index starts from 0
                    if number not in [int(exist)]:
                            fp.write(line)
        
        else :   
            print('Không thấy từ trong từ điển')

    def lookup(self, word):
        for w in self.words:
            if w.word == word:
                return w.meanings
        return None

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for word in self.words:
                f.write(f"{word.word}:\n")
                for meaning in word.meanings:
                    f.write(f"- {meaning.part_of_speech}: {meaning.definition} ({meaning.example})\n")

    def load_from_file(self, filename):
        self.words = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            word = None
            for line in lines:
                if line.strip() == "":
                    continue
                if ':' in line:
                    word = Word(line.split(':')[0].strip())
                    self.words.append(word)
                elif '-' in line:
                    parts = line.split('-')
                    part_of_speech = parts[1].split(':')[0].strip()
                    definition = parts[1].split(':')[1].split('(')[0].strip()
                    example = parts[1].split('(')[1].split(')')[0].strip()
                    word.add_meaning(part_of_speech, definition, example)

    def trans(self, search_item):
            # Đọc dữ liệu từ tệp văn bản
        with open('dict.txt', 'r') as file:
            data = file.readlines()
        # Chuyển đổi dữ liệu thành một danh sách
        data_list = [line.strip() for line in data]
        count = 0
        exist = -1
        # Tìm kiếm mục trong danh sách
    
        for a in data_list:
            
            # using string find() method
            pos = a.find(search_item)
            if pos == 0:
                exist = count
            count = count + 1
        
        if exist >= 0 :
            print('tìm thấy từ trong từ điểnnnn: ', data_list[exist])
        else :   
            print('Không thấy từ trong từ điển')

    

def main():
    dictionary = Dictionary()

    

    while True:
        print("\nMenu:")
        print("1. Thêm từ mới")
        print("2. Xóa từ")
        print("3. Tra cứu nghĩa của từ")
        print("4. Lưu từ điển vào tệp")
        print("5. Nạp từ điển từ tệp")
        print("6. Kết thúc chương trình")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            word = input("Nhập từ mới: ")
            # pos = input("Phân loại từ (danh từ, động từ, tính từ, ...): ")
            # definition = input("Nghĩa của từ: ")
            # example = input("Ví dụ minh họa: ")
            # new_word.add_meaning(pos, definition, example)
            # print("hhhhhhhhhhhhhhhhhhh", word)
            dictionary.add_word(word)

        elif choice == '2':
            word = input("Nhập từ cần xóa: ")
            dictionary.remove_word(word)

        elif choice == '3':
            word = input("Nhập từ cần tra cứu: ")
            dictionary.trans(word)

        elif choice == '4':
            filename = input("Nhập tên tệp để lưu từ điển: ")
            dictionary.save_to_file(filename)
            print("Đã lưu từ điển thành công.")

        elif choice == '5':
            filename = input("Nhập tên tệp để nạp từ điển: ")
            dictionary.load_from_file(filename)
            print("Đã nạp từ điển thành công từ tệp.")

        elif choice == '6':
            print("Đã kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()








