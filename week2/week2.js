function task1(){
    function findAndPrint(messages){
        over_17_name = []
        for(const [name,sentence] of Object.entries(messages)){
            // Skip the negative sentences because it is hard to judge
            if(sentence.search("not")!=-1 && sentence.search("n't")!=-1) continue;
            // Check the ages
            if(sentence.search("years old")!=-1){
                tokens = sentence.split(' ')
                for(token of tokens){
                    let number = parseInt(token);
                    // console.log(number);
                    if(number > 17){
                        over_17_name.push(name);
                        break;
                    }
                }
            }
            // Check the role
            else if(sentence.search("college student")!=-1 || sentence.search("university student")!=-1){
                over_17_name.push(name)
            }
            // Check the legal age
            else if(sentence.search("legal age")!=-1){
                over_17_name.push(name)
            }
            // Check the qualification of voting
            else if(sentence.search("vote")!=-1){
                over_17_name.push(name)
            }
        }
        console.log(`[task1] - possible older than 17 years old name : ${over_17_name}`)
    }
    findAndPrint({
        "Bob":"My name is Bob. I'm 18 years old.",
        "Mary":"Hello, glad to meet you.",
        "Copper":"I'm a college student. Nice to meet you.",
        "Leslie":"I am of legal age in Taiwan.",
        "Vivian":"I will vote for Donald Trump next week",
        "Jenny":"Good morning."
    });
}

function task2(){
    function calculateSumOfBonus(data){
        name2bonus = {};
        max_bonus = 10000;
        for(employees_info of Object.values(data)){
            for(employee of employees_info){
                // Bonus :
                //   max_bonus * (performance_gain + salary_gain)
                //   salary_gain : salary/max_bonus
                //   performance_gain : based on different performance
                // Parse salary
                let salary_str = (String(employee["salary"]).split(",")).join('');
                let salary_gain = 0.01*(String(salary_str).search("USD")==-1 ? parseFloat(salary_str) : (parseFloat(String(salary_str).split('USD')[0])*30))/max_bonus;
                // Parse performance
                let performance_gain = 0.4 // Default is 40%
                if(employee["performance"].search("above"))
                    performance_gain = 0.7;
                else if(employee["performance"].search("below"))
                    performance_gain = 0.2;
                // Add name and bonus
                let final_gain = (performance_gain + salary_gain)>1.0 ? 1.0 : (performance_gain + salary_gain);
                name2bonus[employee["name"]] = max_bonus * final_gain;
            }
        }
        for(const [name, bonus] of Object.entries(name2bonus))
            console.log(`[task2] - name = ${name}, bonus : ${bonus}`);
    }
    
    calculateSumOfBonus(
        {
            "employees":[
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
    ); // call calculateSumOfBonus function
}

function task3(){
    function func(...data){
        middle_name_list = []
        middle_name_cnt = {}
        for(const name of data)
            middle_name_list.push(name[1]);
        // Construct the dictionary based on the key : middle name, value : count of middle name
        for(const middle_name of middle_name_list){
            if(middle_name_cnt.hasOwnProperty(middle_name))
                middle_name_cnt[middle_name] += 1;
            else
                middle_name_cnt[middle_name] = 1;
        }
        ans_name = "沒有"
        // Iterate the name list to get the corresponding full name (There is only one full name corresponding to unique middle name)
        for(const[middle_name,value] of Object.entries(middle_name_cnt)){
            if(value==1){
                for(const name of data)
                    if(name[1]==middle_name)
                        ans_name = name
            }
        }
        console.log(`[task3] - name = ${ans_name}`);
    }

    func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
    func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
}

function task4(){
    function getNumber(index){
        let ans = 4*(Math.floor(index/2)+index%2)-Math.floor(index/2);
        console.log(`[task4] - index : ${index}, ans : ${ans}`);
    }
    getNumber(1); // print 4
    getNumber(5); // print 10
    getNumber(10); // print 15
}

function task5(){
    function findIndexOfCar(seats, status, number){
        idx_with_seats = {};
        for(let i=0 ; i<status.length ; i++){
            if(status[i] == 1){
                idx_with_seats[i] = seats[i];
            }
        }
        difference = 2**64-1;
        most_fit_train_index = -1;
        for(const [index,seats_num] of Object.entries(idx_with_seats)){
            if((seats_num - number) >= 0 &&  (seats_num - number) < difference){
                difference = (seats_num - number);
                most_fit_train_index = index;
            }
        }
        console.log(`[task5] - most fitted train index : ${most_fit_train_index}`);
    }
    findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
    findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
    findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
}

task1();
task2();
task3();
task4();
task5();