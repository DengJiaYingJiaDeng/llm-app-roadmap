# # Day 002: Python data structures and functions

# # 变量和字符串
# def demostrate_variables_and_string()->None:
#     name = "LLM Application"
#     week = 1
#     progress = 2/7
#     completed = True

#     print ("项目名称:" ,name)
#     print ("当前周:" ,week)
#     print ("本周进度:" ,progress)
#     print ("是否已开始:" ,completed)

#     # f-string ：类似java中拼接字符串或String.format  
#     # .2%表示以百分比显示并保留两位小数
#     message = f"{name}: 第{week}周进度为{progress:.2%}"
#     print(message)

#     text = "Python for LLM Application"

#     print("原始文本：",text)
#     print("转为小写：",text.lower())
#     print("转为大写：",text.upper())
#     print("替换内容：",text.replace("Python","java"))
#     print("是否包含LLM：","LLM"in text)
#     print("按空格切分：",text.split())

# # list：可变、有顺序、允许重复 -->接近java中的ArrayList
# def demonstrate_list() -> None:
#     topics = ["Python","Linux","Git"]

#     topics.append("Numpy")
#     topics.insert(1,"Conda")

#     print("\n---list---")
#     print("完整列表：",topics)
#     print("第一个元素：",topics[0])
#     print("最后一个元素：",topics[-1])
#     print("前两个元素：",topics[:2])
#     print("从第二个开始：",topics[1:])
#     print("每隔一个取一个：",topics[::2])

#     topics.remove("Conda")
#     removed_topic = topics.pop()

#     print("删除后的列表：",topics)
#     print("pop删除的元素：",removed_topic)

# tuple ：不可变，有顺序
# def demonstrate_tuple() -> None:
#     python_version = (3,11,15)

#     major,minor,patch = python_version

#     print("\n---tuple---")
#     print("完整版本：", python_version)
#     print("主版本",major)
#     print("次版本：",minor)
#     print("补丁版本：",patch)

# # dict:键值对 --> 接近java中的HashMap
# def demonstrate_dict() -> None:
#     environment = {
#         "python":"3.11.15",
#         "git":"2.34.1",
#         "editor":"VS Code"
#     }

#     environment["virtual_env"] = "llm-app"
#     environment["editor"] = "VS Code 1.131.0"

#     print("\n---dict---")
#     print("完整字典：", environment)
#     print("Python版本",environment["python"])
#     print("操作系统：",environment.get("os","Ubuntu"))

#     print("所有键：",environment.keys())
#     print("所有值：",environment.values())

#     for key,value in environment.items():
#         print(f"{key}:{value}")

# # set:无重复元素集合
# def demonstrate_set()->None:
#     technologies = {"Python","Git","Linux","Python"}
#     backend_technologies = {"Python","Java","PostgreSQL"}

#     print("\n---set---")
#     print("自动去重：", technologies)
#     print("交集:",technologies & backend_technologies)
#     print("并集：",technologies | backend_technologies)
#     print("差集：",technologies - backend_technologies)

#     technologies.add("Docker")
#     technologies.discard("Git")

#     print("修改后的集合：",technologies)

# def exercise_01_string_processing() -> None:

#     text = "Python,Java,Git,Linux"

#     for s in text.strip().split(','):
#         print(s)


# def exercise_02_slicing() -> None:

#     numbers = [1,2,3,4,5,6,7,8,9,10]

#     print(numbers[:3])
#     print(numbers[7:])
#     print(numbers[1::2])

#     new_nums = list(reversed(numbers))
#     print(new_nums)

# def exercise_03_remove_duplicates() -> None:
#     languages = ["Python","Java","Python","C++","Java","Go"]

#     print(set(languages))

#     result = []

#     for s in languages:
#         if s not in result:
#             result.append(s)
#     print(result)



# def exercise_04_score_statics() -> None:
#     score = {
#         "Alice":86,
#         "Bob":92,
#         "Charlie":78,
#         "David":95
#     }

#     max_score = max(score.values())
#     top_student = [name for name,s in score.items() if s == max_score]
#     print(top_student)

#     score_list = list(score.values())
#     avg = sum(score_list)/len(score_list)
#     print(f"平均分:{avg:.2f}")

#     above_90 = [name for name,s in score.items() if s >= 90]
#     print(above_90)



# def exercise_05_set_operations() -> None:

#     java_skills = {"Java","Mybatis","Git","SQL"}
#     ai_skills = {"Python","Git","SQL","PyTorch"}

#     print(java_skills & ai_skills)
#     print(java_skills - ai_skills)
#     print(java_skills | ai_skills)


# # 默认参数
# def greet(name:str,message:str = "Hello") -> str:
#     return f"{message},{name}"

# def demostrate_default_parameter()->None:

#     print("\n ---default parameter ---")
#     print(greet("Tom"))
#     print(greet(
#         "Jerry",
#         "Good morning"
#     ))


# # 可变参数 *args
# def calculate_total(*numbers:int) ->int:
#     return sum(numbers)

# def demonstrate_args() -> None:
#     print("\n ---args---")

#     result = calculate_total(10,20,30)

#     print(result)


# # 关键字参数 **kwargs :类似Java Map参数
# def create_user(**info:str) -> dict:
#     return info

# def demonstrate_kwargs() -> None:
#     print("\n --- kwargs ---")

#     user = create_user(
#         name = "Alice",
#         role = "Developer",
#         lever = "Junior"
#     )

#     print(user)

# # lambda匿名函数
# def demonstrate_lambda() -> None:
#     print("\n --- lambda ---")
#     numbers = [5,2,9,1]

#     sorted_numbers = sorted(
#         numbers,
#         key = lambda x:x
#     )

#     print(sorted_numbers)

#     students = [
#         {
#             "name":"Tom",
#             "score":90
#         },
#         {
#             "name":"Jerry",
#             "score":80
#         }
#     ]

#     result = sorted(
#         students,
#         key = lambda s:s["score"],

#         # reverse = false 升序；reverse = True ,降序
#         reverse=True
#     )

#     print(result)


def exercise06()-> None:
    count = {}

    lines = [
        "hello word",
        "hello python"
        "python llm"
    ]

    for line in lines:
        words = line.split()
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    for k,v in count.items():
        print(f"{k}:{v}")





if __name__ == "__main__":
    # demostrate_variables_and_string()
    # demonstrate_list()
    # demonstrate_tuple()
    # demonstrate_dict()
    # demonstrate_set()

    # exercise_01_string_processing()
    # exercise_02_slicing()
    # exercise_03_remove_duplicates()
    # exercise_04_score_statics()
    # exercise_05_set_operations()
    
    # demostrate_default_parameter()

    # demonstrate_args()

    # demonstrate_kwargs()

    # demonstrate_lambda()

    exercise06()