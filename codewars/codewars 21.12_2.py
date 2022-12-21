def solution(string, ending):
    return (True if (ending in string[len(string)-len(ending):len(string)] or ending=='') else False)



solution('abcde', 'cde')