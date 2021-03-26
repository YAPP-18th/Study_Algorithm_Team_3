def solution(participant, completion):
    answer = ""
    participant_dict = dict()
    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1

    for person in completion:
        participant_dict[person] -= 1

    for person, value in participant_dict.items():
        if value == 1:
            answer = person
            return answer
    return answer
    