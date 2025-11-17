def run_mood_checker_ai():
    """
    A simple rule-based AI program that analyzes user input
    to determine a potential mood and offers a response.
    """
    print("🤖 Simple AI Mood Checker is ready.")
    print("Tell me about your day in a short sentence (or type 'exit').")
    print("-" * 40)

    # Define the rules (keywords associated with moods)
    # This dictionary acts as the "knowledge base" for the AI
    rules = {
        "happy": ["great", "good", "wonderful", "fantastic", "love", "awesome"],
        "sad": ["bad", "terrible", "sad", "unhappy", "difficult", "tired"],
        "stressed": ["work", "deadline", "busy", "stress", "pressure", "too much"],
        "confused": ["why", "what", "how", "confused", "question", "don't know"]
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("🤖 Goodbye! Always here if you need to chat.")
            break

        # Tokenize the input into individual words
        words = user_input.split()

        # Track which moods were detected
        detected_moods = []

        # 1. AI Logic: Check input against the rules
        for mood, keywords in rules.items():
            for keyword in keywords:
                if keyword in words:
                    # Add the mood if a matching keyword is found
                    detected_moods.append(mood)
                    # Move to the next mood check once one keyword is found for efficiency
                    break

                    # 2. AI Decision: Generate a response based on the detected mood(s)

        # Remove duplicates from the list of detected moods
        unique_moods = list(set(detected_moods))

        if not unique_moods:
            # Default response if no rules were triggered
            print("AI: That sounds neutral. Can you elaborate?")

        elif len(unique_moods) == 1:
            mood = unique_moods[0]
            if mood == "happy":
                print("AI: That's wonderful! Keep that positive energy going!")
            elif mood == "sad":
                print("AI: I'm sorry to hear that. Maybe take a moment to breathe and rest.")
            elif mood == "stressed":
                print("AI: Try breaking your big tasks into smaller ones. You got this!")
            elif mood == "confused":
                print("AI: It's okay to be confused. Try writing down the core problem.")

        else:
            # Response if multiple conflicting moods are detected
            print("AI: I detect a mixed signal, perhaps feeling a little complex? Tell me more.")

        print("-" * 40)


# Execute the AI program
if __name__ == "__main__":
    run_mood_checker_ai()