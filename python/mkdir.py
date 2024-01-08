import os
import datetime

current_date = datetime.date.today()
title = input("주제를 입력하세요")
folder_name = title+'_'+current_date.strftime("%y%m%d")

directory_path = os.path.join(os.getcwd(), folder_name)

if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print(f"폴더 {folder_name} 생성이 완료되었습니다.")
else :
    print(f"폴더 {folder_name}가 이미 존재합니다.")