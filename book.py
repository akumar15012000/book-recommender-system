import pickle
import pandas as pd
import numpy as np
from difflib import SequenceMatcher,get_close_matches


def url_list():
    popular_50=top_50()
    popular_50=popular_50.iloc[:,1].apply(lambda x:x.replace('.jpg','.png'))
    return popular_50

def book_title():
    popular_50=top_50()
    return popular_50.iloc[:,0]

def avg_rating():
    popular_50=top_50()
    rating=popular_50.iloc[:,2]
    for i in range(len(rating)):
        rating[i]=round(rating[i],1)
    return rating

def get_author():
    popular_50=top_50()
    return popular_50.loc[:,'Book-Author']

def user_count():
    popular_50=top_50()
    return popular_50.loc[:,'Users_count']

def top_50():
    popular_50=None
    with open(r'popular_50.pkl','rb') as f:
        popular_50=pickle.load(f)
    return popular_50


def Recommend_Book(Book_name):
    pivot_data=None
    similarity_score=None
    book=None

    with open(r'book.pkl','rb') as f:
        book=pickle.load(f)

    with open(r'pivot_data.pkl','rb') as f:
        pivot_data=pickle.load(f)

    with open(r'similarity_score.pkl','rb') as f:
        similarity_score=pickle.load(f)
    
    Book_name=get_close_matches(Book_name,pivot_data.index,n=1,cutoff=0)[0]
    try:
        ind=np.where(pivot_data.index==Book_name)[0][0]
    except:
        print('Book is not in Data Base')
    else:
        distances=sorted(list(enumerate(similarity_score[ind])),key=lambda x:x[1],reverse=True)
        
        
        recommendation=pd.DataFrame(columns=['Book-Title','Book-Author','Image-URL-M'])
        
        book_names=pivot_data.index
        
        for i in distances[1:7]:
            tem=book[book['Book-Title']==book_names[i[0]]][['Book-Title','Book-Author','Image-URL-M']]
            
            recommendation=pd.concat([recommendation,tem])
        
        recommendation.drop_duplicates(['Book-Title'],inplace=True)
        recommendation=recommendation.reset_index(drop=True)
        return recommendation

def recommend(book_name):
    obj=rec()
    df=Recommend_Book(book_name)
    obj.Book_Title=df['Book-Title']
    obj.Book_Author=df['Book-Author']
    obj.url_list=df['Image-URL-M']

    return obj


class rec():

    def __init__(self) -> None:
        pass



