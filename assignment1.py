file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

def solution(file, target):
    item = []
    for item in file:
        if item == target:
            return "HOORAH"
        elif type(item) == list:
            found = solution(item, target)
            if found:
                return found




print(solution(file_system, target))