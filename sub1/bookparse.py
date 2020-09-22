import json
import pandas as pd
import numpy as np
import pandas_profiling
import os
import shutil
import pickle

DATA_DIR = "../data"
DATA_FILE = os.path.join(DATA_DIR, "goodreads_books_poetry.json")
DUMP_FILE = os.path.join(DATA_DIR, "dump.pkl")

book_columns = (
    "book_id", # 도서번호
    "average_rating", # 평균평점
    "is_ebook", # 전자도서 여부 
    "num_pages", # 페이지수
    "publication_year", # 출판년도
    "ratings_count", # 평점 수
    "language_code" # 언어코드
)

review_columns = (
    "user_id", #유저 아이디
    "book_id", # 도서번호 
    "is_read", # 읽었는지 여부 
    "rating", #평점 
)




def import_data(data_path=DATA_FILE):
    """
    도서데이터, 리뷰데이터를 읽어서  Pandas DataFrame 형태로 저장합니다
    """

    books_metadata = pd.read_json('../data/goodreads_books_poetry.json', lines=True)
    books_reviewdata = pd.read_json('../data/goodreads_books_poetry.json', lines=True)
    books = []  # 책 테이블
    review = [] # 리뷰 테이블 


    ##### 책 데이터 
    books = books_metadata.sample(5)  
    book_frame = pd.DataFrame(data=books, columns=book_columns)
    
    # 빈 셀을 NaN
    book_frame.replace('', np.nan, inplace=True)
    
    # 프로파일러 만들기 
    # profile = pandas_profiling.ProfileReport(
    #     book_frame[['average_rating', 'is_ebook', 'num_pages',
    #     'publication_year', 'ratings_count']]
    # )
    # profile.to_file('../data/profiler_books_metadata_1.html')
    
    # pandas cut메소드 사용해서 필드를 이산 간격으로 변환 
    book_frame['num_pages'].replace(np.nan, -1, inplace=True)
    book_frame['num_pages'] = pd.to_numeric(book_frame['num_pages'])
    book_frame['num_pages'] = pd.cut(book_frame['num_pages'], bins=25)

    # .5 점수에 가까운 반올림 평점 
    book_frame['average_rating'] = book_frame['average_rating'].apply(lambda x: round(x*2)/2)

    # pandas qcut 메소드 사용해서 필드를 분위수 기반 이산 간격으로 변환
    book_frame['ratings_count'] = pd.qcut(book_frame['ratings_count'], 5)

    # 누락된 값을 2100년으로 대체 
    book_frame['publication_year'].replace(np.nan, 2100, inplace=True)

    # 누락된 값을 'unknown'으로 대체
    book_frame['language_code'].replace(np.nan, 'unknown', inplace=True)

    # is_ebook 열을 1, 0 으로 변환. (true면 1)
    book_frame['is_ebook'] = book_frame.is_ebook.map(lambda x : 1.0*(x=='true'))

    ## 프로파일러로 확인 
    # profile = pandas_profiling.ProfileReport(
    #     book_frame,[['average_rating', 'is_ebook', 'num_pages', 'publication_year',
    #     'ratings_count']]
    # )
    # profile.to_file('../data/profiler_books_metadata_2.html')



    # 리뷰 데이터 
    review = books_reviewdata.sample(5)
    review_frame = pd.DataFrame(data=review, columns=review_columns)
    
    # 불린을 문자열에 매핑 
    booleanDictionary = {True : 'true', False: 'false'}
    review_frame['is_read'] = review_frame['is_read'].replace(booleanDictionary)

        # profile = pandas_profiling.ProfileReport(
        #     review_frame,[['is_read', 'rating']]
        # )
        # profile.to_file('../data/profiler_interactions.html')

    review_frame['is_read'] = review_frame.is_read.map(lambda x: 1.0*(x=='true'))

    review_frame.groupby(['rating', 'is_read']).size().reset_index().pivot(
        columns='rating', index='is_read', values=0)

    


    return {"books": book_frame , "reviews": review_frame}

def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[책]")
    print(f"{separater}\n")
    print(data["books"].head())
    print(f"\n{separater}\n\n")

    print("[리뷰]")
    print(f"{separater}\n")
    print(data["reviews"].head())
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
