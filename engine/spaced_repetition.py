def sm2(easiness, interval, repetitions, quality):
    if quality >= 3:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval *= easiness
        repetitions += 1
        easiness = max(1.3, easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
    else:
        repetitions = 0
        interval = 1
    return int(interval), repetitions, round(easiness, 2)

interval, reps, ease = sm2(2.5, 6, 2, 4)  # 4 = answered correctly
print("Next review in", interval, "days")

