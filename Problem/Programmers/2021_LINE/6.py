from collections import deque


def solution(companies, applicants):
    answer = []

    companies_dict = {}
    applicants_dict = {}

    answer_dict = {}

    for company in companies:
        value = company.split(' ')
        companies_dict[value[0]] = [deque([i for i in value[1]]), value[2]]
        answer_dict[value[0]] = []

    for applicant in applicants:
        value = applicant.split(' ')
        deq = [value[1][i] for i in range(int(value[2]))]
        applicants_dict[value[0]] = deque(deq)

    for applicant in applicants_dict:
        value = applicants_dict[applicant]
        answer_dict[value.popleft()].append(applicant)

    while True:
        rejected_list = []
        for company in companies_dict:
            value = companies_dict[company]

            temp_rejected_list = []
            company_applicants = answer_dict[company]
            new_list = []
            for idx in range(len(value[0])):
                for applicant in company_applicants:
                    if value[0][idx] == applicant:
                        new_list.append(applicant)
                        break
                if len(new_list) == int(value[1]):
                    break

            for applicant in company_applicants:
                if applicant not in new_list:
                    temp_rejected_list.append(applicant)
            print(temp_rejected_list)
            rejected_list.extend(temp_rejected_list)
            companies_dict[company][0] = new_list

        if len(rejected_list) == 0:
            break

        for company in answer_dict:
            for reject in rejected_list:
                answer_dict[company].append(reject)

        for company in companies_dict:
            value = companies_dict[company]
            new_list = []
            for idx in range(len(value[0])):
                for applicant in rejected_list:
                    if value[0][idx] == applicant:
                        new_list.append(applicant)
                        break
                if len(new_list) == int(value[1]):
                    break
            companies_dict[company][0] = new_list


    answer = [key+''.join(answer_dict[key]) for key in answer_dict]
    return answer

print(solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"], ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]))
# print(solution(["A abc 2", "B abc 1"], ["a AB 1", "b AB 1", "c AB 1"])
