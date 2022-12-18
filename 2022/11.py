import copy
import helpers
import re

def get_input_data():
    MONKEY_STARTUP_ITEMS = r"Starting items:(.*)\n"
    MONKEY_OPERATIONS = r"Operation: new = (.*)\n"
    MONKEY_TESTS = r"Test: divisible by (.*)\n"
    MONKEY_TESTS_TRUE = r"If true: throw to monkey (.*)\n"
    MONKEY_TESTS_FALSE = r"If false: throw to monkey (.*)\n"

    source_filename = helpers.get_input_filename(__file__)
    source_handler = open(source_filename, 'r')
    source_data = source_handler.read()
    result = []

    startup_items = re.findall(MONKEY_STARTUP_ITEMS, source_data, re.M)
    operations = re.findall(MONKEY_OPERATIONS, source_data, re.M)
    tests = re.findall(MONKEY_TESTS, source_data, re.M)
    tests_true = re.findall(MONKEY_TESTS_TRUE, source_data, re.M)
    tests_false = re.findall(MONKEY_TESTS_FALSE, source_data, re.M)
    number_of_monkeys = len(startup_items)

    # Always assuming that input has the right structure
    for monkey in range(number_of_monkeys):
        monkey_items = list(map(int, startup_items[monkey].split(',')))
        result.append({
            "items": monkey_items,
            "operation": operations[monkey],
            "test": int(tests[monkey]),
            "tests_true": int(tests_true[monkey]),
            "tests_false": int(tests_false[monkey]),
            "inspected": 0,
        })

    return result

def execute_updates(data, number_of_rounds, div_factor, mod_factor):
    updated_data = copy.deepcopy(data)
    for round in range(number_of_rounds):
        #print(f"Processing round {round}")
        for index in range(len(updated_data)):
            monkey = updated_data[index]
            for item in monkey["items"]:
                item_final_worry_level = eval(monkey["operation"].replace("old", str(item))) // div_factor
                test_result = item_final_worry_level % monkey["test"] == 0
                destination_monkey = monkey["tests_" + ("true" if test_result else "false")]

                # So, what we want is to reduce the worry level BUT without affecting the other divisors
                # otherwise calculation won't work. A possibility is to do the modulus by the lest common
                # multiple divisor. BUT all the divisors are prime numbers, so the LCD is the multiplication
                # of all of them, and this is what we do.
                item_final_worry_level = item_final_worry_level % mod_factor if mod_factor else item_final_worry_level
                updated_data[destination_monkey]["items"].append(item_final_worry_level)
                monkey["inspected"] += 1
            monkey["items"] = []

        #print([updated_data[i]["inspected"] for i in range(len(updated_data))])
    return updated_data

def calculate_monkey_business_level(data):
    inspections = []
    for monkey in data:
        inspections.append(monkey["inspected"])
    inspections = sorted(inspections)

    # print(inspections)
    return inspections[-1] * inspections[-2]

def extract_div_factor(data):
    factor = 1
    for monkey in data:
        factor *= monkey["test"]
    return factor

def main():
    data = get_input_data()
    """
    updated_data = execute_updates(data, 20, div_factor=3, mod_factor=None)
    monkey_business_level = calculate_monkey_business_level(updated_data)
    print(f"Question 1's answer is {monkey_business_level}")
    """

    mod_factor = extract_div_factor(data)
    updated_data = execute_updates(data, 10000, div_factor=1, mod_factor=mod_factor)
    monkey_business_level = calculate_monkey_business_level(updated_data)
    print(f"Question 2's answer is {monkey_business_level}")

if __name__ == "__main__":
    main()
