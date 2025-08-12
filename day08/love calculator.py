def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_count=0
    love_count=0
    combined_names = name1 + name2
    for letters in combined_names:
        if letters in "true":
            true_count+=1
        if letters in "love":
            love_count+=1 
    love_score = str(true_count) + str(love_count)
    print(f"Love Score = {love_score}" )
calculate_love_score("Kanye West", "Kim Kardashian")
