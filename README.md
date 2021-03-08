<div align="center">
  <img src="doc/img/asagao_logo_face3.png" alt="header" title="asagao-for-minecraft header">
</div>


# はじめに

## asagao-for-minecraftとは

Minecraftを遊んでいるとき以外もサーバー代金が発生するのは無駄です。
Discordから指定のメッセージを送信すると、ConoHaにMinecraft用のVM(バーチャルマシンサーバー)を構築、もしくは(データを保存の上)VMの破棄を行います。
これにより、マインクラフトを遊んでいる時間のみサーバーが課金され、安く運用することができます。

遊び終わった後にDiscordに`/mc close`と投稿すると、VMデータを退避(imageへ保存)しVMを破棄します。
これによって、破棄した後は料金の発生を防ぐことができます。

また遊びたいときはDiscordに`/mc open`と投稿すると、退避していたimageからVMを作成します(使い終わったimageは破棄します)。
これによって、ConoHaの課金が始まりますがMinecraftサーバーでまた遊べるようになります。

## why asagao(朝顔)?

朝顔は夏の朝に咲く花です。咲いたその日のうちにしぼんでしまいます(儚い)。

asagao-for-minecraftもConoHaのVMを構築し、破棄します。

一度しか咲かない朝顔と違い、asagao-for-minecraftは何度でも構築と破棄を繰り返します。

~~作者が朝顔は何度も咲くと勘違いして名付けました。~~

後、リポジトリ名を入力したときに「わかってねぇなあ、イケてるリポジトリ名って短くて簡潔なんだよ(超意訳)」ってGithubに煽られたので短い名前を付けました。


# 使い方

Discordアカウント、ConoHaアカウント(APIアカウント含む)を作成している前提とします。

## 本リポジトリをデプロイ(サーバーに公開して実行)する

このリポジトリをCloneしてきてPythonの動くサーバーにデプロイします。
環境はレンタルサーバー、クラウドなどがいいと思います。

個人的にロリポップマネージドクラウドで運用しているので、他の環境での検証は行っていません。
その他の環境で試してみた情報がございましたら、PR、Issue、ご自身のブログ等で共有いただけますと助かります。
他の環境で動かすために新しくコードが必要になるかもしれません。

最近、HerokuのFreeプランでは24時間の運用ができなくなったので難しいかもしれません(ボットを動かす前にサイトにアクセスする等でHerokuコンテナを起こすなどの工夫がいると思われます)。
レンタルサーバーなど、環境変数の使えない環境では仮想的に環境変数を取り扱ったり、ソースコードに直接トークンなどの情報を入れるしか方法はないと思います(トークンをGithubにアップロードしないように注意してください。また、ソースコードに直接トークンなどの秘匿情報を書くのはセキュリティ的にお行儀が良くない気がしてます)。

## DiscodBotの設定を行う

