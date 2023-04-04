

let options = {
valueNames: [ 'id', 'image', 'name','item_id', 'cmd', 'creators', 'note']
};

let userList = new List('users', options);

// 初期状態はidで昇順ソートする
userList.sort( 'id', {order : 'asc' });

// 高さを取得
window.onload = function() {
    let height = document.getElementsByTagName("html")[0].scrollHeight;
    window.parent.postMessage(["setHeight", height], "*");
}
