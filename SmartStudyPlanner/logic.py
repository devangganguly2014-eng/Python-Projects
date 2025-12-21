def generate_plan(subjects, total_hours):
    """
    Advanced study plan generator.
    - Converts hours to minutes
    - Distributes time smartly
    - Creates time slots
    """

    # Priority weights
    priority = {
        "weak": 3,
        "medium": 2,
        "strong": 1
    }

    total_minutes = int(total_hours * 60)

    # Calculate total priority points
    total_priority = sum(priority[level] for _, level in subjects)

    plan = []
    current_minute = 0

    time_slots = ["Morning", "Afternoon", "Evening"]

    for index, (subject, level) in enumerate(subjects):
        share = priority[level] / total_priority
        minutes = int(total_minutes * share)

        slot = time_slots[index % len(time_slots)]

        plan.append({
            "subject": subject,
            "level": level,
            "minutes": minutes,
            "slot": slot
        })

        current_minute += minutes

    return plan

