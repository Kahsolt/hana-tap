# hana-tap

    Modified from daniwell's MikuTap, replacing with sound of はな_init (UTAU voicebank)

----

一个支持 はな_init 音源的 Mikutap 修改版，是 [HFIProgramming/mikutap](https://github.com/HFIProgramming/mikutap) 的分支

Visit the online Demo => [https://kahsolt.pythonanywhere.com/hana-tap](https://kahsolt.pythonanywhere.com/hana-tap)

### 修改说明  

- 完全集成所需字体及脚本
- 进行了汉化
- 移除了社交分享按钮
- 移除了原作者的Google Analysis
- 移除了页面上部分属性
- 增加了作品来源说明
- 更新了依赖
- 少量兼容性修复
- **替换资源：适配 はな_init 的主声源，网页和icon的色调**
- **整理静态资源文件夹的布局，以默认适配Flask框架**

### はな 调色盘

Logo：`#9BA637 10200631 rgb(155,166,55)`

色彩集： ![colorset.jpg](colorset.jpg)

```
#414149  4276553
#aca0a2  11313314
#b5ab27  11905831
#8a8f8b  9080715
#f5f4f0  16119024
#b6bf6c  11976556
#d5cede  14012126
#debb61  14596961
#d6d0b8  14078136
#d6dadd  14080733
#f8debd  16309949
#ff8f6d  16748397
```

### 基于本 repo 修改快速制作自己的 Tap

- 修改 `static/js/mikutap.js`，搜索两处 `NOTE` 并按照提示修改配色 (数字是颜色的十进制表示)
- 修改 `static/css/mikutap.css`，搜索两处 `NOTE` 并按照提示修改配色 (数字是颜色的十六进制表示)
- 替换文件夹 `static/icon` 中的 icon 素材
- 准备 32 个MP3格式的音频素材，你可以：
  - 手工剪辑、选择合适音高和时长的采样，放在 `mp3` 文件夹下
  - 准备一个长条录音文件，运行 `python mk_mp3.py <wav_fp>` 以自动切片
    - 如果源是 UTAU 声库，可以修改和使用 `tap.ust` 的导出 :)
    - 但你可以需要再找一些噪音片段当打击乐 :(
- 运行 `python mk_data.py` 以更新音频频段数据库
- 运行 `python start.py`，打开浏览器在 `http://127.0.0.1:5000` 进行本地测试


### 致谢

Great thanks to all Nyan Cat!!! :lolipop:

  - daniwell's official site: [https://aidn.jp](https://aidn.jp)
  - daniwell's MikuTap: 
    - demo:
      - official: [https://aidn.jp/mikutap](https://aidn.jp/mikutap)
      - mirror for China mainland: [https://hfiprogramming.github.io/mikutap/](https://hfiprogramming.github.io/mikutap/)
    - repo (mirror): [HFIProgramming/mikutap](https://github.com/HFIProgramming/mikutap)
  - unknown-o's Kagamine-Tap
    - demo: [https://static-1.llilii.cn/web-app/kagamine-tap/](https://static-1.llilii.cn/web-app/kagamine-tap/)
    - repo: [https://github.com/unknown-o/kagamine-tap](https://github.com/unknown-o/kagamine-tap)


### 致所有自行编辑修改的人

请在任何时候**不要移除原作者信息**。你可以添加你自己名字上去，但是保留原作者信息是最基本的尊重。

如果你用于了推广、广告等用途，请参见下方许可证要求联系原作者，谢谢。


### 版权说明

遵循原作者的说明，作品仅用于非盈利的公共使用用途，无需告知  

商业用途请直接联系作者，[详情](https://aidn.jp/about/)

```
daniwell@aidn.jp
※ 本サイトにて公開している楽曲は非営利かつ公序良俗に反しない限り、連絡なしにご自由にお使いいただいて構いません。
※ エグジットチューンズ管理楽曲（「Nyan Cat」や「ねこみみスイッチ」など）の商用利用につきましては、下記お問い合わせ窓口よりご連絡ください。
http://exittunes.com/license/
```

由于违规使用本 repo 带来的后果，HFIProgramming 和 本repo作者 不承担责任

----

by Armit
2022/10/25 
