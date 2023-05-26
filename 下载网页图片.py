#输出s中的图片并保存
s='''<p><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/217258/13/29155/73175/6449e59cF1111fa51/a429b6ec46473c89.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/103745/8/39551/51350/6449e59cF29aac050/d10f7c1a8f35de9c.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/174513/36/36793/187378/6449e59dFf0a6ec43/48d053ad26679ce0.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/108752/10/27734/51300/6449e59dF93b8d84a/d5e08eba7ee4dce2.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/95135/39/36921/45031/6449e59dFfd81eae6/dcf279f248cecbda.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/93724/5/30676/77212/6449e59eF32937986/debd86c95b3834fc.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/188664/1/33945/56436/6449e59eF6084ddfd/a549a1643034166b.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/130325/1/32266/57275/6449e59fF020a43de/495947a30c894c81.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/105201/20/33178/63030/6449e59fF17a1d0af/3105fadb26ea5f6f.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/142943/8/30533/40520/6449e59fFa1d32898/1279afd3040bcdb5.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/98319/31/30600/68892/6449e59fF20deb7b5/8a66f7eb1c47ab05.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/146811/5/36576/69920/6449e59fFc52a17c8/dc85439234c6fd5d.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/100075/27/40613/66628/6449e59fF288e4028/b07024957e0fb49d.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/1156/23/21852/84046/6449e5a0Fb05942a3/ed578d2e04874ee9.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/20088/30/18944/40456/6449e5a0Fcadf6d12/5b7f3fdfaef8da46.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/90997/33/30661/15948/6449e5a0F4faa0d79/0e5894cb5ca3893c.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/114766/33/35294/25572/6449e5a0F2047bddc/3f98f24d653df76c.jpg"><img style="width:auto;height:auto;max-width:100%;" class="" src="//img10.360buyimg.com/imgzone/jfs/t1/143146/9/35961/119661/6449e5a0F9e334f5b/aa6fa4b767b71619.jpg"><br></p>'''

import urllib.request
import os

# 指定保存图片的路径
save_path = 'C:/Users/25830/OneDrive - oganneson/图片/python download'

tou = 'img'
wei = '.jpg'
postou = 0
i = 0
while i < s.count(tou):
    postou = s.find(tou, postou + len(tou))
    poswei = s.find(wei, postou + len(wei))
    url = s[postou:poswei + len(wei)]

    # 检查URL是否完整
    if not url.startswith('http'):
        url = 'https://' + url

    print(url)

    try:
        # 使用urllib.request.urlretrieve下载图片
        urllib.request.urlretrieve(url, os.path.join(save_path, f'img_{i}.jpg'))
    except Exception as e:
        print(f'Failed to download image from {url}: {e}')

    i += 1








