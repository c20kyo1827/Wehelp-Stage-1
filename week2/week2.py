# Unit test
# Logging interface
# HW

def task1():
    def find_and_print(messages):
        over_17_name = []
        for name,sentence in messages.items():
            # Skip the negative sentences because it is hard to judge
            if sentence.find("not")!=-1 and sentence.find("n't")!=-1 : continue
            # Check the ages
            if sentence.find("years old")!=-1:
                tokens = sentence.split()
                for token in tokens:
                    if token.isdigit() and int(token) > 17:
                        over_17_name.append(name)
            # Check the role
            elif sentence.find("college student")!=-1 or sentence.find("university student")!=-1:
                over_17_name.append(name)
            # Check the legal age
            elif sentence.find("legal age")!=-1:
                over_17_name.append(name)
            # Check the qualification of voting
            elif sentence.find("vote")!=-1:
                over_17_name.append(name)

        print("[{step}] - possible older than 17 years old name : {over_17_name}".format(step="task1", over_17_name=over_17_name))
    find_and_print({
        "Bob":"My name is Bob. I'm 18 years old.",
        "Mary":"Hello, glad to meet you.",
        "Copper":"I'm a college student. Nice to meet you.",
        "Leslie":"I am of legal age in Taiwan.",
        "Vivian":"I will vote for Donald Trump next week",
        "Jenny":"Good morning."
    })

def task2():
    def calculate_sum_of_bonus(data):
        name2bonus = {}
        max_bonus = 10000
        for employees_info in data.values():
            for employee in employees_info:
                # Bonus :
                #   max_bonus * (performance_gain + salary_gain)
                #   salary_gain : salary/max_bonus
                #   performance_gain : based on different performance

                # Parse salary
                salary_str = "".join(str(employee["salary"]).split(","))
                salary_gain = 0.01*(float(salary_str) if str(salary_str).find("USD")==-1 else float(salary_str.split("USD")[0])*30) \
                            /max_bonus
                # Parse performance
                performance_gain = 0.4 # Default is 20%
                if employee["performance"].find("above"):
                    performance_gain = 0.7
                elif employee["performance"].find("below"):
                    performance_gain = 0.2
                # Add name and bonus
                final_gain = 1.0 if (performance_gain + salary_gain)>1.0 else (performance_gain + salary_gain)
                name2bonus[employee["name"]] = max_bonus * final_gain
                # Sanity check
                assert(name2bonus[employee["name"]] <= max_bonus)
        # Print
        for name,bonus in name2bonus.items():
            print("[{step}] - name : {name}, bonus : {bonus}".format(step="task2", name=name, bonus=bonus))

    calculate_sum_of_bonus(
    {
        "employees":
        [
            {
                "name":"John",
                "salary":"1000USD",
                "performance":"above average",
                "role":"Engineer"
            },
            {
                "name":"Bob",
                "salary":60000,
                "performance":"average",
                "role":"CEO"
            },
            {
                "name":"Jenny",
                "salary":"50,000",
                "performance":"below average",
                "role":"Sales"
            }
        ]
    }
    ) # call calculate_sum_of_bonus function

def task3():
    def func(*data):
        middle_name_list = [name[1] for name in data]
        middle_name_cnt = {}
        # Construct the dictionary based on the key : middle name, value : count of middle name
        for middle_name in middle_name_list:
            if middle_name in middle_name_cnt:
                middle_name_cnt[middle_name] += 1
            else:
                middle_name_cnt[middle_name] = 1
        ans_name = "沒有"
        # Iterate the name list to get the corresponding full name (There is only one full name corresponding to unique middle name)
        for middle_name,value in middle_name_cnt.items():
            if value==1:
                for name in data:
                    if name[1]==middle_name:
                        ans_name = name
        print("[{step}] - name = {ans_name}".format(step="task3", ans_name=ans_name))
    func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

def task4():
    def get_number(index):
        # 0 4 3 7 6 10 9 13 12 16 15
        print("[{step}] - index : {index}, ans : {ans}".format(step="task4", index=index, ans=4*(int(index/2)+index%2)-int(index/2)))
    get_number(1) # print 4
    get_number(5) # print 10
    get_number(10) # print 15

def task5():
    def find_index_of_car(seats, status, number):
        # Construct a list with available seat => (index, value)
        idx_with_seats = [(index, seats[index]) for index, value in enumerate(status) if value==1]
        # Check 
        #   1. the available seats is larger thant the required number
        #   2. the difference is the smallest(most fitted)
        difference = 2**64-1
        most_fit_train_index = -1
        for index,seats_num in idx_with_seats:
            if (seats_num - number) >= 0 and (seats_num - number) < difference:
                difference = (seats_num - number)
                most_fit_train_index = index
        print("[{step}] - most fitted train index : {most_fit_train_index}".format(step="task5", most_fit_train_index=most_fit_train_index))
        
    find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
    find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
    find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2

if __name__=="__main__":
    print("="*100)
    task1()
    print("="*100)
    task2()
    print("="*100)
    task3()
    print("="*100)
    task4()
    print("="*100)
    task5()