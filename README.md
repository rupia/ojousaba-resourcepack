# Minecraft生活鯖 - [お嬢鯖](https://ojousaba.gamewiki.jp/)サーバーリソースパック

* **[アイテムリスト](https://rupia.github.io/ojousaba-resourcepack/)**

## 更新方法

リソースパックに変更を行う場合は、以下の方法に従ってください。

なお、内容によっては再提出をお願いすることがあります。提出後の修正や変更も受け付けます。

### 方法1 - リソースパックを提出

リソースパック形式で提出する場合は、バニラのMinecraftでも読み込める状態にしてください。モデルやテクスチャの作り方はCITと同じで大丈夫です。

また、`custom_model_data`（カスタムモデルデータ）の設定を行う必要はありません。コードオーナーが設定します。例えば、指定したアイテム全てのテクスチャが変わる……というような状態です。特に指定がない場合、テクスチャは`./assets/minecraft/textures/item/ojousaba`フォルダに格納してください。提出されたファイルは、コードオーナーとPackSquashによる軽量化処理が行われます。

### 方法2 - アセットを提出

bbmodelやJSONと画像など、Blockbenchで読み込める状態のアセットを提出する場合、bbmodelにPCユーザー名が含まれてしまう場合があります。それら不要なメタデータは、`File > Export > Share`からリンクを共有することで削除できます。提出する前に、この手順を使用してメタデータを取り除くことをおすすめします。

### 方法3 - Gitで提出

このリモートリポジトリを`clone`してから、ローカルリポジトリで作業用のブランチを作成します。そこに変更を加えてリモートリポジトリに`push`した後、Pull Requestを作成してください。コードオーナーが内容をレビューした後、mainブランチへの`merge`を行います。

## custom_model_dataの割当

`custom_model_data`（カスタムモデルデータ）の割り当ては下記のとおり。

| Usage      | Number      |
|------------|-------------|
| 設置アイテム   | 1000 ~ 1999 |
| 使用アイテム   | 2000 ~ 2999 |
| ファッションアイテム | 3000 ~ 3999 |
| UIアイテム | 4000 ~ 4999 |

## バージョニング

このプロジェクトは、[Semantic Versioning](https://semver.org/)に一部準拠しつつ、下記のようなルールに従ってバージョン番号が変更されます。

**`v{MAJOR}.{MINOR}.{PATCH}`**

* MAJOR: 基本機能の変更、互換性のない大幅な変更
* MINOR: 新アイテム、新機能の実装やMinecraftアップデートの対応
* PATCH: 既存アイテムのバグやドキュメントの修正

## Special Thanks

* genpyon
* alumina6767
* kashinomi0384
* rupia

## Licence

* Resources Pack is [CC BY-NC-ND 4.0](./LICENSE)
