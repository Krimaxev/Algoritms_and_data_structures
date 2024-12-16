from lab_6.utils import read_file_votes, write_file_votes

def process_votes(lines):

    votes = {}
    for line_vote in lines:
        name, count = line_vote.rsplit(maxsplit=1)
        count = int(count)
        if name in votes:
            votes[name] += count
        else:
            votes[name] = count
    return votes

if __name__=="__main__":
    FILE_INPUT = "../txtf/input.txt"
    FILE_OUTPUT = "../txtf/output.txt"

    line = read_file_votes(FILE_INPUT)

    vote = process_votes(line)

    write_file_votes(FILE_OUTPUT, vote)
    print("В файле src задания №5 ЛР №6 код работает исправно")