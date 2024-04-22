def ask_question(question, options):
    print(question)
    for option in options:
        print(option)
    answer = input("Enter your choice: ").lower()
    return answer

def determine_religion():
    gods_belief = ask_question("How many gods do you believe in?",
                                ["a) None", "b) One", "c) Many"])

    if gods_belief == "a":
        spirituality_belief = ask_question("Do you believe in any kind of spirituality?",
                                           ["a) No", "b) Yes"])
        if spirituality_belief == "a":
            return "Atheist"
        elif spirituality_belief == "b":
            pleasures_denial = ask_question("Should you deny yourself pleasures?",
                                            ["a) Yes", "b) No"])
            if pleasures_denial == "a":
                return "Buddhism"
            elif pleasures_denial == "b":
                return "Spiritual but not religious"

    elif gods_belief == "b":
        god_separate = ask_question("Is God separate from the universe?",
                                    ["a) Yes", "b) No"])
        if god_separate == "a":
            god_interaction = ask_question("Does God interact with the universe?",
                                            ["a) No", "b) Yes"])
            if god_interaction == "a":
                return "Deist"
            elif god_interaction == "b":
                jesus_human = ask_question("Did God become human in Jesus?",
                                           ["a) Yes", "b) No"])
                if jesus_human == "a":
                    return "Christian"
                elif jesus_human == "b":
                    jesus_messiah = ask_question("Is Jesus still the messiah?",
                                                 ["a) No", "b) Yes"])
                    if jesus_messiah == "a":
                        return "Jewish"
                    elif jesus_messiah == "b":
                        return "Muslim"
        elif god_separate == "b":
            worship_idols = ask_question("Can you worship idols?",
                                         ["a) Yes", "b) No"])
            if worship_idols == "a":
                return "Hindu"
            elif worship_idols == "b":
                return "Sikh"

    elif gods_belief == "c":
        reincarnation_belief = ask_question("Do you believe in reincarnation?",
                                            ["a) No", "b) Yes"])
        if reincarnation_belief == "a":
            return "Pagan"
        elif reincarnation_belief == "b":
            return "Hindu"

def main():
    religion = determine_religion()
    print("Based on your beliefs, the religion that best suits you is:", religion)

if __name__ == "__main__":
    main()