簡単に説明します。詳しくは[Discord Botのアカウント初期設定を行う](https://codelabo.com/posts/20210307103912)をご覧ください。

1. [DEVELOPER PORTAL](https://discord.com/developers/applications)にアクセスしてログインします。
1. 「New application」から好きなアプリケーション名を入力して「create」します。
1. 必要ならアイコンを設定しましょう。
1. 「settings」->「Bot」->「build-a-bot」->「Add Bot」をクリックします。「Yes」をクリック。
1. 「settings」->「Bot」->「build-a-bot」->「Add Bot」->「Token」->「Copy」からアクセストークンを取得します。
1. 「settings」->「OAuth2」->「OAuth2 URL Generator」->「SCOPES」の「bot」にチェックを入れます。認証URLが生成されるのでアクセスし、使いたいサーバーを選択して、「認証」します。

これでDiscordアプリから作ったBotアカウントを確認できると思います。

## 環境変数に値を設定する

「CONOHA_API_」から始まる環境変数は[ConoHaの管理画面](https://manage.conoha.jp/API/)から確認できるものです。

DISCORD_TOKENを設定するとConoHaAPIを使わないコマンドは動くようになります。

CONOHA_API_VM_PLAN_FLAVOR_UUIDは使用するConoHaのプランのIDです。
`/mc plan`とDiscordのminecraftチャンネルで投稿すると、ConoHaのプラン一覧を表示してくれます。「g-c3m2d100」は3Core, 2GB memory, 容量100GBのはず。

VM_AND_IMAGE_NAMEはConoHaで作成するVMのネームタグ(instance_name_tag)とimageの名前に使用されます。「asagao-for-minecraft-{VM_AND_IMAGE_NAME}」となります(例:VM_AND_IMAGE_NAME=testとすると、VMのネームタグとimageの名前は「asagao-for-minecraft-test」となります)。
デフォルトのVMのネームタグとimageの名前は「asagao-for-minecraft」です。

ADMIN_USER_IDは管理してる人のユーザーIDです。
`/mc userid`と投稿すると、投稿した人のユーザーIDを表示してくれます。

- 必須の環境変数
  - DISCORD_TOKEN
  - CONOHA_API_TENANT_ID
  - CONOHA_API_IDENTITY_SERVICE
  - CONOHA_API_USER_NAME
  - CONOHA_API_USER_PASSWORD
  - CONOHA_API_IMAGE_SERVICE
  - CONOHA_API_COMPUTE_SERVICE
  - CONOHA_API_NETWORK_SERVICE
  - CONOHA_API_VM_PLAN_FLAVOR_UUID
- オプション環境変数
  - VM_AND_IMAGE_NAME
  - ADMIN_USER_ID

## ConoHaでMinecraft用のVMを作成する

ConoHaでサーバー追加をクリックし、Minecraft用のVMを作成していきます。

- サービス = Minecraft
- VPS割引きっぷ = 利用しない
- プラン = 1GB以上
- イメージタイプ = 好きな方(私はJava版)
- root パスワード = 何でもいい
- ネームタグ = asagao-for-minecraft もしくはVM_AND_IMAGE_NAMEを設定してるならasagao-for-minecraft-{VM_AND_IMAGE_NAME}

この設定でサーバー追加(VM作成)します。

## 実際に使ってみましょう

現在、VMが存在しているのでConoHaに対して料金が発生しています。
以下のコマンドをDiscordのminecraftチャンネルに投稿して観ましょう。

```
/mc close
```

無事成功すれば、サーバーリストから先ほど作成したVMが消えていることが確認できます。
その時、イメージを確認すると同じ名前のネームタグが付いたイメージが生成されていることも確認できます。これで料金がかからない状態になりました。

また、遊びたくなったとします。その時は以下のコマンドを投稿します。

```
/mc open
```

無事成功すれば、サーバーリストにimageから新しくVMが生成され、使い終わったimageはなくなっていることが管理画面から確認できると思います。

VMを再作成している仕様上、毎回サーバーのipアドレスは変更してしまいます。Discordに表示されたものを使用してください。

コマンドの一覧は以下のコマンドで確認できます。

```
/mc help
```


# 問題発生時

API通信がうまくいかなかったときなど、エラーを出して処理が中断、もしくはPythonスクリプトの実行を終了したりする場合があります。

その場合はもう一度実行することでうまくいくこともありますが、ConoHaの管理画面から手を加えなければいけない時もあります。

imageとVMの両方が存在している場合、作成しかけている方を手動で削除してください。imageとVMの両方が存在している場合、本スクリプトでは操作できません。削除する際は可能であればバックアップを取ることをおすすめします。ちなみにimageとVMそれぞれにおいて、同じ名前(もしくはネームタグ)は1つまでです。


# 細かい仕様

imageやVMを削除する前にその両方が有効な状態かチェックしています。これにより、意図しない挙動によってデータが消えるリスクを軽減しています。

imageの判別にはimageの名前(name)、VMの判別にはVMのネームタグ(instance_name_tag)を使用しています。同じものを複数作成しないでください。

asagao-for-minecraftは[discord.py](https://github.com/Rapptz/discord.py)とConoHaAPIを用いています。アイコンの作成には[Textcraft](https://textcraft.net/)を使用しています。


# 最後に
※現在α版って感じです(厳密に決めてないですが)。

使用に関して一切責任は負いかねます。すべて自己責任でお願いします。

ConoHaの課金はクレジットカードでなく、チャージ式のほうが安心な気がしてます(多分)。

製作者はロリポップマネージドクラウド、Minecraft Java edition で使用してます。
