with open('1.txt', 'r', encoding='utf-8') as f1:
    lines1 = f1.readlines()
    # print(len(lines1))

with open('2.txt', 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()
    # print(len(lines2))

with open('3.txt', 'r', encoding='utf-8') as f3:
    lines3 = f3.readlines()
    # print(len(lines3))

with open('4res.txt', 'w', encoding='utf-8') as f4:
    if len(lines1) < len(lines2) < len(lines3):
        f4.write(f1.name + '\n')
        f4.write(str(len(lines1)) + '\n')
        for line in lines1:
            f4.write(line)
        f4.write('\n')
        f4.write(f2.name + '\n')
        f4.write(str(len(lines2)) + '\n')
        for line in lines2:
            f4.write(line)
        f4.write('\n')
        f4.write(f3.name + '\n')
        f4.write(str(len(lines3)) + '\n')
        for line in lines3:
            f4.write(line)
        f4.write('\n')
    elif len(lines2) < len(lines1) < len(lines3):
        f4.write(f2.name + '\n')
        f4.write(str(len(lines2)) + '\n')
        for line in lines2:
            f4.write(line)
        f4.write('\n')
        f4.write(f1.name + '\n')
        f4.write(str(len(lines1)) + '\n')
        for line in lines1:
            f4.write(line)
        f4.write('\n')
        f4.write(f3.name + '\n')
        f4.write(str(len(lines3)) + '\n')
        for line in lines3:
            f4.write(line)
        f4.write('\n')
    elif len(lines3) < len(lines1) < len(lines2):
        f4.write(f3.name + '\n')
        f4.write(str(len(lines3)) + '\n')
        for line in lines3:
            f4.write(line)
        f4.write('\n')
        f4.write(f1.name + '\n')
        f4.write(str(len(lines1)) + '\n')
        for line in lines1:
            f4.write(line)
        f4.write('\n')
        f4.write(f2.name + '\n')
        f4.write(str(len(lines2)) + '\n')
        for line in lines2:
            f4.write(line)
        f4.write('\n')
    else:
        f4.write(f3.name + '\n')
        f4.write(str(len(lines3)) + '\n')
        for line in lines3:
            f4.write(line)
        f4.write('\n')
        f4.write(f2.name + '\n')
        f4.write(str(len(lines2)) + '\n')
        for line in lines2:
            f4.write(line)
        f4.write('\n')
        f4.write(f1.name + '\n')
        f4.write(str(len(lines1)) + '\n')
        for line in lines1:
            f4.write(line)
        f4.write('\n')