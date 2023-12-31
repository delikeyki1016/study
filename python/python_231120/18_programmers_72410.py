import sys, re

# new_id = sys.stdin.readline().rstrip()

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id) 
    
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id) 
    
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id.strip('.') #가장 좋은 방법 
    # if new_id : # 이게 중요! new_id가 ''아무것도 없을 경우에는 if문에서 [0]인덱스를 찾는게 에러로 출력된다. 따라서 해당 줄이 필요한 것
    #     if new_id[0] == '.' :
    #         new_id = new_id[1:]
    # if new_id :
    #     if new_id[-1] == '.':
    #         new_id = new_id[:-1]
    
    #  5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not new_id:
        new_id = 'a'
        
    #  6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거, 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    # if new_id[-1] == '.':
    #     new_id = new_id[:-1]
    
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    lastText = new_id[-1]
    while len(new_id) < 3:
        new_id += lastText
        
    return new_id

print(solution('...!@BaT#*..y.abcdefghijklm')) # bat.y.abcdefghi
print(solution('z-+.^.')) # z--
print(solution('=.=')) # aaa
print(solution('123_.def')) # 123_.def
print(solution('abcdefghijklmn.p')) # abcdefghijklmn