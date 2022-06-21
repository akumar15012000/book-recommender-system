
from flask import Flask,render_template,redirect,url_for,request
import book

app=Flask(__name__)




@app.route('/')
def index():
    url_list=book.url_list()
    book_title=book.book_title()
    avg_rating=book.avg_rating()
    author=book.get_author()
    user_count=book.user_count()
    return render_template('index.html',url_list=url_list,avg_rating=avg_rating,book_title=book_title,
    author=author,user_count=user_count)


@app.route('/recommedation',methods=['GET'])
def recommedation():
    bookName=request.args.get('bookName',None)
    print(bookName)
    if (bookName==None):
        return render_template('recommender.html',flag=0)
    else:
        obj=book.recommend(bookName)
        book_title=obj.Book_Title
        url_list=obj.url_list
        author=obj.Book_Author
        
        return render_template('recommender.html',url_list=url_list,book_title=book_title,author=author,flag=1,
        val=bookName)



if __name__=='__main__':
    app.run()




