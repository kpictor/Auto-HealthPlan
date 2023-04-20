def strength_training_plan(squat_1rm, bench_1rm, deadlift_1rm):
    main_exercises = {
        'Lower Body': [{'name': 'Squat', '1rm': squat_1rm}, {'name': 'Deadlift', '1rm': deadlift_1rm}],
        'Upper Body': [{'name': 'Bench Press', '1rm': bench_1rm}]
    }

    accessory_exercises = {
        'Lower Body': [
            {'name': 'Romanian Deadlift', 'sets': 3, 'reps': 10},
            {'name': 'Leg Press', 'sets': 3, 'reps': 12},
            {'name': 'Plank', 'sets': 3, 'reps': 1, 'unit': 'min'},
        ],
        'Upper Body': [
            {'name': 'Weighted Chin-ups', 'sets': 3, 'reps': 6},
            {'name': 'Dumbbell Shoulder Press', 'sets': 3, 'reps': 10},
            {'name': 'Dumbbell Rows', 'sets': 3, 'reps': 10},
            {'name': 'Close-grip Bench Press', 'sets': 3, 'reps': 10},
            {'name': 'Barbell Rows', 'sets': 3, 'reps': 10},
            {'name': 'Dumbbell Bicep Curls', 'sets': 3, 'reps': 12},
        ]
    }

    weeks = [
        {'week': [1, 2], 'intensity': 0.7, 'reps': 8},
        {'week': [3], 'intensity': 0.75, 'reps': 6},
        {'week': [4], 'intensity': 0.85, 'reps': 4},
        {'week': [5], 'intensity': 0.5, 'reps': 5},
    ]

    for week_num in range(1, 6):
        week = next(w for w in weeks if week_num in w['week'])
        print(f"Week {week_num}")

        for day, exercises in main_exercises.items():
            print(f"{day} Exercises:")
            for exercise in exercises:
                weight = round(exercise['1rm'] * week['intensity'] / 2.5) * 2.5
                print(f"{exercise['name']}: 4 sets x {week['reps']} reps @ {weight} kg")
            print("\n")

            for exercise in accessory_exercises[day]:
                print(f"{exercise['name']}: {exercise['sets']} sets x {exercise['reps']} {exercise.get('unit', 'reps')}")
            print("\n")


squat_1rm = float(input("Enter your squat 1RM: "))
bench_1rm = float(input("Enter your bench press 1RM: "))
deadlift_1rm = float(input("Enter your deadlift 1RM: "))

strength_training_plan(squat_1rm, bench_1rm, deadlift_1rm)



