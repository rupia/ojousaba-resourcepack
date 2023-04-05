import json
import glob

def models2dic(f, item):
    # JSONモデルから辞書型に

    # 読み込み
    d = json.load(f)

    # CMDが記載されているものだけに制限
    overrides = [x for x in d['overrides'] if 'custom_model_data' in x['predicate']]

    # カスタムモデルデータに元がなんのモデルか書き込み
    for o in overrides:
        # 適用先アイテム
        o['item'] = item

        ## サムネイル
        o['image'] = 'pack/assets/minecraft/models/'+ o['model'] + '.mng'

        # 参照先モデル
        o['model'] = o['model'].split('/')[-1]

        # コメント
        if '__comment' in o:
            o['comment'] = o['__comment']
            del o['__comment']

        # 名前
        if '__name' in o:
            o['name'] = o['__name']
            del o['__name']

        # 製作者
        if '__creator' in o:
            o['creator'] = o['__creator']
            del o['__creator']

    return overrides


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
