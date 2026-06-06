def Z36116(Z36116K1, Z36116K2, Z36116K3, Z36116K4, Z36116K5):
    import random
    number_of_generations = 0

    VALID_CHARS = list(dict.fromkeys(Z36116K5))
    TARGET_LIST = list(Z36116K4)
    if not VALID_CHARS:
        raise ValueError("There must be at least one permitted character.")
    if not set(TARGET_LIST).issubset(VALID_CHARS):
        raise ValueError("The target string has at least one character that is not in the list of permitted characters.")
    if Z36116K2 <= 0:
        raise ValueError("The chance of a mutation must be greater than zero.")
    if Z36116K2 > 1:
        raise ValueError("The chance of a mutation must be less than or equal to one.")
    if Z36116K3 < 1:
        raise ValueError("The number of copies must be at least one.")
    if not Z36116K4:
        raise ValueError("The target string must not be empty.")
    
    def string_distance(a, b):
        return sum(a != b for a, b in zip(a, b))

    def generate_random_string(Z36116K1): 
        random.seed(Z36116K1)
        rand_string = ""
        for i in range(len(Z36116K4)):
            rand_string = rand_string + random.choice(VALID_CHARS)
        return rand_string

    def copy_once(string, Z36116K2):
        new_string = string
        for i in range(len(new_string)):
            if random.random() < Z36116K2:
                new_string = new_string[:i] + random.choice(VALID_CHARS) + new_string[(i + 1):]
        return new_string

    def copy_multiple_times(string, Z36116K2, Z36116K3):
        copies = []
        for i in range(Z36116K3):
            copies.append(copy_once(string, Z36116K2))
        return copies

    def select(string_list):
        list_of_distances = []
        for s in string_list:
            dist = string_distance(s, Z36116K4)
            list_of_distances.append(dist)
        best_dist = min(list_of_distances)
        index = list_of_distances.index(best_dist)
        selected_string = string_list[index]
        print(selected_string)
        return selected_string
    
    def reach_target(string, Z36116K2, Z36116K3):
        new_string = select(copy_multiple_times(string, Z36116K2, Z36116K3))
        while not new_string == Z36116K4:
            nonlocal number_of_generations
            number_of_generations += 1
            newer_string = select(copy_multiple_times(new_string, Z36116K2, Z36116K3))
            new_string = newer_string
        return number_of_generations
    
    return reach_target(generate_random_string(Z36116K1), Z36116K2, Z36116K3)
