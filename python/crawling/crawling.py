from bs4 import BeautifulSoup
import urllib.request as req

url = "http://dolbegae.co.kr/book_category/%EC%A0%88%ED%8C%90%EB%8F%84%EC%84%9C/"
html = req.urlopen(url)
html = html.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

# 절판도서 정보가 포함된 요소를 선택
out_of_print_books = soup.select(".book-embed")

for i, book in enumerate(out_of_print_books, start=1):
    # 각 절판도서의 정보 추출
    bookImg = book.select_one(".book-thumbnail > a > img").get("src")
    
    # .select_one(".book-title > a")에서 반환된 요소가 존재하는지 확인
    
    # 이미지 다운로드
    img_data = req.urlopen(bookImg).read()
    
    # 이미지를 파일로 저장
    with open(f"bookImg_{i}.jpg", "wb") as img_file:
        img_file.write(img_data)
    
    title_element = book.select_one(".book-hover-title")
        
    title = title_element.text.strip() if title_element else "제목 정보 없음"
    
    # 저자 정보가 없을 경우를 대비하여 조건문 추가
    author_element = book.select_one(".book-hover-author")
    author = author_element.get_text(strip=True).split("|")[0].rstrip(' 지음') if author_element else "저자 정보 없음"
    
    
    # 결과 출력 또는 저장
    # print("책이미지:", bookImg)
    print(f"책이미지({i}): {bookImg}")
    print("제목:", title)
    print("저자:", author)
    print("\n---\n")