import random
import psycopg2
class Multiple_Question:
    Question = ""
    AN_A = ""
    AN_B = ""
    AN_C = ""
    AN_D = ""
    Correct_An = 1

class Single_Question:
    Question = ""
    Correct_ANS = True

conn = psycopg2.connect(database="postgres",
                        host="204.216.215.242",
                        user="app",
                        password="emptiness",
                        port="5432")
cur = conn.cursor()
#multiple_row = conn.execute("SELECT * FROM quiz")

cur.execute("INSERT INTO quiz (question, answer1, answer2, answer3, answer4, correct_answer) VALUES (%s, %s, %s, %s, %s, %s)", 
                ("value1", "value2", "value3","value3","value3", "12"))
conn.commit()

List_Multiple = []
List_Single = []
file1 = open("questions.txt", "r")
file2 = open("multiple_ans.txt", "r")
file3 = open("new_multiple_ans.txt", "w")
conta = 0
conta_vuoto = 0
Lines = file2.readlines()
for line in Lines:
    if line.strip():
        new = Multiple_Question()
        conta= conta +1
        #print(line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[1])
        new.Question = line.strip().split('?')[0].strip()+" ?"
        new.AN_A = line.strip().split('?')[1].split('a.')[1].split('b.')[0].strip()
        new.AN_B = line.strip().split('?')[1].split('b.')[1].split('c.')[0].strip()
        new.AN_C = line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[0].strip()
        new.AN_D = line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[0].strip()
        temp = 0
        if(line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[1].strip() == 'a'): temp = 1
        if(line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[1].strip() == 'b'): temp = 2
        if(line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[1].strip() == 'c'): temp = 3
        if(line.strip().split('?')[1].split('b.')[1].split('c.')[1].split('d.')[1].split('Answer:')[1].strip() == 'd'): temp = 4
        new.Correct_An = temp
        #print(new.Correct_An)
        List_Multiple.append(new)
Lines = file1.readlines()
for line in Lines:
    if line.strip():
        new = Single_Question()
        temp = 0
        new.Question = line.strip().split('.')[0].strip()
        new.Correct_ANS = line.strip().split('.')[1].split('(')[1].split(')')[0].strip()
        if(line.strip().split('.')[1].split('(')[1].split(')')[0].strip() == "True"): temp = 1
        if(line.strip().split('.')[1].split('(')[1].split(')')[0].strip() == "False"): temp = 0
        new.Correct_ANS = temp
        List_Single.append(new)
        #print(line.strip().split('.')[1].split('(')[1].split(')')[0].strip()+str(temp))
random.shuffle(List_Multiple)
random.shuffle(List_Single)
#for ele in List_Multiple:
    #cur.execute("INSERT INTO quiz (question, answer1, answer2, answer3, answer4, correct_answer) VALUES (%s, %s, %s, %s, %s, %s)", 
                #(ele.Question, ele.AN_A, ele.AN_B,ele.AN_C,ele.AN_D, ele.Correct_An))
    #conn.commit()

for ele in List_Single:
    cur.execute("INSERT INTO quiz01 (question, correct_answer) VALUES (%s, %s)", 
                (ele.Question, ele.Correct_ANS))
    conn.commit()




