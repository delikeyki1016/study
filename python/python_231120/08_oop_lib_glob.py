import glob # 파일 목록 추출

print(glob.glob('*.py')) # 현재 경로의 모든 .py 파일을 리스트로 반환 
print(glob.glob('c:\*')) # c드라이브 아래의 모든 폴더,파일을 리스트로 반환 