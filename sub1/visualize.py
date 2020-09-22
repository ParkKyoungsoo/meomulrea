import itertools
from collections import Counter
from parse import load_dataframes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium


def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


def show_store_categories_graph(dataframes, n=100):
    """
    Tutorial: 전체 음식점의 상위 `n`개 카테고리 분포를 그래프로 나타냅니다.
    """

    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)
    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )

    # 그래프로 나타냅니다
    chart = sns.barplot(x="category", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 카테고리 분포")
    plt.show()


def show_store_review_distribution_graph(dataframes, n=100):
    """
    Req. 1-3-1 전체 음식점의 리뷰 개수 분포를 그래프로 나타냅니다. 
    """
    stores = dataframes["stores"]

    storeList = stores.store_name.apply(lambda c: c.split("|"))
    storeList = itertools.chain.from_iterable(storeList)

    storeList_count = Counter(list(storeList))
    best_storeList = storeList_count.most_common(n=n)
    df = pd.DataFrame(best_storeList, columns=["store_name", "review_cnt"]).sort_values(
        by=["review_cnt"], ascending=False
    )

    # 그래프로 나타냅니다
    chart = sns.barplot(x="store_name", y="review_cnt", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 리뷰 분포")
    plt.show()


def show_store_average_ratings_graph(dataframes, n=100):
    """
    Req. 1-3-2 각 음식점의 평균 평점을 그래프로 나타냅니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group = stores_reviews.groupby(["store", "store_name"])
    scores = scores_group.mean().reset_index()

    df = pd.DataFrame(scores, columns=["store_name", "score"]).sort_values(
        by=["score"], ascending=False
    ).head(n=n)

    # 그래프로 나타냅니다
    chart = sns.barplot(x="store_name", y="score", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 리뷰 분포")
    plt.show()


def show_user_review_distribution_graph(dataframes):
    """
    Req. 1-3-3 전체 유저의 리뷰 개수 분포를 그래프로 나타냅니다.
    """
    user_review = dataframes["users"]
    user_review_count = pd.DataFrame(
        user_review["id"].value_counts().reset_index())
    user_review_count.rename(
        columns={'id': 'cnt', 'index': 'id'}, inplace=True)
    user_review_list = pd.merge(
        user_review, user_review_count, left_on='id', right_on='id'
    )
    user_review_group = user_review_list.groupby(['id'])
    user = user_review_group.mean().reset_index()
    user.rename(
        columns={'id': 'id', 'cnt': 'review_cnt'}, inplace=True)

    df = pd.DataFrame(user).sort_values(
        by='review_cnt', ascending=False
    ).head(n=100)

    # 그래프로 나타냅니다
    chart = sns.barplot(x='id', y="review_cnt", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("유저 리뷰 개수 분포")
    plt.show()


def show_user_age_gender_distribution_graph(dataframes):
    """
    Req. 1-3-4 전체 유저의 성별/나이대 분포를 그래프로 나타냅니다.
    """
    users = dataframes["users"]
    chart = sns.countplot(x="gender", data=users)
    plt.show()
    raise NotImplementedError


def show_stores_distribution_graph(dataframes):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    stores = dataframes["stores"].head(n=200)

    # 지도 객체 생성 (zoom_start: 배율 1~22)
    map_osm = folium.Map(location=[33.34, 126.10], zoom_start=9)

    # df2의 행 수만큼 반복하면서 마커 생성
    for i in stores.index:
        # 행 우선 접근 방식으로 값 추출
        name = stores.loc[i, 'store_name']
        lat = stores.loc[i, 'latitude']
        lng = stores.loc[i, 'longitude']

        # 마커 객체 생성, 추출한 정보를 지도에 표시
        marker = folium.Marker([lat, lng], popup=name,
                               icon=folium.Icon(color='red'))
        marker.add_to(map_osm)
        map_osm.save('map.html')


def main():
    set_config()
    data = load_dataframes()
    # show_store_categories_graph(data)
    # show_store_review_distribution_graph(data)
    # show_store_average_ratings_graph(data)
    # show_user_review_distribution_graph(data)
    show_user_age_gender_distribution_graph(data)
    # show_stores_distribution_graph(data)


if __name__ == "__main__":
    main()
