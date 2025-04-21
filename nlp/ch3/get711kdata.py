from datasets import load_dataset
#text: the actual novel text, all chapters
#meta: novel metadata
    #subset: dataset tag: syosetu
    #lang: dataset language: ja (Japanese)
    #id: novel ID/ncode
    #author: author name
    #userid: author user ID
    #title: novel title
    #length: novel length in words
    #points: global points (corresponds to global_point from the Syosetu API)
    #q: q-score (quality score) calculated based on points
    #chapters: number of chapters (corresponds to general_all_no from the Syosetu API)
    #keywords: array of novel keywords (corresponds to keyword from the Syosetu API, split on spaces)
    #isr15: whether the novel is rated R15+
    #genre: novel genre ID (optional, see Syosetu API documentation)
    #biggenre: general novel genre ID (optional, see Syosetu API documentation)
    #isr18: whether the novel is rated R18+
    #nocgenre: novel genre ID (optional, only available if isr18 is true, see Syosetu API documentation)

#dataset = load_dataset("botp/RyokoAI_Syosetu711K")
#dataset.set_format(type="pandas")
#df = dataset["train"][:]
#df.head()

#dataset = load_dataset("KakologArchives/KakologArchives")
#dataset.set_format(type="pandas")
#df = dataset["train"][:]
#df.head()

#thread	string	コメントのスレッド ID
#no	int64	コメント番号 (コメ番)
#vpos	int64	スレッド ID から起算したコメントの再生位置 (1/100秒)
#date	int64	コメント投稿時間の UNIX タイムスタンプ
#date_usec	int64	コメント投稿時間の小数点以下の時間
#user_id	string	ユーザー ID (コマンドに 184 が指定されている場合は匿名化され、1週間ほどでシャッフルされる)
#mail	string	コメントのコマンド (184, red naka big など、省略されることもある)
#premium	boolean	コメントしたユーザーがプレミアム会員であれば True
#anonymity	boolean	匿名コメントであれば True
#content	string	コメント本文 (AA など、まれに複数行コメントがあるので注意)

from datasets import load_dataset



dataset = load_dataset('KakologArchives/KakologArchives', 'sample', channel_id='jk211', year=2023, number_of_files=10)
for data in dataset['train']:
    print(data)


