# Greeting

## ポイント
- gdbで`run`するとすぐに止まる
  →デバッガは、今動いているプロセスを追うので、子プロセスを作成されると止まってしまう。
  こういう場合は、`set follow-fork-mode parent`というコマンドで対応できる。
- 書き換えるべき関数がprintfの後に呼ばれていない！
  →デストラクタを書き換えればよい。
  ` readelf -S greeting` で`.fini_array` を見る。
- printfの出力が `Nice to meet you, ` の18バイト分はじめに出力されているので、それを考慮してFSAを仕掛ける



## 解法

`.fini_array` -> `main`

`strlen` のGOT -> `system` のPLT
