def compare_hobbies(person1_hobbies, person2_hobbies):
    hobbies1 = set(person1_hobbies)
    hobbies2 = set(person2_hobbies)
    return {
        "shared": person1_hobbies & person2_hobbies,
        "only_person1": person1_hobbies - person2_hobbies,
        "only_person2": person2_hobbies - person1_hobbies,
    }


print(compare_hobbies({"reading", "coding"}, {"coding", "gaming"}))