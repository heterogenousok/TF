import happybase

from sklearn.metrics import roc_auc_score, accuracy_score




def main():

    pool = happybase.ConnectionPool(size=10, host='hadoop-master')

    # 进行为相似文章获取
    with pool.connection() as conn:
        article_similar = conn.table('article_similar')
        article_dict = article_similar.row(str(116724).encode(), columns=[b'similar'])
        print(article_dict)
        _srt = sorted(article_dict.items(), key=lambda item: item[1], reverse=True)
        print(_srt)
        reco_set = [int(i[0].split(b':')[1]) for i in _srt][:10]
        print(reco_set)
        conn.close()


if __name__ == '__main__':
    main()