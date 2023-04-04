import json
import glob

def models2dic(f, item):
    # JSONモデルから辞書型に

    # 読み込み
    d = json.load(f)

    # カスタムモデルデータに元がなんのモデルか書き込み
    for i in range(len(d['overrides'])):
        # 適用先アイテム
        d['overrides'][i]['item'] = item

        ## サムネイル
        d['overrides'][i]['image'] = 'pack/assets/minecraft/models/'+ d['overrides'][i]['model'] + '.mng'

        # 参照先モデル
        d['overrides'][i]['model'] = d['overrides'][i]['model'].split('/')[-1]

        # コメント
        d['overrides'][i]['comment'] = d['overrides'][i]['__comment']
        del d['overrides'][i]['__comment']

        # 名前
        d['overrides'][i]['name'] = d['overrides'][i]['__name']
        del d['overrides'][i]['__name']

        # 製作者
        d['overrides'][i]['creator'] = d['overrides'][i]['__creator']
        del d['overrides'][i]['__creator']

    return d['overrides']


if __name__ == '__main__':
    textures = []
    for vanilla_model in glob.glob('./pack/assets/minecraft/models/item/*.json', recursive=False):
        with open(vanilla_model, mode='r', encoding='utf-8') as f:
            # ファイル名からアイテム名を抽出
            item = vanilla_model.split('\\')[-1].replace('.json','')

            # 読み込み
            textures += models2dic(f, item)

    d = {
        "textures" : textures
    }

    # JSONとして保存
    with open('./site/result.json', mode='w',encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
